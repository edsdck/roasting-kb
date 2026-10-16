---
id: S0016
title: "Skywalker, the ALM chinese one pound roaster (Home Roasters forum main thread)"
url: "https://homeroasters.org/forum/viewthread.php?thread_id=6974"
type: forum
author: "Home Roasters forum members — mainly renatoa (forum administrator); also HarryDog, Mike_Mathis, allenb, sloppyjosh and others"
author_credentials: "renatoa: forum admin, years of building convection roasters, among the first Skywalker V1 owners, reverse-engineered the factory profiles (also source of S0003; S0001 appears to summarise several of these posts). allenb: long-time drum and fluid-bed home roaster"
published: 2023-11-24   # thread start; posts run to 2025-11-14
accessed: 2026-10-16
language: en
grade: C
heat: IR
machine: "Skywalker V1 (ITOP CBR / ALM), mostly 250 g (renatoa) and 350 g (others); mentions of V2"
topics: [heat-transfer, measurement-and-artisan, roast-planning, charge-and-batch, equipment, rate-of-rise]
novelty: mixed
corroborates: [S0001, S0003, S0009]
kb_status: integrated
---

# S0016 — Skywalker main thread (Home Roasters forum)

**Author:** several Skywalker owners, mainly renatoa · **Type:** forum thread (339 posts, Nov 2023 – Nov 2025) · **Grade:** C · **Heat context:** IR · [Original](https://homeroasters.org/forum/viewthread.php?thread_id=6974)

## Summary
The original Skywalker discussion on the Home Roasters forum. renatoa documents how the V1's
factory "Auto" mode works (fixed lookup tables, no feedback), how the preheat logic behaves and why
it should be overridden, an empty-machine test showing heat comes mainly from the beans, and his
general approach (few, well-timed power changes). Other owners add first-roast numbers and a
side-by-side reading of the stock probe against an added thermocouple. Much of the physics here is
already summarised in S0001/S0003; the new material is the factory profile logic, preheat/charge
practice, lamp-life advice and specific roast readings.

## Key claims
1. **C1** — The V1 Auto mode is a fixed table of presets with no feedback from roast progress: preheat 200 °C (naturals), 220 °C (washed), 215 °C (honey) with fan at zero, controlled on/off with ~10 °C overshoot on first preheat; at roast start heater 65 % (naturals, honey) or 70 % (washed), fan 65 %; at 170 °C heater drops to 40 % with fan 90 % (naturals) or 50 % with fan 80 % (washed); drop is at a preset temperature (e.g. 196 °C for naturals).
   > "it seems there aren't algorithms involved, simply some lookup tables with parameters (presets), and that's all..." — *post #10, renatoa, 2023-11-25*
   > "For example, preheat temp is 200C for naturals, 220C for washed, and 215 for honey. Fan is zero during preheat." — *post #10*
   > "When temperature reach 170C parameters are changed to 40% heater and 90% fan for naturals, or 50% htr 80% fan for washed." — *post #10*
2. **C2** — Because Auto drops at a fixed temperature, development time depends on where each coffee cracks: two roasts with FC at 191 °C and 184 °C got ~40 s and ~2 min of development; both were within medium roast.
   > "For two roasts today, different origins, one having FC at 191C and the other at 184, you can guess the result: very different development times, 40 seconds vs 2 minutes... but both were ok, withing the boundaries of the medium roast range." — *post #10*
3. **C3** — With 250 g on the gentlest (natural) auto program, FC came around 6:40.
   > "loaded with 250g of greens, using natural, the least powerful profile, that starts preheated at 200C, with 65% power, then reduced to 40% at 170C FC, FC happens in the 6:40 ballpark." — *post #20*
4. **C4** — The machine has lots of power for its load: empty, preheated to 220 °C, at only 50 % heater it hit the 250 °C over-temperature limit (error E2) in under a minute.
   > "when empty, preheated at 220C, then started a simulated roast (empty) with power reduced at 50%, the 250 C limit is reached in less than a minute, entering into error E2 = over temp protection." — *post #20*
5. **C5** — The Skywalker lamp is a near-infrared (NIR, visibly glowing) source, which heats surfaces rather than penetrating deeply, unlike far-IR panels; it should not be confused with gas "IR burners" that heat a drum.
   > "NIR produces superficial heat, not penetrating too deep the tissues." — *post #22, renatoa*
   > "Do not mismatch IR burners, as those used in Diedrich rosters to heat the drum, with direct to bean IR radiation." — *post #22*
6. **C6** — The machine has high inertia from the lamp, not from drum mass; use logged data to plan the next roast rather than to steer in real time; 3–5 power changes per roast, timing matters more than size.
   > "it has very high inertia, almost as a commercial drum, but due to different reasons, in this case is the lamp/heat source inertia, not the drum mass accumulated heat" — *post #46, renatoa*
   > "Roasting with Skwalker means only few power changes, not many... probably 3-5 are more than enough... most important is now when to change, rather than how much." — *post #46*
7. **C7** — Empty-machine test: on program P11 (40 % heater, 90 % fan after 170 °C) the empty roaster levelled at ~178–179 °C for 15 minutes, while with beans the same program reaches its ~194 °C cut-off; so during a roast the probe's heat comes mainly from the beans.
   > "you imagine my surprise to find that 40% heater and 90% fan alone are unable to heat the empty machine beyond 179C !" — *post #50*
   > "Thus, during a real roast the heat measured by probe comes mainly from the beans, with minimal environment influence, unlike any other designs known so far." — *post #50*
8. **C8** — The factory preheat is on/off with oscillations of at least ±5 °C; lowering the heater to the roast-start level and adding air ~20–30 °C before the set point (e.g. 65 % / 65 %) cuts overshoot to ~2 °C.
   > "Oscillations having at least 5 C degrees amplitude, over and under." — *post #62*
   > "For example, 65% Heater and 65% air would reduce the over/under shoot to 2 degrees." — *post #62*
9. **C9** — At charge the factory preheat logic sees the temperature drop (opening the door alone costs ~5 °C) and pushes the heater to 100 % until the roast timer is started — an unwanted heat spike at charge. Fix: start the roast (R) before charging so the heater sits at its start level, or preheat in manual at the chosen power.
   > "When we charge, even the lamp is off, the temperature drops by about 5 degrees just due the simple fact we removed the entrance door... enough for the preheat logic to push up the heat at 100%." — *post #73*
   > "The solution for profile roasting is to press R, the heat will drop to 70% and stay there, then charge beans." — *post #90*
10. **C10** — 40 % heater with 65 % fan holds an empty machine at about 178–179 °C continuously.
    > "As I already wrote, 40% heater with 65% fan is good for 178-179 C, continuous regime." — *post #73*
11. **C11** — With FC at 181–182 °C on this machine, beans show clear yellow at about 150 °C (allenb had expected first yellow at 151–160 °C).
    > "Yes, it's around 150C, rather under than above.
    > I mean at 150C are visible yellow, not just a pale hue change.
    > Sounds logical to be under 150C, if FC is at 181-182C." — *post #75, renatoa*
12. **C12** — An added thermocouple (shorter, placed lower/right) read well below the stock probe in one owner's roast: preheat 200 vs 154 °C, TP 99 vs 115 °C, DE 150 vs 136 °C, FC 185 vs 166 °C, drop 185 vs 179 °C; sloppyjosh saw similar on his.
    > "Sky Roaster Thermocouple
    > PHT 200C 154C
    > TP 99C 115C
    > DE 150C 136C
    > FC 185C 166C
    > Drop 185C 179C" — *post #87, HarryDog*
13. **C13** — In Manual mode the V1 panel lets you set an automatic heater-stop temperature with the +/- keys (default 230 °C); renatoa uses it to end roasts at a planned temperature for repeatability. His roasts always dropped below 194 °C.
    > "Short story, is about a way to automatically drop heater at a preset temperature, which could improve the precision and repeatability of your roasts." — *post #63*
    > "if looking at my roasts that were always dropped under 194C." — *post #63*
14. **C14** — Don't use the factory preheat (100 % heater, no airflow): it accelerates lamp wear and, on 115 V units, overheats the control board. Preheat at the power you will use while roasting (≤75–80 %) with ≥40–50 % air. The lamp lasts about 100 kg; keep a spare (part AER350). V2 preheats at 80 % / 20 % air.
    > "do not use factory preheat, with power at 100% and no airflow !!!
    > It's lamp aging acceleration on steroids, more than the roast itself !" — *post #284*
    > "But remember that lamp life is limited to about 100 kgs... a wise man would buy a spare without waiting that milestone." — *post #309*
    > "On V2 they finally reduced to 80% power, increasing air to 20%." — *post #309*
15. **C15** — The V1 panel RoR is computed once per minute (shown alternating with the profile number in Auto), which makes it nearly useless for steering; V2 appears to update about every 30 s, as an integer.
    > "computed only per minute intervals of time... so it could barely be considered an information of interest, almost useless to drive the roast process." — *post #63*
    > "seems to be updating every 30 seconds now" — *post #301 (V2)*
16. **C16** — First-roast example: 350 g washed Panama, profile 22 in Assist mode: DE 4:50 at 170 °C, FC 6:00 at 181 °C, end 8:29 at 197 °C, 14.28 % weight loss. Charging after the 220 °C preheat let the temperature run to 230 °C before the timer was started.
    > "DE was 4:50 in @170°. 1C was 6:00 in @ 181°. End was 8:29 @ 197°." — *post #88, Mike_Mathis*
    > "I was aiming for about 14% W/L and it ended at 14.28% so not bad." — *post #88*
17. **C17** — One owner gets a "green nasty acidic" taste unless he roasts long/hot enough on this machine.
    > "I get a green nasty acidic taste if I don't roast it long-hot enough. For me this is something you just have to roast past on this roaster." — *post #282, HarryDog*
18. **C18** — Expected drift: coffee deposits will darken the drum over dozens of roasts, increasing heat absorption and drum-to-bean contact heating; 5–10 % more air may compensate (renatoa's expectation, not measured).
    > "Probably 5-10% more air should be enough to counteract this effect." — *post #139*

## Numbers & parameters
| Parameter | Value | Context (machine, batch, unit) | Claim |
|---|---|---|---|
| Auto preheat | 200 / 220 / 215 °C (natural / washed / honey) | V1 factory profiles, fan 0 | C1 |
| Auto start power | 65 / 70 / 65 %; fan 65 % | V1 factory | C1 |
| Auto step at 170 °C | 40 % heater + 90 % fan (natural); 50 % + 80 % (washed) | V1 factory | C1 |
| Auto drop (natural) | 196 °C | V1 factory | C1 |
| Preheat overshoot | ~10 °C first, then 1–2 °C; ≥5 °C amplitude (later post) | factory on/off | C1, C8 |
| Development, two auto roasts | 40 s (FC 191 °C) vs 2 min (FC 184 °C) | same program, different origins | C2 |
| FC time | ~6:40 | 250 g, natural program | C3 |
| Over-temp limit | 250 °C (E2), reached <1 min at 50 % empty | V1 | C4 |
| Empty-machine plateau | 178–179 °C | 40 % heater, 65–90 % fan | C7, C10 |
| P11 cut-off | ~194 °C | with beans | C7 |
| Charge door temp drop | ~5 °C | V1 | C9 |
| Yellow | ~150 °C | FC 181–182 °C, renatoa | C11 |
| Stock vs added TC | PHT 200/154, TP 99/115, DE 150/136, FC 185/166, drop 185/179 °C | HarryDog V1 | C12 |
| Heater auto-stop default | 230 °C | V1 manual mode | C13 |
| Preheat advice | ≤75–80 % heater, ≥40–50 % air | V1 | C14 |
| Lamp life | ~100 kg | V1 (AER350 element) | C14 |
| Assist 22 roast | 350 g; DE 4:50/170 °C; FC 6:00/181 °C; end 8:29/197 °C; 14.28 % | Mike_Mathis | C16 |

## Relevance to Skywalker (IR, 350 g)
*Gatherer judgement:* Same machine. C1/C2 explain why auto roasts vary so much in development; C9
and C14 are practical (charge without the 100 % spike; gentler preheat for lamp life). C11's
yellow at ~150 °C and C16's FC at 181 °C / DE at 170 °C are useful reference points. C12 is one
owner's numbers with an oddly placed thermocouple — it says probe placement changes readings a lot,
not which reading is "true".

## Gatherer notes
- Factory-table inconsistency: post #10 says washed gets 50 % heater + 80 % fan at 170 °C; the
  mods thread (S0017, post #82) and thread 7063 give fan 90 % for all and honey at 45 % / 40 %.
  Versions may differ; record as uncertain.
- C7 and C6 are the original posts behind S0001 C6 and C1/C4/C5 (corroborating, same author).
- C12's thermocouple TP (115 °C) is higher than the stock probe's (99 °C) while every other point is
  lower — possibly a transcription quirk in the original post; quoted as written.
- Thread 7063 ("Profile chart for Skywalker built in Profiles") repeats C1; registered as duplicate.
- Attached images (graphs, photos) were not viewed.
