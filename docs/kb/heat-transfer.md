---
title: Heat transfer
---

# Heat transfer

!!! abstract "In short"
    - Roasters move heat into beans by conduction (hot metal), convection (hot air) and radiation. Most commercial drum and fluid-bed advice assumes hot air dominates.
    - The Skywalker is different: its infrared lamp heats the beans mostly by **radiation**, and the air is *cooler* than the beans. `conf: medium`
    - Its "lag" comes from the lamp, which keeps glowing after you cut power — make changes early and in small steps.
    - Because heat delivery behaves differently, curve shapes and temperatures from hot-air machines don't transfer 1:1.

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

**Beans are the main heat sink.** Run empty on the same program, the machine plateaued at
~178 °C and couldn't pass 179 °C, while with beans the program reached ~194 °C. The interpretation
given: beans are the main absorber and thermal mass of the system. `conf: low` (one informal test;
the probe may also read differently with no beans around it) [S0001](../sources/S0001-skywiki-infrared-roaster.md)

**Where the lamp sits matters.** A roaster with its lamp *outside* the drum (e.g. Smola S5) behaves
more like a convection-dominant machine, unlike the Skywalker's in-drum radiant design.
`conf: low` [S0009](../sources/S0009-skywiki-putrid-upstairs-response.md)

**Drum surface.** A darker drum absorbs more IR and helps heating; polished metal would reflect
more. `conf: low` [S0001](../sources/S0001-skywiki-infrared-roaster.md)

**IR power vs time (lab study).** In a 1 kg far-infrared roaster, more lamp power meant higher
bean temperature and much shorter roasts (1000 W: 81 min → 3000 W: 18 min), with the lowest
energy use per gram at 2500 W. `conf: medium` `ctx: IR, 1 kg lab roaster, no flavour data` [S0004](../sources/S0004-puntuwanit-2023-far-infrared-power.md)

## In practice

- **Thermal inertia / lag.** On the Skywalker the lag comes from the lamp, which keeps radiating
  after a power cut. Power changes act with a delay, RoR responds slowly, and large adjustments
  overshoot or collapse. `conf: medium` [S0001](../sources/S0001-skywiki-infrared-roaster.md) Generic drum advice also stresses that late
  corrections can't undo earlier decisions [S0005](../sources/S0005-coffeemind-rate-of-rise-bad-reference.md).
- **Few, early, small changes.** 3–5 power changes per roast, 5–10 % each; decide *when* to
  change rather than micro-adjusting. `conf: medium` [S0001](../sources/S0001-skywiki-infrared-roaster.md) [S0005](../sources/S0005-coffeemind-rate-of-rise-bad-reference.md)

## On the Skywalker (IR)

This page is mostly about the Skywalker already. Practical consequences:

- Expect the RoR to keep moving for a while after a power change — judge a change only after
  the lag has played out. **Inference — test it:** measure that lag on your machine (see
  [experiments](../skywalker/experiments.md)).
- Keep airflow (fan setting, kitchen hood, open windows) identical between roasts you want to
  compare — see [Airflow](airflow.md).
- Don't import RoR "rules" from hot-air machines without testing — see [Rate of rise](rate-of-rise.md).

## Open questions
- Measured data on bean surface vs core temperature under IR heating; scorching/tipping risk.
- How much heat the drum itself contributes by conduction on the Skywalker.
- Does lamp power (rather than fan) change convective cooling inside the drum?
