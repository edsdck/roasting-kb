---
title: Roast planning & experimenting
---

# Roast planning & experimenting

!!! abstract "In short"
    - **Plan → Execute → Learn.** Run the plan to the end, then change the *next* roast — don't improvise mid-roast. `conf: medium`
    - Change **one variable at a time** and keep **final colour (degree) equal**, or colour will decide your cupping. `conf: medium`
    - First check if a difference is even tasteable (blind triangle test) before building theories on it.
    - On the Skywalker: 3–5 planned power changes per roast, 5–10 % each.
    - Matched time-and-colour profiles were hard to tell apart across three roasters (about 30 % correct in triangles, chance 25–33 %), so the profile, not the machine, is what to test [S0056](../sources/S0056-cooper-hoos-2019-can-you-taste-the-roasting-system.md). `conf: low` (pilot, no significance test)

## In practice

- **Plan, execute, learn.** Mid-roast corrections come too late to undo earlier decisions; finish
  the planned roast, measure how far it missed, adjust the next plan. `conf: medium` [S0005](../sources/S0005-coffeemind-rate-of-rise-bad-reference.md) [S0001](../sources/S0001-skywiki-infrared-roaster.md)
- **Few deliberate changes.** On the Skywalker, 3–5 power changes of 5–10 %; timing matters more
  than micro-adjusting. `conf: medium` [S0001](../sources/S0001-skywiki-infrared-roaster.md)
- **Ceteris paribus.** When testing airflow, drum speed etc., make sure all samples end at the same
  colour; otherwise you are really comparing roast degree. `conf: medium` [S0005](../sources/S0005-coffeemind-rate-of-rise-bad-reference.md) [S0006](../sources/S0006-alstrup-2020-development-time-sensory.md)
- **Is it perceptible?** Small profile differences at equal colour are often undetectable even by
  professionals; test with blind discrimination (e.g. triangle) before concluding. `conf: low` [S0005](../sources/S0005-coffeemind-rate-of-rise-bad-reference.md)
- **Priorities.** Roast degree (colour) moves flavour most; at equal colour, development time
  next; time to first crack least. `conf: medium` [S0012](../sources/S0012-munchow-2020-roasting-conditions-multi-study.md)
- **Plan with checkpoints** tied to physical events (yellowing, first crack) and plan heat changes
  ahead of them. [S0011](../sources/S0011-cooper-cropster-rate-of-rise-production.md)
- **Big levers first.** Development time at equal colour produces clearly different cups
  (brighter vs roastier) [S0006](../sources/S0006-alstrup-2020-development-time-sensory.md) — a good first experiment.
- **Cup blind, then look at the curve.** [S0008](../sources/S0008-rao-what-is-baked-coffee.md)
- **Practise without beans.** An experienced owner simulated whole roasts on an empty machine to
  learn how it responds to each command before risking coffee. [S0017](../sources/S0017-homeroasters-skywalker-mods-thread.md)
- **Change one stage and hold the rest.** Sweet Maria's three-part test is a template: lengthen the drying stage, or the first crack itself, by 30–60 s while the other stages and the ~30 s finish after the end of crack stay fixed, then cup with two panels. `ctx: electric drum` [S0034](../sources/S0034-sweet-marias-stretchin-out-the-roast-pt2.md) [S0035](../sources/S0035-sweet-marias-stretchin-out-the-roast-pt3.md)
- **Use a sample kit as a calibration.** Hacea's 9 × 30 g kit (three profiles × three coffees) let members compare their own roasts of the same profile against a reference; the lesson is to line up seconds per phase, not temperatures. `conf: low` [S0036](../sources/S0036-home-barista-hacea-roast-approach-tasting-kit.md)
- **When a roast goes wrong, learn rather than rescue.** A ROEST owner's stalled batch ended light and under-developed (193.5 °C at 6:03); moving the inlet-temperature decline later gave a better coffee (195.8 °C at 6:01). Münchow's point as relayed: if the graphs show a roast is already off, it is too late to fix it meaningfully. `conf: low` `ctx: hot-air` [S0046](../sources/S0046-home-barista-why-ror-is-a-bad-reference-webinar.md)
- **Rest all samples equally before cupping** — rest advice runs from a week to 4–6 weeks for very light roasts, so uneven rest can decide a comparison. See [Resting & degassing](resting-and-storage.md). `conf: low` [S0036](../sources/S0036-home-barista-hacea-roast-approach-tasting-kit.md)
- **To copy a recipe across machines, match what every machine can measure.** Cooper and Hoos matched time to yellow, time to first crack, development time and end colour (Agtron within 3 points) and left temperature unmatched because probes differ; the matched roasts were hard to tell apart in blind triangles [S0056](../sources/S0056-cooper-hoos-2019-can-you-taste-the-roasting-system.md). `conf: low` `ctx: 2–7 kg drums`
- **Call first crack the same way every time.** Consecutive pops, not the first stray one [S0057](../sources/S0057-cooper-2026-standards-and-the-mother-sauce.md) [S0055](../sources/S0055-home-barista-underdeveloped-coffee-1kg-drum.md); the 2026 report also calls development ratio "a very inconsistent data point" on its own, so log times and degrees too [S0057](../sources/S0057-cooper-2026-standards-and-the-mother-sauce.md). `conf: low`
- **A clean airflow test holds the heat.** Hold the environment temperature (or first-crack time) and change only airflow, and expect electric machines to need more heater power with more air [S0054](../sources/S0054-home-barista-conduction-vs-convection-test-results-are-confusing.md) [S0053](../sources/S0053-home-barista-desnudo-conduction-convection-thread-roest-airflow.md). The Desnudo test (same coffee, two roasts, blind Q-grader cupping, only the fan changed) is a template, but it is one pair [S0052](../sources/S0052-desnudo-2026-conduction-vs-convection-taste.md). `conf: low`
- **Weigh every roast, to 1 g.** Hoos treats a loss 0.5 points or more away from the baseline of the same coffee and method as a warning [S0059](../sources/S0059-hoos-why-take-weight-loss-percentage.md); at 350 g that is 1.75 g (derived). Log green weight and moisture with it. `conf: low`
- **Recipe standards can come from blind tastings.** A 2026 report had roasters taste one washed coffee roasted 13 ways blind (mostly batch brew, some cupped) and derived phase-time targets from the favourites [S0057](../sources/S0057-cooper-2026-standards-and-the-mother-sauce.md). Useful as a design, not as a result: no scores or taster counts are given.

