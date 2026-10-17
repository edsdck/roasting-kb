---
title: Rate of rise (RoR)
---

# Rate of rise (RoR)

!!! abstract "In short"
    - RoR = how many degrees per minute the bean-probe temperature is rising. It's the slope of the BT curve, not new information.
    - Use it as a **speedometer**: are you heading for first crack early or late? `conf: medium`
    - One influential drum-roasting author (Rao; take with a grain of salt, not a rule) says keep RoR declining smoothly and avoid a "crash" near first crack. This is **contested**, and on an IR roaster a *flat* RoR may be normal.
    - RoR curves are noisy and depend on probe and software settings — check your Artisan settings before reading too much into them.
    - Two physics-minded forum threads add: with a steady environment temperature the bean temperature approaches it smoothly, so a declining RoR is the default and wiggles are mostly noise; heat changes take 30 s or more to reach the beans, so chasing RoR mid-roast is too late. Others answer that crashes and plateaus lasting tens of seconds are real and RoR is a good planning tool. **Contested.** `conf: low`

## Concepts

- **Definition.** Degrees per minute the bean-pile temperature is increasing; plotted through the
  roast as the RoR curve. [S0008](../sources/S0008-rao-what-is-baked-coffee.md)
- **Why it usually declines (hot-air machines).** As the beans approach the environment
  temperature, the gradient shrinks and heating slows. At constant gas and airflow a roaster
  shows a fairly stable declining RoR on its own. `conf: medium` `ctx: gas-drum` [S0005](../sources/S0005-coffeemind-rate-of-rise-bad-reference.md) [S0008](../sources/S0008-rao-what-is-baked-coffee.md) [S0002](../sources/S0002-skywiki-convection-vs-radiant.md)
- **Why it may stay flat on IR.** With a radiant source much hotter than the beans, energy
  delivery is roughly constant, so a flat RoR can simply mean stable energy delivery.
  `conf: low` `ctx: IR (reasoning)` [S0002](../sources/S0002-skywiki-convection-vs-radiant.md)
- **Early-roast artefact.** After charge the probe is hotter than the beans and has to shed heat,
  so software shows RoR starting low and rising for the first minutes; the real early RoR is high
  and drops fast. `conf: low` [S0008](../sources/S0008-rao-what-is-baked-coffee.md)
- **The "crash".** Near first crack, moisture leaving the bean cores is cooler than the bean
  surfaces/probe and can make RoR drop rapidly. `conf: low` [S0008](../sources/S0008-rao-what-is-baked-coffee.md)
- **The "flick".** A late rise in RoR after a crash. Crashed roasts are more likely to flick and to
  be underdeveloped, which muddles tasting. `conf: low` [S0008](../sources/S0008-rao-what-is-baked-coffee.md) A deliberately exaggerated flick
  profile in a lab study didn't change *peak* acidity, but its acidity timing differed from other
  profiles [S0007](../sources/S0007-anokye-bempah-2024-titratable-acidity.md).
- **Why RoR declines by itself (physics argument).** With a constant environment temperature (ET) the bean temperature climbs toward it along a smooth curve, so a smooth decline is the default and flicks or crashes are noise or a first-crack disturbance. A heat change takes 30 s or more to reach the beans in a drum roaster. The same BT profile can taste different if ET and batch load differ; too high an ET gave an acrid cup. Argued by Jim Schulman (another_jim) and others, partly relaying a webinar by CoffeeMind's Münchow that the Gatherer did not read. Grade C, forum. `conf: low` `ctx: multiple machines` [S0046](../sources/S0046-home-barista-why-ror-is-a-bad-reference-webinar.md)
- **Reading the curve.** Two RTD probes 1–2 cm apart with a 10 s delta span and no smoothing gave RoR traces that "very much agree"; with 20 s smoothing they correlate, so you wait about 20 s to know a bump is real. Probe mounting changes the look: a 4 mm probe bolted to a gas drum's faceplate gave a straight RoR line, a thinner insulated one did not, though both declined. `conf: low` [S0046](../sources/S0046-home-barista-why-ror-is-a-bad-reference-webinar.md)
- **Timed schedules instead of watching RoR.** One roaster holds gas steady for about 3:20 from charge (no soak) and then lowers it 0.5 kPa every 30 s (perforated-drum Huky, 400 g); Schulman starts turning heat down at BT 190 °C on a Quest (reported; adj. ≈ 175 °C) and sets the decrease from a constant ET. Gas drums cut to near zero still coast 20–30 °F (11–17 °C) toward second crack. `conf: low` [S0046](../sources/S0046-home-barista-why-ror-is-a-bad-reference-webinar.md)
- **A Quest owner's numbers (NoStream).** Aggressive power at the end of the ramp (about 360–370 °F BT = 182–188 °C reported; adj. ≈ 167–172 °C), a momentum entry to first crack, then heat cut and fan up gave about 1:45 from first crack to drop, a RoR of 8–10 °F/min (4.4–5.6 °C/min) in development, a drop 15–25 °F (8–14 °C) after first-crack start, 12–13.5 % weight loss and a ~20 % development ratio. `conf: low` `ctx: electric drum, Quest` [S0044](../sources/S0044-home-barista-matt-perger-on-roast-development.md)

