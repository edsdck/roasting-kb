#!/usr/bin/env python3
"""Parse Artisan .alog files in roasts/ into:
  data/roasts.csv                 one row per roast (metrics)
  data/roasts/<stem>.json         metrics + events + downsampled curve (for the Builder)
  docs/skywalker/roasts/<stem>.md one wiki page per roast (metrics, SVG curve, notes, cupping)
  docs/skywalker/roast-log.md     table of all roasts
Cupping notes: Artisan's cupping-notes field and/or roasts/<stem>.md|.txt next to the .alog.
Idempotent: safe to run every build. Prints which roasts are new since last run.
"""
import ast, csv, glob, json, os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RDIR = os.path.join(ROOT, "roasts")
DATA = os.path.join(ROOT, "data")
PAGES = os.path.join(ROOT, "docs", "skywalker", "roasts")
EVENT_NAMES = ["CHARGE", "DRY", "FCs", "FCe", "SCs", "SCe", "DROP", "COOL"]


def load_alog(path):
    raw = open(path, encoding="utf-8", errors="replace").read()
    try:
        return ast.literal_eval(raw)
    except Exception:
        return json.loads(raw)


def fmt_t(s):
    if s is None:
        return ""
    s = int(round(s))
    return f"{s // 60}:{s % 60:02d}"


def r1(x):
    return None if x is None else round(float(x), 1)


def ror(timex, temps, i, window=30):
    """BT rate of rise in deg/min at index i over a trailing window (seconds)."""
    t0 = timex[i] - window
    j = i
    while j > 0 and timex[j - 1] >= t0:
        j -= 1
    if j == i or timex[i] == timex[j]:
        return None
    return (temps[i] - temps[j]) / (timex[i] - timex[j]) * 60


def idx_at(timex, t):
    for k, tt in enumerate(timex):
        if tt >= t:
            return k
    return len(timex) - 1


