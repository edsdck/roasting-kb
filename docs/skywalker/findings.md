# Findings from my roasts

*Maintained by the Builder from the [roast log](roast-log.md) and cupping notes. Personal evidence
(grade **P**): the best evidence for this machine, but uncontrolled, one roaster, and only one roast
cupped so far. Updated 2026-10-16 (Build 4), 41 roasts (Jan–Oct 2026).*

!!! abstract "In short"
    - **First crack reads ~184 °C** on your machine (median of 41 roasts; range 174–193 °C) — matching other Skywalker owners (179–183 °C), far below the ~200 °C of convection roasters.
    - **Honduras Honey cracks ~6 °C higher** — but those roasts were also slower, and *within* each coffee FC time barely predicts FC temperature. Coffee vs speed can't be separated yet.
    - **Your development has shortened a lot:** median 1:37 (DTR 16.5 %) in Jan–Feb → **~1:00 (DTR ~9 %)** since June. That's shorter than the *"fast"* roast in the key development study (1:30), shorter than typical light roasters (1:20–1:30, 13–16 %) and the best roast reported by an experienced Skywalker owner (~1:35, 18 %) — but not unheard of (Nordic ~45 s).
    - Development time predicts your weight loss strongly (r = 0.72, n = 28) — more than drop temperature (r = 0.42).
    - The one roast you cupped (id39: 0:41 development, heater cut to 17 % right after first crack) tasted bitter, very acidic when cooled, with no clear flavour.
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

**2b. How far above first crack you drop (new, n=41).** Median drop is **+8.3 °C** over the
first-crack reading (5.6–22.4 °C), and it moves with development time (r = 0.78). Four roasts ended
under 6 °C above first crack (id4, id19, id31, id32). N3Roaster reports a vegetal note that stays
until ~10 °F (5.6 °C) above first-crack start on his machines, independent of time, and another
roaster puts it at ~+6–7 °C [S0023](../sources/S0023-home-barista-vegetal-flavor-first-crack.md). The id39 roast (cupped sharp, very acidic, bitter) ended +6.2 °C;
id40 (same coffee) ended +12.0 °C but has no notes yet. Different probe and first-crack convention,
so this is a lead, not a rule. → [experiment 2](experiments.md). *Grade P, n=41 but only one cup.*

**3. Weight loss follows development time.** Correlation 0.72 between development time and weight
loss (n=28 roasts with output weight), vs 0.42 for drop temperature. On your machine, *how long* you
develop moves roast degree more than the drop temperature you choose. Light roasts throughout
(12–16 % loss).

**4. Heater handling around first crack.** Typically heater ~60 % a minute before first crack,
~50 % at first crack, 40–55 % in development (31 logged roasts) — moderate steps, consistent with the
advice to use few, modest changes on this lamp-driven machine [S0001](../sources/S0001-skywiki-infrared-roaster.md). Compare renatoa's
schedule (250 g): 70 % after the turning point, then 65 → 60 → 55 → 50 % between dry end (3:31) and 5:32,
first crack at 7:00, fan 65 → 80 % [S0015](../sources/S0015-homeroasters-skywalker-roasts-thread.md) — he starts reducing earlier (around dry end/minute 4) and in more
steps than the factory logic [S0017](../sources/S0017-homeroasters-skywalker-mods-thread.md). **Exception: id39** — 70 % →
50 % → **17 %** within ~30 s of first crack, then dropped at 0:41.

**5. The Honduras Honey series (id20–id34, 14 roasts).** Charge varied 141–186 °C, batch 325–375 g,
first crack 9:18–13:23. Lower charge → much later first crack (141.5 °C charge: FC 12:21; 186 °C:
FC 9:46). No cupping notes, so flavour effects are unknown.

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

**n = 1 — treat as a lead, not a finding.**

## What would make these findings much stronger
1. Cupping notes for most roasts (even 3 lines: sweetness, acidity, bitterness, anything off).
   Other owners' best results were judged by cupping — without notes, their recipes can't be
   compared with yours.
2. Label the coffee in Artisan every time (11 early roasts are unlabelled).
3. Always enter the roasted weight (13 roasts have no output weight).
4. Note room temperature and how you marked first crack (first pop vs regular pops) — both shift
   readings and development time [S0015](../sources/S0015-homeroasters-skywalker-roasts-thread.md) [S0019](../sources/S0019-sweet-marias-first-crack-faq.md).
