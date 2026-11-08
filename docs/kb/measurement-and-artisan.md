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
    - **The RoR line is always late — by half the delta span** (15 s span → 7.5 s late), and smoothing adds more. Cut noise at the source, then use the shortest span that is still readable. `conf: medium`
    - **Colour is the profile-independent marker:** in a 39-roast study ground coffee read the same colour at first crack (L* ≈ 30) whatever the profile or origin — but colour numbers don't transfer between meters. `conf: medium` `ctx: gas-drum`
    - **Probe depth alone moved one Quest M6's first-crack reading by ~11 °C** (362–369 °F with the tip about 1 in into the drum, 380–390 °F at about 1.75 in) — more than your own first-crack spread (SD 4.3 °C). Check depth before trusting any first-crack temperature. `conf: low` (one owner, two roasts)

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
  ~201–208 °C (adj. ≈ 185–192 °C) [S0019](../sources/S0019-sweet-marias-first-crack-faq.md); Quest and Aillio Bullet owners see ~200 °C (adj. ≈ 185 °C) [S0020](../sources/S0020-home-barista-bean-temperature-at-first-crack.md). See [Temperatures](temperature-adjustment.md). `ctx: convection/drum`
- **Batch size shifts readings.** With smaller loads the probe is surrounded by more air, so it
  reads lower; production roasters see the same (227 °C full vs 224 °C half batch; adj. ≈ 211 vs 208 °C). The probe must
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
- **Probe thickness changes the curve, not the coffee.** Hoos ran 1.6, 3.2 and 6.4 mm thermocouples in the same roast: turnaround came at 0:47, 1:43 and 2:46, and only the thinnest probe showed the reaction to a burner change around first crack. After his roastery swapped a 6.4 mm for a 1.6 mm drop-door probe, the thin one showed a **negative RoR after first crack** on batches that looked on-profile on the thick probe and tasted slightly baked. Placement adds to this through exposure to airflow and radiant energy. His conclusion: readings are relative, good for consistency, and quality is checked by colour, weight loss and cupping. `conf: medium` (one B source, measured) `ctx: drum` [S0067](../sources/S0067-hoos-our-world-through-a-keyhole-thermocouple-limits.md)
- **…but thinner is not simply better.** MaKoMo (works on Artisan) uses a 3 mm probe as the compromise between speed, noise and durability: thinner probes break sooner and need more smoothing, the sheath's mass acts as a useful filter, and "RTDs are slower than thermocouples" is misleading. He also questions the hot-water method of Hoos's speed test. Drum bean RoR rarely exceeds 30 °C/min after dry end, so a system need not be faster than that. `conf: low` [S0068](../sources/S0068-makomo-artisan-blog-on-idle-noise-rtd-vs-tc-ror-delay.md)
- **Colour at the milestones is nearly fixed.** UC Davis sampled 39 roasts every minute (seven very different 16-minute profiles, three coffees, 5 kg Probat): every ground sample fell on one curve in L*a*b* space, and the colour at colour change, first crack and second crack barely moved with profile or origin (L* 62.4 ± 2.6 / **29.7 ± 1.9** / 20.0 ± 1). Faster profiles only got there sooner. A check against 20 published studies mostly agreed. `conf: medium` (one A study; same dataset as [S0007](../sources/S0007-anokye-bempah-2024-titratable-acidity.md)) `ctx: gas-drum` [S0066](../sources/S0066-anokye-bempah-2025-universal-color-curve-roasted-arabica.md)
- **Colour numbers are instrument-specific.** There is no agreed definition of light/medium/dark, and an Agtron number on one device "may not correspond to the same value on other devices"; the study measured ground coffee on a lab spectrophotometer [S0066](../sources/S0066-anokye-bempah-2025-universal-color-curve-roasted-arabica.md). Compare colours only from the same meter and the same grind.
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
- **Span and smoothing are the same trade.** A longer delta span, averaging smoothing and a longer sampling interval all make the RoR smoother *and later*; the lag from the span alone is half its length. MaKoMo cut idle noise at the source (3 mm PT100 RTD on a quiet meter: noise StdDev 2.64 → 0.09) and now runs a 1 s span with no smoothing; Artisan's "optimal smoothing", which avoids the time shift, only works offline (not while recording). Low-resolution readings (0–1 decimal) add digital noise to the RoR. `conf: medium` [S0068](../sources/S0068-makomo-artisan-blog-on-idle-noise-rtd-vs-tc-ror-delay.md)
- **What others run.** A Santoker with RTDs: 1 s sampling, 10 s span (≥ 5 s late); a Mill City 1 kg needed 15 s and stayed noisier; a home roaster with a K-type at 15 s span saw "quite a bit of delay", and after switching to an RTD ran 1 s / no smoothing / 1 s span [S0069](../sources/S0069-home-barista-on-idle-noise-thread-artisan-delta-span.md). On a Kaleido M2 (IR/hybrid) owners call a spiky RoR normal and say to read the general shape; one used a 20 s / 40 Delta BT filter with polyfit and optimal smoothing [S0071](../sources/S0071-home-barista-new-to-artisan-ror-curve-help-kaleido-m2.md) — about 10 s of lag by the half-span rule, and the optimal part applies only after the roast [S0068](../sources/S0068-makomo-artisan-blog-on-idle-noise-rtd-vs-tc-ror-delay.md). `conf: low`
- **Measure idle noise to pick a span.** Record ~2 minutes with nothing happening (0.5–1 s sampling), look at how much the RoR wanders, then take the smallest span that removes it; real roasts may need a bit more [S0068](../sources/S0068-makomo-artisan-blog-on-idle-noise-rtd-vs-tc-ror-delay.md). A probe that is dead still looks quieter than it is — let the temperature drift a little while you test [S0069](../sources/S0069-home-barista-on-idle-noise-thread-artisan-delta-span.md).
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
- **Your data (P, n=42):** first crack median 184.5 °C (174–193 °C), in line with other owners;
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
  *Build 8:* do it by measurement instead of by eye — with the drum turning, fan at your usual
  setting and the heater off (or steady), record two minutes and pick the shortest span that
  flattens the RoR [S0068](../sources/S0068-makomo-artisan-blog-on-idle-noise-rtd-vs-tc-ror-delay.md). Remember the price: 15 s span = 7.5 s late, on top of the lamp lag. The RoR
  on your roast pages here is computed over 30 s, so it is about 15 s late (derived from [S0068](../sources/S0068-makomo-artisan-blog-on-idle-noise-rtd-vs-tc-ror-delay.md)).