## In practice

- **Speedometer use.** Watch RoR to predict whether you'll reach first crack (or another
  waypoint) on time. `conf: medium` [S0005](../sources/S0005-coffeemind-rate-of-rise-bad-reference.md) [S0001](../sources/S0001-skywiki-infrared-roaster.md)
- **Categorizing profiles.** Average RoR after first crack can label your own profiles
  (higher = shorter development, typically brighter). Only comparable on one machine. [S0005](../sources/S0005-coffeemind-rate-of-rise-bad-reference.md)
- **Don't roast the software.** A textbook straight declining RoR produced worse espresso than a
  less "perfect" curve; ask "are you roasting the software or the coffee?" `conf: low` [S0011](../sources/S0011-cooper-cropster-rate-of-rise-production.md)
- **Window size.** RoR is computed over a window (often 30 or 60 s). A 60 s window reads directly
  in °/min, which helps planning; shorter windows react faster but are noisier. [S0011](../sources/S0011-cooper-cropster-rate-of-rise-production.md) [S0008](../sources/S0008-rao-what-is-baked-coffee.md)
- **Don't chase small wiggles.** Small RoR fluctuations are magnified by the derivative and are
  likely below what tasters can detect at equal colour. `conf: low` [S0005](../sources/S0005-coffeemind-rate-of-rise-bad-reference.md)
- **Hardware shapes the line.** Probe type, size, placement, wiring and power all add noise;
  curves from different machines aren't comparable — match phase timings and colour instead.
  `conf: medium` [S0011](../sources/S0011-cooper-cropster-rate-of-rise-production.md) [S0005](../sources/S0005-coffeemind-rate-of-rise-bad-reference.md)
- **Data quality first.** Slow (thick) probes hide crashes; heavy smoothing hides them too. Rao's
  settings: 1 s sampling, Artisan *delta span* ≤ 15 s, no extra smoothing, and a probe fast enough
  that the turning point shows by ~1:30. `conf: low` `ctx: gas-drum` [S0008](../sources/S0008-rao-what-is-baked-coffee.md) See
  [Measurement & Artisan](measurement-and-artisan.md).

## On the Skywalker (IR)

- The Skywalker's lamp lag makes RoR respond slowly; large corrections overshoot or collapse,
  so steer with a few early changes. `conf: medium` [S0001](../sources/S0001-skywiki-infrared-roaster.md) [S0016](../sources/S0016-homeroasters-skywalker-main-thread.md)
- **Typical Skywalker numbers (other owners):** ~11 °C/min at dry end falling to 6–7 at first crack,
  rarely above ~11 (renatoa, 250 g) [S0015](../sources/S0015-homeroasters-skywalker-roasts-thread.md); 12–14 °C/min (400 g) [S0015](../sources/S0015-homeroasters-skywalker-roasts-thread.md); ≤ 11 °C/min in a cool
  room [S0015](../sources/S0015-homeroasters-skywalker-roasts-thread.md). 14–20 °C/min shows up with high mains voltage or very hot settings, and an
  experienced owner doubts that suits radiant heat (only the top layer absorbs) [S0015](../sources/S0015-homeroasters-skywalker-roasts-thread.md). `conf: low`
- **A V2 owner's RoR targets (250 g, "convection-adjusted"):** dry end (150 °C) 11–12 °C/min, mid
  Maillard 9–10, late Maillard 8–9, pre-FC 7–8, flick to 7–8 at FC, drop 4–5 °C/min; if RoR falls
  under a floor he adds 3–5 % power. `conf: low` [S0027](../sources/S0027-coffeesnobs-skywalker-roasters-thread.md) Compare your ~9 °C/min at first crack.
- **Shaping it:** to avoid flat stretches and a sharp step, start reducing power around minute 4
  and in steps (70→60→50 %) rather than the factory's single 70→50 % step at 170 °C. `conf: low`
  [S0017](../sources/S0017-homeroasters-skywalker-mods-thread.md)
- **The panel's RoR is a 1-minute average**, refreshed once a minute on V1 (about every 30 s on V2)
  — use Artisan's. [S0015](../sources/S0015-homeroasters-skywalker-roasts-thread.md) [S0016](../sources/S0016-homeroasters-skywalker-main-thread.md) Trier pulls and data spikes also distort Artisan's RoR [S0017](../sources/S0017-homeroasters-skywalker-mods-thread.md).
