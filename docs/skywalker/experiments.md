# Experiments to try

*One variable at a time. Keep the coffee, batch (350 g), preheat and brew the same within a test, taste blind, and rest the samples equally. Updated 2026-11-20 (Build 13). The reasoning and sources for each are in [Experiments — background](experiments-detail.md).*

## Status

| # | Experiment | Status | Next step |
|---|---|---|---|
| 2 | Development 1:30 vs 2:14 | **Running** | Taste id44 vs id45 blind at 10–14 days (about 2026-11-30 to 12-04) |
| 11 | Hunt the bitterness | **Next** | Arm D: clean the roaster, repeat the 1:30 plan |
| 1 | Lamp lag | Done from logs | A dedicated step test only if you want a tighter number |
| 5 | Repeat a roast by replaying it | Done in effect | You replayed id42's plan by hand; id44 reproduced it |
| 3 | Flat vs declining RoR | Open | Needs two matched roasts |
| 9 | Maillard 4:00 vs 3:30 | Open | Needs two matched roasts |
| 7 | Hotter charge, lower power | Open | Needs two matched roasts |
| 6 | Why Honduras cracks hotter | Open | Only if you roast Honduras again |
| 8 | Fan step, heat held | Open | Low priority |
| 4 | 350 g vs 400 g | Open | Low priority |
| 10 | Storage: portions vs one container | Optional | After four weeks |
| 0 | Artisan RoR settings | Setup | A ten-minute idle recording |

## Experiment 2 — development 1:30 vs 2:14 (running)

