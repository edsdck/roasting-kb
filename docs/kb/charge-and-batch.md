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

## Concepts

- **Capacity guidelines.** ~80 % of drum capacity as a maximum; suggested minimums vary (20, 25 or
  40 %). `conf: low` `ctx: commercial drums` [S0013](../sources/S0013-melheim-2023-optimal-batch-size.md)
- **Readings shift with batch size.** The same coffee was dropped at 440 °F in a full batch but
  435 °F in a half batch [S0013](../sources/S0013-melheim-2023-optimal-batch-size.md); on the Skywalker smaller loads read lower because the probe sees
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

## On the Skywalker (IR)
- Rated 400–500 g (sources differ) [S0009](../sources/S0009-skywiki-putrid-upstairs-response.md); users prefer 350–450 g [S0009](../sources/S0009-skywiki-putrid-upstairs-response.md). 350 g = 70–88 % of
  capacity.
- Heatsink mod fitted → back-to-back roasts are reasonable; watch drum-motor heat in long
  sessions [S0009](../sources/S0009-skywiki-putrid-upstairs-response.md).
- **Inference — test it:** "10 °C per kg" doesn't scale down meaningfully; a 50 g change is
  ~14 % of your batch. Measure it instead: [experiment 4](../skywalker/experiments.md).
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
