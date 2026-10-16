---
id: S0009
title: "Putrid_Upstairs Response — Skywalker V1/V2 buying and setup advice"
url: "https://skywiki.coffee/books/general-information/page/putrid-upstairs-response"
type: forum
author: "Skywiki community member (Skywalker Community Discord; owns V1, Kaleido M2, Kaffelogic Nano 7)"
author_credentials: "Long-time Skywalker V1 owner/modder involved in community firmware; compares several roasters first-hand"
published: unknown
accessed: 2026-10-16
language: en
grade: C
heat: IR
machine: "Skywalker V1 and V2 (also compares Kaleido M2, Smola S5, Kaffelogic Nano 7)"
topics: [measurement-and-artisan, charge-and-batch, heat-transfer, equipment]
novelty: mixed
corroborates: [S0001]
kb_status: new
---

# S0009 — Putrid_Upstairs Response (Skywiki)

**Author:** Skywiki community member · **Type:** forum-style answer on wiki · **Grade:** C · **Heat context:** IR · [Original](https://skywiki.coffee/books/general-information/page/putrid-upstairs-response)

## Summary
A detailed answer to someone choosing a roaster, written by an experienced Skywalker V1 owner. It
explains how V1 logging works (no built-in logging; community firmware on an Arduino Nano or
ESP32-S3 translates the roaster's signals into the TC4 protocol for Artisan/HiBean), the batch
sizes users prefer, overheating weak points (back-to-back roasts, drum motor gears) and the
mods that help, the stock probe type (NTC) and probe upgrades, and how the Skywalker compares
with Kaleido, Smola and Kaffelogic.

## Key claims
1. **C1** — V1 has no built-in logging; community firmware on an Arduino Nano or ESP32-S3 converts the roaster's internal communication into the TC4 protocol so Artisan and HiBean can read and control it.
   > "V1 doesn't have it built-in but the community basically taking all the bit banging going on in the roaster and converting that info into TC4 protocol" — *Temperature logging support*
2. **C2** — V1/V2 can do 500 g, but users prefer 350–450 g.
   > "V1 and V2 can do 500g but users like the 350g to 450g range." — *Batch size*
3. **C3** — The community PID implementation still needs tuning; replaying a previous roast's heat and air changes (HiBean "power tracking", i.e. event replication) worked just as well for repeating a roast.
   > "Hibean power tracking, which is basically event replication, worked just as well recreating a past roast" — *Electric drum roaster*
4. **C4** — For back-to-back roasting the V1 heatsink mod is highly recommended (V2 has it built in); heavy use (40 kg+/month) on a V1 is not recommended.
   > "V1 with heatsink mod is highly recommended where the V2 already has this installed." — *back-to-back roasts*
5. **C5** — Known weak points: early V1 thermal runaway (later fixed with fuses/relays), and a drum motor with plastic internal gears that suffers in long back-to-back sessions; metal-gear and brushless replacements exist.
   > "Drum motor does have some issues especially with back to back roasts." — *Skywalker V1 and V2 (All Cons)*
6. **C6** — The stock V1 probe is an NTC thermistor; it can be swapped for a K-type thermocouple or PT100 RTD with the right amplifier and firmware.
   > "I was able to get probes like a K style TC and a PT100 RTD swap out the our NTC probe" — *Accessories or modifications*
7. **C7** — The Smola S5 has its heat lamp outside the drum, making it more convection-dominant like a Kaleido, unlike the radiant-dominant Skywalker.
   > "Heat lamp is out of the drum so it's more similar to a Kaliedo convection dominant roaster than a radiant dominant roaster like a Skywalker." — *Smola S5*
8. **C8** — The author gets results on the V1 similar to a much more expensive Kaleido M2.
   > "It just cost so much more and I get similar results to my V1." — *Kaliedo M2*
9. **C9** — The bean trier and being able to see and smell the roast are valuable for learning on Skywalker/Kaleido.
   > "Especially both have triers great ways to monitor progress of your roast by seeing and smelling." — *Kaffelogic Nano 7*

## Numbers & parameters
| Parameter | Value | Context (machine, batch, unit) | Claim |
|---|---|---|---|
| Max batch | 500 g | Skywalker V1/V2 | C2 |
| Preferred batch | 350–450 g | Skywalker V1/V2 users | C2 |
| Not recommended load | 40 kg+/month | Skywalker V1 | C4 |
| Price (as stated) | V1 ~$450, V2 ~$720 | — | — |

## Relevance to Skywalker (IR, 350 g)
*Gatherer judgement:* Very relevant: confirms the owner's 350 g is in the preferred range, that
his Artisan readings come from an **NTC probe** via community TC4 firmware, and that replaying
heater/fan events is a solid way to repeat a roast. Worth checking whether his V1 has the
heatsink mod before roasting back-to-back.

## Gatherer notes
Related Skywiki pages (not separately accepted): "Overheating Drum Motor" (stub; reports drum
motor temperatures of 122–127 °C, E3 errors, stripped plastic gears) and "Welcome" (V1 quirks:
SCR thermal runaway, weak bean cooling, ineffective filter fan). The owner describes his V1 as
400 g max; this source says V1/V2 can do 500 g — worth confirming.
