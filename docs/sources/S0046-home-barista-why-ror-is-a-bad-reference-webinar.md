---
id: S0046
title: "Why RoR is a bad reference for ... [webinar] (Home-Barista thread)"
url: "https://www.home-barista.com/roasting/why-ror-is-bad-reference-for-t84925.html"
type: forum
author: "baldheadracing (OP), another_jim (Jim Schulman), rmongiovi, Milligan, OldmatefromOZ, luca, MaKoMo, Marcelnl, Trjelenc, TomC and others"
author_credentials: "Forum members. baldheadracing and another_jim are marked Team HB; another_jim says he has built four PID-controlled roasters and wrote a roaster simulation in R; luca lists Q Grader and roasts on a ROEST; rmongiovi roasts on a Hottop; Milligan roasts on a Cormorant; baldheadracing roasts on a Bella Taiwan gas drum; Marcelnl uses a perforated-drum Huky. MaKoMo's signature links artisan-scope.org. Others' experience not stated."
published: 2023-01-14
accessed: 2026-10-17
language: en
grade: C
heat: multiple
machine: "Mixed: Hottop and Quest (electric), Cormorant, Bella Taiwan and Huky (gas drums), ROEST (hot-air); batch sizes mostly not stated (Marcelnl: 400 g)"
topics: [rate-of-rise, heat-transfer, measurement-and-artisan, myths-and-contested, temperature-adjustment]
novelty: mixed
corroborates: [S0044]
kb_status: new
---

# S0046 — Why RoR is a bad reference for ... [webinar] (Home-Barista thread)

