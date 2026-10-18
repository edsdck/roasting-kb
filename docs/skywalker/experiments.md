# Experiments to try

*Suggested by the Builder. One variable at a time; keep batch size (350 g), fan and room airflow
fixed; cup blind; compare at equal roast degree (weight loss within ±0.5 % if no colour meter —
**Inference**). Updated 2026-10-18 (Build 7).*

## 0. Setup first — Artisan RoR settings
Set sampling to 1 s and delta span ≈ 15 s, minimal extra smoothing [S0008](../sources/S0008-rao-what-is-baked-coffee.md). If the RoR line becomes
unreadably noisy on the Skywalker, lengthen the span and note the value you settled on.

## 0b. Log two extra things with every roast
- **Green moisture:** ask the supplier or measure it; Hoos targets light-roast weight loss ~1–2 %
  above moisture [S0025](../sources/S0025-roast-rebels-hoos-cultivars-airflow-interview.md) and wetter coffee needs more mid-roast energy [S0025](../sources/S0025-roast-rebels-hoos-cultivars-airflow-interview.md).
- **Drop relative to first crack:** note drop BT minus first-crack BT with each roast (your data
  show median +8.3 °C) [S0023](../sources/S0023-home-barista-vegetal-flavor-first-crack.md) [S0024](../sources/S0024-home-barista-first-crack-temperature-changed.md).
