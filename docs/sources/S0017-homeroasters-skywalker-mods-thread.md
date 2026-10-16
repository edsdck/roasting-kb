---
id: S0017
title: "Skywalker roaster mods (Home Roasters forum thread) — roasting-relevant posts"
url: "https://homeroasters.org/forum/viewthread.php?thread_id=6979"
type: forum
author: "Home Roasters forum members — renatoa (forum administrator), sloppyjosh (wrote the first Artisan bridge), Mike_Mathis, Dan N, HarryDog, Tomoaki Nakamura, allenb and others"
author_credentials: "sloppyjosh reverse-engineered the V1 controller protocol (basis of the community Artisan firmware). renatoa: forum admin, electronics/roaster builder. Mike_Mathis and HarryDog fitted thermocouples beside the stock probe. Dan N: ~800 DIY-roaster roasts"
published: 2023-12-03   # thread start; posts run to 2026-09-15
accessed: 2026-10-16
language: en
grade: B
heat: IR
machine: "Skywalker V1, 227–430 g batches; stock NTC probe vs added thermocouples/RTDs"
topics: [measurement-and-artisan, rate-of-rise, roast-planning, heat-transfer, equipment]
novelty: mixed
corroborates: [S0001, S0003, S0009, S0016]
kb_status: new
---

# S0017 — Skywalker roaster mods thread (Home Roasters forum)

**Author:** several Skywalker owners · **Type:** forum thread (405 posts, Dec 2023 – Sep 2026); this file covers only the roasting-relevant posts · **Grade:** B · **Heat context:** IR · [Original](https://homeroasters.org/forum/viewthread.php?thread_id=6979)

## Summary
The thread where the community reverse-engineered the V1 controller and built the Artisan
connection (most posts are electronics and are not extracted here). The roasting-relevant parts:
how the stock probe and the roaster's temperature readings behave (NTC thermistor, smoothing,
resolution, noise and spikes), side-by-side comparisons with added thermocouples (including one
washed vs honey roast), why first crack reads ~180 °C on this machine and why that is fine,
renatoa's advice on reducing power earlier and in smaller steps, a 250 g recipe, and practical
notes (5 % control steps, ET as a first-crack early warning, preheat practice, cooling big batches).

## Key claims
1. **C1** — On an early auto-profile roast (300 g, profile 022, City, 12 % loss) renatoa thought the beans looked medium but the weight loss was that of a light roast and the beans were smaller than from a mixed convection/radiation roaster; he suspected IR overheating the surface and suggested lower power, longer roasts, maybe more air. He compared a 6–7 min Skywalker roast to a fluid-bed roast without the convection.
   > "This could mean the IR is too powerful and penetrate only the surface, letting the inside less developed.
   > Should experiment more with Manual mode, using lower power and longer roast times. And maybe more air." — *post #14, renatoa, 2023-12-05*
2. **C2** — renatoa recommends a continuously declining RoR after dry end without flat areas, reducing power earlier (about minute 4) and in several steps (70→60→50 %) rather than the auto logic's single 70→50 % step at 170 °C; fan in smaller steps too.
   > "So the power reduction should start earlier, about minute 4, and be done in many smaller steps, at last two steps 70-60-50 instead the sharp 70-50 at 170C done by auto logic." — *post #10*
3. **C3** — A 250 g recipe that gave a satisfactory ~8-minute roast: preheat 200 °C, start at 60 % heater, step to 50 % at dry end and 40 % at 170 °C. The factory start levels (70 % washed, 65 % naturals) were probably tuned for 350–400 g; 75 % is too much for 227 g. Steps smaller than 5 % don't move the profile much on this machine.
   > "In my tests I found for 250 grams that a 200C preheat, then 60% start value, followed by 2 steps, first at dry end, down to 50%, then the second 40% at 170C led to a satisfactory 8 minute profile, better than good enough." — *post #42*
   > "As I already wrote about the thermal dynamics of this machine, there is no need for steps smaller than 5%, will not move significantly the profile." — *post #42*
4. **C4** — The roaster only accepts heater and fan changes in 5 % steps (other values are ignored); the factory controller drives the lamp with slow PWM of about one-second cycles.
   > "This is correct. I tested by setting something low like 25 then going to 78. Nothing happens. But if you go to 75 you'll see the heater get brighter." — *post #25, sloppyjosh*
   > "the original machine is using for control a slow PWM pulsing method, having about one second cycle" — *post #42, renatoa*
5. **C5** — With the chamber empty the stock probe read about 15 degrees higher than an added probe, but once beans were charged and past the turning point the two matched quite well (unit not stated; the poster works in °F).
   > "I was actually pretty surprised to see that the temps matched up quite well once I charged and the beans hit the turn around. With the chamber empty, The skywalker probe tended to read about 15 degrees high." — *post #26, sloppyjosh*