**Author:** many forum members · **Type:** forum thread (41 posts over 5 pages, 2023-01-14 to 2023-01-20; all pages read) · **Grade:** C · **Heat context:** multiple · [Original](https://www.home-barista.com/roasting/why-ror-is-bad-reference-for-t84925.html)

## Summary
The thread discusses a webinar and blog post by Morten Münchow of CoffeeMind arguing that rate of rise (RoR) is a poor guide to flavour; the webinar itself was not watched or read for this source, so Münchow's views appear only through the posters. The discussion is a more physical version of the 2015 Perger thread (S0044). Jim Schulman (another_jim) argues that with a steady environment temperature (ET) the bean temperature rises toward ET along a smooth curve, so RoR declines by itself, and that wiggles in the RoR are mostly noise and cannot be corrected in time because heat changes take 30 s or more to reach the beans; others reply that RoR is a planning tool for the next roast and that crashes and plateaus lasting tens of seconds are real. Useful extras: two probes 1–2 cm apart with matching RoR traces, a note that probe mounting changes whether a RoR curve looks straight, and Schulman's model, which needs a lower specific heat from first crack on.

## Key claims
1. **C1** — The same bean-temperature profile (hence the same RoR) can taste different if the environment temperature and batch load differ; too high an ET gives acrid coffee.
   > "still get a different tasting roast if you use 1) a high bean load and a high ET, or 2) a low bean load and a low ET." — *post #4, another_jim*
   > "If it is too high, the coffee gets acrid" — *post #4, another_jim (about environmental temperature)*
2. **C2** — Per a poster summarising the webinar, in blind tasting the largest driver of flavour is roast colour, then end temperature, then time to reach it. *Second-hand.*
   > "in blind tasting, for most people the biggest determining factor for flavour outcomes is roast colour." — *post #7, OldmatefromOZ*
3. **C3** — The physical argument: with a steady ET the bean temperature climbs toward it smoothly, so a smooth RoR decline is the default; flicks and crashes are noise or first-crack disturbance.
   > "If your ET is steady, the bean temperature climbs towards it smoothly and asymptotically, in a negative exponential curve." — *post #12, another_jim*
4. **C4** — A drum roaster is slow to respond: a heat change takes 30 s or more to reach the beans.
   > "Every change you make to the heat will take thirty seconds or more to reach the beans." — *post #15, another_jim*
5. **C5** — The counter-argument: coffee is not a simple system, so a declining RoR is not guaranteed by a constant ET.
   > "However, coffee is not a simple system." — *post #14, Milligan*
6. **C6** — The case for declining RoR as a goal (rmongiovi): it aims at developing the inside of the bean without over-developing the outside, and says nothing about flavour on its own.
   > "a smoothly declining RoR is an attempt at one goal: maximizing the development of the bean interior while minimizing the development of the exterior" — *post #18, rmongiovi*
7. **C7** — Straight-line RoR is not required: Milligan says some coffees will not give a straight RoR at his roast level and still taste great, and says a great RoR with a 320 °F drop is still a bad roast.
   > "Some coffees I've roasted simply will not give a straight line RoR within the roast level I'm targeting. They still taste great." — *post #17, Milligan*
   > "For example, you can have a great RoR and drop at 320F." — *post #30, Milligan*
8. **C8** — Two probes 1–2 cm apart, same RTD and meter, no smoothing, 10 s delta span, gave traces that "very much agree"; Schulman agrees they correlate once smoothed over 20 s, so you wait about 20 s to know whether a bump is real.
   > "To my eye they very much agree modulo some noise from beans bumping, air turbulence and measuring equipment." — *post #25, MaKoMo*
   > "The two traces are tightly correlated if you smooth them over 20 seconds" — *post #28, another_jim*
9. **C9** — Probe mounting changes how straight the RoR looks: a 4 mm probe bolted to the faceplate gives a straight line; the same roast with an insulated or thinner probe does not, though it is always declining. baldheadracing says he asked Rao and does not concern himself with linearity.
   > "Decouple the same probe from the faceplate with insulation, or run a 2.5mm insulated probe, and those RoR curves will not be linear for the exact same roast" — *post #33, baldheadracing*
10. **C10** — Schulman's roast model needs a higher specific heat before first crack and a lower one during and after it, i.e. the beans warm faster for the same heat at first crack; this is offered as a reason to cut heat going into crack.
    > "In my model, the most parsimonious good fit was using two specific heat values, a higher one for before the first crack, a lower one during and after the first crack." — *post #37, another_jim*
11. **C11** — Several roasters coast through development on little or no heat: gas cut to near zero still carries 20–30 °F toward second crack.
    > "Many roasters completely cut gas (or lower it to 5% or so) and still coast for 20-30F to get into 2nd crack quite easily." — *post #39, Milligan*
12. **C12** — A timed power schedule instead of watching RoR: Marcelnl on a perforated-drum Huky, 400 g batches, keeps airflow constant, holds gas steady for about 3:20 from charge (no soak) and then lowers it 0.5 kPa every 30 s; Schulman uses BT 190 °C as the trigger to start reducing heat on a Quest and holds ET constant to set the decrease.
    > "gas power input steady for x seconds (3'20 or thereabout) from charge (no soak) to then decrease by Y Kpa per Z seconds (0.5KPa per 30 sec)" — *post #40, Marcelnl*
    > "I use BT = 190C as my trigger to start turning down the heat" — *post #41, another_jim*
13. **C13** — A ROEST (hot-air) owner's example: a batch that stalled and was manually changed finished at 193.5 °C BT at 6:03 and was light and underdeveloped; moving the inlet-temperature decline later gave 195.8 °C at 6:01 and a better coffee. Münchow's argument as relayed: when a roast has already gone wrong it is too late to rescue, so follow the plan and learn from the failure.
    > "So the roast finished at 193.5C BT at 6:03." — *post #24, luca*
    > "if something has gone wrong in the roast that you have worked out from the graphs, and it is so bad that it is going to cause a taste issue, then it is too late to fix it meaningfully." — *post #24, luca describing the webinar*

## Numbers & parameters
| Parameter | Value | Context (machine, batch, unit) | Claim |
|---|---|---|---|
| Lag from a heat change to the beans | 30 s or more | drum roasters, another_jim | C4 |
| Probe spacing | 1–2 cm | two RTD probes, MaKoMo | C8 |
| Delta span / smoothing | 10 s (MaKoMo); 20 s smoothing for correlation (another_jim) | Artisan | C8 |
| Heat-cut trigger | BT 190 °C | Quest, another_jim | C12 |
| Power schedule | steady about 3:20, then −0.5 kPa per 30 s | perforated-drum Huky, 400 g, Marcelnl | C12 |
| Coast after cutting gas | 20–30 °F | gas drums, Milligan | C11 |
| Probe diameters in the faceplate example | 4 mm bolted vs 2.5 mm insulated | baldheadracing's gas drum | C9 |
| ROEST batches | 193.5 °C at 6:03 vs 195.8 °C at 6:01 | hot-air roaster, luca | C13 |
| Specific-heat model | two values, step at first-crack start | another_jim's model | C10 |
| Development share quoted from Rao | 20–25 % (does not apply to Nordic or dark roasts) | Milligan, post #20 | context |

## Relevance to Skywalker (IR, 350 g)
*Gatherer judgement:* Gives the owner a well-argued counterweight to "keep RoR declining" for gap #6, with a physical reason (a smooth ET drives a smooth RoR) and a practical one (a 30 s lag means in-roast corrections arrive late). The probe-mounting point (C9) and the two-probe test (C8) bear on how Artisan RoR curves from the Skywalker should be read. IR heating adds a radiant term that none of the posters discuss, so no IR conclusions follow. All opinions; no cup data.

## Gatherer notes
- The thread is about a CoffeeMind webinar the Gatherer did not view; Münchow's claims are second-hand through the thread.
- Pairs with S0044 (the 2015 Perger thread); the two disagree about whether a declining RoR is needed.
