# What to do next

*The plain version, updated 2026-11-20 (Build 14). The reasoning and sources for each idea are in [Experiments — background](experiments-detail.md).*

## This weekend: clean the roaster, then roast once

**The question:** does the "infamous" bitter flavour come from the dirty roaster?

1. **Clean the roaster.** Empty the chaff tray, then brush or vacuum the drum and chimney. Keep liquid off the lamps and electronics, and check the manual for your model. Write "cleaned [date]" in the roast notes.
2. **Roast the same Colombia with the id44 plan (1:30)**, changing nothing else:
   * Charge 180 w/ 70% heater and 40% air
   * Increase heater to 80% @ BT 90 °C (just after TP)
   * Increase AIR to 50% @ BT 148 °C
   * Decrease heater to 70% @ BT 154 °C
   * Decrease heater to 65% @ BT 177 °C
   * Increase AIR to 70% @ 1C
   * Decrease heater to 48% @ 1C + 0:15
   * Decrease heater to 30% @ 1C + 0:35
   * Dev = 1:30, drop
3. **Compare the timing with id44:** dry end 5:03, first crack 8:25. If yours is more than about 30 s off, note it, because a clean drum can run a little differently.

## Tasting day: about 2026-12-05

Taste three cups together, blind, with your second taster, using the same brew. Let them cool and taste again.

- **id44** — 1:30, roasted before cleaning
- **id45** — 2:14, roasted before cleaning
- **the weekend roast** — 1:30, roasted after cleaning

For each cup write down sweetness, bitterness, body, and whether the "infamous" flavour is there.

| If you find… | It means… |
|---|---|
| The weekend roast is clearly less "infamous" than id44 | The dirty roaster was the cause. Keep it clean. |
| It tastes the same as id44 | Cleaning wasn't the cause. Look at the profile and the green coffee next. |
| id45 tastes better than id44 | A longer finish helps. Note it, but id45 is also darker (15.1 vs 13.7 % loss). |
| id44 tastes better than id45 | 1:30 is enough. Don't go longer. |

## Every roast: log these

- Roasted weight (14 roasts have none).
- How you marked first crack: the first stray pop, or regular pops (three or more in about a second) [S0055](../sources/S0055-home-barista-underdeveloped-coffee-1kg-drum.md).
- Probe depth, and the coffee name in Artisan.
- Rest days at each tasting, and the brew recipe.
- Whether the roaster was cleaned since the last roast, and any visible smoke.

## Already done

- **Your brewing is fine:** store-bought coffee tastes right on your setup, and a coarser grind only added acidity (id40).
- **Your roast is repeatable:** id44 reproduced id42.
- **How fast the heater works:** the RoR reacts about 15–30 s after a heater step and is mostly settled by 60 s. After first crack, each heater point is worth about 0.35 °C/min (rough). Plan changes about 30 s early. [Background](experiments-detail.md#1-measure-the-lamp-lag).

## Ideas for later

Not urgent; each needs two roasts that differ in one thing only.

- **Flat vs declining RoR before first crack** [S0002](../sources/S0002-skywiki-convection-vs-radiant.md) [S0008](../sources/S0008-rao-what-is-baked-coffee.md). [Details](experiments-detail.md#3-flat-vs-declining-ror-after-drying)
- **A shorter middle phase:** first crack about 30 s sooner [S0063](../sources/S0063-cooper-eqmr-roast-level-flavour-profile-strategies-chart.md). [Details](experiments-detail.md#9-maillard-400-versus-330)
- **A hotter charge with lower power** [S0026](../sources/S0026-home-barista-kaleido-m10-astringent-roasts.md) [S0043](../sources/S0043-osorio-2022-cenicafe-initial-roast-temperature-sensory-quality.md). [Details](experiments-detail.md#7-charge-hotter-lower-power-does-it-remove-doneastringent-notes)
- **A fan step with the heat held.** [Details](experiments-detail.md#8-a-fan-step-with-the-heat-held-is-it-airflow-or-just-speed)
- **350 g vs 400 g** [S0003](../sources/S0003-skywiki-renatoa-words-of-wisdom.md). [Details](experiments-detail.md#4-350-g-vs-400-g-how-readings-shift)
- **Why Honduras Honey cracks hotter,** only if you roast it again. [Details](experiments-detail.md#6-why-does-honduras-honey-crack-hotter-the-coffee-or-the-speed)
- **Storage in portions vs one container.** [Details](experiments-detail.md#10-optional-portions-or-one-big-container-after-four-weeks)
- **Preheat and Artisan RoR settings:** preheat the same way every time and start the timer before charging [S0016](../sources/S0016-homeroasters-skywalker-main-thread.md) [S0017](../sources/S0017-homeroasters-skywalker-mods-thread.md); set sampling to 1 s and delta span to about 15 s [S0068](../sources/S0068-makomo-artisan-blog-on-idle-noise-rtd-vs-tc-ror-delay.md). [Details](experiments-detail.md#0-setup-first-artisan-ror-settings)
