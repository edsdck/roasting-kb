---
title: Measurement & Artisan
---

# Measurement & Artisan

!!! abstract "In short"
    - A bean probe in a moving bean pile reads an **air–bean average**, not bean temperature. `conf: medium`
    - On the Skywalker the air is cooler than the beans, so readings — especially late in the roast — are **lower than on hot-air machines**: first crack shows around **~182 °C**. `conf: medium`
    - Smaller batches read lower still (more air around the probe).
    - Treat temperatures as machine-specific; compare by time, events (first crack), weight loss and colour.

## Concepts

- **What the probe sees.** Point-contact probes can't read the surface of moving solids; they read
  an average including the surrounding air. `conf: medium` [S0003](../sources/S0003-skywiki-renatoa-words-of-wisdom.md) [S0005](../sources/S0005-coffeemind-rate-of-rise-bad-reference.md) Münchow calls bean
  temperature "a relative reading", with first crack and colour the absolute indicators of how
  much energy went in [S0005](../sources/S0005-coffeemind-rate-of-rise-bad-reference.md).
- **Skywalker readings are lower.** Because air is cooler than the beans here (unlike convection
  machines), late-roast readings are lower; first crack has been read around ~182 °C, explained by
  probe placement and the radiant environment rather than miscalibration. `conf: medium` [S0001](../sources/S0001-skywiki-infrared-roaster.md) [S0003](../sources/S0003-skywiki-renatoa-words-of-wisdom.md)
- **Batch size shifts readings.** With smaller loads the probe is surrounded by more air, so it
  reads lower. `conf: low` [S0003](../sources/S0003-skywiki-renatoa-words-of-wisdom.md)
- **Probe speed.** Thicker probes respond slowly and smooth out events like an RoR crash; Rao
  suggests ≤ 4 mm (ungrounded), and checks that the turning point appears by ~1:30. `conf: low`
  `ctx: gas-drum` [S0008](../sources/S0008-rao-what-is-baked-coffee.md)
- **Early-roast artefact.** Right after charge, the probe is hotter than the beans and cools
  toward them, distorting the first minutes of the RoR curve. [S0008](../sources/S0008-rao-what-is-baked-coffee.md)

## In practice — Artisan

- **RoR settings (Rao):** 1 s sampling, *delta span* ≤ 15 s, no additional smoothing. `conf: low`
  `ctx: gas-drum` [S0008](../sources/S0008-rao-what-is-baked-coffee.md)
- **Don't over-read the RoR line:** the derivative amplifies probe noise; bumps look bigger than
  they are. [S0005](../sources/S0005-coffeemind-rate-of-rise-bad-reference.md)
- **Don't use Artisan PID aggressively on the Skywalker:** the lamp's lag causes overshoot. Use the
  data to understand the machine and plan profiles. `conf: medium` [S0001](../sources/S0001-skywiki-infrared-roaster.md) [S0005](../sources/S0005-coffeemind-rate-of-rise-bad-reference.md)
- **Log what matters:** first crack time, drop time, weight in/out, colour (if you can measure it),
  and cupping notes. Colour plus development time describes a roast better than colour alone [S0006](../sources/S0006-alstrup-2020-development-time-sensory.md).

## On the Skywalker (IR)
- Compare your roasts to each other, not to published drop temperatures. Your roast pages show
  first crack and drop temperatures for this purpose.
- Keep batch size constant when comparing temperatures (350 g vs 400 g will read differently) [S0003](../sources/S0003-skywiki-renatoa-words-of-wisdom.md).
- **Inference — test it:** with a slow-responding probe/lamp system, try a delta span around 15 s
  and see whether the curve becomes too noisy to read; adjust and note the setting.

## Open questions
- Exact Skywalker V1 probe type, diameter and position; how Artisan reads it (USB protocol).
- Recommended Artisan smoothing/delta-span on a Skywalker from experienced owners.
