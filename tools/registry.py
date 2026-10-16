#!/usr/bin/env python3
"""Source registry: dedupe, ids, status, index. Run from repo root.

  check URL [--title T]      exact (canonical URL) and near-title matches
  next-id                    next free S#### id
  add --url U --status S ... add a row (statuses: new, integrated, superseded, rejected, duplicate, needs-manual)
  set-status ID STATUS       update registry row + source file frontmatter
  list [--status S]          list rows
  stats                      counts by status/type/grade
  build-index                regenerate docs/sources/index.md from source files
"""
import argparse, csv, difflib, glob, os, re, sys
from datetime import date
from urllib.parse import urlsplit, urlunsplit, parse_qsl, urlencode

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REG = os.path.join(ROOT, "registry.csv")
SRC = os.path.join(ROOT, "docs", "sources")
FIELDS = ["id", "status", "type", "title", "author", "canonical_url", "url", "file",
          "grade", "heat", "discovered", "reason"]
STATUSES = {"new", "integrated", "superseded", "rejected", "duplicate", "needs-manual"}
DROP_PARAMS = re.compile(r"^(utm_.*|fbclid|gclid|mc_.*|ref|ref_src|si|feature|igshid|share|source)$", re.I)


def canonical(url):
    url = url.strip()
    if "://" not in url:
        url = "https://" + url
    p = urlsplit(url)
    host = p.netloc.lower()
    for pre in ("www.", "m.", "mobile."):
        if host.startswith(pre):
            host = host[len(pre):]
    # YouTube -> youtube.com/watch?v=ID
    vid = None
    if host == "youtu.be":
        vid = p.path.strip("/").split("/")[0]
    elif host.endswith("youtube.com"):
        q = dict(parse_qsl(p.query))
        if "v" in q:
            vid = q["v"]
        else:
            m = re.match(r"^/(shorts|embed|live)/([^/?]+)", p.path)
            if m:
                vid = m.group(2)
    if vid:
        return f"https://youtube.com/watch?v={vid}"
    query = urlencode(sorted((k, v) for k, v in parse_qsl(p.query) if not DROP_PARAMS.match(k)))
    path = re.sub(r"/+$", "", p.path) or ""
    return urlunsplit(("https", host, path, query, ""))


