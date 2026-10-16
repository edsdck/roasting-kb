---
title: Measurement & Artisan
---

# Measurement & Artisan

!!! abstract "In short"
    - A bean probe in a moving bean pile reads an **air–bean average**, not bean temperature. `conf: medium`
    - On the Skywalker the air is cooler than the beans, so readings are **lower than on hot-air machines**: first crack shows around **180–185 °C**, vs ~200 °C on convection roasters with contact probes. `conf: high`
    - Probe type and placement move the number by 10–20 °C; what matters is that *your* probe is consistent through development. `conf: medium`
    - **Does first-crack temperature depend on the coffee?** Some roasters see the same reading for every bean; others (and your Honduras Honey) don't. **Contested.**
    - Treat temperatures as machine-specific; compare by time, events (first crack), weight loss and colour.

## Concepts

- **What the probe sees.** Point-contact probes can't read the surface of moving solids; they read
  an average including the surrounding air. `conf: medium` [S0003](../sources/S0003-skywiki-renatoa-words-of-wisdom.md) [S0005](../sources/S0005-coffeemind-rate-of-rise-bad-reference.md) Münchow calls bean
  temperature "a relative reading", with first crack and colour the absolute indicators of how
  much energy went in [S0005](../sources/S0005-coffeemind-rate-of-rise-bad-reference.md). No probe reads the bean interior, and there's always some
  environmental influence [S0019](../sources/S0019-sweet-marias-first-crack-faq.md).
- **Skywalker readings are lower.** Because air is cooler than the beans here (unlike convection
  machines), late-roast readings are lower. First crack is reported at ~182 °C [S0001](../sources/S0001-skywiki-infrared-roaster.md), "around 180
  is the norm" (the manual gives 170–190 °C) [S0017](../sources/S0017-homeroasters-skywalker-mods-thread.md), and individual owners log 179–183 °C [S0015](../sources/S0015-homeroasters-skywalker-roasts-thread.md)
  [S0016](../sources/S0016-homeroasters-skywalker-main-thread.md). Explained by probe placement and the radiant environment rather than miscalibration;
  moving the probe wouldn't bring it up to ~200 °C. `conf: high` [S0001](../sources/S0001-skywiki-infrared-roaster.md) [S0003](../sources/S0003-skywiki-renatoa-words-of-wisdom.md) [S0015](../sources/S0015-homeroasters-skywalker-roasts-thread.md) [S0017](../sources/S0017-homeroasters-skywalker-mods-thread.md)
- **Other machines, for contrast:** contact probes on commercial roasters show first crack at
  ~201–208 °C [S0019](../sources/S0019-sweet-marias-first-crack-faq.md); Quest and Aillio Bullet owners see ~200 °C [S0020](../sources/S0020-home-barista-bean-temperature-at-first-crack.md). `ctx: convection/drum`
- **Batch size shifts readings.** With smaller loads the probe is surrounded by more air, so it
  reads lower; production roasters see the same (440 °F full vs 435 °F half batch). The probe must
  stay buried in the beans. `conf: medium` [S0003](../sources/S0003-skywiki-renatoa-words-of-wisdom.md) [S0013](../sources/S0013-melheim-2023-optimal-batch-size.md) On the Skywalker, below ~250 g the stock
  probe may not be fully immersed; at 85 g first crack read ~173 °C vs ~183 °C for larger batches
  [S0015](../sources/S0015-homeroasters-skywalker-roasts-thread.md).
- **Probe placement and type.** Owners who fitted a thermocouple beside the stock probe got very
  different numbers: one read 14–19 °C *below* stock from dry end to first crack [S0016](../sources/S0016-homeroasters-skywalker-main-thread.md); another
  read 1–15 °C *above* stock through the roast, with the gap differing between a honey and a washed
  coffee [S0017](../sources/S0017-homeroasters-skywalker-mods-thread.md). With the chamber empty the stock probe read ~15° high, but after charge the two
  agreed [S0017](../sources/S0017-homeroasters-skywalker-mods-thread.md). `conf: medium` — placement dominates.
