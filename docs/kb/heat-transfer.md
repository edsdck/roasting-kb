---
title: Heat transfer
---

# Heat transfer

!!! abstract "In short"
    - Roasters move heat into beans by conduction (hot metal), convection (hot air) and radiation. Most commercial drum and fluid-bed advice assumes hot air dominates.
    - The Skywalker is different: its infrared lamp heats the beans mostly by **radiation**, and the air is *cooler* than the beans. `conf: medium`
    - Its "lag" comes from the lamp, which keeps glowing after you cut power — make changes early and in small steps.
    - Because heat delivery behaves differently, curve shapes and temperatures from hot-air machines don't transfer 1:1.
    - Only the top layer of the tumbling pile catches the radiation at any moment; owners think this is why very fast, hot Skywalker roasts come out dark outside and under-developed inside. `conf: low`
    - A fitted single-bean model of a *gas* drum puts radiation ahead of convection (overall coefficient 60–103 vs a calculated convective 16–17 W m⁻² °C⁻¹), so "drums are convection, the Skywalker is radiation" is less clean than often told. `conf: low` `ctx: gas-drum`
    - Beans heat unevenly: the model's Biot numbers (0.48–0.82) mean the inside lags the surface, which fits owners' "dark outside, raw inside" reports from fast roasts. `conf: low`

## Concepts

