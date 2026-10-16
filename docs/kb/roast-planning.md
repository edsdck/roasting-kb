---
title: Roast planning & experimenting
---

# Roast planning & experimenting

!!! abstract "In short"
    - **Plan → Execute → Learn.** Run the plan to the end, then change the *next* roast — don't improvise mid-roast. `conf: medium`
    - Change **one variable at a time** and keep **final colour (degree) equal**, or colour will decide your cupping. `conf: medium`
    - First check if a difference is even tasteable (blind triangle test) before building theories on it.
    - On the Skywalker: 3–5 planned power changes per roast, 5–10 % each.

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
- See [experiments](../skywalker/experiments.md) for the current plan.
