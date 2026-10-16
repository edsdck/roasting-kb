---
id: S0001
title: "Infrared Roaster — Skywalker roaster key characteristics and behavior"
url: "https://skywiki.coffee/books/general-information/page/infrared-roaster"
type: article
author: "Skywiki community (unnamed contributor)"
author_credentials: "Skywalker owner community wiki; includes an empty-machine test on a Skywalker"
published: unknown
accessed: 2026-10-16
language: en
grade: B
heat: IR
machine: "Skywalker (version not stated), built-in program P11"
topics: [heat-transfer, measurement-and-artisan, roast-planning, airflow]
novelty: novel
corroborates: []
kb_status: integrated
---

# S0001 — Infrared Roaster (Skywiki)

**Author:** Skywiki community · **Type:** wiki article · **Grade:** B · **Heat context:** IR · [Original](https://skywiki.coffee/books/general-information/page/infrared-roaster)

## Summary
A community wiki page describing how the Skywalker behaves thermally. Its two main points: the
machine has high thermal inertia that comes from the IR lamp (not from drum mass), and heat
transfer is primarily radiative, not convective. It argues against aggressive PID/real-time
control and for a few planned power changes. It reports an empty-machine test in which the
roaster could not exceed ~179 °C, versus ~194 °C reached with beans on the same program, and
explains first crack being read around ~182 °C by probe placement and the radiant environment.

## Key claims
1. **C1** — The Skywalker has high thermal inertia, but it comes mainly from the IR lamp, which keeps radiating after power is reduced; power changes take effect with a delay.
   > "In this machine, inertia comes primarily from the infrared heating element (lamp)." — *§1 High Thermal Inertia*
2. **C2** — Because of this lag, RoR reacts slowly and large power adjustments cause overshoot or collapse.
   > "Large adjustments cause overshoot or collapse." — *§1*
3. **C3** — Heat transfer is primarily radiative: the air is not the main heat carrier and the drum is not the main heat reservoir.
   > "Heat transfer here is primarily radiative, not convective." — *§2*
4. **C4** — Aggressive PID control is counterproductive on this machine; use data to understand the machine and plan profiles instead.
   > "Trying to aggressively PID this machine is largely counterproductive" — *Data and PID Control*
5. **C5** — Use few, deliberate power changes (3–5 per roast) of modest size (5–10 %); timing of changes matters more than micro-adjustment.
   > "3–5 adjustments per roast are usually sufficient." — *Data and PID Control*
6. **C6** — Empty machine (P11, preheat 200 °C) plateaued at ~178 °C and could not exceed 179 °C; with beans the same program's cutoff reaches ~194 °C. Interpreted as: beans are the main energy absorbers / thermal mass.
   > "It means the beans are the primary energy absorbers and thermal mass in the system." — *Surprising Observation*
7. **C7** — First crack reads relatively low (~182 °C) on this machine, attributed to probe placement, radiant-dominant heating and less superheated air — not necessarily miscalibration. Temperatures should not be compared directly with hot-air machines.
   > "Do not compare temperature numbers directly with hot-air machines" — *Practical Takeaways*
8. **C8** — A darker drum improves radiative absorption; a polished drum would reflect more and heat beans less efficiently.
   > "A darker drum improves radiative absorption." — *Design Implications*

## Numbers & parameters
| Parameter | Value | Context (machine, batch, unit) | Claim |
|---|---|---|---|
| Power changes per roast | 3–5 | Skywalker | C5 |
| Heat step size | 5–10 % | Skywalker | C5 |
| Empty test settings | preheat 200 °C, heater 65 %, fan 65 %; at 170–172 °C heater → 40 %, fan → 90 % | Skywalker, program P11, no beans | C6 |
| Empty-machine plateau | ~178 °C (177–179 °C), timed out after 15 min | Skywalker, no beans | C6 |
| P11 cutoff with beans | ~194 °C | Skywalker, batch not stated | C6 |
| First crack reading | ~182 °C | Skywalker, probe placement not stated | C7 |

## Relevance to Skywalker (IR, 350 g)
*Gatherer judgement:* Directly about his machine. The ~182 °C first-crack reading is a key
calibration point when comparing his Artisan numbers with generic advice (often 196–200 °C+).
Machine version (V1/V2) and batch size of the tests are not stated.

## Gatherer notes
Physics explanations are the contributor's reasoning, not measured. The empty-machine
interpretation is plausible but the probe may also read differently with no bean mass around it
(see S0003 C4).
