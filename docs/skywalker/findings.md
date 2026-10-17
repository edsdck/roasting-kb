# Findings from my roasts

*Maintained by the Builder from the [roast log](roast-log.md) and cupping notes. Personal evidence
(grade **P**): the best evidence for this machine, but uncontrolled, one roaster, and only one roast
cupped so far. Updated 2026-10-17 (Build 6), 41 roasts (Jan–Oct 2026).*

!!! abstract "In short"
    - **First crack reads ~184 °C** on your machine (median of 41 roasts; range 174–193 °C) — matching other Skywalker owners (179–183 °C), far below the ~200 °C of convection roasters.
    - **Honduras Honey cracks ~6 °C higher** — but those roasts were also slower, and *within* each coffee FC time barely predicts FC temperature. Coffee vs speed can't be separated yet.
    - **Your development has shortened a lot:** median 1:37 (DTR 16.5 %) in Jan–Feb → **~1:00 (DTR ~9 %)** since June. That's shorter than the *"fast"* roast in the key development study (1:30), shorter than typical light roasters (1:20–1:30, 13–16 %) and the best roast reported by an experienced Skywalker owner (~1:35, 18 %) — but not unheard of (Nordic ~45 s).
    - Development time predicts your weight loss strongly (r = 0.72, n = 28) — more than drop temperature (r = 0.42).
    - The one roast you cupped (id39: 0:41 development, heater cut to 17 % right after first crack) tasted bitter, very acidic when cooled, with no clear flavour.
    - **New in Build 6:** a higher charge goes with a faster roast (about −4 s per °C of charge, r = −0.58 among the 37 roasts charged at 170 °C or above) — the same order as a Colombian production test, where the cup did not change with charge at medium colour. Most of your roasts (29 of 41) end drying later than the 3:30–4:30 window one Skywalker owner uses. Weight loss rises from ~13 % at 1:00 development to ~14 % at 1:30 or more.
    - **Biggest gap: cupping notes.** Without them, these numbers can't tell you what tastes good.

## Your typical roast (median, 41 roasts)

| | Median | Range |
|---|---|---|
| Batch | 350 g | 325–385 g |
| Charge BT | 181 °C | 108–205 °C |
| Turning point | ~1:04 | — |
| Dry end (yellow) | 4:40 @ ~145 °C | 3:55–7:00 |
| First crack | 8:59 @ **184.5 °C** | 7:12–13:23 / 174–193 °C |
| Development | **1:08** · DTR 11.1 % | 0:41–2:41 · 7–27 % |
| Drop BT | 193.6 °C | 186–206 °C |
| Total time | 10:33 | 8:27–14:23 |
| Weight loss | 13.4 % (n=28) | 12.0–15.9 % |
| RoR at first crack | 9.1 °C/min | 5.8–11.5 |

## Patterns

**1. First crack temperature.** Median 184.5 °C over 41 roasts, consistent with the ~182 °C reported
for the Skywalker [S0001](../sources/S0001-skywiki-infrared-roaster.md) and with the explanation that the probe reads an air–bean mix with air
cooler than the beans [S0003](../sources/S0003-skywiki-renatoa-words-of-wisdom.md). It varies by coffee: Ethiopian Washed ~184 °C (n=9, 181–186),
Costa Rican Natural ~184 °C (n=4), but **Honduras Honey ~190 °C** (n=14, 185–193) — even at
350 g. *Unclear why* (processing/density, or when you call first crack); see
[Measurement](../kb/measurement-and-artisan.md). Batch-size effects can't be separated here: all
325 g roasts were the Honduras.

*New context (Build 4):* your ~184 °C matches other owners' 179–183 °C [S0015](../sources/S0015-homeroasters-skywalker-roasts-thread.md) [S0016](../sources/S0016-homeroasters-skywalker-main-thread.md) [S0017](../sources/S0017-homeroasters-skywalker-mods-thread.md).
Some roasters see the *same* first-crack reading for every bean on consistent machines [S0020](../sources/S0020-home-barista-bean-temperature-at-first-crack.md) —
which would point to measurement or profile, not the coffee — while others find it bean-dependent
[S0020](../sources/S0020-home-barista-bean-temperature-at-first-crack.md) [S0019](../sources/S0019-sweet-marias-first-crack-faq.md). Checked against your data: across all 41 roasts, a later first crack goes with a
higher reading (r = 0.73), but within one coffee the link is weak (Honduras r = 0.16, n=14;
Ethiopia r = 0.05, n=10). The Honduras roasts were slower (median FC 10:28 vs ~8:30 for the others)
*and* read higher, so coffee and speed are confounded. Also possible: naturals/honeys can crack
quietly and be marked late [S0019](../sources/S0019-sweet-marias-first-crack-faq.md). → [experiment 6](experiments.md).

