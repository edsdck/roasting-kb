---
title: Charge & batch size
---

# Charge temperature & batch size

!!! abstract "In short"
    - Conventional range: up to ~**80 %** of rated capacity; minimums suggested from 20 % to 40 %. Starting points, not rules. `conf: low`
    - Pick the batch size that lets you hit your intended times, then keep it **fixed** — changing it shifts both dynamics and temperature readings. `conf: medium`
    - Skywalker owners mostly roast **350–450 g**; your 350 g is in that range. [S0009](../sources/S0009-skywiki-putrid-upstairs-response.md)
    - Small batches: make sure the probe stays buried in the beans — on the Skywalker, below ~250 g it may not be. `conf: medium`
    - **Don't use the Skywalker's factory preheat** (100 % heater, no air): preheat at roasting-level power (≤ 75–80 %) with ≥ 40–50 % air, and avoid the 100 % heat spike at charge. `conf: medium`
    - **Charge temperature mostly moves time.** In a Colombian production test, charges from 170 to 230 °C changed roast time from about 11.5 to 8.4 min but left the cup score unchanged when every roast was stopped at the same medium colour. `conf: medium` for that test (grade A, 5 kg units, six varieties); whether it holds for light roasts or on a lamp roaster is unknown. **Contested** against the "too-cool charge → astringent" report.

## Concepts

- **Capacity guidelines.** ~80 % of drum capacity as a maximum; suggested minimums vary (20, 25 or
  40 %). `conf: low` `ctx: commercial drums` [S0013](../sources/S0013-melheim-2023-optimal-batch-size.md)
- **Readings shift with batch size.** The same coffee was dropped at 227 °C in a full batch but 224 °C in a half batch (adj. ≈ 211 vs 208 °C) [S0013](../sources/S0013-melheim-2023-optimal-batch-size.md); on the Skywalker smaller loads read lower because the probe sees
  more air [S0003](../sources/S0003-skywiki-renatoa-words-of-wisdom.md). `conf: medium`
- **Probe immersion.** In small batches the bean probe must be fully covered by beans or readings
  mislead. `conf: medium` [S0013](../sources/S0013-melheim-2023-optimal-batch-size.md) [S0015](../sources/S0015-homeroasters-skywalker-roasts-thread.md)