- Its probe reads an air–bean mix where air is cooler than the beans [S0003](../sources/S0003-skywiki-renatoa-words-of-wisdom.md), which will also
  shape the RoR curve. **Inference — test it:** don't judge a Skywalker curve against the shape
  of a gas-drum "ideal" curve.
- Whether a declining or flat RoR tastes better on this machine is an open question → see the
  flat-vs-declining experiment in [experiments](../skywalker/experiments.md).

## Contested

**Does a crashing or non-declining RoR cause "baked" coffee?**

- **Yes (Rao):** the main cause of baked coffee is a pronounced RoR crash — a drastic change in
  RoR slope; flatness and lost sweetness scale with crash severity. Evidence: consultancy
  experience and curve examples; clients learned to identify crashed roasts blind. Grade C, gas drum. [S0008](../sources/S0008-rao-what-is-baked-coffee.md)
- **Not a useful reference (Münchow / CoffeeMind):** "constantly declining RoR" is a vague theory
  that makes no specific flavour predictions, can't be tested at equal colour and development,
  and small differences are typically undetectable. Use time, temperature and colour instead.
  Grade C (author also has published sensory research, [S0006](../sources/S0006-alstrup-2020-development-time-sensory.md)). [S0005](../sources/S0005-coffeemind-rate-of-rise-bad-reference.md)
- **IR angle:** on a radiant roaster a flat RoR may be normal, while on convection a flat RoR
  implies rising energy input, which "can taste baked or dull". Grade C, IR reasoning. [S0002](../sources/S0002-skywiki-convection-vs-radiant.md)
  An experienced Skywalker owner now says the "declining RoR mantra" doesn't apply to radiant
  roasting and a flat RoR in drying is "the new normal" (opinion, 2026) [S0015](../sources/S0015-homeroasters-skywalker-roasts-thread.md) — though two years
  earlier he advised a continuously declining RoR after dry end on the same machine [S0017](../sources/S0017-homeroasters-skywalker-mods-thread.md). His
  accidental flat-RoR development tasted fine (one cup) [S0015](../sources/S0015-homeroasters-skywalker-roasts-thread.md).

- **Crash and flick around first crack (gas drums):** energy "where it should be" just before first
  crack minimizes the flick-and-crash [S0028](../sources/S0028-home-barista-roasting-phase-ratios.md); one roaster avoids the pre-FC hump, crash and flick with a
  hard gas cut 30–40 s before FC [S0028](../sources/S0028-home-barista-roasting-phase-ratios.md); on a Kaleido a plateau before first crack followed by a
  crash was said to lose sweetness [S0026](../sources/S0026-home-barista-kaleido-m10-astringent-roasts.md). Grade C, `ctx: gas drum / IR + hot air`.

- **Heavy gas drum vs light electric roaster.** Members say a declining RoR is easier on a heavy, stable gas drum than on lighter perforated electric ones, and that a light roaster lacks the momentum to coast through first crack: without a power push at the endothermic point before crack it stalls and then bakes. Against it: one roaster has "not found correlation between declining rate of rise and better coffee", another says forcing it down after first crack makes things worse, Milligan says some coffees will not give a straight RoR at his roast level and still taste great ("a great RoR with a 320 °F drop is still a bad roast"), while rmongiovi says the point of a decline is to develop the inside without over-developing the outside — it says nothing about flavour by itself. Second-hand claim that raising RoR at any stage widens the outside–inside gap (a workshop, relayed). Grade C, forum threads. [S0044](../sources/S0044-home-barista-matt-perger-on-roast-development.md) [S0046](../sources/S0046-home-barista-why-ror-is-a-bad-reference-webinar.md)

Not settled. See also [Myths & contested](myths-and-contested.md) and [Defects](defects.md).

- **Your RoR (P, n=41; not shifted):** 9.1 °C/min at first crack (5.8–11.5), 6.4 °C/min 60 s later (4.7–10.9, n=31), 6.3 °C/min at drop (1.2–9.4). The Quest owner's 4.4–5.6 °C/min through development [S0044](../sources/S0044-home-barista-matt-perger-on-roast-development.md) is a little below your figure, but the machines, probes and drops differ. **Inference — test it:** the "push into first crack, then cut" pattern on a light roaster [S0044](../sources/S0044-home-barista-matt-perger-on-roast-development.md) resembles what the factory programs do at 170 °C [S0016](../sources/S0016-homeroasters-skywalker-main-thread.md) and what other Skywalker owners advise (reduce power from about minute 4, in steps); the open point is how much momentum your 350 g needs.

## Open questions
- Controlled sensory data comparing crash vs no-crash roasts at equal colour and development.
- Real Skywalker RoR curves paired with cupping notes.
- How much of a real RoR "crash" on a lamp roaster is lag from the lamp rather than a change in the beans? (30 s or more in a drum [S0046](../sources/S0046-home-barista-why-ror-is-a-bad-reference-webinar.md); longer on a lamp [S0001](../sources/S0001-skywiki-infrared-roaster.md).)
