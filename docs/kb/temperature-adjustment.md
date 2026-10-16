---
title: Temperatures & adjustment
---

# Temperatures & adjustment to the Skywalker

!!! abstract "In short"
    - **All temperatures here are °C.** Sources quoted in °F are converted: °C = (°F − 32) × 5/9; for *differences* and RoR just multiply by 5/9 (10 °F = 5.6 °C; 10 °F/min = 5.6 °C/min).
    - The Skywalker probe reads **lower** than the contact probes most sources use, so a published drum temperature cannot be used as is.
    - Every temperature from another machine is shown twice: **reported** (what the source measured, in °C) and **adjusted** (`adj. ≈`, what a Skywalker V1 would probably show). The adjusted number is an estimate with about ±4 °C of doubt.
    - Temperature *differences* (degrees above first crack, RoR) are converted to °C but **not shifted**; whether they shrink on a lamp roaster is unknown.

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

Your own roasts need no adjustment: drop median 193.6 °C, first crack 184.5 °C, drop **+8.3 °C**
above first crack (see [findings](../skywalker/findings.md)).

## Open questions
- Is the offset really constant, or does it grow or shrink with bean temperature? A second anchor
  (an added thermocouple, as some owners fitted [S0016](../sources/S0016-homeroasters-skywalker-main-thread.md) [S0017](../sources/S0017-homeroasters-skywalker-mods-thread.md), or logging second crack on a
  roast that goes that far) would settle it.
- Do temperature differences above first crack compress on a lamp roaster?
