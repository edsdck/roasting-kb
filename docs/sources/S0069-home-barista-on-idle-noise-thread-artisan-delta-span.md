---
id: S0069
title: "On Idle Noise (Home-Barista thread t57637, pages 1 and 6, 2019)"
url: "https://www.home-barista.com/roasting/on-idle-noise-t57637.html"
type: forum
author: "MaKoMo (OP), JavaMD, danetrainer, Madman13, Almico, Bunkmil, tonescout and others"
author_credentials: "Home-Barista members describing their own Artisan setups; MaKoMo wrote the blog post S0068. 69 posts over 7 pages, March to July 2019; only posts #1-#10 (page 1) and #51-#60 (page 6) were read."
published: 2019-03-15
accessed: 2026-10-19
language: en
grade: C
heat: multiple
machine: "Santoker 500 (RTD probes), Mill City North 1 kg, and several home setups with Phidget meters; probes 3 mm RTD and 3 mm K-type TC."
topics: [measurement-and-artisan, rate-of-rise]
novelty: corroborating
corroborates: [S0068]
kb_status: new
---

# S0069 — Home-Barista: "On Idle Noise" thread (Artisan delta-span settings)

**Author:** MaKoMo and others · **Type:** forum thread (pages 1 and 6 of 7 read) · **Grade:** C · **Heat context:** multiple · [Original](https://www.home-barista.com/roasting/on-idle-noise-t57637.html)

## Summary
Discussion of MaKoMo's blog post (S0068). On page 1 users report their own delta-span needs (a Santoker with RTDs is clean at 10 s; a Mill City 1 kg needs 15 s and is still noisier), MaKoMo explains that cheap PIDs add delay before Artisan sees the signal, and replies discuss RTD hardware. On page 6 a user who moved to an RTD runs 1 s sampling, zero smoothing and a 1 s delta-span and compares it with his old 15 s setting. No cup results.

## Key claims
1. **C1** — A user with RTD probes on a Santoker gets a fair RoR at 1 s sampling and 10 s delta-span; a Mill City 1 kg needs 15 s and is far less clean (different machines).
   > "I get a fair reading with it on the ROR with 1 sec sampling and Delta span of 10 sec."
   — *post #5, JavaMD*
2. **C2** — A 10 s delta-span means at least a 5 s delay in the RoR, and cheap PIDs used as meters add their own delay before the data reach the software.
   > "Your 10sec delta-span produces at least a 5sec RoR delay @1sec."
   > "However, many of those PIDs do considerable processing generating on their temperature input and thus a corresponding large delay on the signal"
   — *post #7, MaKoMo*
3. **C3** — Test idle noise with some movement on the probe; a dead-calm probe can look quieter than it really is.
   > "When checking idle noise it's helpful to have a bit of temperature deviation on the probe."
   — *post #9, Almico*
4. **C4** — After switching the bean probe to an RTD, one user saw the RoR jump and settle back instead of oscillating, with 1 s sampling, zero smoothing and a 1 s delta-span.
   > "With the RTD, it jumped and then settled right back down."
   — *post #54, Almico*
5. **C5** — His earlier thermocouple setup worked at a 15 s delta-span, but with a visible delay.
   > "But the 15s delta span adds quite a bit of delay to the RoR curve."
   — *post #56, Almico*
6. **C6** — A user whose probe sat high in the drum saw extra noise from air turbulence; he moved the probe lower, idle noise is very low, but he still sees a lot of noise during real roasts and asks whether settings or probes are at fault.
   > "this gave too much air turbulence = variation I believe as it sat too high near the top of the bean mass"
   — *post #59, tonescout*

## Numbers & parameters
| Parameter | Value | Context (machine, batch size, unit) | Claim |
|---|---|---|---|
| Delta-span for a clean RoR | 10 s | Santoker 500, RTD probes, 1 s sampling | C1 |
| Delta-span needed | 15 s | Mill City North 1 kg (probe type not stated) | C1 |
| RoR delay of a 10 s span | at least 5 s | at 1 s sampling | C2 |
| Settings after RTD swap | 1 s sampling, 0 smoothing, 1 s delta-span (later 5 s on a different roast) | home roaster, 3 mm RTD for BT, 3 mm K-type for ET | C4 |
| Old settings | 1 s sampling, 0 curve smoothing, 2 delta smoothing, 15 s delta-span | home roaster, 3 mm K-type | C5 |

## Relevance to Skywalker (IR, 350 g)
*Gatherer judgement:* Gives real-user settings to compare with whatever the owner uses, and repeats the point that the span is a delay (here at least 5 s for 10 s). None of the machines is a lamp roaster. The Skywalker's noisy NTC signal (S0017, S0046) is not discussed.

## Gatherer notes
- Pages 2-5 and 7 were not read; Bunkmil's question about the best combination (post #55) is not answered on page 6.
- Images (RoR charts) not recorded.
