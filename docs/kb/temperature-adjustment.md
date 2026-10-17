---
title: Temperatures & adjustment
---

# Temperatures & adjustment to the Skywalker

!!! abstract "In short"
    - **All temperatures here are °C.** Sources quoted in °F are converted: °C = (°F − 32) × 5/9; for *differences* and RoR just multiply by 5/9 (10 °F = 5.6 °C; 10 °F/min = 5.6 °C/min).
    - The Skywalker probe reads **lower** than the contact probes most sources use, so a published drum temperature cannot be used as is.
    - Every temperature from another machine is shown twice: **reported** (what the source measured, in °C) and **adjusted** (`adj. ≈`, what a Skywalker V1 would probably show). The adjusted number is an estimate with about ±4 °C of doubt.
    - Temperature *differences* (degrees above first crack, RoR) are converted to °C but **not shifted**; whether they shrink on a lamp roaster is unknown.
    - **Probe depth and probe make move first-crack readings by 10–20 °C** (one Quest M6: ~11 °C from depth alone; Aillio Bullets are reported at both ~182 and ~200 °C), so an adjusted value is only as good as the source's probe. Where a source states its own first-crack reading, use that, not a generic 200 °C.

## Method
1. **Anchor on first crack.** Your 41 roasts read first crack at a median of **184.5 °C**
   (middle half 182.9–189.0 °C, SD 4.3 °C; 183.8 °C without the Honduras Honey, which reads ~190 °C).
   Other Skywalker owners log 179–183 °C [S0015](../sources/S0015-homeroasters-skywalker-roasts-thread.md) [S0017](../sources/S0017-homeroasters-skywalker-mods-thread.md). Reference machines read first crack at
   about **200 °C** (Quest 200 °C ± 2, Aillio Bullet 200 °C ± 2–3 [S0020](../sources/S0020-home-barista-bean-temperature-at-first-crack.md); a Quest M6 owner,
   200 °C ± 2 [S0024](../sources/S0024-home-barista-first-crack-temperature-changed.md); Sweet Maria's cites 201–208 °C [S0019](../sources/S0019-sweet-marias-first-crack-faq.md)).
2. **Shift rule.** `adjusted = reported − (source first crack − 184.5)`.
   If the source gives its own first-crack reading, use it. If not, assume 200 °C, which means
   **−15.5 °C**.
3. **Round honestly.** Adjusted values are rounded to whole degrees and written `adj. ≈`.

## Limits — read before trusting a number
- **One anchor only.** Your data tell us the Skywalker side (first crack). The other side comes
  from published first-crack readings, not from your data, and the shift is assumed constant from
  charge to drop. The probe reads an air–bean mix with air cooler than the beans [S0003](../sources/S0003-skywiki-renatoa-words-of-wisdom.md), so the gap
  may be different at 150 °C than at 190 °C. Not testable with your data alone.
- **Spread.** Your own first-crack readings vary with SD 4.3 °C (Honey ~6 °C higher), so an
  adjusted value is only good to about ±4 °C.
- **Batch size** moves readings too (smaller loads read lower) [S0003](../sources/S0003-skywiki-renatoa-words-of-wisdom.md) [S0013](../sources/S0013-melheim-2023-optimal-batch-size.md).
- **Differences.** Use them as reported; where a flavour effect is tied to a temperature (for
  example a note that disappears above first crack), prefer "degrees above *your* first crack"
  over an absolute adjusted temperature.
- **Probe depth.** One Quest M6 owner read first crack at 183–187 °C (362–369 °F) with the tip ~1 in into the drum and 193–199 °C (380–390 °F) at ~1.75 in; the usual Quest figure is ~200 °C (392 °F ± 2), and an M3S reads ~4 °C above an M3 with the same probes [S0045](../sources/S0045-home-barista-quest-m6-first-crack-temperature-probe-depth.md). A generic −15.5 °C shift assumes the source's probe sits like the reference machines'.
- **Machines of one make disagree.** On the Hacea writer's Proaster, first crack is marked at 385 °F (196 °C); she says an Aillio Bullet reads 25 °F (14 °C) lower than her Proaster, i.e. first crack near 182 °C [S0039](../sources/S0039-hacea-roast-phases-for-profile-development.md), while an experienced Bullet owner reports 200 °C ± 2–3 [S0020](../sources/S0020-home-barista-bean-temperature-at-first-crack.md). A Quest M3s read 10 degrees (about 5.6 °C, unit assumed °F) above the Proaster [S0036](../sources/S0036-home-barista-hacea-roast-approach-tasting-kit.md). Use each source's own first-crack reading as the anchor and treat any adjusted value as ±4 °C at best; where the probe is unknown, assume more.

## Worked examples
| Source value | Reported (°C) | Source FC (°C) | Shift | Adjusted (Skywalker) |
|---|---|---|---|---|
| Quest/Bullet first crack | 200 | 200 | −15.5 | ≈ 185 |
| Contact-probe first crack, Sweet Maria's | 201–208 | — | −15.5 | ≈ 185–192 [S0019](../sources/S0019-sweet-marias-first-crack-faq.md) |
| Light-roast drop, 385–390 °F, FC 370 °F [S0021](../sources/S0021-home-barista-development-time-light-roasts.md) | 196–199 | 188 | −3.3 | ≈ 193–196 |
| N3Roaster: FC / vegetal note leaves / 2nd crack (380 / 390 / 430 °F) [S0023](../sources/S0023-home-barista-vegetal-flavor-first-crack.md) | 193 / 199 / 221 | 193 | −8.8 | ≈ 185 / 190 / 212 |
| Marcelnl: note leaves below / finishes at [S0023](../sources/S0023-home-barista-vegetal-flavor-first-crack.md) | 204–205 / 206–207 | 198 | −13.5 | ≈ 191 / 193–194 |
| Study drops, fast → "baked" profile [S0006](../sources/S0006-alstrup-2020-development-time-sensory.md) | 204.1 → 191.1 | not given | −15.5 | ≈ 189 → 176 |
| Full vs half batch drop (440 vs 435 °F) [S0013](../sources/S0013-melheim-2023-optimal-batch-size.md) | 227 vs 224 | not given | −15.5 | ≈ 211 vs 208 |
| Hacea phase marks 300 / 340 / 385 °F [S0039](../sources/S0039-hacea-roast-phases-for-profile-development.md) | 149 / 171 / 196 | 196 | −11.6 | ≈ 137 / 160 / 185 |
| Hacea kit marks 305 / 350 / 385 °F [S0036](../sources/S0036-home-barista-hacea-roast-approach-tasting-kit.md) | 152 / 177 / 196 | 196 | −11.6 | ≈ 140 / 165 / 185 |
| Gayo drops, 2:50 / 3:50 / 4:50 development [S0037](../sources/S0037-fadhil-2025-gayo-arabica-development-phase-roasting-time.md) | 213.6 / 221.6 / 219.2 | 196.8 / 192.8 / 193.1 | −12.3 / −8.3 / −8.6 | ≈ 201 / 213 / 211 |
| Quest first crack, probe ~1 in / ~1.75 in deep [S0045](../sources/S0045-home-barista-quest-m6-first-crack-temperature-probe-depth.md) | 183–187 / 193–199 | own readings | — | not shifted: depth, not the machine, explains the gap |
| Quest heat-cut trigger BT 190 °C [S0046](../sources/S0046-home-barista-why-ror-is-a-bad-reference-webinar.md) | 190 | not given | −15.5 | ≈ 175 |
| Quest development RoR 8–10 °F/min [S0044](../sources/S0044-home-barista-matt-perger-on-roast-development.md) | 4.4–5.6 °C/min | — | none (RoR) | 4.4–5.6 |
| Production-roaster charge 170–230 °C [S0043](../sources/S0043-osorio-2022-cenicafe-initial-roast-temperature-sensory-quality.md) | 170–230 | not given | −15.5 | ≈ 155–215 (rough: charge, not first crack) |

Your own roasts need no adjustment: drop median 193.6 °C, first crack 184.5 °C, drop **+8.3 °C**
above first crack (see [findings](../skywalker/findings.md)).

## Open questions
- Is the offset really constant, or does it grow or shrink with bean temperature? A second anchor
  (an added thermocouple, as some owners fitted [S0016](../sources/S0016-homeroasters-skywalker-main-thread.md) [S0017](../sources/S0017-homeroasters-skywalker-mods-thread.md), or logging second crack on a
  roast that goes that far) would settle it.
- Do temperature differences above first crack compress on a lamp roaster?
- Which probe depth and tip coverage does your Skywalker probe have at 350 g? If it behaves like the Quest M6's, your first-crack spread may be partly mounting, not coffee. [S0045](../sources/S0045-home-barista-quest-m6-first-crack-temperature-probe-depth.md)