- **A probe just above the bean bed** read the same as one buried in beans but reacted faster to
  turning point and first crack (one roaster's tests on another machine). `conf: low` [S0017](../sources/S0017-homeroasters-skywalker-mods-thread.md)
- **Probe speed.** Thicker probes respond slowly and smooth out events like an RoR crash; Rao
  suggests ≤ 4 mm (ungrounded), and checks that the turning point appears by ~1:30. `conf: low`
  `ctx: gas-drum` [S0008](../sources/S0008-rao-what-is-baked-coffee.md)
- **Early-roast artefact.** Right after charge, the probe is hotter than the beans and cools
  toward them, distorting the first minutes of the RoR curve. [S0008](../sources/S0008-rao-what-is-baked-coffee.md)
- **Your probe and connection.** The stock Skywalker V1 probe is an **NTC thermistor**; V1 has no
  built-in logging — community firmware on an Arduino Nano or ESP32-S3 translates the roaster's
  signals into the **TC4 protocol** that Artisan and HiBean read. K-type thermocouple or PT100
  upgrades exist (need the right amplifier + firmware). `conf: low` [S0009](../sources/S0009-skywiki-putrid-upstairs-response.md)
- **How good is the stock probe?** A comparable thermistor is ±3 °C at 200 °C vs ±1.5 °C for a
  K-type thermocouple — not enough to justify a swap [S0017](../sources/S0017-homeroasters-skywalker-mods-thread.md). The roaster already smooths
  (rolling-averages) its reading, and read ~1 °C low at room temperature against an RTD [S0017](../sources/S0017-homeroasters-skywalker-mods-thread.md).
  Resolution is ~0.17–0.2 °C per step [S0017](../sources/S0017-homeroasters-skywalker-mods-thread.md). `conf: low`
- **Consistency beats accuracy.** In a tumbling bean bed, absolute accuracy matters little; what
  matters is a linear, consistent reading through development, where the 8–16 °C rise after first
  crack is a *difference* and so more precise than the absolute numbers. `conf: low` [S0017](../sources/S0017-homeroasters-skywalker-mods-thread.md) Once you
  know where first crack and a good drop happen on your machine, the absolute number doesn't matter
  [S0017](../sources/S0017-homeroasters-skywalker-mods-thread.md).

## In practice — Artisan

- **RoR settings (Rao):** 1 s sampling, *delta span* ≤ 15 s, no additional smoothing. `conf: low`
  `ctx: gas-drum` [S0008](../sources/S0008-rao-what-is-baked-coffee.md)
- **Don't over-read the RoR line:** the derivative amplifies probe noise; bumps look bigger than
  they are. [S0005](../sources/S0005-coffeemind-rate-of-rise-bad-reference.md)
- **Spikes and trier pulls.** The Skywalker's data stream contains occasional temperature spikes,
  and pulling the trier causes a ~2 °C dip that recovers in ~2 s — both distort the RoR curve.
  Ignore RoR jumps right after using the trier; a spike filter (not just rolling average) helps.
  `conf: low` [S0017](../sources/S0017-homeroasters-skywalker-mods-thread.md)
- **Repeat roasts by replaying events.** Replaying a past roast's heater/fan changes (HiBean "power
  tracking") worked as well as the still-untuned community PID. `conf: low` [S0009](../sources/S0009-skywiki-putrid-upstairs-response.md) **Inference —
  test it:** Artisan can load a past roast as a *background* profile and replay its events.
- **Don't use Artisan PID aggressively on the Skywalker:** the lamp's lag causes overshoot. Use the
  data to understand the machine and plan profiles. `conf: medium` [S0001](../sources/S0001-skywiki-infrared-roaster.md) [S0005](../sources/S0005-coffeemind-rate-of-rise-bad-reference.md) [S0016](../sources/S0016-homeroasters-skywalker-main-thread.md)
- **Exhaust (ET) as a first-crack warning.** An exhaust probe rises ~10–20 s before first crack —
  useful if FC is hard to hear, too late for timing power cuts. `conf: low` [S0017](../sources/S0017-homeroasters-skywalker-mods-thread.md)
- **Marking first crack.** Mark FCs when you hear regular, successive pops, not the first isolated
  pops [S0019](../sources/S0019-sweet-marias-first-crack-faq.md); Rao marks it at "more than one or two isolated cracks" [S0018](../sources/S0018-rao-2014-development-time-ratio.md). Different marking
  habits shift development time and DTR. `conf: low`
- **Log what matters:** first crack time, drop time, weight in/out, colour (if you can measure it),
  and cupping notes. Colour plus development time describes a roast better than colour alone [S0006](../sources/S0006-alstrup-2020-development-time-sensory.md).

## On the Skywalker (IR)
- **Your data (P, n=41):** first crack median 184.5 °C (174–193 °C), in line with other owners;
  Honduras Honey ran ~6 °C higher than washed coffees at the same batch size — see
  [findings](../skywalker/findings.md).
- The V1 panel's RoR is a once-a-minute average, not a live RoR — use Artisan's. [S0015](../sources/S0015-homeroasters-skywalker-roasts-thread.md) [S0016](../sources/S0016-homeroasters-skywalker-main-thread.md)
- Compare your roasts to each other, not to published drop temperatures. Your roast pages show
  first crack and drop temperatures for this purpose.
- Keep batch size constant when comparing temperatures (350 g vs 400 g will read differently) [S0003](../sources/S0003-skywiki-renatoa-words-of-wisdom.md).
- **Inference — test it:** log ground colour (if you can get a reading) next to drop temperature;
  one roaster found ground colour followed drop temperature better than development time [S0024](../sources/S0024-home-barista-first-crack-temperature-changed.md).
- **Inference — test it:** with a slow-responding probe/lamp system, try a delta span around 15 s
  and see whether the curve becomes too noisy to read; adjust and note the setting.

## Contested
**Does first crack happen at a different temperature for different coffees?**

- **No — it's the measurement.** Two experienced roasters report first crack at the same reading
  for every bean over hundreds of batches (Quest: 200 °C ± 1–2; Aillio Bullet: 200 °C ± 2–3);
  probe type and placement matter far more than the bean. Grade C. [S0020](../sources/S0020-home-barista-bean-temperature-at-first-crack.md)
- **Same again on a third Quest account (2026):** FC is the same ±2 °C (200 °C on his Quests) for
  nearly all greens; probe placement matters more than bean type; first check for a loose or bent
  probe. He drops by absolute bean temperature [S0024](../sources/S0024-home-barista-first-crack-temperature-changed.md). Grade C.
- **Yes — roaster, bean and profile all matter.** Another roaster finds FC "very roaster, bean and
  profile dependent" (392–405 °F on a 1 kg drum) [S0020](../sources/S0020-home-barista-bean-temperature-at-first-crack.md); Sweet Maria's says readings vary with
  measurement and altitude [S0019](../sources/S0019-sweet-marias-first-crack-faq.md). A decaf on a Skywalker cracked late (~189 °C) [S0015](../sources/S0015-homeroasters-skywalker-roasts-thread.md). A drum roaster that always cracked at 386 °F saw 395 °F with a new origin [S0024](../sources/S0024-home-barista-first-crack-temperature-changed.md); another roaster sees 390–395 °F usually and ~400 °F on a new Ethiopian [S0024](../sources/S0024-home-barista-first-crack-temperature-changed.md); a third believes FC depends on bean, entry rate and profile, and marks it at a set temperature when he cannot hear it [S0024](../sources/S0024-home-barista-first-crack-temperature-changed.md). Grade C.
- **Possible mechanisms (untested):** a faster approach might raise the surface reading at crack
  (surface–core gap) [S0020](../sources/S0020-home-barista-bean-temperature-at-first-crack.md); the probe offset may differ by coffee [S0017](../sources/S0017-homeroasters-skywalker-mods-thread.md); quiet first cracks in
  some dry-process coffees could be marked late [S0019](../sources/S0019-sweet-marias-first-crack-faq.md).
- **Your data (P):** across all roasts, later first crack goes with a higher reading (r = 0.73,
  n=41), but *within* one coffee the link is weak (Honduras r = 0.16, Ethiopia r = 0.05). The
  Honduras roasts were both slower and higher-reading, so coffee and roast speed can't be separated
  yet.

Open — see [experiments](../skywalker/experiments.md).

## Open questions
- Recommended Artisan smoothing/delta-span on a Skywalker from experienced owners.
- Why first crack reads higher for some coffees on the same machine (above).