- **Batch size on a radiant roaster.** Only the top layer catches the lamp, so more beans need
  proportionally more time at the same heater % [S0015](../sources/S0015-homeroasters-skywalker-roasts-thread.md); conversely a power profile found for 250 g
  gave close results on smaller loads [S0015](../sources/S0015-homeroasters-skywalker-roasts-thread.md). `conf: low` (one owner's reasoning)
- **Compensating.** When batch size changes, adjust charge temperature, heat and soak; one
  consultant uses ~10 °C per kg of batch change (multi-kilo machines). `conf: low` [S0013](../sources/S0013-melheim-2023-optimal-batch-size.md)
- **Bigger batches** raise the risk of facing, tipping, scorching and uneven development
  (dark outside, underdeveloped inside). [S0013](../sources/S0013-melheim-2023-optimal-batch-size.md) [S0010](../sources/S0010-hoos-loring-avoiding-roasting-defects.md)
- **Density and charge.** Denser coffees are often started with a higher charge temperature (and
  less airflow), then pushed after colour change. `conf: low` `ctx: gas-drum` [S0014](../sources/S0014-lee-2025-bean-density-roasting.md) See
  [Green coffee](green-coffee.md).

## In practice
- Choose batch size from the profile you want, track yellowing, first crack, development and end
  colour, and confirm by cupping. [S0013](../sources/S0013-melheim-2023-optimal-batch-size.md) [S0011](../sources/S0011-cooper-cropster-rate-of-rise-production.md)
- Keep the batch size fixed when comparing roasts — otherwise temperatures aren't comparable.

- **Charge follows batch size, not processing** — Hoos's rule for his drum roaster; wetter coffee
  may need a hotter preheat or different airflow instead [S0025](../sources/S0025-roast-rebels-hoos-cultivars-airflow-interview.md). `conf: low` `ctx: drum`
- **Charge too low → under-developed inside.** Compensating a low charge with lots of heat to reach
  first crack can leave the bean's inside behind (astringent cups); a higher charge fixed it for
  one drum roaster [S0026](../sources/S0026-home-barista-kaleido-m10-astringent-roasts.md). `conf: low` `ctx: drum`
- **Charge temperature in a production test (Cenicafé).** Six Colombian improved varieties were each roasted in five 5 kg work units per lot at charge temperatures of 200 °C (base), 215, 230, 185 and 170 °C, always stopped at Agtron/SCA 55–65 (medium). Average roast time was 11.47 min at 170 °C and 8.39 min at 230 °C (about 3 s per degree of charge); by variety, from 8.03 min (Castillo El Tambo) to 11.90 min (Castillo Pueblo Bello). Five Q-Graders found cup scores depended on variety (Castillo El Tambo 83.00 best, Castillo General 81.96 lowest) and not on charge temperature. Not reported: first-crack time or temperature, weight loss, rest days, heat source or roaster. Charge temperatures are as reported (adj. ≈ 155–215 °C with the default −15.5 °C shift, rough because a charge reading is not a first-crack reading). `conf: medium` for medium roasts; no light-roast or development-time data [S0043](../sources/S0043-osorio-2022-cenicafe-initial-roast-temperature-sensory-quality.md)
- **Preheat/charge numbers from other machines are not portable:** Quest owners charge at about 380 °F (193 °C) for a 4.5-min yellow on 400 g in an M6, or at 482–485 °F (250–252 °C) with yellow at ~4 min and a ~9.5-min roast; the fan goes to maximum after BT 150 °C and the heater to about half once first crack is under way (reported; adj. ≈ 178 / 235 °C for the two charges) `conf: low` `ctx: electric drum, Quest M6` [S0045](../sources/S0045-home-barista-quest-m6-first-crack-temperature-probe-depth.md)

## On the Skywalker (IR)
- Rated 400–500 g (sources differ) [S0009](../sources/S0009-skywiki-putrid-upstairs-response.md); users prefer 350–450 g [S0009](../sources/S0009-skywiki-putrid-upstairs-response.md). 350 g = 70–88 % of
  capacity.
- Heatsink mod fitted → back-to-back roasts are reasonable; watch drum-motor heat in long
  sessions [S0009](../sources/S0009-skywiki-putrid-upstairs-response.md).
- **Inference — test it:** "10 °C per kg" doesn't scale down meaningfully; a 50 g change is
  ~14 % of your batch. Measure it instead: [experiment 4](../skywalker/experiments.md).
- A Gen 1 owner calls the machine "very stable for a 400 g load" [S0027](../sources/S0027-coffeesnobs-skywalker-roasters-thread.md); two V1 owners work at
  350–400 g (one with 45 batches) [S0027](../sources/S0027-coffeesnobs-skywalker-roasters-thread.md). A V2 owner's light-roast recipe uses 250 g with a charge BT of
  180 °C at 60 % power [S0027](../sources/S0027-coffeesnobs-skywalker-roasters-thread.md) — different model, smaller batch. `conf: low`
- Owners call 350–400 g the machine's comfortable range [S0015](../sources/S0015-homeroasters-skywalker-roasts-thread.md); the factory start levels
  (65–70 % heater) were probably tuned for 350–400 g [S0017](../sources/S0017-homeroasters-skywalker-mods-thread.md).
- **Preheat — what the factory does:** 200 °C (naturals), 220 °C (washed), 215 °C (honey), heater
  on/off at 100 % with the fan off; overshoot ~10 °C on the first cycle, then oscillations of
  ±1–5 °C. `conf: low` [S0016](../sources/S0016-homeroasters-skywalker-main-thread.md)
- **Preheat — what experienced owners do instead:** preheat in manual mode at the power you'll roast
  with (≤ 75–80 %) and ≥ 40–50 % air — easier on the lamp (life ~100 kg; keep a spare) and, on
  115 V units, on the control board. Lowering heat and adding air ~20–30 °C before the set point
  cuts overshoot to ~2 °C. `conf: medium` [S0016](../sources/S0016-homeroasters-skywalker-main-thread.md) [S0017](../sources/S0017-homeroasters-skywalker-mods-thread.md) If you preheat manually, set the target
  above the temperature you want so the on/off logic never cuts in [S0015](../sources/S0015-homeroasters-skywalker-roasts-thread.md).
- **The charge spike.** Opening the charge door drops the reading ~5 °C and the factory preheat logic
  responds with 100 % heater until you start the roast timer. Start the roast (R) before charging,
  or preheat manually at your start settings. `conf: low` [S0016](../sources/S0016-homeroasters-skywalker-main-thread.md)
- **Charge examples (250 g, renatoa):** 200 °C held at 55 % heater / 50 % fan, raised to 65–70 % after
  the turning point [S0015](../sources/S0015-homeroasters-skywalker-roasts-thread.md); 200 °C, start 60 %, 50 % at dry end, 40 % at 170 °C for a ~8 min roast
  [S0017](../sources/S0017-homeroasters-skywalker-mods-thread.md); 160 °C at 55 % for a slow natural [S0015](../sources/S0015-homeroasters-skywalker-roasts-thread.md). Another owner: 400 g from 200 °C at 65 % / 65 %
  [S0015](../sources/S0015-homeroasters-skywalker-roasts-thread.md). **Inference — test it:** scale up for 350 g (bigger batch → more time) rather than copying.
- **Heater % isn't portable.** Settings shift ~5 % with mains voltage (238 vs 230 V) and with room
  temperature; a 125 V owner overshot badly using a 230 V recipe. `conf: low` [S0015](../sources/S0015-homeroasters-skywalker-roasts-thread.md)
- **Cooling big batches:** above ~430 g the stock tray struggles (beans still hot after 3 min); an
  external cooler did 430 g in under a minute. [S0017](../sources/S0017-homeroasters-skywalker-mods-thread.md)

- **Your charge (P):** median 181 °C (range 108–205 °C, n=41). Among the 37 roasts charged at 170 °C or above (median 185 °C) a higher charge goes with a shorter roast: total time r = −0.58 (about −4.3 s per °C), time to first crack r = −0.67 (about −5.4 s per °C). That is the same order as the production test's ~3 s per °C [S0043](../sources/S0043-osorio-2022-cenicafe-initial-roast-temperature-sensory-quality.md). Only four roasts charged lower (id5 108 °C, id28 141.5, id29 152.9, id30 166.4); their first crack came between 7:12 and 12:21, so there is no clean low-charge test. Across all 41, r = −0.48. **Inference — test it:** treat charge temperature as a time lever, and if you want to know whether a lower charge changes the cup, hold final weight loss equal and cup both.

## Contested

**Does a charge that is too cool hurt the cup?**

- **Yes:** on a drum roaster, compensating a low charge with plenty of heat to reach first crack left the inside behind and the cup astringent; a higher charge fixed it [S0026](../sources/S0026-home-barista-kaleido-m10-astringent-roasts.md). Grade C, `ctx: drum`.
- **No (within a medium-roast target):** 170 °C charges took ~3 min longer than 230 °C ones and scored the same [S0043](../sources/S0043-osorio-2022-cenicafe-initial-roast-temperature-sensory-quality.md). Grade A, 5 kg units, medium roasts only.
- **Not strictly in conflict:** the astringent case combined a low charge with a hard push; the production test only slowed the roast. **Inference — test it:** the damage may come from how much heat is applied while the beans are still wet, not from the charge number itself. Neither source covers a 350 g lamp roast aimed at light colour.
