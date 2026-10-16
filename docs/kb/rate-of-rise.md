---
title: Rate of rise (RoR)
---

# Rate of rise (RoR)

!!! abstract "In short"
    - RoR = how many degrees per minute the bean-probe temperature is rising. It's the slope of the BT curve, not new information.
    - Use it as a **speedometer**: are you heading for first crack early or late? `conf: medium`
    - Mainstream drum advice (Rao) says keep RoR declining smoothly and avoid a "crash" near first crack. This is **contested**, and on an IR roaster a *flat* RoR may be normal.
    - RoR curves are noisy and depend on probe and software settings — check your Artisan settings before reading too much into them.

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

Not settled. See also [Myths & contested](myths-and-contested.md) and [Defects](defects.md).

## Open questions
- Controlled sensory data comparing crash vs no-crash roasts at equal colour and development.
- Real Skywalker RoR curves paired with cupping notes.
