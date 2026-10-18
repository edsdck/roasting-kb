---
title: Airflow
---

# Airflow

!!! abstract "In short"
    - On the Skywalker, air doesn't deliver heat to the beans — it removes it. `conf: medium`
    - Airflow changes alter roast dynamics a lot; even a kitchen hood above the roaster is noticeable.
    - Fan is a **faster, finer** lever than the heater during development — but the factory profiles already run it at 80–90 % late, leaving little room. `conf: low`
    - Room temperature and drafts act mainly through the air drawn through the drum: in a cold room, lower the fan. `conf: low`
    - On a gas drum a Rwandan natural and its decaf tasted green or astringent until airflow was **restricted for longer than usual** (normally 100 % just before first crack); on IR/hot-air machines others run maximum airflow. **Contested**, different heat sources. `conf: low`
    - **Airflow tests on other machines point different ways and are all single comparisons:** a Bullet R1 half-batch ran ~30 s slower with high air and cupped brighter [S0047](../sources/S0047-sweet-marias-bullet-r1-airflow-test-rwanda-kageyo.md); a Roest owner's high-air and low-air profiles at equal time and loss were "extremely similar" in the cup [S0053](../sources/S0053-home-barista-desnudo-conduction-convection-thread-roest-airflow.md); a fluid-bed blind pair scored higher with the fan at its lowest fluidising setting (83.25 → 84.5) [S0052](../sources/S0052-desnudo-2026-conduction-vs-convection-taste.md). `conf: low` `ctx: induction / hot-air drum / fluid bed`
    - **Airflow is hard to test alone:** holding the environment temperature, four airflow levels gave almost the same bean curve on a gas drum [S0054](../sources/S0054-home-barista-conduction-vs-convection-test-results-are-confusing.md), and on electric drums more air also needs more heater power [S0053](../sources/S0053-home-barista-desnudo-conduction-convection-thread-roest-airflow.md) [S0054](../sources/S0054-home-barista-conduction-vs-convection-test-results-are-confusing.md). On the Skywalker the fan removes heat, so a fan step also changes roast speed. `conf: low`

## Concepts
- In a radiant roaster the air is cooler than the beans and takes heat from them [S0003](../sources/S0003-skywiki-renatoa-words-of-wisdom.md); it is
  not the main heat carrier [S0001](../sources/S0001-skywiki-infrared-roaster.md). `conf: medium` Its main jobs are cooling the beans and
  removing smoke; it's "a light breeze" compared with a conventional drum, and there is "no source of
  hot air having a significant role in the roast". [S0015](../sources/S0015-homeroasters-skywalker-roasts-thread.md) [S0017](../sources/S0017-homeroasters-skywalker-mods-thread.md)
- **Contrast — convection drums:** Nordic roasters running ~45 s developments relied on very high
  airflow for the whole roast to develop the coffee [S0022](../sources/S0022-home-barista-nordic-roasters-forum-exercise.md); a home roaster found that cutting
  airflow instead of raising power gave "absolutely terrible results" [S0022](../sources/S0022-home-barista-nordic-roasters-forum-exercise.md). `ctx: gas-drum`

- **Contrast — a leading consultant changed his mind (2026).** Rob Hoos used to think airflow was
  just one heat-transfer route with little effect on flavour; his airflow experiments (mainly drum
  roasters, also seen on fluid beds) now show airflow *tastes different* and changes the
  weight-loss curve. His research is about airflow volume and how it changes inlet and exhaust air
  temperature; drum speed shifts the convection/conduction balance. No data shown. `conf: low`
  `ctx: drum` [S0025](../sources/S0025-roast-rebels-hoos-cultivars-airflow-interview.md) Forum members relay it as "lower airflow raises input air temperature and
  dries faster"; one Quest owner's inlet temperature barely changes with airflow, and nobody has
  tested the flavour effect [S0028](../sources/S0028-home-barista-roasting-phase-ratios.md). `ctx: gas drum / electric air`