*New context (Build 6):* the same spread seen from outside. renatoa uses 182 °C as his first-crack reference with about a 7-degree spread by origin on a Skywalker [S0029](../sources/S0029-homeroasters-roast-assistant-for-skywalker.md); yours is SD 4.3 °C with a 19.4 °C full range (23 of 41 within ±3.5 °C of the median). The probe-depth case — a Quest M6 reading first crack ~11 °C higher after the tip was pushed in from ~1 in to ~1.75 in [S0045](../sources/S0045-home-barista-quest-m6-first-crack-temperature-probe-depth.md) — is larger than your middle half, so mounting changes could be part of the Honduras gap. Still unresolved; log probe depth each time.

**2. Development got shorter.** Jan–Feb median 1:37 (DTR 16.5 %, n=10); May–Jun 1:07 (11.2 %, n=13);
Jul–Aug 1:00 (9.1 %, n=15); Oct 1:01 (n=3). The research shows that at equal colour, short
development gives brighter, more acidic, fruitier cups, and longer development roastier/more bitter
ones — but its *shortest* tested roast was 1:30 [S0006](../sources/S0006-alstrup-2020-development-time-sensory.md) [S0012](../sources/S0012-munchow-2020-roasting-conditions-multi-study.md). Very short development tastes
"aggressive acidity, malty/nutty, metallic or vegetal" when it overshoots [S0010](../sources/S0010-hoos-loring-avoiding-roasting-defects.md). Whether ~1:00 is
right for you is the single most useful thing to test → [experiment 2](experiments.md).