6. **C6** — Exhaust temperature (ET) rises about 10–20 s before first crack, so an ET probe can warn of FC when it is hard to hear; it comes too late to time power reductions.
   > "Exhaust could be maybe useful to predict the FC approaching, when having troubles with acoustic detection of FC, ET having a rise about 10-20 seconds in advance.
   > But not usable for a power reduction prediction... when ET start to rise, it's already too late to reduce power." — *post #50*
7. **C7** — Airflow in the Skywalker mainly cools the beans; there is no significant hot-air heat source. Beans move both ways in the drum (two vanes push back-to-front, one front-to-back).
   > "The convection acts in the sense of cooling beans mainly, there is no source of hot air having a significant role in the roast." — *post #50*
8. **C8** — Probe position: from renatoa's experiments on another machine, a probe 3–4 mm above the bean bed reads the same as one buried in beans but reacts faster to TP/FC; moving the Skywalker probe would not bring FC up to the ~200 °C seen on other machines.
   > "During my TO experiments I found that a probe not touching anything, at 3-4 mm above beans bed shows the same values as one completely immersed into beans." — *post #90*
   > "Surely would not bring the temperature range back to where the people is accustomed, with FC at 200C/400F, nor allow to compare profiles with those from other non-radiant machines." — *post #90*
9. **C9** — First crack around 180 °C is normal on the Skywalker (the manual gives 170–190 °C); comparing its temperatures with typical internet values, or stretching profiles to match other machines, is a mistake.
   > "FC around 180 is the norm here.
   > Manufacturer states in the manual 170-190 as FC range, and he is right." — *post #149, renatoa*
   > "Trying to stretch the profile to match the other machines is a mistake even bigger." — *post #149*
10. **C10** — Side-by-side stock probe vs installed thermocouple, two Assist/Auto roasts (Mike_Mathis): the thermocouple read higher throughout — about 5–11 °C higher on a honey Colombian (FC by TC 197.9 °C at 6:22) and 1–15 °C higher on a washed Guatemala — 12–15 °C from minute 2 on (FC by TC 198.2 °C at 5:42). He wondered whether processing explains the bigger gap; both roasts ran fast (drop ~7:26–7:38) on a 124–125 V supply.
    > "Roast 1 Columbian Aponte Narino (Honey processed)" … "6:30 199 190 -9 FC@ 197.9 6:22" — *post #162*
    > "Roast 2 Guatemala La Flor Del Cafe (washed)" … "5:30 196 182 -14 FC@ 198.2 5:42" — *post #162*
    > "Higher diff in 2nd roast probably because washed -vs- honey process?" — *post #162*
11. **C11** — A thermistor matching the stock one has ±3 °C tolerance at 200 °C vs ±1.5 °C for a K-type thermocouple — not enough to justify a swap; what matters is learning your own FC and drop numbers.
    > "The temperature tolerance at 200C is +/-3C while a K-type thermocouple tolerance is +/-1.5C." — *post #167, Dan N*
    > "Once you've done enough roasts to know the number where FC happens and the number for end/dump that gives the best flavor coffee, it doesn't matter what the absolute number is." — *post #167*
