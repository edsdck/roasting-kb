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

## On the Skywalker (IR)

This page is mostly about the Skywalker already. Practical consequences:

- Expect the RoR to keep moving for a while after a power change — judge a change only after
  the lag has played out. **Inference — test it:** measure that lag on your machine (see
  [experiments](../skywalker/experiments.md)).
- Keep airflow (fan setting, kitchen hood, open windows) identical between roasts you want to
  compare — see [Airflow](airflow.md).
- Don't import RoR "rules" from hot-air machines without testing — see [Rate of rise](rate-of-rise.md).
- **Inference — test it:** if only the top layer heats, very fast roasts risk uneven development on
  this machine. Before chasing short total times, check the inside of a few beans (cut or grind
  separately) from your fastest roasts.

## Open questions
- An experienced owner argues radiant roasting follows different rules from convection (a post on
  the Home Roasters forum the Gatherer couldn't locate) — worth finding.
- Measured data on bean surface vs core temperature under IR heating; scorching/tipping risk.
- How much heat the drum itself contributes by conduction on the Skywalker.
- Does lamp power (rather than fan) change convective cooling inside the drum?