- **Question:** on the same coffee, does a longer finish change sweetness, bitterness and body?
- **Done:** id41 (1:01) vs id42 (1:30) in October–November (1:30 tasted sweeter), and id44 (1:30) vs id45 (2:14) roasted on 2026-11-20.
- **Next:** rest both 10–14 days. With a second taster, taste blind with the same brew, hot and again after cooling. If you still have any id42, add it as a third cup.
- **Taste for:** sweetness, bitterness, body, fruit vs roasted, and whether the "infamous" flavour is stronger in either.
- **Caveat:** the pair differs in roast degree too (13.7 vs 15.1 % loss), and id45 reached first crack 29 s later.
- Background: [details](experiments-detail.md#2-development-time-at-equal-degree).

## Experiment 11 — hunt the bitterness

*Bitterness is in all five cupped roasts. What is left after your own checks is the roaster, the profile and the green coffee.*

| Arm | What | Status |
|---|---|---|
| A | Pick out charred and pale beans | **Routine** — you already do this every roast |
| B | Brew: coarser grind, cooler water | **Mostly done** — a coarser grind (10 micro-steps) only added acidity, and store-bought coffee tastes right on your setup, so brewing is unlikely |
| C | Rest: taste at 1, 4, 14 and 28 days | Partly seen — id39 and id40 were still bitter at 34–41 days |
| D | **Clean the roaster, then repeat the 1:30 plan** | **Next** |

**Arm D:**

1. Clean the roaster: chaff tray, drum and chimney. Keep liquid off the lamps and electronics, and check the manual or Skywalker owner threads for method.
2. Roast the id44 plan (1:30, same coffee, temperature-triggered) soon after, so the rest days match id44's closely.
3. Taste it blind beside id44 (uncleaned roaster), same rest and same brew, with your second taster.
4. **Reading it:** the "infamous" flavour clearly weaker → the dirty roaster was the cause. Same → look at the profile and the green coffee next.

Write "cleaned [date]" in the roast notes.

Background: [details](experiments-detail.md#11-hunt-the-bitterness-one-roast-split-several-ways).

## Every roast: log these

- Roasted weight (14 roasts have none).
- How you marked first crack: the first stray pop, or regular pops (three or more in about a second) [S0055](../sources/S0055-home-barista-underdeveloped-coffee-1kg-drum.md).
- Probe depth, and the coffee name in Artisan.
- Rest days at each tasting, and the brew recipe.
- Whether the roaster was cleaned since the last roast, and any visible smoke.

## Preheat and RoR setup

- **Preheat the same way every time.** Experienced owners avoid the factory preheat (100 % heater, fan off) and preheat at roasting power, at most 75–80 %, with 40–50 % air or more. Start the roast timer before charging so the heater does not jump to 100 % when the door opens [S0016](../sources/S0016-homeroasters-skywalker-main-thread.md) [S0017](../sources/S0017-homeroasters-skywalker-mods-thread.md).
- **Artisan RoR:** sampling 1 s, delta span about 15 s, and little extra smoothing. To tune it, record about two minutes with no beans and keep the shortest span that removes the wander. Each span costs half its length in delay [S0068](../sources/S0068-makomo-artisan-blog-on-idle-noise-rtd-vs-tc-ror-delay.md).

## Experiment 1 — lamp lag (done from logs)

From id39–id43: the RoR starts to react about 15–30 s after a heater step and is mostly settled by 60 s. Before first crack a −10 point step lowers it by about 1–2 °C/min over a minute. After first crack the effect is larger, roughly 0.35 °C/min per heater point. This is rough (five roasts, natural RoR decline mixed in, steps near the drop cut off). On id45 the model predicted 3–4 °C/min at the drop and the log showed about 5.5, so the post-crack figure is probably a little high. Plan changes about 30 s before you want to see them. [Background](experiments-detail.md#1-measure-the-lamp-lag).

## The rest

- **3. Flat vs declining RoR after drying.** Roast A holds power steady after drying, roast B steps it down from about minute 4 (70 → 60 → 50 %), same first-crack time, development and weight loss. Taste for hollowness, sweetness and how the cup holds up as it cools. Contested between IR theory and drum advice [S0002](../sources/S0002-skywiki-convection-vs-radiant.md) [S0008](../sources/S0008-rao-what-is-baked-coffee.md). id42 and id44 (flat at ~10 °C/min into first crack) against id43 (declining) already show both shapes, but they are not matched. [Details](experiments-detail.md#3-flat-vs-declining-ror-after-drying).
- **9. Maillard 4:00 vs 3:30.** Roast A your usual plan (about 4:00), roast B the same dry end with more power in browning so first crack comes about 30 s sooner. Hold development (~1:08) and weight loss. A chart expects less sweetness and body with the shorter middle phase [S0063](../sources/S0063-cooper-eqmr-roast-level-flavour-profile-strategies-chart.md). Your id41 had 3:03 and was flat, id42 had 3:13 and was better, so development may explain it. [Details](experiments-detail.md#9-maillard-400-versus-330).
- **7. Hotter charge, lower power.** Roast A your usual plan, roast B charged 10–15 °C hotter with the same or lower start power and small stepwise cuts from about minute 4, no big cut at first crack, with first crack and development matched. One Kaleido user cut astringency this way [S0026](../sources/S0026-home-barista-kaleido-m10-astringent-roasts.md); a Colombian production test found charge changed time but not the cup [S0043](../sources/S0043-osorio-2022-cenicafe-initial-roast-temperature-sensory-quality.md). **Inference — test it.** [Details](experiments-detail.md#7-charge-hotter-lower-power-does-it-remove-doneastringent-notes).
- **6. Why Honduras Honey cracks hotter.** Roast it and a washed coffee back to back aiming for the same first-crack time, mark the first pop and regular pops separately, keep probe depth fixed. If the gap shrinks it was speed; if it stays it is the coffee. [Details](experiments-detail.md#6-why-does-honduras-honey-crack-hotter-the-coffee-or-the-speed).
- **8. A fan step with the heat held.** Roast A your usual fan, roast B fan ±15 points from dry end with the heater nudged so first crack lands within about 10 s of A. Learn how many seconds a fan step costs and whether the cup differs when timing matches. **Inference — test it.** [Details](experiments-detail.md#8-a-fan-step-with-the-heat-held-is-it-airflow-or-just-speed).
- **4. 350 g vs 400 g.** Same settings, two batch sizes; note first-crack temperature and time. Smaller loads read lower on this probe [S0003](../sources/S0003-skywiki-renatoa-words-of-wisdom.md). [Details](experiments-detail.md#4-350-g-vs-400-g-how-readings-shift).
- **10. Storage (optional).** Split ~300 g after one roast: a small full jar opened only on the tasting day against a larger container opened daily; cup both at week 4. [Details](experiments-detail.md#10-optional-portions-or-one-big-container-after-four-weeks).