- **Inference — test it:** your stock NTC probe is already rolling-averaged by the roaster [S0017](../sources/S0017-homeroasters-skywalker-mods-thread.md),
  which behaves like a thick probe: a short RoR dip after first crack — the kind Hoos's thin probe
  revealed on "slightly baked" batches [S0067](../sources/S0067-hoos-our-world-through-a-keyhole-thermocouple-limits.md) — may not show on your curve at all. A flat-looking
  development on your log is not proof that there was no dip.
- **Inference — test it:** colour is the one roast-degree marker that barely moves with the profile [S0066](../sources/S0066-anokye-bempah-2025-universal-color-curve-roasted-arabica.md). If you get any colour reading (phone app or meter), always grind the same way and use the same device, and log it with weight loss; it is the best way to compare roasts whose times differ.
- **Inference — test it:** four things that are not the coffee have each been shown to move a first-crack reading by several degrees — probe depth (~11 °C on a Quest [S0045](../sources/S0045-home-barista-quest-m6-first-crack-temperature-probe-depth.md)), probe type (~11 °C between K-type and RTD on a gas drum [S0054](../sources/S0054-home-barista-conduction-vs-convection-test-results-are-confusing.md)), which pop you call (a stray pop can lead the main crack by 5.6–8.3 °C [S0055](../sources/S0055-home-barista-underdeveloped-coffee-1kg-drum.md)) and, on one hot-air drum, airflow [S0053](../sources/S0053-home-barista-desnudo-conduction-convection-thread-roest-airflow.md). Your first-crack readings have a 19.4 °C full range (SD 4.3 °C); keep depth, probe, call and fan fixed before reading any of it as a coffee effect.
- The 2019 matched-profile pilot left temperature out on purpose, because probes differ between machines, and matched times and colour instead [S0056](../sources/S0056-cooper-hoos-2019-can-you-taste-the-roasting-system.md) — the same reason this base prefers time after first crack to absolute temperature.

## Contested
**Does first crack happen at a different temperature for different coffees?**

- **No — it's the measurement.** Two experienced roasters report first crack at the same reading
  for every bean over hundreds of batches (Quest: 200 °C ± 1–2; Aillio Bullet: 200 °C ± 2–3; adj. ≈ 185 °C);
  probe type and placement matter far more than the bean. Grade C. [S0020](../sources/S0020-home-barista-bean-temperature-at-first-crack.md)
- **Same again on a third Quest account (2026):** FC is the same ±2 °C (200 °C on his Quests) for
  nearly all greens; probe placement matters more than bean type; first check for a loose or bent
  probe. He drops by absolute bean temperature [S0024](../sources/S0024-home-barista-first-crack-temperature-changed.md). Grade C.