- **Airflow also moves where the heat comes from (hot-air drums).** A Roest L200 owner roasted one coffee twice to equal duration and about equal loss, once with high airflow and a low inlet temperature and once with lower airflow and a higher inlet. Drum pressure was held equal. Air temperature inside the drum was about the same although the inlet temperatures differed by nearly 28 °C (50 °F) at the peak; the high-airflow roast needed more heater power, the low-airflow roast ran lower drum and exhaust temperatures, and bean-probe readings were higher in the high-airflow roast, which he puts down to faster transfer to the probe. Cup: "extremely similar", the low-airflow roast slightly better in body and juicy fruit (not blind, not replicated). `conf: low` `ctx: electric drum, Roest L200` [S0053](../sources/S0053-home-barista-desnudo-conduction-convection-thread-roest-airflow.md)
- **Hold the environment temperature and airflow barely shows in the bean curve (gas drum).** One owner made the environmental temperature (ET) follow one curve at four airflow levels (20–50 % of the machine's air range) and the bean-temperature curves almost overlaid; a 750 g vs 1,500 g test gave a delayed copy of the same curve. Replies: more air makes the burner work harder, which heats the drum, so conduction does not simply fall; and drying is more affected by air temperature than by the other paths. No cup results. `conf: low` `ctx: gas drum` [S0054](../sources/S0054-home-barista-conduction-vs-convection-test-results-are-confusing.md)
- **Same heat plan, only airflow changed (induction drum).** 440 g of Rwanda in a Bullet R1 with airflow at 1 vs 9 (of 12), heat 9 until 160 °C then P5, slow drum. High airflow ran about 30 s later at every stage, never rose faster than ~12 °C/min (22 °F/min) against ~17 °C/min (30 °F/min) after drying at low airflow, was pulled 3 °C (6 °F) lower after the same time past first crack, and lost 11.5 % against almost 13 %. In the cup the high-air roast was brighter and more complex and the low-air one tasted a bit more developed; the author stresses there is "no one size fits all". One pair, one taster, no replicate, and the original Bullet sensor gave a steep, probably false, jump after first crack in the low-air roast. `conf: low` `ctx: induction drum, half batch` [S0047](../sources/S0047-sweet-marias-bullet-r1-airflow-test-rwanda-kageyo.md)
- **Fluid bed: lowest fan that still fluidises.** A roastery lowered the fan on its Sivetz as far as still gave proper fluidisation and a Q grader scored the same washed Castillo blind at 83.25 and 84.5 (better body, balance, aftertaste). Second-hand, a Roest owner got better body and sweetness from lower paddle speed with less energy. No times, temperatures or fan values given. `conf: low` `ctx: fluid bed` [S0052](../sources/S0052-desnudo-2026-conduction-vs-convection-taste.md)
- **Judge airflow by the exhaust-to-bean gap (gas drum).** Rob Hoos reads airflow from the exhaust-air curve against the bean curve: a wide gap that lasts means airflow is too low (hotter metal and inlet air, scorching and tipping risk), an exhaust curve that dips close to the bean curve is safe, one that hugs it may be too slow. His rules: change the fan early (before 50 % of the roast), down-batch to 75–80 % if first crack is later than 8:30–9:00, and he sees more people with airflow set too low than too high. No numeric gap is given. `conf: low` `ctx: gas drum` [S0058](../sources/S0058-hoos-how-to-adjust-coffee-roaster-airflow-lighter-method.md)

## In practice
- **Higher fan on light roasts (V2 Skywalker, 250 g):** one owner finds higher fan and drum speed
  best for light roasts and says it makes heater adjustments more responsive; his schedule raises
  fan from 65 % to ~78 % through first crack. `conf: low` [S0027](../sources/S0027-coffeesnobs-skywalker-roasters-thread.md)
- **Kaleido (IR + hot air):** one experienced user runs maximum airflow throughout [S0026](../sources/S0026-home-barista-kaleido-m10-astringent-roasts.md).
  `ctx: Kaleido`
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
- **A fan step is also a speed step.** The Bullet half-batch ran ~30 s slower at high air [S0047](../sources/S0047-sweet-marias-bullet-r1-airflow-test-rwanda-kageyo.md), and on electric drums more air also needs more heater power [S0053](../sources/S0053-home-barista-desnudo-conduction-convection-thread-roest-airflow.md) [S0054](../sources/S0054-home-barista-conduction-vs-convection-test-results-are-confusing.md). On the Skywalker the fan only removes heat, so changing it alone changes roast speed along with whatever else it does. To isolate airflow, compensate power to land first crack at the same time, or accept that you are testing speed — see [experiment 8](../skywalker/experiments.md). **Inference — test it.**
- **Inference — test it:** one Roest owner's bean probe read higher with more air [S0053](../sources/S0053-home-barista-desnudo-conduction-convection-thread-roest-airflow.md). If yours does too, a fan step shifts first-crack and drop readings on its own, so compare fan settings by time and weight loss, not by temperature.
- No airflow test in the base was run on a lamp roaster; every cup comparison is a single pair.

## Contested

**Restricted or high airflow?**

- **Restrict it:** a natural Red Bourbon from Rwanda lost over 15 % on four standard profiles and tasted green, tart and sweet-less; restricting airflow all roast cut loss to 14.5 % (about 0.75 points less) at a similar end temperature and development time and gave a balanced, fruit-forward cup [S0040](../sources/S0040-hacea-roast-approach-rwanda-muhororo-natural.md). Its Swiss Water decaf was astringent on every standard profile; three roasts that combined a lower-heat "soak" with longer-restricted airflow removed the astringency [S0041](../sources/S0041-hacea-roast-approach-swiss-water-rwanda-muhororo.md). Grade B, `ctx: gas-drum, 400 g in a 1.5 kg drum`, one coffee each, airflow changed together with other things.
- **Keep it high:** a Kaleido user runs maximum airflow throughout [S0026](../sources/S0026-home-barista-kaleido-m10-astringent-roasts.md); a V2 Skywalker owner raises the fan from 65 % to ~78 % through first crack and finds light roasts best with higher fan and drum speed [S0027](../sources/S0027-coffeesnobs-skywalker-roasters-thread.md). Grade C.
- **Possible reading (not stated by the sources):** the gas-drum writer's usual practice is full airflow just before first crack and the change was to restrict it for longer, so the 'restrict' and 'keep high' accounts may describe different stretches of the roast; the machines also remove heat with air to very different degrees.
- **Inference — test it:** on the Skywalker the fan *removes* heat from the beans, so a lower fan setting also makes the roast faster. A fan-only test is confounded unless you compensate power or compare at equal timing.

**Newer evidence (Build 7) — `conf: contested`.**

- **Lower air looked better, or no worse:** the fluid-bed fan test (83.25 → 84.5, one blind pair) [S0052](../sources/S0052-desnudo-2026-conduction-vs-convection-taste.md); the Roest comparison at equal time and loss, low air slightly better but "extremely similar" [S0053](../sources/S0053-home-barista-desnudo-conduction-convection-thread-roest-airflow.md); the two restricted-airflow fixes above [S0040](../sources/S0040-hacea-roast-approach-rwanda-muhororo-natural.md) [S0041](../sources/S0041-hacea-roast-approach-swiss-water-rwanda-muhororo.md).
- **Higher air looked better, or is the safer default:** the Bullet high-airflow roast was brighter and more complex (the author says no one size fits all) [S0047](../sources/S0047-sweet-marias-bullet-r1-airflow-test-rwanda-kageyo.md); Hoos sees airflow set too low more often than too high and runs 100 % air at half batch [S0058](../sources/S0058-hoos-how-to-adjust-coffee-roaster-airflow-lighter-method.md); a Colombian washed light roast that tasted underdeveloped was assigned to too little airflow or heat, and more airflow is the fix offered [S0051](../sources/S0051-cho-2023-firescope-light-roast-colombian-washed-2.md).
- **It may not change the roast much if the heat is compensated:** four airflow levels at one ET curve gave almost the same bean curve [S0054](../sources/S0054-home-barista-conduction-vs-convection-test-results-are-confusing.md); one electric Quest owner says his machine "does not respond to airflow adjustments much at all" [S0053](../sources/S0053-home-barista-desnudo-conduction-convection-thread-roest-airflow.md).
- **Why they may not conflict:** the complaints differ (green or sweet-less cup, scorching and tipping, speed), the machines differ (gas drum, induction, hot-air electric, fluid bed) and each test changed airflow together with something else (heater power, inlet temperature or roast time). None was repeated. Hoos's "too low" is a scorch-and-tip concern read from an exhaust probe [S0058](../sources/S0058-hoos-how-to-adjust-coffee-roaster-airflow-lighter-method.md); the gas-drum "restrict it" cases were about a green-tasting natural and an astringent decaf [S0040](../sources/S0040-hacea-roast-approach-rwanda-muhororo-natural.md) [S0041](../sources/S0041-hacea-roast-approach-swiss-water-rwanda-muhororo.md).
## Open questions
- Recommended fan curves from Skywalker owners at 350 g; how much a fan step changes RoR. The
  V2 owner's 250 g schedule [S0027](../sources/S0027-coffeesnobs-skywalker-roasters-thread.md) is the only worked example so far.
- Whether Hoos's airflow findings (taste, weight-loss curve) hold on a lamp-heated roaster where
  air mainly cools. **Inference — test it:** repeat a roast with a fan step and compare weight loss.
- Is there an exhaust-versus-bean signal a Skywalker owner can use as Hoos does [S0058](../sources/S0058-hoos-how-to-adjust-coffee-roaster-airflow-lighter-method.md)? The Skywalker has no exhaust probe in the stock setup (not checked for every version).
- How much of the Bullet's 30 s delay and 6 °F lower end temperature [S0047](../sources/S0047-sweet-marias-bullet-r1-airflow-test-rwanda-kageyo.md) would a fan step of the same relative size give on a lamp roaster, and does the brighter cup survive compensating for speed?
