# Changelog

Every change the Builder makes to the knowledge base, newest first.

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