def clean(vals):
    """Replace dropouts (Artisan writes -1 when a reading fails) by linear interpolation."""
    v = [None if (x is None or x <= 0) else float(x) for x in vals]
    good = [i for i, x in enumerate(v) if x is not None]
    if not good:
        return [0.0] * len(v)
    # despike: a reading more than 10 degrees away from the median of its neighbours is a glitch
    for i in good:
        nb = sorted(v[j] for j in range(max(0, i - 6), min(len(v), i + 7)) if v[j] is not None)
        if len(nb) >= 5 and abs(v[i] - nb[len(nb) // 2]) > 10:
            v[i] = None
    good = [i for i, x in enumerate(v) if x is not None]
    out = list(v)
    for i in range(len(v)):
        if out[i] is None:
            lo = max((g for g in good if g < i), default=None)
            hi = min((g for g in good if g > i), default=None)
            if lo is None:
                out[i] = v[hi]
            elif hi is None:
                out[i] = v[lo]
            else:
                out[i] = v[lo] + (v[hi] - v[lo]) * (i - lo) / (hi - lo)
    return out


def analyse(path):
    d = load_alog(path)
    stem = os.path.splitext(os.path.basename(path))[0]
    timex = d.get("timex") or []
    # Artisan writes -1 for channels that aren't connected (the Skywalker V1 has no ET probe)
    et = [None if (v is None or v < 0) else v for v in (d.get("temp1") or [])]
    bt = clean(d.get("temp2") or [])
    ti = list(d.get("timeindex") or [-1, 0, 0, 0, 0, 0, 0, 0]) + [0] * 8
    comp = d.get("computed") or {}
    unit = d.get("mode", "C")
    n = min(len(timex), len(bt))
    ev = {}
    for k, name in enumerate(EVENT_NAMES):
        v = ti[k]
        if (k == 0 and v is not None and v >= 0) or (k > 0 and v and v > 0):
            if v < n:
                ev[name] = v
    c = ev.get("CHARGE", 0)
    t0 = timex[c] if n else 0

    def at(name):
        i = ev.get(name)
        if i is None:
            return None, None, None
        return timex[i] - t0, bt[i], (et[i] if i < len(et) else None)

    def cval(key, fallback):
        v = comp.get(key)
        return fallback if (v is None or v == -1 or v == -1.0) else v

    # turning point: min BT in first 3 min after charge
    tp_t = tp_bt = None
    if n:
        end = idx_at(timex, t0 + 180)
        seg = range(c, max(c + 1, end))
        k = min(seg, key=lambda j: bt[j])
        tp_t, tp_bt = timex[k] - t0, bt[k]
    dry_t, dry_bt, _ = at("DRY")
    fcs_t, fcs_bt, fcs_et = at("FCs")
    drop_t, drop_bt, drop_et = at("DROP")
    charge_bt = bt[c] if n else None
    charge_et = et[c] if n and c < len(et) else None
    dev = (drop_t - fcs_t) if (drop_t is not None and fcs_t is not None) else None
    dtr = (dev / drop_t * 100) if (dev is not None and drop_t) else None
    maillard = (fcs_t - dry_t) if (fcs_t is not None and dry_t is not None) else None
    w = d.get("weight") or [0, 0, "g"]
    win, wout = (float(w[0] or 0), float(w[1] or 0))
    if len(w) > 2 and str(w[2]).lower() == "kg":
        win, wout = win * 1000, wout * 1000
    loss = ((win - wout) / win * 100) if win and wout else None
    ror_fc = ror(timex, bt, ev["FCs"]) if "FCs" in ev else None
    ror_fc60 = (ror(timex, bt, idx_at(timex, timex[ev["FCs"]] + 60))
                if "FCs" in ev and "DROP" in ev and timex[ev["DROP"]] - timex[ev["FCs"]] >= 60 else None)
    ror_drop = ror(timex, bt, ev["DROP"]) if "DROP" in ev else None
    # peak RoR after turning point
    peak = None
    if n and tp_t is not None:
        stop = ev.get("DROP", n - 1)
        vals = [ror(timex, bt, j) for j in range(idx_at(timex, t0 + tp_t + 30), stop + 1)]
        vals = [v for v in vals if v is not None]
        peak = max(vals) if vals else None
    # control events (Artisan stores slider values as v/10+1)
    etypes = d.get("etypes") or ["Air", "Drum", "Damper", "Burner", "--"]
    events = []
    for k, i in enumerate(d.get("specialevents") or []):
        try:
            typ = d["specialeventstype"][k]
            val = d["specialeventsvalue"][k]
            label = (d.get("specialeventsStrings") or [""] * 999)[k]
            name = etypes[typ] if typ < len(etypes) else str(typ)
            name = {"Burner": "Heater", "Air": "Fan"}.get(name, name) if "skywalker" in str(d.get("roastertype", "")).lower() else name
            try:
                value = float(label)
            except (TypeError, ValueError):
                value = max(0, round((val - 1) * 10))
            events.append({"t": fmt_t(timex[i] - t0), "sec": round(timex[i] - t0), "type": name, "value": value})
        except Exception:
            pass
    cup = (d.get("cuppingnotes") or "").strip()
    for ext in (".md", ".txt"):
        side = os.path.join(RDIR, stem + ext)
        if os.path.exists(side):
            note = open(side, encoding="utf-8").read().strip()
            note = re.sub(r"(?m)^(#{1,3}) ", lambda mm: "#" * (len(mm.group(1)) + 2) + " ", note)  # nest under page headings
            cup = (cup + "\n\n" if cup else "") + note
    m = {
        "stem": stem,
        "date": d.get("roastisodate") or d.get("roastdate") or "",
        "title": (d.get("title") if d.get("title") not in (None, "", "Roaster Scope") else (d.get("beans") or f"Unlabelled ({stem})")).strip(),
        "roaster": d.get("roastertype") or "",
        "beans": (d.get("beans") or "").strip(),
        "unit": unit,
        "weight_in": win or None, "weight_out": wout or None,
        "weight_loss_pct": r1(loss),
        "charge_bt": r1(cval("CHARGE_BT", charge_bt)), "charge_et": r1(cval("CHARGE_ET", charge_et)),
        "tp_time": fmt_t(tp_t), "tp_bt": r1(tp_bt),
        "dry_time": fmt_t(dry_t), "dry_bt": r1(dry_bt),
        "fcs_time": fmt_t(fcs_t), "fcs_bt": r1(fcs_bt), "fcs_et": r1(fcs_et),
        "drop_time": fmt_t(drop_t), "drop_bt": r1(drop_bt), "drop_et": r1(drop_et),
        "maillard_time": fmt_t(maillard), "dev_time": fmt_t(dev), "dtr_pct": r1(dtr),
        "ror_peak": r1(peak), "ror_at_fcs": r1(ror_fc), "ror_fcs_plus60": r1(ror_fc60), "ror_at_drop": r1(ror_drop),
        "whole_color": d.get("whole_color") or "", "ground_color": d.get("ground_color") or "",
        "density_gl": (lambda x: round(x[0] / x[2] * (1000 if str(x[3]).lower() in ("ml",) else 1), 1) if x and x[0] else "")(d.get("density")),
        "heater_at_charge": next((e["value"] for e in events if e["type"] == "Heater" and e["sec"] <= 5), ""),
        "heater_changes": sum(1 for e in events if e["type"] == "Heater" and e["sec"] > 5),
        "fan_changes": sum(1 for e in events if e["type"] == "Fan"),
        "roasting_notes": (d.get("roastingnotes") or "").strip(),
        "cupping_notes": cup,
        "events": events,
    }
    # downsampled curve (every ~10 s) from charge to drop (+30 s)
    end_i = idx_at(timex, timex[ev["DROP"]] + 30) if "DROP" in ev else n - 1
    curve, last = [], -999
    for j in range(c, end_i + 1):
        if timex[j] - last >= 10:
            last = timex[j]
            rr = ror(timex, bt, j)
            curve.append([round(timex[j] - t0, 1), r1(bt[j]), r1(et[j]) if j < len(et) else None, r1(rr)])
    m["curve"] = curve
    m["markers"] = {k: round(timex[i] - t0, 1) for k, i in ev.items()}
    return m


def svg(m):
    W, H, L, R, T, B = 720, 360, 50, 50, 15, 35
    pts = m["curve"]
    if not pts:
        return ""
    tmax = max(p[0] for p in pts) or 1
    temps = [v for p in pts for v in (p[1], p[2]) if v is not None and v > 0]
    ymax = (max(temps) // 50 + 1) * 50
    ymin = 0
    rmax = 30 if m["unit"] == "C" else 55
    X = lambda t: L + t / tmax * (W - L - R)
    Y = lambda v: T + (1 - (v - ymin) / (ymax - ymin)) * (H - T - B)
    YR = lambda v: T + (1 - max(0, min(v, rmax)) / rmax) * (H - T - B)

    def line(idx, yf, color, width=2):
        seg = " ".join(f"{X(p[0]):.1f},{yf(p[idx]):.1f}" for p in pts if p[idx] is not None)
        return f'<polyline fill="none" stroke="{color}" stroke-width="{width}" points="{seg}"/>'
    g = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" style="max-width:100%;font:11px sans-serif">']
    for v in range(0, int(ymax) + 1, 50):
        g.append(f'<line x1="{L}" x2="{W-R}" y1="{Y(v):.1f}" y2="{Y(v):.1f}" stroke="#8884" />'
                 f'<text x="{L-6}" y="{Y(v)+4:.1f}" text-anchor="end" fill="#888">{v}</text>')
    for v in range(0, rmax + 1, 10 if m["unit"] == "C" else 10):
        g.append(f'<text x="{W-R+6}" y="{YR(v)+4:.1f}" fill="#2a9d8f">{v}</text>')
    for t in range(0, int(tmax) + 1, 60):
        g.append(f'<text x="{X(t):.1f}" y="{H-B+16}" text-anchor="middle" fill="#888">{t//60}</text>')
    g.append(f'<text x="{(L+W-R)/2}" y="{H-4}" text-anchor="middle" fill="#888">minutes from charge</text>')
    for k, t in m["markers"].items():
        if k in ("CHARGE", "COOL"):
            continue
        g.append(f'<line x1="{X(t):.1f}" x2="{X(t):.1f}" y1="{T}" y2="{H-B}" stroke="#999" stroke-dasharray="3,3"/>'
                 f'<text x="{X(t)+3:.1f}" y="{T+10}" fill="#888">{k}</text>')
    if any(p[2] is not None for p in pts):
        g.append(line(2, Y, "#e76f51"))
    g.append(line(1, Y, "#4a7fb5", 2.5))
    g.append(line(3, YR, "#2a9d8f", 1.5))
    has_et = any(p[2] is not None for p in pts)
    g.append(f'<text x="{L+8}" y="{H-B-8}" fill="#4a7fb5">BT</text>'
             + (f'<text x="{L+32}" y="{H-B-8}" fill="#e76f51">ET</text>' if has_et else '')
             + f'<text x="{L+(56 if has_et else 32)}" y="{H-B-8}" fill="#2a9d8f">RoR (°{m["unit"]}/min, right axis)</text>')
    g.append("</svg>")
    return "".join(g)


def page(m):
    u = "°" + m["unit"]
    m = {k: ("—" if v is None or v == "" else v) for k, v in m.items()}
    rows = [
        ("Beans", m["beans"] or "—"),
        ("Batch in / out", f"{m['weight_in']} g / {m['weight_out']} g · loss {m['weight_loss_pct']} %"),
        ("Charge", f"BT {m['charge_bt']}{u}" + (f" · ET {m['charge_et']}{u}" if m['charge_et'] != "—" else "")),
        ("Turning point", f"{m['tp_time']} @ {m['tp_bt']}{u}"),
        ("Dry end", f"{m['dry_time'] or '—'} @ {m['dry_bt'] or '—'}{u}"),
        ("First crack", f"{m['fcs_time'] or '—'} @ {m['fcs_bt'] or '—'}{u}"),
        ("Drop", f"{m['drop_time'] or '—'} @ {m['drop_bt'] or '—'}{u}"),
        ("Maillard / development", f"{m['maillard_time'] or '—'} / {m['dev_time'] or '—'} (DTR {m['dtr_pct'] or '—'} %)"),
        ("RoR peak / at FCs / FCs+60s / at drop", f"{m['ror_peak']} / {m['ror_at_fcs']} / {m['ror_fcs_plus60']} / {m['ror_at_drop']} {u}/min"),
        ("Color (whole / ground)", f"{m['whole_color'] or '—'} / {m['ground_color'] or '—'}"),
    ]
    out = [f"# {m['date']} — {m['title']}", "", "*Generated from the Artisan file by `tools/roastlog.py` — don't edit; "
           "edit the cupping notes file instead.*", "", "| Metric | Value |", "|---|---|"]
    out += [f"| {k} | {v} |" for k, v in rows]
    out += ["", svg(m), "", "RoR computed over a 30 s window from raw BT (may differ from Artisan's smoothed RoR).", ""]
    if m["events"]:
        out += ["## Control changes", "", "| Time | Control | Value |", "|---|---|---|"]
        out += [f"| {e['t']} | {e['type']} | {e['value']:g} % |" for e in m["events"]]
        out.append("")
    out += ["## Roasting notes", "", m["roasting_notes"] or "*none*", "", "## Cupping notes", "",
            m["cupping_notes"] or "*none yet — add `roasts/" + m["stem"] + ".md`*", ""]
    return "\n".join(out)


def main():
    os.makedirs(os.path.join(DATA, "roasts"), exist_ok=True)
    os.makedirs(PAGES, exist_ok=True)
    known = {os.path.splitext(f)[0] for f in os.listdir(os.path.join(DATA, "roasts"))}
    ms, errors = [], []
    for p in sorted(glob.glob(os.path.join(RDIR, "*.alog"))):
        try:
            ms.append(analyse(p))
        except Exception as e:
            errors.append(f"{os.path.basename(p)}: {e}")
    ms.sort(key=lambda m: (m["date"], m["stem"]))
    cols = [k for k in (ms[0].keys() if ms else []) if k not in ("events", "curve", "markers", "cupping_notes", "roasting_notes")]
    with open(os.path.join(DATA, "roasts.csv"), "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(cols + ["has_cupping_notes"])
        for m in ms:
            w.writerow([m[k] for k in cols] + ["yes" if m["cupping_notes"] else "no"])
    for m in ms:
        with open(os.path.join(DATA, "roasts", m["stem"] + ".json"), "w", encoding="utf-8") as f:
            json.dump(m, f, indent=1, ensure_ascii=False)
        with open(os.path.join(PAGES, m["stem"] + ".md"), "w", encoding="utf-8") as f:
            f.write(page(m))
    lines = ["# Roast log", "", f"*{len(ms)} roasts, newest first, generated from Artisan files. "
             "Click a date for the curve, phases, heater/fan changes and cupping notes.*", "",
             "| Date | Coffee | g | Loss % | FC | Dev | DTR % | Drop °C | Cupped |",
             "|---|---|---|---|---|---|---|---|---|"]
    for m in reversed(ms):
        g = f"{m['weight_in']:g}" if m['weight_in'] else ""
        lines.append(f"| [{m['date']}](roasts/{m['stem']}.md) | {m['title'][:40]} | {g} | "
                     f"{m['weight_loss_pct'] or ''} | {m['fcs_time']} | {m['dev_time']} | "
                     f"{m['dtr_pct'] or ''} | {m['drop_bt'] or ''} | {'✓' if m['cupping_notes'] else ''} |")
    with open(os.path.join(ROOT, "docs", "skywalker", "roast-log.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")
    new = [m["stem"] for m in ms if m["stem"] not in known]
    print(f"parsed {len(ms)} roasts; new: {', '.join(new) if new else 'none'}")
    for e in errors:
        print("ERROR", e)


if __name__ == "__main__":
    main()
