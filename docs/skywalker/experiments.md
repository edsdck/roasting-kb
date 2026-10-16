# Experiments to try

*Suggested by the Builder. One variable at a time; keep batch size (350 g), fan and room airflow
fixed; cup blind; compare at equal roast degree (weight loss within ±0.5 % if no colour meter —
**Inference**). Updated 2026-10-16 (Build 3).*

## 0. Setup first — Artisan RoR settings
Set sampling to 1 s and delta span ≈ 15 s, minimal extra smoothing [S0008](../sources/S0008-rao-what-is-baked-coffee.md). If the RoR line becomes
unreadably noisy on the Skywalker, lengthen the span and note the value you settled on.

## 0b. Log two extra things with every roast
- **Green density:** weigh a fixed volume of green coffee (e.g. 100 ml in a measuring cylinder) → g/L.
  Density changes how a coffee takes heat [S0014](../sources/S0014-lee-2025-bean-density-roasting.md).
- **Mark DRY END (yellowing) in Artisan**, so each roast page shows drying / Maillard / development
  durations [S0011](../sources/S0011-cooper-cropster-rate-of-rise-production.md) [S0012](../sources/S0012-munchow-2020-roasting-conditions-multi-study.md).

## 1. Measure the lamp lag
**Why:** power changes act late on this machine [S0001](../sources/S0001-skywiki-infrared-roaster.md); you need to know how late to plan changes.
**How:** in a normal roast, make one clean power step (e.g. −10 %) mid-Maillard. Note the time until
the RoR visibly changes direction. Repeat once.
**Outcome:** a number ("my lag ≈ X s") to plan all future changes earlier by.

## 2. Development time at equal degree — **do this next**
*Your roasts have settled at ~1:00 development (DTR ~9 %), shorter than anything in the research,
and your one cupped roast (0:41) was sharp and flat — see [findings](findings.md).*

**Why:** at equal colour, shorter development = brighter/sweeter, longer = roastier/bitter [S0006](../sources/S0006-alstrup-2020-development-time-sensory.md).
**How:** one coffee (the Costa Rican Natural or Colombia you have now), three roasts with your usual
path to first crack; development ≈ **1:00 / 1:45 / 2:30**. On your machine development time drives
weight loss (r = 0.72), so expect loss to rise with it; if you want equal degree, lower the heater
during development for the longer ones rather than dropping earlier. Rest equally, cup blind.
**Taste for:** acidity, sweetness, fruit vs roasted, bitterness, body.

## 3. Flat vs declining RoR after drying
**Why:** IR theory says a flat RoR may be fine here [S0002](../sources/S0002-skywiki-convection-vs-radiant.md); drum advice says avoid crashes and keep
RoR declining [S0008](../sources/S0008-rao-what-is-baked-coffee.md). Contested.
**How:** same coffee, same first-crack time, development time and weight loss; roast A holds power
steady after drying (flatter RoR), roast B steps power down (declining). Cup blind; triangle test
if unsure they differ [S0005](../sources/S0005-coffeemind-rate-of-rise-bad-reference.md).
**Taste for:** hollowness/flatness, sweetness, does it hold up as it cools [S0008](../sources/S0008-rao-what-is-baked-coffee.md).

## 4. 350 g vs 400 g — how readings shift
**Why:** smaller loads read lower on this probe [S0003](../sources/S0003-skywiki-renatoa-words-of-wisdom.md).
**How:** same settings, two batch sizes; note first-crack temperature and time.
**Outcome:** a correction you can use when changing batch size.

## 5. Repeat a good roast by replaying its events
**Why:** replaying heater/fan changes reproduced roasts as well as PID on Skywalkers [S0009](../sources/S0009-skywiki-putrid-upstairs-response.md).
**How:** load your best recent roast as the Artisan background profile and replay its events on the
same coffee and batch size. **Inference — test it:** compare first-crack time, drop time and cup.
**Outcome:** tells you how repeatable the machine is — the baseline every other experiment needs.
