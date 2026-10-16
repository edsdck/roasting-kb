---
title: Green coffee
---

# Green coffee

!!! abstract "In short"
    - **Density** is a better guide than altitude: denser beans take heat slowly at first, then transfer it efficiently, tolerate more heat, and hold more water. `conf: low`
    - Measure it cheaply (weigh a fixed volume) and log it with each roast.
    - Let the flavour you want drive the profile; density only changes *how* you drive the roaster.
    - First crack is driven mainly by steam from the bean's ~10–12 % moisture; older/drier coffees crack louder, some naturals crack very quietly. `conf: low`
    - Processing changes how coffees are roasted (the Skywalker's own presets differ by natural/washed/honey), but whether it changes the first-crack *temperature* is **contested**.

## Concepts
- **Density and elevation.** Higher-grown coffee ripens slower and tends to be denser — e.g.
  687.5 kg/m³ at 1,400–1,500 m vs 619.75 kg/m³ at 800–900 m in a Nepal study — but latitude and
  climate make elevation alone unreliable. `conf: low` [S0014](../sources/S0014-lee-2025-bean-density-roasting.md)
- **Heat behaviour.** Dense beans absorb energy slowly at first, then transfer heat internally more
  efficiently; they also tend to contain more water, which can cause a stall approaching first
  crack. `conf: low` `ctx: gas-drum` [S0014](../sources/S0014-lee-2025-bean-density-roasting.md)
- **Defect susceptibility.** Bean shape, density and growing altitude affect how easily beans tip.
  [S0010](../sources/S0010-hoos-loring-avoiding-roasting-defects.md)
- **Moisture and first crack.** Green coffee holds roughly 10–12 % moisture; first crack is mainly
  steam pressure from it. Older or drier coffee, and less dense (often lower-grown) coffee, can
  crack louder; some high-grown dry-process (natural) coffees have a very quiet, short first crack.
  `conf: low` [S0019](../sources/S0019-sweet-marias-first-crack-faq.md)
- **Processing and first-crack temperature.** On the same machine, some roasters see first crack at
  the same reading for all beans; others find it bean-dependent. A decaf cracked late (~189 °C) on a
  Skywalker. **Contested** — see [Measurement § Contested](measurement-and-artisan.md#contested).
  [S0020](../sources/S0020-home-barista-bean-temperature-at-first-crack.md) [S0019](../sources/S0019-sweet-marias-first-crack-faq.md) [S0015](../sources/S0015-homeroasters-skywalker-roasts-thread.md)
- **Coffee type and very short development.** Nordic roasters found Kenyans respond well to very
  short, hot roasts but Brazilians wouldn't [S0022](../sources/S0022-home-barista-nordic-roasters-forum-exercise.md); one home roaster found dry-processed coffees did
  better with shorter development [S0022](../sources/S0022-home-barista-nordic-roasters-forum-exercise.md); another says only very good coffees "shine" with short
  light roasts [S0022](../sources/S0022-home-barista-nordic-roasters-forum-exercise.md). `conf: low`

## In practice
- **Dense coffee:** higher charge, then more energy after colour change; keep heat up into first
  crack to avoid a stall; can take more heat in development, possibly a slightly higher drop.
  `conf: low` [S0014](../sources/S0014-lee-2025-bean-density-roasting.md)
- **Lower-density coffee** aimed at sweetness and body: gentler, slower heat, longer browning
  (Maillard), possibly darker. `conf: low` [S0014](../sources/S0014-lee-2025-bean-density-roasting.md)
- **Flavour first.** Even if a dense coffee *can* take more heat, the desired cup decides the
  profile. [S0014](../sources/S0014-lee-2025-bean-density-roasting.md)
- **Moisture sets how hard to push and how much weight to lose.** Per Rob Hoos: wetter coffee is
  harder to push heat into (water resists heat uptake after boiling point), so it needs more energy
  in the middle of the roast, shows a slightly higher turning point and can seem to run away early
  before it lags; drier coffee may need less. For light roasts he aims for weight loss ~1–2 % above
  the green moisture (10 % moisture → 11–12 %; 12 % → 13–14 %). `conf: low` `ctx: drum` [S0025](../sources/S0025-roast-rebels-hoos-cultivars-airflow-interview.md)
- **Cultivar and processing set the timings.** Hoos sets roast length, development time and
  first-crack time from cultivar and processing (naturals: slightly shorter development in his
  fruit-forward recipe), and heat application from moisture and density. Typica and Ethiopian-type
  cultivars prefer slightly faster roasts, Bourbon types slower; "fast" is a trend, not a rule.
  `conf: low` [S0025](../sources/S0025-roast-rebels-hoos-cultivars-airflow-interview.md)
- **Measure:** weigh a fixed volume of green (measuring cylinder), log g/L. [S0014](../sources/S0014-lee-2025-bean-density-roasting.md)

## On the Skywalker (IR)
- **Inference — test it:** gas/airflow levers translate to lamp power (slow-acting) and fan
  (removes heat) [S0001](../sources/S0001-skywiki-infrared-roaster.md) [S0003](../sources/S0003-skywiki-renatoa-words-of-wisdom.md). For a dense coffee that means starting higher and making the
  "push" earlier than you would on gas, to beat the lamp lag.
- Start logging density with each roast — see [experiments](../skywalker/experiments.md).
- The factory auto profiles treat processing differently: preheat 200 °C (natural) / 220 °C
  (washed) / 215 °C (honey); start power 65 / 70 / 65 % [S0016](../sources/S0016-homeroasters-skywalker-main-thread.md).
- **Inference — test it:** your median weight loss is 13.4 % (n=28). On Hoos's rule that fits
  coffee with ~11.5–12.5 % moisture roasted light, but your green moisture is unknown — ask the
  supplier or use a meter before reading anything into it [S0025](../sources/S0025-roast-rebels-hoos-cultivars-airflow-interview.md).
- **Your data (P):** Honduras Honey cracks ~6 °C higher than your washed coffees — see
  [findings](../skywalker/findings.md).

## Open questions
- Measured moisture/density vs first-crack temperature and time — no data yet.
- Does processing change the first-crack temperature, or only how it's measured/heard?
  Roasters still split: same ±2 °C for all beans vs a new origin cracking 5–5.6 °C higher [S0024](../sources/S0024-home-barista-first-crack-temperature-changed.md).
- What is the green moisture of the coffees you roast (needed to use the weight-loss rule)?
- How radiant heating interacts with density (surface vs core).