## On the Skywalker (IR)
- **Inference — test it:** weight loss % is a practical stand-in for colour if you don't have a
  colour meter; keep it equal (±0.5 %) across samples in an experiment.
- Keep fan and room airflow fixed during experiments [S0003](../sources/S0003-skywiki-renatoa-words-of-wisdom.md); note room temperature too — a cold
  room or a draft changes the roast noticeably [S0015](../sources/S0015-homeroasters-skywalker-roasts-thread.md).
- **Plan, don't steer.** Use logged data to plan the next roast rather than to drive the machine in
  real time; the lamp's inertia makes real-time steering ineffective. `conf: medium` [S0001](../sources/S0001-skywiki-infrared-roaster.md) [S0016](../sources/S0016-homeroasters-skywalker-main-thread.md)
- **End at a planned temperature.** In manual mode the V1 panel can stop the heater automatically
  at a set temperature (+/- keys; default 230 °C) — useful for repeatable drops. [S0016](../sources/S0016-homeroasters-skywalker-main-thread.md)
- **Borrowed recipes need scaling:** heater % depends on mains voltage, room temperature and batch
  size [S0015](../sources/S0015-homeroasters-skywalker-roasts-thread.md). Treat other owners' numbers as a shape, not a setting — see
  [Charge & batch](charge-and-batch.md).
- **Pick what you trust to end the roast.** A V2 owner's rule: development time, weight loss and
  drop temperature over colour, because lamp roasts look darker than their degree [S0027](../sources/S0027-coffeesnobs-skywalker-roasters-thread.md). Log
  drop temperature as degrees above first crack as well as seconds [S0023](../sources/S0023-home-barista-vegetal-flavor-first-crack.md) [S0024](../sources/S0024-home-barista-first-crack-temperature-changed.md).
- **Weight-loss target.** Hoos aims for light roasts at ~1–2 % above green moisture [S0025](../sources/S0025-roast-rebels-hoos-cultivars-airflow-interview.md); get
  your coffees' moisture before using it. `conf: low`
- **Borrow phase grids, not temperatures.** The 2026 light-roast grid (4:00–4:30 / 3:00–3:30 / 1:00–1:20) and the chart's Light rows (4:30–5:30 / 3:30–4:00 / 1:00–1:30) are candidate times to hold in a one-coffee test [S0057](../sources/S0057-cooper-2026-standards-and-the-mother-sauce.md) [S0063](../sources/S0063-cooper-eqmr-roast-level-flavour-profile-strategies-chart.md); their machine and batch size are unknown, so run them as relative changes from your own best roast — see [Roast phases](roast-phases.md). **Inference — test it.**
- See [experiments](../skywalker/experiments.md) for the current plan.
- **Cup after a set rest.** Your one cupped roast (id39) was tasted after 5 days. Plan to taste an experiment's samples on the same day and at the same rest (a week or more for your light roasts is a safe start, per the forum range) — see [Resting & degassing](resting-and-storage.md).