*New context (Build 4):* practitioners' light roasts commonly run 13–16 % DTR / 1:20–1:30 [S0021](../sources/S0021-home-barista-development-time-light-roasts.md),
30 s – 1:30 [S0020](../sources/S0020-home-barista-bean-temperature-at-first-crack.md); Rao's rule is 20–25 % [S0018](../sources/S0018-rao-2014-development-time-ratio.md) (contested for light roasts — see
[Development](../kb/development.md#contested)). On a Skywalker, renatoa's best early cup had ~1:35
(18 %) [S0015](../sources/S0015-homeroasters-skywalker-roasts-thread.md), and his accidental ~45 s still cupped well (one anecdote) [S0015](../sources/S0015-homeroasters-skywalker-roasts-thread.md). Your RoR at first
crack (median 9.1 °C/min) is modest, so by the momentum argument [S0021](../sources/S0021-home-barista-development-time-light-roasts.md) your ~1:00 may develop
less than the same time on a hotter roast — **Inference — test it.**

*New context (Build 5):* more practitioner reports: a fruit-forward natural at 1:00–1:10 by Rob Hoos
[S0025](../sources/S0025-roast-rebels-hoos-cultivars-airflow-interview.md), a V2 Skywalker owner at 85–100 s (DTR 16–18 %) [S0027](../sources/S0027-coffeesnobs-skywalker-roasters-thread.md), and a roaster who dropped ~1 min after
first crack with no vegetal notes but thin body [S0023](../sources/S0023-home-barista-vegetal-flavor-first-crack.md). Still no controlled data below 1:30.

*New context (Build 6):* two more studies, both favouring the shorter development but neither at equal colour: a 2 kg gas-drum Gayo at 2:50 / 3:50 / 4:50 scored 85 / 82 / 81 while getting darker (Agtron 55 / 45 / 35) [S0037](../sources/S0037-fadhil-2025-gayo-arabica-development-phase-roasting-time.md), and a Probat series found panels preferring *longer* first-crack stretches (2:00–2:28) for body and sweetness, with the shortest crack brightest [S0034](../sources/S0034-sweet-marias-stretchin-out-the-roast-pt2.md). Your 1:00 is below every tested value (Gayo 2:50, Probat 1:32 from first-crack start to drop, calculated). Quest roasters report ~1:45, 20 % DTR and a drop 15–25 °F (8–14 °C) after first crack [S0044](../sources/S0044-home-barista-matt-perger-on-roast-development.md); yours drops +8.3 °C. Still no controlled data below 1:30.

**2b. How far above first crack you drop (new, n=41).** Median drop is **+8.3 °C** over the
first-crack reading (5.6–22.4 °C), and it moves with development time (r = 0.78). Four roasts ended
under 6 °C above first crack (id4, id19, id31, id32). N3Roaster reports a vegetal note that stays
until ~5.6 °C above first-crack start on his machines, independent of time, and another
roaster puts it at ~+6–7 °C [S0023](../sources/S0023-home-barista-vegetal-flavor-first-crack.md). The id39 roast (cupped sharp, very acidic, bitter) ended +6.2 °C;
id40 (same coffee) ended +12.0 °C but has no notes yet. Different probe and first-crack convention,
so this is a lead, not a rule. → [experiment 2](experiments.md). *Grade P, n=41 but only one cup.*

**3. Weight loss follows development time.** Correlation 0.72 between development time and weight
loss (n=28 roasts with output weight), vs 0.42 for drop temperature. On your machine, *how long* you
develop moves roast degree more than the drop temperature you choose. Light roasts throughout
(12–16 % loss).

*New context (Build 6), by development bucket (28 roasts with output weight):* under 0:50 (n=2) 12.6 % loss; 0:50–1:10 (n=12) mean 13.2 % (12.3–14.3); 1:10–1:30 (n=4) 13.2 %; 1:30 and over (n=10) 14.2 % (13.1–15.9). Home roasters log 11–15 %, mostly 13–14 % [S0032](../sources/S0032-home-barista-green-coffee-weight-loss.md); very light drops are ~10 % [S0030](../sources/S0030-royal-coffee-understanding-roast-yield-and-loss.md). Your lightest-looking roasts (12–13 %) are therefore not "very light" by weight loss. Green moisture is unknown, so loss cannot be read as a degree on its own [S0030](../sources/S0030-royal-coffee-understanding-roast-yield-and-loss.md).

**4. Heater handling around first crack.** Typically heater ~60 % a minute before first crack,
~50 % at first crack, 40–55 % in development (31 logged roasts) — moderate steps, consistent with the
advice to use few, modest changes on this lamp-driven machine [S0001](../sources/S0001-skywiki-infrared-roaster.md). Compare renatoa's
schedule (250 g): 70 % after the turning point, then 65 → 60 → 55 → 50 % between dry end (3:31) and 5:32,
first crack at 7:00, fan 65 → 80 % [S0015](../sources/S0015-homeroasters-skywalker-roasts-thread.md) — he starts reducing earlier (around dry end/minute 4) and in more
steps than the factory logic [S0017](../sources/S0017-homeroasters-skywalker-mods-thread.md). **Exception: id39** — 70 % →
50 % → **17 %** within ~30 s of first crack, then dropped at 0:41.

*New context (Build 6):* a Quest owner's pattern — hard power to the end of the ramp, momentum into first crack, then heat cut and fan up [S0044](../sources/S0044-home-barista-matt-perger-on-roast-development.md) — has the same shape as yours; whether a cut as deep as id39's 17 % in 30 s is too much is untested. Schulman starts turning heat down at BT 190 °C on a Quest (reported; adj. ≈ 175 °C) [S0046](../sources/S0046-home-barista-why-ror-is-a-bad-reference-webinar.md); the factory programs cut at 170 °C [S0016](../sources/S0016-homeroasters-skywalker-main-thread.md) and your typical first crack is 184.5 °C.

**5. The Honduras Honey series (id20–id34, 14 roasts).** Charge varied 141–186 °C, batch 325–375 g,
first crack 9:18–13:23. Lower charge → much later first crack (141.5 °C charge: FC 12:21; 186 °C:
FC 9:46). No cupping notes, so flavour effects are unknown.

**6. Charge temperature is a time lever (new, n=41).** Among the 37 roasts charged at 170 °C or above (median 184.9 °C) a higher charge goes with shorter total time (r = −0.58, about −4.3 s per °C) and earlier first crack (r = −0.67, about −5.4 s per °C). Four roasts charged lower (id5 108 °C, id28 141.5, id29 152.9, id30 166.4) cracked between 7:12 and 12:21, so they do not give a clean low-charge test. All 41: r = −0.48. A Colombian production test (170–230 °C charges, 5 kg units, medium colour) gave about 3 s per °C and *no* change in cup score [S0043](../sources/S0043-osorio-2022-cenicafe-initial-roast-temperature-sensory-quality.md). Whether that holds for light roasts on your machine is untested. → [experiment 7](experiments.md).

**7. Dry end is later than other owners' (new, n=41).** Median 4:40, range 3:55–7:00; 12 of 41 ended drying by 4:30 and 29 later. renatoa's target is 3:30–4:30 from charge, and he has seen others at nearly 6 min [S0029](../sources/S0029-homeroasters-roast-assistant-for-skywalker.md). A Probat test found a ~35 s change in the drying stage audible in the cup [S0035](../sources/S0035-sweet-marias-stretchin-out-the-roast-pt3.md). No cup data link your dry end to anything yet.

## The one cupped roast — id39 (Costa Rican Natural, 2026-10-09)
Development 0:41 (DTR 7.4 %), drop 192 °C, loss 12.9 %, heater cut to 17 % after first crack.
Cup at 5 days: *unpleasant bitterness, very acidic when cooled, no clear flavour, medium body.*

- "Very acidic, especially as it cools" + "no clear flavour" fit **under-development**
  (aggressive acidity, lack of sweetness) [S0010](../sources/S0010-hoos-loring-avoiding-roasting-defects.md) [S0006](../sources/S0006-alstrup-2020-development-time-sensory.md). Acidity is highest around first crack and
  drops as roasting continues [S0007](../sources/S0007-anokye-bempah-2024-titratable-acidity.md); dropping 41 s after first crack leaves it high.
- Losing pleasantness as it cools is also Rao's description of **baked** coffee [S0008](../sources/S0008-rao-what-is-baked-coffee.md); the big
  heater cut right after first crack could be a candidate, though the logged RoR at drop (8.5 °C/min)
  shows no crash. **Not resolvable from one cup.**
- **Bitterness** is unexpected in a light, short roast. Possible: brew/extraction, rest time, or the
  coffee. Worth re-tasting id40 (same coffee, 1:12 development) side by side.

Added in Build 5: id39 ended only **+6.2 °C** above its first-crack reading (median +8.3 °C), close to
the ~+5.6–7 °C where one roaster says a vegetal note disappears [S0023](../sources/S0023-home-barista-vegetal-flavor-first-crack.md) — consistent with the
"under-developed" reading, but same caveats as above. id40 (same coffee, +12.0 °C) is the natural
comparison once it has rested.

Added in Build 6: id39 was cupped after only 5 days. Forum advice for light roasts runs from a week to 4–6 weeks [S0036](../sources/S0036-home-barista-hacea-roast-approach-tasting-kit.md), and a lab study shows light roasts keep degassing for hundreds of hours [S0042](../sources/S0042-smrke-2018-time-resolved-gravimetric-degassing.md) — though nothing ties that to taste. Part of "bitter, very acidic when cooled, no clear flavour" could be rest, which is another reason to re-cup id39's coffee (and id40) at several rests — see [Resting & degassing](../kb/resting-and-storage.md).

**n = 1 — treat as a lead, not a finding.**

## What would make these findings much stronger
1. Cupping notes for most roasts (even 3 lines: sweetness, acidity, bitterness, anything off).
   Other owners' best results were judged by cupping — without notes, their recipes can't be
   compared with yours.
2. Label the coffee in Artisan every time (11 early roasts are unlabelled).
3. Always enter the roasted weight (13 roasts have no output weight).
4. Note probe depth, room temperature and how you marked first crack (first pop vs regular pops) — both shift
   readings and development time [S0015](../sources/S0015-homeroasters-skywalker-roasts-thread.md) [S0019](../sources/S0019-sweet-marias-first-crack-faq.md) [S0045](../sources/S0045-home-barista-quest-m6-first-crack-temperature-probe-depth.md).
5. Log green moisture (or at least density) and the days of rest at each cupping — weight loss and cup notes can't be read without them [S0030](../sources/S0030-royal-coffee-understanding-roast-yield-and-loss.md) [S0042](../sources/S0042-smrke-2018-time-resolved-gravimetric-degassing.md).