def load():
    if not os.path.exists(REG):
        return []
    with open(REG, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def save(rows):
    with open(REG, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=FIELDS)
        w.writeheader()
        for r in rows:
            w.writerow({k: r.get(k, "") for k in FIELDS})


def norm_title(t):
    return re.sub(r"[^a-z0-9 ]", "", (t or "").lower()).strip()


def next_id(rows):
    nums = [int(r["id"][1:]) for r in rows if re.fullmatch(r"S\d{4}", r.get("id", ""))]
    nums += [int(m) for m in re.findall(r"S(\d{4})-", " ".join(os.listdir(SRC)))]
    return "S%04d" % (max(nums, default=0) + 1)


def cmd_check(a):
    rows = load()
    c = canonical(a.url)
    found = False
    for r in rows:
        if r["canonical_url"] == c:
            print(f"SEEN  {r['id'] or '-'}  [{r['status']}]  {r['title']}  ({r['reason']})")
            found = True
    if a.title:
        nt = norm_title(a.title)
        for r in rows:
            ratio = difflib.SequenceMatcher(None, nt, norm_title(r["title"])).ratio()
            if ratio >= 0.8 and r["canonical_url"] != c:
                print(f"SIMILAR TITLE ({ratio:.2f})  {r['id'] or '-'}  [{r['status']}]  {r['title']}  {r['url']}")
                found = True
    if not found:
        print(f"NEW  {c}")
    sys.exit(1 if found else 0)


def cmd_add(a):
    if a.status not in STATUSES:
        sys.exit(f"bad status {a.status}; use one of {sorted(STATUSES)}")
    rows = load()
    c = canonical(a.url)
    if any(r["canonical_url"] == c for r in rows):
        sys.exit(f"already registered: {c}")
    if a.id and any(r["id"] == a.id for r in rows):
        sys.exit(f"id {a.id} already used")
    rows.append(dict(id=a.id or "", status=a.status, type=a.type or "", title=a.title or "",
                     author=a.author or "", canonical_url=c, url=a.url, file=a.file or "",
                     grade=a.grade or "", heat=a.heat or "", discovered=date.today().isoformat(),
                     reason=a.reason or ""))
    save(rows)
    print(f"added {a.id or '-'} {a.status} {c}")


def set_frontmatter(path, key, value):
    with open(path, encoding="utf-8") as f:
        txt = f.read()
    new, n = re.subn(rf"(?m)^{key}:[^\n]*$", f"{key}: {value}", txt, count=1)
    if n:
        with open(path, "w", encoding="utf-8") as f:
            f.write(new)
    return bool(n)


def cmd_set_status(a):
    if a.status not in STATUSES:
        sys.exit(f"bad status {a.status}")
    rows = load()
    hit = [r for r in rows if r["id"] == a.id]
    if not hit:
        sys.exit(f"no registry row {a.id}")
    for r in hit:
        r["status"] = a.status
        if r["file"] and os.path.exists(os.path.join(ROOT, r["file"])):
            set_frontmatter(os.path.join(ROOT, r["file"]), "kb_status", a.status)
    save(rows)
    print(f"{a.id} -> {a.status}")


def cmd_list(a):
    for r in load():
        if a.status and r["status"] != a.status:
            continue
        print(f"{r['id'] or '-':6} {r['status']:12} {r['grade'] or '-':2} {r['heat'] or '-':14} {r['title'][:70]}  {r['file'] or r['url']}")


def cmd_stats(a):
    rows = load()
    from collections import Counter
    print(f"total rows: {len(rows)}")
    for k in ("status", "type", "grade", "heat"):
        print(f"{k}: " + ", ".join(f"{v or '-'}={n}" for v, n in Counter(r[k] for r in rows).most_common()))
    print("next id:", next_id(rows))


def parse_fm(path):
    with open(path, encoding="utf-8") as f:
        txt = f.read()
    m = re.match(r"^---\n(.*?)\n---", txt, re.S)
    fm = {}
    if m:
        for line in m.group(1).splitlines():
            mm = re.match(r"^(\w+):\s*(.*?)\s*(#.*)?$", line)
            if mm:
                v = mm.group(2).strip().strip('"').strip("'")
                fm[mm.group(1)] = v
    return fm


def cmd_build_index(a):
    files = sorted(glob.glob(os.path.join(SRC, "S[0-9][0-9][0-9][0-9]-*.md")))
    lines = ["# Sources", "",
             "Every source collected by the Gatherer. Grades: **A** experiment/paper · **B** practitioner with data · "
             "**C** practitioner opinion · **D** marketing/unverified.", "",
             f"*{len(files)} sources.*", "",
             "| ID | Title | Type | Grade | Heat context | Status |", "|---|---|---|---|---|---|"]
    for p in files:
        fm = parse_fm(p)
        name = os.path.basename(p)
        title = (fm.get("title") or name).replace("|", "\\|")
        lines.append(f"| {fm.get('id','')} | [{title}]({name}) | {fm.get('type','')} | {fm.get('grade','')} | "
                     f"{fm.get('heat','')} | {fm.get('kb_status','')} |")
    with open(os.path.join(SRC, "index.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")
    print(f"index: {len(files)} sources")


def main():
    ap = argparse.ArgumentParser()
    sp = ap.add_subparsers(dest="cmd", required=True)
    p = sp.add_parser("check"); p.add_argument("url"); p.add_argument("--title")
    sp.add_parser("next-id")
    p = sp.add_parser("add")
    for k in ("url", "status"):
        p.add_argument("--" + k, required=True)
    for k in ("id", "type", "title", "author", "file", "grade", "heat", "reason"):
        p.add_argument("--" + k)
    p = sp.add_parser("set-status"); p.add_argument("id"); p.add_argument("status")
    p = sp.add_parser("list"); p.add_argument("--status")
    sp.add_parser("stats")
    sp.add_parser("build-index")
    a = ap.parse_args()
    {"check": cmd_check, "next-id": lambda a: print(next_id(load())), "add": cmd_add,
     "set-status": cmd_set_status, "list": cmd_list, "stats": cmd_stats,
     "build-index": cmd_build_index}[a.cmd](a)


if __name__ == "__main__":
    main()