12. **C12** — When the heater was cut early in development (renatoa's accident; see S0015 C8), bean temperature held at 182 °C for 30 s. With fan already at 90 % there is little air margin to steer development as on a typical drum roaster.
    > "Surprise: the temperature was rock stable for 30 seconds at 182C, without sinking even a single C degree.
    > Fan already at 90%, not enough margin to use air as in a typical drum roaster." — *post #178*
13. **C13** — Absolute accuracy matters little in a tumbling bean bed; what matters is linear, consistent readings through development, where FC is ~180 °C on a radiant roaster vs ~200 °C on hot-air machines. The 8–16 °C rise during development is a temperature difference and is more precise than the absolute values.
    > "This could happens at 180C for radiant roaster, or near 200C for for hot air roasters... and both are right, even if only one of them is true." — *post #347*
    > "What is important is to have a consistent monitoring of evolution of progress for the next 8-16 degrees during development." — *post #347*
14. **C14** — The Skywalker already applies a rolling average to its temperature; compared with an RTD it read about 1 °C low even at room temperature.
    > "This is because Skywalker already applied rolling average on the raw temp. It is not a raw temp and quite low compared to raw temp." — *post #346, Tomoaki Nakamura*
    > "Skywalker temp is 1C off(low) in room temp already." — *post #346*
15. **C15** — Readings resolve about 6 ADC steps per °C (≈0.17 °C) from 30–180 °C and 5 per °C (≈0.2 °C) from 180–210 °C; e.g. 175–195 °C spans 111 steps.
    > "we have at least 6 ADC values per C degree (i.e. 0,17C per ADC step resolution) in the range 30-180C, decreasing to 5 ADC values per C degree (i.e. 0,2C per ADC step) in the range 180-210C." — *post #386*
16. **C16** — Roaster data contain occasional temperature spikes that wreck the RoR curve; opening the trier causes a ~2 °C dip that also disturbs RoR. Spike filtering beyond Artisan's rolling average is needed.
    > "the data coming from the roaster could be noisy, so the filtering should be enforced even more, with a separate spike filtering, operating on other logic than rolling average." — *post #232*
    > "This time this is not a data issue, but build/operator issue... is the effect of trier removal !
    > Just 2 degrees drop and recovering 2 seconds back, and such a mess..." — *post #232*
17. **C17** — Preheat in manual mode under roasting-like conditions (max 75 % power, at least 50 % airflow) — "mandatory" on 115 V units because of control-board overheating.
    > "Always preheat in manual mode, under same conditions as during a roast: maximum 75% power and minimum 50% airflow." — *post #288*
18. **C18** — The stock cooling tray struggles above ~430 g: beans were still hot after 3 minutes; an external box-fan screen cooler cooled 430 g in under a minute.
    > "The biggest weakness left for >430g roasts is the cooling system." — *post #205, Dan N*
    > "As expected it cooled a 430g batch in less than a minute." — *post #214*
19. **C19** — Practise on an empty machine: renatoa simulated roasts with no beans to learn the machine's response to commands (with lower power and charge temperature to mimic a loaded TP).
    > "I simply simulated a roast with empty machine, trying to follow a profile, just to train my senses with machine response to different commands." — *post #363*

## Numbers & parameters
| Parameter | Value | Context (machine, batch, unit) | Claim |
|---|---|---|---|
| Auto roast | 300 g, profile 022, 12 % loss, ~City | sloppyjosh | C1 |
| Start of power reduction | ~minute 4; 70→60→50 % | renatoa advice | C2 |
| 250 g recipe | preheat 200 °C; 60 % → 50 % at DE → 40 % at 170 °C; ~8 min | renatoa, 230 V | C3 |
| Too much power | 75 % (750 W) for 227 g | renatoa | C3 |
| Control step | 5 % | V1 protocol | C4 |
| PWM cycle | ~1 s | V1 factory controller | C4 |
| Empty-chamber probe offset | ~15° high (likely °F) | sloppyjosh, added probe | C5 |
| ET early warning | 10–20 s before FC | renatoa | C6 |
| FC (Skywalker) | ~180 °C; manual 170–190 °C | V1 | C9, C13 |
| TC − stock, honey | +5 to +11 °C; FC (TC) 197.9 °C at 6:22; drop 7:26 | Mike_Mathis, 124–125 V | C10 |
| TC − stock, washed | +1 °C at 0:30, then +7 to +15 °C (+12 to +15 from 2:00); FC (TC) 198.2 °C at 5:42; drop 7:38 | same | C10 |
| Thermistor vs K-type tolerance | ±3 °C vs ±1.5 °C at 200 °C | datasheet cited by Dan N | C11 |
| Heater-off hold | 182 °C for 30 s in development | renatoa | C12 |
| Development rise | 8–16 °C | renatoa, radiant | C13 |
| Offset at room temp | ~1 °C low vs RTD | Tomoaki Nakamura | C14 |
| Resolution | ~0.17 °C (30–180 °C); ~0.2 °C (180–210 °C) | V1 sensor/ADC | C15 |
| Trier dip | ~2 °C, recovers in ~2 s | V1 | C16 |
| Preheat | ≤75 % heater, ≥50 % air | V1 | C17 |
| Cooling | stock tray still hot after 3 min at >430 g; external cooler <1 min | Dan N | C18 |

## Relevance to Skywalker (IR, 350 g)
*Gatherer judgement:* Directly relevant to the owner's measurement and control. C9/C13 support
treating ~184 °C FC as normal and focusing on the rise during development rather than absolute
values. C10 is the only side-by-side washed/honey data found (n=2, different coffees, fast roasts),
so it does not explain the owner's honey ~190 °C vs washed ~184 °C (gap #3), but it does show that
the probe offset can differ by coffee. C2/C3 give concrete heater schedules to adapt for 350 g. C16
matters for the owner's RoR readings (trier pulls show up as RoR spikes).

## Gatherer notes
- Only ~70 of 405 posts were read in full; the rest are electronics/firmware. The 6979 thread also
  holds the community Artisan bridge history (relevant to S0009).
- C10: on the washed roast the difference is only 1 °C at 0:30 and 7–8 °C at 1:00–1:30 before
  settling at 12–15 °C; the poster's own table is quoted. Both roasts were fast; he blamed his high mains voltage.
- C12 describes the same event as S0015 C8 (same author, cross-posted).
- C5's "15 degrees" has no unit; sloppyjosh logs in °F elsewhere in the thread.