- **Probe depth is a measurement effect big enough to mimic a coffee effect.** A Quest M6 owner (400 g, Phidgets PT1000, Artisan) read first crack at 362–369 °F (183–187 °C); other owners give the usual ~392 °F (200 °C ± 1), a M3 at ~392 vs an M3S at ~400 °F with the same probes and meter. Suggested reasons for the low reading: the tip is only about 1 in into the drum, a small batch does not cover it, and the metal shield pulls heat out of the tip. After pushing the probe in to about 1.75 in the same roaster read 380–390 °F (193–199 °C). Grade C, a clear before/after. [S0045](../sources/S0045-home-barista-quest-m6-first-crack-temperature-probe-depth.md)
- **Probe type moved the reading by about 11 °C too (gas drum).** An owner of a '2k' MCR drum swapped K-type thermocouples for RTD probes: the roaster then read about 11 °C (20 °F) lower and first crack appeared at 185 °C (365 °F) instead of the usual 196 °C (385 °F); an offset felt wrong, so he went back to K-type and 385 °F returned. He adds that the bean probe in a drum mostly reads the probe itself. Grade C, a clear before/after. `conf: low` [S0054](../sources/S0054-home-barista-conduction-vs-convection-test-results-are-confusing.md)
- **Which pop you call.** The first stray pop can come 10–15 °F (5.6–8.3 °C) or more before the rest of the popping, so a first-crack temperature taken at the first pop reads lower and makes development look longer; call it at three or more pops in about a second [S0055](../sources/S0055-home-barista-underdeveloped-coffee-1kg-drum.md). Grade C, `ctx: gas-drum`.
- **Airflow can move the probe reading.** On one Roest the bean-probe readings ran higher in a high-airflow roast than in a low-airflow roast of the same coffee; the owner puts this down to faster transfer to the probe. Grade C, not a measured probe test. `conf: low` `ctx: electric drum` [S0053](../sources/S0053-home-barista-desnudo-conduction-convection-thread-roest-airflow.md)
- **Yes — roaster, bean and profile all matter.** Another roaster finds FC "very roaster, bean and
  profile dependent" (200–207 °C on a 1 kg drum; adj. ≈ 185–192 °C) [S0020](../sources/S0020-home-barista-bean-temperature-at-first-crack.md); Sweet Maria's says readings vary with
  measurement and altitude [S0019](../sources/S0019-sweet-marias-first-crack-faq.md). A decaf on a Skywalker cracked late (~189 °C) [S0015](../sources/S0015-homeroasters-skywalker-roasts-thread.md). A drum roaster that always cracked at 197 °C (adj. ≈ 185 °C) saw 202 °C (adj. ≈ 190 °C) with a new origin [S0024](../sources/S0024-home-barista-first-crack-temperature-changed.md); another roaster sees 199–202 °C usually (adj. ≈ 185–188 °C) and ~204 °C (adj. ≈ 189 °C) on a new Ethiopian [S0024](../sources/S0024-home-barista-first-crack-temperature-changed.md); a third believes FC depends on bean, entry rate and profile, and marks it at a set temperature when he cannot hear it [S0024](../sources/S0024-home-barista-first-crack-temperature-changed.md). Grade C.
- **Possible mechanisms (untested):** a faster approach might raise the surface reading at crack
  (surface–core gap) [S0020](../sources/S0020-home-barista-bean-temperature-at-first-crack.md); the probe offset may differ by coffee [S0017](../sources/S0017-homeroasters-skywalker-mods-thread.md); quiet first cracks in
  some dry-process coffees could be marked late [S0019](../sources/S0019-sweet-marias-first-crack-faq.md).
- **Moisture alone doesn't set it (one test):** dehydrated green beans still cracked audibly at the same temperature as normal green, which argues against a simple residual-moisture explanation for what sets the first-crack reading. `ctx: IKAWA, fluid bed` [S0031](../sources/S0031-home-barista-add-moisture-during-a-roast.md)
- **Your data (P):** across all roasts, later first crack goes with a higher reading (r = 0.73,
  n=41), but *within* one coffee the link is weak (Honduras r = 0.16, Ethiopia r = 0.05). The
  Honduras roasts were both slower and higher-reading, so coffee and roast speed can't be separated
  yet.

Open — see [experiments](../skywalker/experiments.md).

- **Your first-crack spread (P, n=42):** SD 4.3 °C; range 173.8–193.2 °C (19.4 °C wide; the low end is id40); 24 of 42 within ±3.5 °C of the median 184.5 °C. renatoa's reference is 182 °C with about a 7-degree spread by origin on a Skywalker [S0029](../sources/S0029-homeroasters-roast-assistant-for-skywalker.md) — consistent in size with your middle half but narrower than your full range. The Quest M6 probe-depth change (~11 °C) [S0045](../sources/S0045-home-barista-quest-m6-first-crack-temperature-probe-depth.md) is larger than your whole interquartile spread, so a loose, moved or re-seated probe can fake a coffee effect on yours too. **Inference — test it:** note probe depth and whether the tip is covered by the 350 g pile each time you re-seat it.
- **Optional tool:** renatoa built a spy-only ESP32 add-on that reads the roaster's panel protocol, shows time, temperature, RoR, power and air on an LCD (later an Android app) and auto-detects charge, turning point, dry end, first crack and drop, with a trend arrow for the RoR; control stays on the original panel. Grade C, a forum post, not a product. [S0029](../sources/S0029-homeroasters-roast-assistant-for-skywalker.md)

## Open questions
- Recommended Artisan smoothing/delta-span on a Skywalker from experienced owners — still none; general method now known (idle noise, half-span lag [S0068](../sources/S0068-makomo-artisan-blog-on-idle-noise-rtd-vs-tc-ror-delay.md)) and the closest IR-type setting is one Kaleido owner's 20 s / 40 [S0071](../sources/S0071-home-barista-new-to-artisan-ror-curve-help-kaleido-m2.md). An idle-noise recording on your own V1 would answer it.
- Why first crack reads higher for some coffees on the same machine (above).