**Convection (hot air).** Heat flow is proportional to the air–bean temperature difference
(Newton's law of cooling). As beans warm toward the air temperature, heat flow falls, so at a
constant heat setting the bean temperature rises more and more slowly — a naturally declining
rate of rise. `conf: medium` [S0002](../sources/S0002-skywiki-convection-vs-radiant.md) [S0005](../sources/S0005-coffeemind-rate-of-rise-bad-reference.md) [S0008](../sources/S0008-rao-what-is-baked-coffee.md)

**Radiation (infrared).** Heat flow scales with the difference of the *fourth powers* of source
and bean temperatures (Stefan–Boltzmann). With a lamp far hotter than the beans, the delivered
energy stays almost constant through the roast. Beans also absorb IR better as they darken, so
absorption rises late in the roast. `conf: low` (physics reasoning, no measurements) [S0002](../sources/S0002-skywiki-convection-vs-radiant.md)

**Who carries the heat in the Skywalker.** Heat transfer is primarily radiative: the air is not
the main heat carrier and the drum is not the main heat reservoir — the lamp heats the beans
directly. The air is cooler than the beans and actually removes heat from them.
`conf: medium` [S0001](../sources/S0001-skywiki-infrared-roaster.md) [S0003](../sources/S0003-skywiki-renatoa-words-of-wisdom.md)

**Beans are the main heat sink.** Run empty on the same program (P11: 40 % heater, 90 % fan after
170 °C), the machine plateaued at ~178 °C and couldn't pass 179 °C for 15 minutes, while with beans
the program reached its ~194 °C cut-off; 40 % heater with 65 % fan also holds an empty machine at
~178–179 °C. The interpretation given: beans are the main absorber and thermal mass, and the probe's
heat during a roast comes mainly from the beans. `conf: low` (one owner's informal tests; the probe
may also read differently with no beans around it) [S0001](../sources/S0001-skywiki-infrared-roaster.md) [S0016](../sources/S0016-homeroasters-skywalker-main-thread.md)

**Where the lamp sits matters.** A roaster with its lamp *outside* the drum (e.g. Smola S5) behaves
more like a convection-dominant machine, unlike the Skywalker's in-drum radiant design.
`conf: low` [S0009](../sources/S0009-skywiki-putrid-upstairs-response.md)

**Drum surface.** A darker drum absorbs more IR and helps heating; polished metal would reflect
more. `conf: low` [S0001](../sources/S0001-skywiki-infrared-roaster.md) Coffee deposits darken the drum over dozens of roasts, so expect slightly
more heat absorption over time; one owner guesses 5–10 % more air compensates (not measured).
[S0016](../sources/S0016-homeroasters-skywalker-main-thread.md)

**The lamp is near-infrared.** The Skywalker's lamp glows visibly (near-IR), which heats surfaces
rather than penetrating deeply; far-IR panels heat deeper. Not the same as the gas "IR burners" in
some drum roasters, which heat the drum, not the beans. `conf: low` [S0016](../sources/S0016-homeroasters-skywalker-main-thread.md)

**Only the top layer absorbs.** At any moment only the beans on top of the pile are exposed to the
lamp; they pass heat to the others as the drum turns. Implications drawn by an experienced owner:
a bigger batch needs proportionally more time at the same heater %, and pushing power hard gives
some beans more energy than others with less time to even out. `conf: low` (reasoning, one author)
[S0015](../sources/S0015-homeroasters-skywalker-roasts-thread.md) Related observations: his two fastest roasts (~7 min) were under-developed inside while
looking darker than average outside [S0015](../sources/S0015-homeroasters-skywalker-roasts-thread.md), and early auto-profile roasts looked medium but had
light-roast weight loss, suggesting surface over-heating [S0017](../sources/S0017-homeroasters-skywalker-mods-thread.md). `conf: low`

**Plenty of power.** Empty and preheated to 220 °C, the machine reached its 250 °C over-temperature
limit in under a minute at only 50 % heater. [S0016](../sources/S0016-homeroasters-skywalker-main-thread.md)

**IR power vs time (lab study).** In a 1 kg far-infrared roaster, more lamp power meant higher
bean temperature and much shorter roasts (1000 W: 81 min → 3000 W: 18 min), with the lowest
energy use per gram at 2500 W. `conf: medium` `ctx: IR, 1 kg lab roaster, no flavour data` [S0004](../sources/S0004-puntuwanit-2023-far-infrared-power.md)

**Radiation also dominates in a gas drum (model).** Single Catuaí beans held at the centre of a
gas-fired drum (45 rpm) at constant air temperatures of 200–280 °C were fitted with a lumped model.
The fitted overall coefficient (convection + radiation) rose from 60 to 103 W m⁻² °C⁻¹ with
temperature, against a calculated convective coefficient of only 16–17; the authors attribute the
gap to radiation from the hot walls and the low air speed inside a rotating drum. R² of the fit
0.973–0.994. `conf: medium` for the numbers (peer-reviewed, grade A), `conf: low` for "radiation
dominates", which rests on the difference between a fitted and a calculated coefficient. `ctx:
gas-drum, single bean, constant air temperature` [S0033](../sources/S0033-bustos-vanegas-2025-bean-heating-model-heat-generation.md)

**Evaporation matters more than the reactions, and the inside lags.** In the same model the
heat taken up by evaporation changes the bean temperature more than the heat released by
exothermic reactions, which are assumed to start at about 150 °C bean temperature; ignoring the
exotherm underestimates temperature. Biot numbers of 0.48–0.82 are not small, so the model's one
temperature per bean hides a surface that runs ahead of the core. `conf: medium` `ctx: gas-drum,
single bean` [S0033](../sources/S0033-bustos-vanegas-2025-bean-heating-model-heat-generation.md)

## In practice

- **Thermal inertia / lag.** On the Skywalker the lag comes from the lamp, which keeps radiating
  after a power cut — "almost as a commercial drum", but from the lamp rather than drum mass.
  Power changes act with a delay, RoR responds slowly, and large adjustments overshoot or collapse.
  `conf: medium` [S0001](../sources/S0001-skywiki-infrared-roaster.md) [S0016](../sources/S0016-homeroasters-skywalker-main-thread.md) Example: with the heater cut early in development, bean temperature
  held at 182 °C for 30 s [S0017](../sources/S0017-homeroasters-skywalker-mods-thread.md). Generic drum advice also stresses that late
  corrections can't undo earlier decisions [S0005](../sources/S0005-coffeemind-rate-of-rise-bad-reference.md).
- **Few, early, small changes.** 3–5 power changes per roast, 5–10 % each; decide *when* to
  change rather than micro-adjusting. `conf: medium` [S0001](../sources/S0001-skywiki-infrared-roaster.md) [S0005](../sources/S0005-coffeemind-rate-of-rise-bad-reference.md) [S0016](../sources/S0016-homeroasters-skywalker-main-thread.md) The roaster only
  accepts 5 % steps anyway, and smaller steps wouldn't move the profile much [S0017](../sources/S0017-homeroasters-skywalker-mods-thread.md).

- **IR roasters tip and turn astringent easily (Kaleido: IR plus hot air).** An experienced Kaleido
  user says infrared roasters "tip easily, leading to bitterness and astringency"; his M10 recipe:
  charge higher, start at 70–80 % power, maximum airflow throughout, then tiny cuts (−2 % per 5 °C
  from 160 °C), −5 % per 5 °C from 180 °C, back off before first crack, −10 % about 45 s after it.
  His reasons: darker beans absorb more infrared so power must fall faster, and thermocouple lag
  means corrections must come before the curve shows them. `conf: low` `ctx: Kaleido M10, large
  batches, forced hot air` [S0026](../sources/S0026-home-barista-kaleido-m10-astringent-roasts.md)
- **Wide power swings hurt.** The same thread blames PID-driven swings (100 % → 30 %) for
  astringency on the M10 and recommends temperature-triggered stepwise cuts; the owner also saw
  RoR dips at each power change and wondered whether each change briefly disturbs the IR heating.
  `conf: low` `ctx: Kaleido M10` [S0026](../sources/S0026-home-barista-kaleido-m10-astringent-roasts.md)
- **Charging too cool (drum roasters).** A low charge made up for with lots of heat to reach first
  crack can leave the inside under-developed and the roast astringent; raising the charge made it
  disappear for one drum roaster, and an IKAWA user got a pleasant cup after adding a hotter initial
  step. `conf: low` `ctx: drum` [S0026](../sources/S0026-home-barista-kaleido-m10-astringent-roasts.md)

## On the Skywalker (IR)

This page is mostly about the Skywalker already. Practical consequences:

- Expect the RoR to keep moving for a while after a power change — judge a change only after
  the lag has played out. **Inference — test it:** measure that lag on your machine (see
  [experiments](../skywalker/experiments.md)).
- Keep airflow (fan setting, kitchen hood, open windows) identical between roasts you want to
  compare — see [Airflow](airflow.md).
- **Inference — test it:** the Kaleido advice (higher charge, lower power percentage, small
  stepwise cuts, larger cuts only late) points the same way as renatoa's advice to start reducing
  power from about minute 4 in steps [S0017](../sources/S0017-homeroasters-skywalker-mods-thread.md) — and it adds a failure to watch for: astringency from
  an under-developed inside. A V2 owner also finds higher fan and drum speed make heater
  adjustments "more responsive" on light roasts [S0027](../sources/S0027-coffeesnobs-skywalker-roasters-thread.md). See [Defects](defects.md).
- Don't import RoR "rules" from hot-air machines without testing — see [Rate of rise](rate-of-rise.md).
- **Inference — test it:** if only the top layer heats, very fast roasts risk uneven development on
  this machine. Before chasing short total times, check the inside of a few beans (cut or grind
  separately) from your fastest roasts.
- **Inference — test it:** if hot walls already carry most of the heat in a gas drum [S0033](../sources/S0033-bustos-vanegas-2025-bean-heating-model-heat-generation.md), the
  lamp is a stronger version of the same mechanism rather than a different kind. The practical
  advice (early, small steps; judge changes after the lag) is unchanged, but "RoR rules do not
  transfer because the heat arrives differently" is weaker than it sounds — the argument has to
  rest on lag and on the top-layer effect, not on radiation alone.

## Open questions
- An experienced owner argues radiant roasting follows different rules from convection (a post on
  the Home Roasters forum the Gatherer couldn't locate) — worth finding.
- Measured data on bean surface vs core temperature under IR heating; scorching/tipping risk.
  The only measurement so far is on a fluid bed with a small dose and strong airflow: beans
  followed inlet air within ~30 s for linear ramps (~60 s to reach ~90 % of a 40 °C step), so the
  author doubts large internal gradients for gentle ramps [S0023](../sources/S0023-home-barista-vegetal-flavor-first-crack.md). `ctx: fluid bed` — it does not
  say what an IR lamp does, and others still link fast roasts to raw cores [S0023](../sources/S0023-home-barista-vegetal-flavor-first-crack.md).
- How much heat the drum itself contributes by conduction on the Skywalker.
- Does lamp power (rather than fan) change convective cooling inside the drum?
- Does the radiation share keep rising with temperature on the Skywalker, as the fitted coefficient did on the gas drum (60 → 103 W m⁻² °C⁻¹ from 200 to 280 °C)? [S0033](../sources/S0033-bustos-vanegas-2025-bean-heating-model-heat-generation.md)
