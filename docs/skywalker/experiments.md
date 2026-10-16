# Experiments to try

*Suggested by the Builder. One variable at a time; keep batch size (350 g), fan and room airflow
fixed; cup blind; compare at equal roast degree (weight loss within ±0.5 % if no colour meter —
**Inference**). Updated 2026-10-16.*

## 0. Setup first — Artisan RoR settings
Set sampling to 1 s and delta span ≈ 15 s, minimal extra smoothing [S0008](../sources/S0008-rao-what-is-baked-coffee.md). If the RoR line becomes
unreadably noisy on the Skywalker, lengthen the span and note the value you settled on.

## 1. Measure the lamp lag
**Why:** power changes act late on this machine [S0001](../sources/S0001-skywiki-infrared-roaster.md); you need to know how late to plan changes.
**How:** in a normal roast, make one clean power step (e.g. −10 %) mid-Maillard. Note the time until
the RoR visibly changes direction. Repeat once.
**Outcome:** a number ("my lag ≈ X s") to plan all future changes earlier by.

## 2. Development time at equal degree (replicate the key study on IR)
**Why:** at equal colour, shorter development = brighter/sweeter, longer = roastier/bitter [S0006](../sources/S0006-alstrup-2020-development-time-sensory.md).
**How:** one coffee, three roasts with the same path to first crack; development ≈ 1:00 / 1:45 /
2:30, adjusting drop so weight loss is equal. Rest equally, cup blind.
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
