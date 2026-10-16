---
title: Airflow
---

# Airflow

!!! abstract "In short"
    - On the Skywalker, air doesn't deliver heat to the beans — it removes it. `conf: medium`
    - Airflow changes alter roast dynamics a lot; even a kitchen hood above the roaster is noticeable.
    - Fan is a **faster, finer** lever than the heater during development — but the factory profiles already run it at 80–90 % late, leaving little room. `conf: low`
    - Room temperature and drafts act mainly through the air drawn through the drum: in a cold room, lower the fan. `conf: low`

## Concepts
- In a radiant roaster the air is cooler than the beans and takes heat from them [S0003](../sources/S0003-skywiki-renatoa-words-of-wisdom.md); it is
  not the main heat carrier [S0001](../sources/S0001-skywiki-infrared-roaster.md). `conf: medium` Its main jobs are cooling the beans and
  removing smoke; it's "a light breeze" compared with a conventional drum, and there is "no source of
  hot air having a significant role in the roast". [S0015](../sources/S0015-homeroasters-skywalker-roasts-thread.md) [S0017](../sources/S0017-homeroasters-skywalker-mods-thread.md)
- **Contrast — convection drums:** Nordic roasters running ~45 s developments relied on very high
  airflow for the whole roast to develop the coffee [S0022](../sources/S0022-home-barista-nordic-roasters-forum-exercise.md); a home roaster found that cutting
  airflow instead of raising power gave "absolutely terrible results" [S0022](../sources/S0022-home-barista-nordic-roasters-forum-exercise.md). `ctx: gas-drum`

## In practice
- Avoid changing airflow casually: any change "will change dramatically the roast dynamics";
  one owner could detect the speed setting of a hood ~0.5 m above the machine. `conf: low` [S0003](../sources/S0003-skywiki-renatoa-words-of-wisdom.md)
- The built-in program P11 raises fan to 90 % while dropping heater to 40 % at ~170 °C
  (observed in an empty-machine test). [S0001](../sources/S0001-skywiki-infrared-roaster.md) Factory profiles start at 65 % fan for all coffees
  and raise it to 80–90 % at ~170 °C [S0016](../sources/S0016-homeroasters-skywalker-main-thread.md) (versions may differ).
- **Development control.** Modulating airflow gives faster and finer control in development than a
  5 % heater step. `conf: low` [S0015](../sources/S0015-homeroasters-skywalker-roasts-thread.md) With the fan already at 90 %, though, there's little margin
  left [S0017](../sources/S0017-homeroasters-skywalker-mods-thread.md).
- **Ambient.** In a ~14 °C basement the factory 22 program reached dry end only around minute 6;
  lowering the fan from 65 % to 55 % restored normal times. Try +5–10 % fan in a hot (~30 °C) room
  (suggested, untested). An owner at ~19 °C never saw RoR above 11 °C/min. `conf: low` [S0015](../sources/S0015-homeroasters-skywalker-roasts-thread.md)
- **Drafts.** The machine reacts even to a kitchen door opening on a windy day; opening the chaff
  tray 1 cm shows up in the graph. `conf: low` [S0015](../sources/S0015-homeroasters-skywalker-roasts-thread.md)
- **Preheat with air on:** preheating with at least 40–50 % air spares the lamp. [S0016](../sources/S0016-homeroasters-skywalker-main-thread.md) [S0017](../sources/S0017-homeroasters-skywalker-mods-thread.md)
  See [Charge & batch](charge-and-batch.md).

## On the Skywalker (IR)
- Keep fan %, hood and windows the same across roasts you compare; note them in Artisan.
- Raising the fan as a fast brake on RoR is now backed by an experienced owner's practice [S0015](../sources/S0015-homeroasters-skywalker-roasts-thread.md)
  — still **test it** on your machine and note how big a fan step it takes.
- **Inference — test it:** if your room temperature changes with the seasons, re-check your fan
  setting rather than your heater first.

## Open questions
- Recommended fan curves from Skywalker owners at 350 g; how much a fan step changes RoR.
