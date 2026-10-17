---
id: S0029
title: "Roast Assistant for Skywalker (Home Roasters forum thread)"
url: "https://homeroasters.org/forum/viewthread.php?thread_id=7105"
type: forum
author: "renatoa (administrator and thread author); replies from IWantJava, billsey, greencardigan"
author_credentials: "renatoa is shown as Administrator of Home Roasters (3,566 posts) and is the main poster in the Skywalker threads collected as S0015–S0017 (and the author of S0002/S0003 on Skywiki). In this thread he says he built an adapter based on Josh Moore's code and then his own LCD/ESP32 extension and app."
published: 2025-01-10
accessed: 2026-10-17
language: en
grade: C
heat: IR
machine: "Skywalker (version and batch size not stated); controlled from the original Skywalker panel, ESP32 + LCD or Android app reading the roaster's serial protocol"
topics: [rate-of-rise, roast-phases, development, measurement-and-artisan, heat-transfer]
novelty: mixed
corroborates: [S0016, S0017]
kb_status: new
---

# S0029 — Roast Assistant for Skywalker (Home Roasters forum thread)

**Author:** renatoa · **Type:** forum thread (20 posts, 2025-01-10 to 2026-01-22; read in full) · **Grade:** C · **Heat context:** IR (Skywalker) · [Original](https://homeroasters.org/forum/viewthread.php?thread_id=7105)

## Summary
renatoa describes a spy-only add-on for the Skywalker: an ESP32 reads the roaster's panel protocol, shows time, temperature, RoR, power and air on an LCD (later an Android app), auto-detects charge, turning point, dry end, first crack and drop, and shows predictors plus a trend arrow for the RoR. Control stays manual from the roaster's own panel. Along the way he gives concrete operating rules for a Skywalker roast: what the RoR trend should do in drying and in browning, the temperature he uses as a first-crack reference (182 °C, with about 7 degrees spread by origin), and later in the thread a dry-end target and an example power schedule. He also reports wide spread in dry-end times between owners and suggests checking real wattage. This is practitioner knowledge without logged data or cup results in the thread.

## Key claims
1. **C1** — The add-on does the RoR computation itself, shows trends and event predictors, auto-detects some roast phases, and leaves all heat/air control to the original panel.
   > "roasting calculator, doing a much better RoR computation, showing trends and event predictors. Also some roast phases auto detected." — *post #1, bullet list*
   > "I would like to emphasize that all control is done manually from the original Skywalker control panel." — *post #1*
2. **C2** — His adapter code fixes data acquisition problems of the basic translator (packet skipping, resolution).
   > "using interrupts, without any packet skipping, and also improved resolution using oversampling." — *post #1, first bullet*
3. **C3** — During drying the RoR trend marker should show only a rise or no change; a RoR dip that lasts more than 5 seconds means raise the power.
   > "during the drying phase we should only see an upward trend" — *post #1*
   > "Any appearance of the _ sign, which indicates a dip in RoR, which lasts more than 5 seconds, would require increasing the power." — *post #1*
4. **C4** — During browning the RoR trend should be permanently falling; a rise lasting more than 5 seconds is a cue to cut power, add air, or both.
   > "The RoR evolution trend this time will have to be permanently falling" — *post #1*
   > "Any attempt of RoR increase, signaled with ^, and lasting more than 5 seconds, should alert us to decrease power, or increase air, or both." — *post #1*
5. **C5** — The dry-end predictor only becomes reliable after minute 2 and is then within about 5–10 s of the real dry end.
   > "stabilizes at a reasonably accurate value only after minute 2." — *post #1*
   > "The DE prediction is quite realistic, in the 5-10 seconds ballpark around the display estimate." — *post #1*
6. **C6** — First crack is predicted from a fixed 182 °C reference; he sees FC there in about three of four roasts, and says FC can sit anywhere in a range of about 7 degrees depending on origin (dry end is more predictable because it is detected at a fixed temperature).
   > "The reference I am using in prediction computation is the temperature of 182 C degrees, where I have FC in 3/4 of the cases." — *post #1*
   > "FC can be anywhere in a range of about 7 degrees, depending on the beans origin." — *post #1*
7. **C7** — Dry-end target: from minute 2, move power in small steps so the dry-end estimate lands at 3:30–4:30 counted from the charge. (The 3:30–4:30 range is a Facebook comment of renatoa quoted by another user; renatoa confirms it is "total from charge".)
   > "From minute 2, when you have a stable dry end estimator, adjust power level in small steps, to bring the dry end estimator in the 3:30-4:30 range." — *post #17, IWantJava quoting renatoa's Facebook comment*
   > "Total from charge." — *post #18, renatoa*
8. **C8** — Example schedule: power 65 % then 70 % then 75 % to bring the dry end near minute 4, then back to 70 % with more air once the beans are judged on track.
   > "Started with power 65%, followed by 70 then 75% to bring the DE closer to minute 4." — *post #18, renatoa*
   > "Stepped back to 70% plus pushed more air, when estimated the beans are on the right track." — *post #18, renatoa*
9. **C9** — Owners' dry-end times and power settings vary widely; one new user's dry end was almost 6 minutes, another case ended well past minute 5 at 90 % power. renatoa wonders whether lamp bulbs differ between units and advises a plug-through wattmeter to check that a power setting really draws the matching wattage.
   > "The DE time from my roast today was almost 6 minutes." — *post #19, IWantJava*
   > "drying ended significantly past minute 5, using 90% power !" — *post #20, renatoa*
   > "Wondering if the manufacturers are using same bulb for all the batches." — *post #20, renatoa*
   > "Also recommended to use a plug-through wattmeter, to check that 80% really means 800 Watts drawn, and adjust accordingly." — *post #20, renatoa*
10. **C10** — After first crack the display shows development time as seconds and as a percentage, and the drop decision is made from that plus the RoR.
    > "showing us development time, both as a time value and as a ratio, i.e. percentage" — *post #1*
    > "based on this information, as well as the evolution of RoR, we will make the decision to drop." — *post #1*

## Numbers & parameters
| Parameter | Value | Context (machine, batch, unit) | Claim |
|---|---|---|---|
| First-crack reference temperature | 182 °C (FC there in ~3 of 4 roasts) | Skywalker; renatoa's own prediction constant; version/batch not stated | C6 |
| First-crack spread by origin | about 7 degrees (unit not stated; Celsius assumed from context) | Skywalker | C6 |
| Dry-end estimator reliable after | minute 2 | Skywalker add-on display | C5 |
| Dry-end prediction error | 5–10 s | Skywalker add-on display | C5 |
| Dry-end target | 3:30–4:30 from charge | Skywalker, via renatoa's Facebook comment | C7 |
| Example power steps | 65 % → 70 % → 75 %, then 70 % + more air | Skywalker, dry end near 4:00 | C8 |
| RoR trend rule threshold | marker held longer than 5 s | drying: dip → more power; browning: rise → less power / more air | C3, C4 |
| Dry end seen by a new owner | almost 6 min | Skywalker, user IWantJava | C9 |
| Slow case reported by renatoa | drying ended past minute 5 at 90 % power | Skywalker, someone else's roast | C9 |

## Relevance to Skywalker (IR, 350 g)
*Gatherer judgement:* Directly about the Skywalker and from its most experienced forum analyst, so high relevance for the "what should the RoR do and when does dry end happen" questions. Missing: batch size, which version, any cup notes. The 3:30–4:30 dry-end window is second-hand (quoted from Facebook) and no development targets are given beyond "watch time and percent". Note the wattage point: the same power % may not draw the same watts on different units.

## Gatherer notes
- The first-crack figure can be compared with the Skywalker first-crack readings already collected in S0015–S0017 (same forum author); this thread gives his working constant for the predictor.
- The thread links to a GitHub project and an Android app (release posted 2025-05-08); links are truncated on the page and were not followed.
- The Facebook comment (post #17) and the case with 90 % power (post #20) were not seen directly.
- Full thread read via browser page text; first post edited by the author on 2025-01-10 12:00.
