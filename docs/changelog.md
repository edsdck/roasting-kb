# Changelog

Every change the Builder makes to the knowledge base, newest first.

## 2026-10-16 — Build 4
Sources integrated: S0015–S0022 · Roasts parsed: 0 new

- **CONTEST** [Development § Contested](kb/development.md#contested) — is a 20–25 % DTR needed? Rao (2014) vs light roasters at 13–16 % / 1:20–1:30 and Nordic ~45 s [S0018 vs S0020, S0021, S0022, S0015]
- **CONTEST** [Measurement § Contested](kb/measurement-and-artisan.md#contested) — does first-crack temperature depend on the coffee? Same reading for all beans on Quest/Bullet vs bean-dependent; your data checked (P) [S0020, S0019, S0017, S0015]
- **EXTEND** [Measurement & Artisan](kb/measurement-and-artisan.md) — Skywalker FC ~180–185 °C raised to `conf: high` (several owners) vs ~200 °C on convection machines; added-thermocouple comparisons (placement dominates); stock-probe tolerance, smoothing, resolution; consistency over accuracy; trier dips and data spikes; ET as FC warning; how to mark first crack; small-batch immersion (85 g FC 173 °C) [S0015, S0016, S0017, S0019, S0020, S0018]
- **ADD** [Development](kb/development.md) — development time depends on roast speed and RoR at first crack; what light roasters actually do; stretching to hit a % can taste under-developed; short finishes shift flavour; when development starts; other Skywalker owners' development and the low-momentum inference [S0015–S0018, S0020–S0022]
- **EXTEND** [Development](kb/development.md) — "Don't define the end by DTR alone" raised to `conf: medium` [S0011, S0021]
- **ADD** [Charge & batch](kb/charge-and-batch.md) — factory preheat behaviour, lamp-friendly manual preheat, the 100 % charge spike, renatoa's charge/power examples, heater % shifts with mains voltage and room temperature, batch size on a radiant roaster, cooling >430 g [S0015, S0016, S0017]
- **EXTEND** [Charge & batch](kb/charge-and-batch.md) — probe immersion raised to `conf: medium`; removed "not yet known: preheat/charge for 350 g" (partly answered for 250 g; 350 g still in gaps) [S0015](sources/S0015-homeroasters-skywalker-roasts-thread.md)
- **ADD** [Heat transfer](kb/heat-transfer.md) — NIR lamp; only the top layer absorbs (fast roasts dark outside, under-developed inside); plenty of power; drum darkening over time [S0015, S0016, S0017]
- **EXTEND** [Heat transfer](kb/heat-transfer.md) — empty-machine test (original post), lamp inertia, 5 % control steps [S0016, S0017]
- **ADD** [Roast phases](kb/roast-phases.md) — what first crack is; no "correct" time to first crack; other owners' phase tables; judging dry end under IR (~150 °C yellow) [S0015, S0016, S0019]
- **EXTEND** [Roast phases § Contested](kb/roast-phases.md#contested) — more practitioner weight on late Maillard [S0020, S0021, S0022]
- **ADD** [Rate of rise](kb/rate-of-rise.md) — typical Skywalker RoR numbers; reducing power from ~minute 4 in steps; panel RoR is a 1-minute average [S0015, S0016, S0017]
- **EXTEND** [Rate of rise § Contested](kb/rate-of-rise.md#contested) — renatoa's 2026 "flat RoR is the new normal" vs his 2023 advice for a declining RoR [S0015, S0017]
- **ADD** [Airflow](kb/airflow.md) — air mainly cools and removes smoke; fan as a finer development lever (limited margin at 90 %); ambient and drafts; factory fan schedule; contrast with high-airflow Nordic roasting `ctx: gas-drum` [S0015, S0016, S0017, S0022]
- **ADD** [Defects](kb/defects.md) — grainy / vegetal under-development; baked cause #5 (development out of proportion, Rao); a flat-RoR development without baked taste (anecdote); charcoal beans; dark-outside/under-developed-inside [S0015–S0019, S0022]
- **ADD** [Green coffee](kb/green-coffee.md) — moisture and first crack; processing vs FC temperature (contested); coffee type and very short development; factory presets by processing [S0015, S0016, S0019, S0020, S0022]
- **ADD** [Roast planning](kb/roast-planning.md) — practise on an empty machine; plan rather than steer; heater auto-stop temperature; borrowed recipes need scaling [S0015, S0016, S0017]
- **EXTEND** [Myths & contested](kb/myths-and-contested.md) — two new contested rows; flat-RoR row updated; temperature comparison and "development time without context" [S0015–S0021]
- **EXTEND** [Glossary](kb/glossary.md) — Auto/Assist/Manual, NIR, Nordic style, Preheat; DTR and First crack updated [S0016, S0017, S0018, S0019, S0020, S0022]
- **CORRECT** [Measurement & Artisan](kb/measurement-and-artisan.md) — was: batch-size bullet cited "[S0013](sources/S0013-melheim-2023-optimal-batch-size.md)" but linked to S0003's file → now links to S0013 — plain linking error
- **CORRECT** [Measurement & Artisan](kb/measurement-and-artisan.md) — removed open question "Exact Skywalker V1 probe type…": the type (NTC) and Artisan connection (TC4) are already answered on the page [S0009](sources/S0009-skywiki-putrid-upstairs-response.md)
- **ROASTS** [Findings](skywalker/findings.md) — first crack vs other owners and convection machines; checked FC time vs FC temperature (all r = 0.73; within Honduras 0.16, Ethiopia 0.05 — coffee and speed confounded); development vs practitioner norms; heater schedule vs renatoa's (n=41, no new roasts)
- **EXTEND** [Experiments](skywalker/experiments.md) — 0c lamp-friendly preheat; experiment 2 and 3 updated; **new experiment 6**: Honduras vs washed at matched first-crack time
- **GAPS** rewritten (13 items; Home-Barista via Chrome)

## 2026-10-16 — Fixes
- **FIX** Roast charts now use the temperature and RoR axis ranges from each Artisan file, so curves cross where they do in Artisan (previously a fixed 0–30 RoR axis shifted the crossing ~1.5 min earlier)
- **FIX** [Experiments](skywalker/experiments.md), [Roast phases](kb/roast-phases.md) — removed the incorrect "mark DRY END" advice; all roasts already have CHARGE, DRY, FCs and DROP marked

## 2026-10-16 — Build 3
Sources integrated: none · Roasts parsed: 41 new (id1–id41), 1 with cupping notes

- **ADD** [Roast log](skywalker/roast-log.md) — 41 roast pages with curves, phases and heater/fan changes
- **ADD** [Findings](skywalker/findings.md) — first crack ~184.5 °C; development shortened to ~1:00; development time drives weight loss; heater handling; id39 cupping analysis
- **EXTEND** [Measurement & Artisan](kb/measurement-and-artisan.md), [Development](kb/development.md) — personal evidence notes
- **EXTEND** [Experiments](skywalker/experiments.md) — development-time experiment promoted to "do next", tailored to current roasts
- **FIX** roast parser: handles Artisan's −1 dropouts, missing ET probe, kg weights, Skywalker heater/fan naming
- **GAPS** updated

## 2026-10-16 — Build 2
Sources integrated: S0009–S0014 · Roasts parsed: 0

- **ADD** [Roast phases](kb/roast-phases.md) — phases, checkpoints, matching phases across machines [S0011, S0012]
- **ADD** [Charge & batch size](kb/charge-and-batch.md) — capacity guidelines, readings shift with batch size, probe immersion, Skywalker 350–450 g [S0003, S0009, S0013, S0014]
- **ADD** [Green coffee](kb/green-coffee.md) — density vs elevation, dense vs light beans [S0014](sources/S0014-lee-2025-bean-density-roasting.md)
- **EXTEND** [Defects](kb/defects.md) — rewritten: objective (scorching, facing, tipping, chipping) and subjective (under/over-development, roasty) defects; baked causes listed [S0010, S0013]
- **CONTEST** [Defects § Baked](kb/defects.md#baked) — cause of "baked" now has four competing explanations [S0008, S0010]
- **CONTEST** [Roast phases § Contested](kb/roast-phases.md#contested) — importance of pre-first-crack phases [S0011 vs S0012]
- **EXTEND** [Development](kb/development.md) — colour is the strongest driver; multi-study support; under/over-development tastes; DTR alone isn't enough [S0010, S0011, S0012]
- **EXTEND** [Rate of rise](kb/rate-of-rise.md) — "don't roast the software", RoR window size, hardware noise [S0011](sources/S0011-cooper-cropster-rate-of-rise-production.md)
- **EXTEND** [Measurement & Artisan](kb/measurement-and-artisan.md) — V1 NTC probe and TC4 firmware; replaying events; batch-size effect raised to medium confidence [S0009, S0013]
- **EXTEND** [Heat transfer](kb/heat-transfer.md) — lamp position (in-drum vs outside) [S0009](sources/S0009-skywiki-putrid-upstairs-response.md)
- **EXTEND** [Roast planning](kb/roast-planning.md) — priorities (colour > development > time to FC), checkpoints [S0011, S0012]
- **EXTEND** [Myths & contested](kb/myths-and-contested.md), [Glossary](kb/glossary.md)
- **EXTEND** [Experiments](skywalker/experiments.md) — log density and DRY END; replay-a-roast experiment
- **GAPS** updated

## 2026-10-16 — Build 1
Sources integrated: S0001–S0008 · Roasts parsed: 0

- **ADD** [Heat transfer](kb/heat-transfer.md) — radiation vs convection; Skywalker heats mainly by radiation, air cooler than beans; lamp lag; empty-machine test; FIR lab study [S0001–S0005, S0008]
- **ADD** [Rate of rise](kb/rate-of-rise.md) — definition, speedometer use, crash/flick, probe artefacts, Artisan settings [S0001, S0002, S0005, S0007, S0008]
- **CONTEST** [Rate of rise § Contested](kb/rate-of-rise.md#contested) — "RoR crash causes baked" (Rao) vs "declining RoR is a weak reference" (Münchow) vs "flat RoR is normal on IR" [S0002, S0005, S0008]
- **ADD** [Development](kb/development.md) — development time at equal colour (sensory + chemistry); acidity peaks at first crack and declines after [S0006, S0007]
- **ADD** [Defects](kb/defects.md) — "baked": two different definitions [S0005, S0006, S0008]
- **ADD** [Measurement & Artisan](kb/measurement-and-artisan.md) — probe reads air–bean mix; Skywalker first crack ≈182 °C; batch size shifts readings; Artisan RoR settings [S0001, S0003, S0005, S0008]
- **ADD** [Roast planning](kb/roast-planning.md) — plan–execute–learn, one variable, equal colour, few deliberate power changes [S0001, S0005, S0006, S0008]
- **ADD** [Airflow](kb/airflow.md) — air removes heat on the Skywalker; keep airflow constant [S0001, S0003]
- **ADD** [Myths & contested](kb/myths-and-contested.md), [Glossary](kb/glossary.md)
- **ADD** [Experiments](skywalker/experiments.md) — lamp lag, development at equal degree, flat vs declining RoR, 350 vs 400 g
- **GAPS** updated: Skywalker practicals, IR RoR evidence, charge/batch, phases, other defects, green coffee

## 2026-10-16 — Setup
- Knowledge base created (empty).
