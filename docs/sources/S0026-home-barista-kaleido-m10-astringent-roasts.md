---
id: S0026
title: "Buyers Remorse - Kaleido M10 Astringent Roasts (Home-Barista)"
url: "https://www.home-barista.com/roasting/buyers-remorse-kaleido-m10-astringent-roasts-t92558.html"
type: forum
author: "Agtron70 (OP), Rytopa, drgary, yakster, Milligan, GDM528, PaulTheRoaster, amh0001, others"
author_credentials: "OP is a self-described novice who also owns two Kaffelogic Nano 7 roasters; Rytopa says he has used Kaleido machines and owned a Bullet; drgary (Team HB) and yakster are long-standing forum regulars on other machines. Rytopa's total experience is not stated."
published: 2024-02-25
accessed: 2026-10-16
language: en
grade: C
heat: IR
machine: "Kaleido M10 (Gen 2, sealed; carbon-fibre infrared heating plus hot-air circulation per vendor pages), Artisan control; comparison roaster Kaffelogic Nano 7"
topics: [heat-transfer, defects, development, charge-and-batch, measurement-and-artisan]
novelty: novel
corroborates: []
kb_status: new
---

# S0026 — Buyers Remorse - Kaleido M10 Astringent Roasts (Home-Barista)

**Author:** Agtron70 and others · **Type:** forum thread (45 posts, 5 pages, 2024-02-25 to 2024-02-29) · **Grade:** C · **Heat context:** IR (Kaleido; vendor pages describe carbon-fibre infrared heating plus hot air) · [Original](https://www.home-barista.com/roasting/buyers-remorse-kaleido-m10-astringent-roasts-t92558.html)

## Summary
A new Kaleido M10 owner finds every coffee astringent, even though the same beans on his Kaffelogic Nano 7 taste excellent and the roast colour (Agtron 70–74) and weight loss match. Changing development (15–30 %), roast length (6:30–12:30) and charge temperature did not help while he ran Artisan PID control. Replies split between "charge too cool, inside under-developed" (drgary, yakster) and "infrared roasters tip easily and PID power swings are the problem; use a higher charge, lower power percentages and small stepwise power cuts" (Rytopa). The owner reports a "positive result" after switching to manual power steps, without describing the cup in detail. No cup data other than the owner's descriptions are shown.

## Key claims
1. **C1** — Same coffee, matched colour and weight loss, very different cups: the M10 roasts are astringent and the Nano 7 roasts excellent; varying development (15–30 %) and roast length (6:30–12:30) did not help.
   > "The beans are roasted to similar levels on both the Kaffelogic and the Kaleido as measured by my Difluid Omni roast analyzer - between an Agtron 70 and 74." — *post #1, Agtron70*
   > "The beans also have very similar weight loss during roasting." — *post #1, Agtron70*
   > "I've tried short development (15%), long development (30%), long roasts (12:30), short roasts (6:30), baking the roasts, etc." — *post #1, Agtron70*
2. **C2** — Even with a charge raised from 160 to about 210 °C (displayed), the PID-driven M10 roast tasted "done" with a drying astringent aftertaste, and a longer roast at the same charge was much worse.
   > "a subtile but very noticeable tongue drying astringent after taste" — *post #17, Agtron70*
   > "Same charge temp - longer roast - much worse result." — *post #17, Agtron70*
3. **C3** — Rytopa: infrared roasters tip easily, which causes bitterness and astringency; remedy is a higher charge with a lower power percentage and gentle, stepwise power cuts.
   > "IR roasters like the Kaleido are quite different compared with normal roasters, they tip easily, leading to bitterness and astrigency" — *post #14, Rytopa*
   > "so the trick is to use higher charge, but lower peak % to get the roast going" — *post #14, Rytopa*
   > "power adjustment cannot be drastic, but very subtle, slowly lowering the power thruout the roast, at around 180c is when bigger cuts happen" — *post #14, Rytopa*
4. **C4** — Rytopa's reason: as beans darken they absorb more heat from an infrared source, so power must fall faster, and thermocouple lag means corrections must come before they show on the curve.
   > "M10 is predominately driven by Infrared, which will require drastic adjustments to the power as the beans get darkers, as it absorbs more heat from the heat source" — *post #29, Rytopa*
   > "corrective heat adjusts have to be made before its shows up in the graph" — *post #29, Rytopa*
5. **C5** — Rytopa's M10 power schedule (small batches not specified): 80 % charge power, maximum airflow throughout, then −2 % steps from 160 °C, −5 % steps from 180 °C, back off before FC, −10 % about 45 s after FC.
   > "How i usually set up is 80% charge power, airflow max thruout, 160c -2%, 165c -2%, 170 -2% 175c -2% 180c -5% 185 -5% -190c -5%, at this point as you are nearing FC, you will likely back off from the heat adjustments and let it run thru FC, 45 secs after FC, -10% followed by -10% every 5c" — *post #29, Rytopa*
   > "180c (critcal temp where by beans have lost most of the moisture and is very sensitive to heat)" — *post #29, Rytopa*
6. **C6** — Rytopa advises against PID driving on the M10: wide power swings hurt the beans; use PID only to set the charge temperature, then replay temperature-triggered power steps.
   > "PID roasting on the M10 is a big no no, the wide swings in % power is causing a lot of problems for the beans" — *post #27, Rytopa*
   > "PID is good for setting the Charge Temp and that is about it." — *post #27, Rytopa*
7. **C7** — After switching to manual power steps plus a higher charge the owner reports a positive result; he also sees downward RoR spikes at each power change and wonders about a momentary disturbance of the IR heating.
   > "A positive result achieved by using manual roasting and the power settings advised by rytopa and an elevated charge temperature suggested by many." — *post #37, Agtron70*
   > "The downward spikes generally correlate with movements in the power settings" — *post #37, Agtron70*
8. **C8** — drgary and yakster: astringency came from a charge that was too cool, leaving the inside under-developed while the outside reached the drop temperature.
   > "I noticed that when I charged too cool I got astringent roasts. I'm guessing that I didn't develop the inside of the bean enough while the outside got to target temperature for the drop." — *post #10, drgary (drum roaster, cool room)*
   > "you may be under developing the inside of the bean because you compensate with a low charge temp by applying a lot of heat to get the bean to first crack" — *post #11, yakster*
9. **C9** — Too much momentum into FC makes a plateau and crash, which loses sweetness; high initial airflow with low charge and high heat can tip.
   > "you're coming into first crack with too much momentum. This creates a plateau just before first crack and a crash that can lose sweetness." — *post #16, drgary*
   > "High initial air flow with high heat and low charge temp can be a recipe for tipping in my experience." — *post #5, Milligan*
10. **C10** — GDM528 (IKAWA, stepped profiles): a longer browning phase correlated with less vegetal and astringent character, achievable by a larger initial temperature step.
    > "I did note a correlation between the duration of the browning phase and vegetal+astringency: longer = less horrible." — *post #38, GDM528*
11. **C11** — Heat-source cycling is blamed by amh0001 (relaying Scott Rao); drgary says an automated roast can taste good if the PID is well set and watched, and that always-decreasing, gradual heat should heat the bean through evenly.
    > "He said he always notices an astringency that the coffee gets from the heat source going on and off over and over." — *post #44, amh0001*
    > "As long as that's done gradually the coffee should heat through evenly." — *post #45, drgary*

## Numbers & parameters
| Parameter | Value | Context (machine, batch size, unit) | Claim |
|---|---|---|---|
| Colour matched | Agtron 70–74 | M10 vs Nano 7, owner's DiFluid Omni | C1 |
| Development / roast time tried | 15–30 % / 6:30–12:30 | M10, owner | C1 |
| Charge tried | 160 → ~210 °C displayed (owner believes the probe reads ~20 °C low) | M10 PID roasting | C2 |
| FC reading | 178–180 °C on M10 vs ~198 °C on Nano 7 (owner's belief: M10 probe ~20 °C low) | same bean | C2 |
| Rytopa start / steps | 80 % power; −2 % per 5 °C 160–175 °C; −5 % per 5 °C 180–190 °C; −10 % at FC+45 s and per 5 °C after | M10 manual power | C5 |
| M10 batch size (other owner) | 650–850 g typical | Ypuh, post #15 | context |

## Relevance to Skywalker (IR, 350 g)
*Gatherer judgement:* This is the closest IR-specific evidence found so far on astringency and tipping. It supports the owner's own observation that fast IR roasts can look done outside but be under-developed inside (S0015, S0017) and offers a practical rule: charge hotter, run lower lamp power, and cut power in small steps instead of large swings. The "Kaleido M10" differs from a Skywalker V1: it has hot-air circulation in addition to the infrared heaters and takes larger batches, so heat-transfer proportions are not the same. The advice on PID swings relates to the 5 % heater steps of S0016/S0017. The astringency link to a short browning phase (C10) and to cold charges (C8) is a testable idea for the owner's light roasts.

## Gatherer notes
- Roaster temperature readings on this M10 were thought to be ~20 °C low by the OP; absolute numbers should not be compared with a Skywalker.
- The OP does not describe the cup after his final change, only "a positive result" (post #37).
- Rytopa's claims are unsupported by data and his experience level is not stated.
- Later threads by the same OP ("Roasting on a Kaleido", 2026-01) and "Profile tips" (M10) were seen in search results but not read.