- **How you mark first crack:** note the time of the first stray pop *and* of the regular pops (three or more in about a second). A stray pop can lead the main crack by 5.6–8.3 °C [S0055](../sources/S0055-home-barista-underdeveloped-coffee-1kg-drum.md), and the 2026 tasting report called it at consecutive pops [S0057](../sources/S0057-cooper-2026-standards-and-the-mother-sauce.md); your development time and ΔT depend on which you use.
- **Rest days and probe depth:** write down how many days the beans rested before tasting, and how far the probe tip sits into the pile (one Quest owner's first-crack reading rose ~11 °C when he pushed the probe in) [S0045](../sources/S0045-home-barista-quest-m6-first-crack-temperature-probe-depth.md) [S0036](../sources/S0036-home-barista-hacea-roast-approach-tasting-kit.md).
- **Green density:** weigh a fixed volume of green coffee (e.g. 100 ml in a measuring cylinder) → g/L.
  Density changes how a coffee takes heat [S0014](../sources/S0014-lee-2025-bean-density-roasting.md).

## 0c. Lamp-friendly preheat (setup, not an experiment)
Experienced owners avoid the factory preheat (100 % heater, fan off): preheat in manual at your
roasting power (≤ 75–80 %) with ≥ 40–50 % air, and start the roast timer *before* charging so the
heater doesn't jump to 100 % when you open the door [S0016](../sources/S0016-homeroasters-skywalker-main-thread.md) [S0017](../sources/S0017-homeroasters-skywalker-mods-thread.md). Keep the preheat routine
identical from roast to roast — it's part of the profile.

## 1. Measure the lamp lag
**Why:** power changes act late on this machine [S0001](../sources/S0001-skywiki-infrared-roaster.md); you need to know how late to plan changes.
**How:** in a normal roast, make one clean power step (e.g. −10 %) mid-Maillard. Note the time until
the RoR visibly changes direction. Repeat once.
**Outcome:** a number ("my lag ≈ X s") to plan all future changes earlier by. For scale: drum roasters quote 30 s or more from a heat change to the beans [S0046](../sources/S0046-home-barista-why-ror-is-a-bad-reference-webinar.md).

## 2. Development time at equal degree — **do this next**
*Your roasts have settled at ~1:00 development (DTR ~9 %), shorter than anything in the research,
and your one cupped roast (0:41) was sharp and flat — see [findings](findings.md).*

**Why:** at equal colour, shorter development = brighter/sweeter, longer = roastier/bitter [S0006](../sources/S0006-alstrup-2020-development-time-sensory.md).
Practitioners disagree on how short is too short: Rao (one practitioner's opinion) says 20–25 % DTR [S0018](../sources/S0018-rao-2014-development-time-ratio.md); light roasters use
13–16 % / 1:20–1:30 [S0021](../sources/S0021-home-barista-development-time-light-roasts.md); an experienced Skywalker owner's best early cup was ~1:35 (18 %) [S0015](../sources/S0015-homeroasters-skywalker-roasts-thread.md). Newer: a 2026 recipe proposes 1:00–1:20 for a very light roast [S0057](../sources/S0057-cooper-2026-standards-and-the-mother-sauce.md), a chart gives 1:00 (natural) or 1:30 (washed) [S0063](../sources/S0063-cooper-eqmr-roast-level-flavour-profile-strategies-chart.md), and a gas-drum thread wants 2:00–2:15 for a new machine or coffee [S0055](../sources/S0055-home-barista-underdeveloped-coffee-1kg-drum.md) — so the three arms below sit on those three numbers.
**How:** one coffee (the Costa Rican Natural or Colombia you have now), three roasts with your usual
path to first crack; development ≈ **1:00 / 1:30 / 2:15**. On your machine development time drives
weight loss (r = 0.72), so expect loss to rise with it; if you want equal degree, lower the heater
during development for the longer ones rather than dropping earlier. Rest equally, cup blind.
**Rest:** let every sample rest the same time — **at least a week, two if you can wait** — and taste each at day 7, 14 and 28 if you can. Forum advice for light roasts runs from a week to 4–6 weeks [S0036](../sources/S0036-home-barista-hacea-roast-approach-tasting-kit.md), and id39 was cupped at 5 days; if the cup changes more with rest than between roasts, rest is the bigger lever (see [Resting & degassing](../kb/resting-and-storage.md)).
**Variant (2b) — by temperature, not seconds:** your id39 (+6.2 °C above first crack, 0:41) and
id40 (+12.0 °C, 1:12) are the same coffee, so cup them blind side by side first (rest equally, ≥ 5 days).
If id39 tastes raw/vegetal and id40 does not, repeat the pair at +6 / +9 / +12 °C. One roaster
reports a vegetal note that stays until ~5.6 °C above first crack [S0023](../sources/S0023-home-barista-vegetal-flavor-first-crack.md); a roaster who dropped ~5.6 °C above first crack after a fast dry end found no vegetal notes but thin body [S0023](../sources/S0023-home-barista-vegetal-flavor-first-crack.md).
Your probe and first-crack call differ from theirs, so you are looking for *your* threshold.
Because development time and ΔT move together on your machine (r = 0.78), use the heater during
development to change one without the other if you can.

**Taste for:** acidity, sweetness, fruit vs roasted, bitterness, body — and grainy/vegetal notes,
the classic signs of too-short development [S0019](../sources/S0019-sweet-marias-first-crack-faq.md) [S0016](../sources/S0016-homeroasters-skywalker-main-thread.md). Mark first crack the same way in all
three (at regular pops, not the first isolated pop) [S0019](../sources/S0019-sweet-marias-first-crack-faq.md).

## 3. Flat vs declining RoR after drying
**Why:** IR theory says a flat RoR may be fine here [S0002](../sources/S0002-skywiki-convection-vs-radiant.md); drum advice says avoid crashes and keep
RoR declining [S0008](../sources/S0008-rao-what-is-baked-coffee.md). Contested.
**How:** same coffee, same first-crack time, development time and weight loss; roast A holds power
steady after drying (flatter RoR), roast B steps power down from ~minute 4 in 5–10 % steps
(70 → 60 → 50 %, as an experienced owner recommends [S0017](../sources/S0017-homeroasters-skywalker-mods-thread.md)). Cup blind; triangle test
if unsure they differ [S0005](../sources/S0005-coffeemind-rate-of-rise-bad-reference.md).
**Taste for:** hollowness/flatness, sweetness, does it hold up as it cools [S0008](../sources/S0008-rao-what-is-baked-coffee.md).

## 4. 350 g vs 400 g — how readings shift
**Why:** smaller loads read lower on this probe [S0003](../sources/S0003-skywiki-renatoa-words-of-wisdom.md).
**How:** same settings, two batch sizes; note first-crack temperature and time.
**Outcome:** a correction you can use when changing batch size.

## 5. Repeat a good roast by replaying its events
**Why:** replaying heater/fan changes reproduced roasts as well as PID on Skywalkers [S0009](../sources/S0009-skywiki-putrid-upstairs-response.md).
**How:** load your best recent roast as the Artisan background profile and replay its events on the
same coffee and batch size. **Inference — test it:** compare first-crack time, drop time and cup.
**Outcome:** tells you how repeatable the machine is — the baseline every other experiment needs.

## 6. Why does Honduras Honey crack hotter — the coffee or the speed?
*Your Honduras roasts crack ~6 °C higher, but they were also slower; within each coffee, first-crack
time barely predicts the reading — see [findings](findings.md).*

**Why:** some roasters see first crack at the same reading for every bean on a consistent machine
[S0020](../sources/S0020-home-barista-bean-temperature-at-first-crack.md); others find it bean-dependent [S0019](../sources/S0019-sweet-marias-first-crack-faq.md) [S0020](../sources/S0020-home-barista-bean-temperature-at-first-crack.md). Your data can't separate coffee from speed.
**How:** roast the Honduras Honey and a washed coffee (e.g. the Ethiopian) back-to-back at 350 g with
the same preheat and heater/fan plan, aiming for the **same first-crack time**. In Artisan, mark
the *first pop* with a custom event and FCs at *regular pops* [S0019](../sources/S0019-sweet-marias-first-crack-faq.md). Note room temperature, and re-seat the probe at the same depth each time (a Quest M6 read ~11 °C higher after the tip was pushed in from ~1 to ~1.75 in [S0045](../sources/S0045-home-barista-quest-m6-first-crack-temperature-probe-depth.md)).
**Outcome:** gap persists at equal speed → it's the coffee (or how it cracks); gap shrinks → it was
the slower profile. Either way you learn which number to trust for timing development.


## 7. Charge hotter, lower power — does it remove "done"/astringent notes?
**Why:** on an IR roaster (Kaleido, IR + hot air) an experienced user cut astringency with a higher
charge, lower power percentages, small stepwise cuts and no big power swings [S0026](../sources/S0026-home-barista-kaleido-m10-astringent-roasts.md); drum users
found cool charges left the inside behind [S0026](../sources/S0026-home-barista-kaleido-m10-astringent-roasts.md). A longer browning phase also correlated with less
vegetal/astringent character on an IKAWA [S0026](../sources/S0026-home-barista-kaleido-m10-astringent-roasts.md). **Inference — test it** on a lamp roaster.
**How:** one coffee, 350 g, same fan. Roast A: your usual charge and heater plan. Roast B: charge
~10–15 °C hotter with the same or slightly lower start power, then reduce power in small steps
from about minute 4 (as in experiment 3), no big cut at first crack. Keep first-crack time and
development time within a few seconds of each other. Cup blind.
**Arm C (optional, "soak"):** same charge as A, but start power and fan ~10 points lower until about minute 2, then bring power up so first crack still lands within seconds of A. It is borrowed from a gas-drum fix for a dense decaf that tasted astringent on standard profiles [S0041](../sources/S0041-hacea-roast-approach-swiss-water-rwanda-muhororo.md) — one coffee, three things changed at once — so treat it as a probe, not a recipe.
**Read the result carefully:** a Colombian production test found charge temperature changed roast time but not the cup at medium colour [S0043](../sources/S0043-osorio-2022-cenicafe-initial-roast-temperature-sensory-quality.md). If A and B end with the same first-crack time and development, a cup difference points to the power plan and the steps, not to the charge number.
**Taste for:** astringent/drying finish, "done" flavour, sweetness, vegetal/raw notes.


## 8. A fan step, with the heat held — is it airflow or just speed?
**Why:** airflow results are mixed and every test changed something else with it. A Bullet half-batch ran ~30 s slower at high air and cupped brighter [S0047](../sources/S0047-sweet-marias-bullet-r1-airflow-test-rwanda-kageyo.md); lower air looked no worse on a fluid bed and a Roest [S0052](../sources/S0052-desnudo-2026-conduction-vs-convection-taste.md) [S0053](../sources/S0053-home-barista-desnudo-conduction-convection-thread-roest-airflow.md); Hoos thinks most people set it too low [S0058](../sources/S0058-hoos-how-to-adjust-coffee-roaster-airflow-lighter-method.md); and with the heat held the bean curve barely moved on a gas drum [S0054](../sources/S0054-home-barista-conduction-vs-convection-test-results-are-confusing.md). On the Skywalker the fan only removes heat, so a fan step changes speed. **Inference — test it.**
**How:** one coffee, 350 g, same preheat, same heater plan. Roast A: your usual fan. Roast B: fan ±15 points from dry end (before half the roast is done [S0058](../sources/S0058-hoos-how-to-adjust-coffee-roaster-airflow-lighter-method.md); go lower if your fan is already at 80–90 % late) with the heater nudged by 5–10 % so first crack lands within about 10 s of A. Optional roast C: the same fan step with no heater change, to see the pure speed effect. Hold development and weight loss equal. Note the first-crack and drop readings — one Roest read higher bean temperatures with more air [S0053](../sources/S0053-home-barista-desnudo-conduction-convection-thread-roest-airflow.md).
**Outcome:** (1) how many seconds a fan step costs, (2) whether the cup differs when timing is matched. Cup blind, same rest.

## 9. Maillard 4:00 versus 3:30
**Why:** a one-page chart expects the same light roast to taste less sweet, with less body and more acidity and fruit when the middle phase is cut from 4:00 to 3:30 [S0063](../sources/S0063-cooper-eqmr-roast-level-flavour-profile-strategies-chart.md); your median Maillard is 4:06 and the 2026 recipe uses 3:00–3:30 [S0057](../sources/S0057-cooper-2026-standards-and-the-mother-sauce.md). Chart and recipe, not a test. A Probat series found a 30–40 s change in drying audible, though that changed total time as well [S0035](../sources/S0035-sweet-marias-stretchin-out-the-roast-pt3.md).
**How:** one coffee, 350 g. Roast A: your usual plan (Maillard ~4:00). Roast B: same dry end, a little more power in browning so first crack comes ~30 s sooner; hold development (~1:08) and weight loss equal. Mark first crack the same way (see 0b). Cup blind.
**Taste for:** sweetness and body against acidity and fruit.

## 10. (Optional) Portions or one big container — after four weeks
**Why:** the only measured storage test found a screw-cap bag best and a transferred-to-canister coffee worst on a chemical index, with no taste data [S0048](../sources/S0048-smrke-2022-coffee-storage-methods-after-opening.md); the review says loss is fastest early and oxygen is the driver [S0049](../sources/S0049-sage-2012-shelf-life-roasted-coffee-staling-review.md). **Inference — test it:** at home, headspace and reopening are what you control.
**How:** after one roast, split ~300 g into two airtight containers: A is one small full jar opened only on the tasting day; B is the same beans in a larger container opened daily. Rest and store the same way; cup blind at week 4.
**Outcome:** whether you taste the closure at all. If not, it does not matter for your volumes.
