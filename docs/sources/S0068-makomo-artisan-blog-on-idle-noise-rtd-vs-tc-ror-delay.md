---
id: S0068
title: "On Idle Noise (MaKoMo, Artisan blog, March 2019)"
url: "https://artisan-roasterscope.blogspot.com/2019/03/on-idle-noise.html"
type: article
author: "MaKoMo (signs the post as 'Marko')"
author_credentials: "Writes on the Artisan blog and as MaKoMo on Home-Barista (LMWDP #360, artisan-scope.org). The post says he has worked on Artisan for years and that he implemented an Artisan feature (async mode for Yoctopuce modules, v1.6.1); surname not on the page."
published: 2019
accessed: 2026-10-19
language: en
grade: B
heat: n/a
machine: "Bench tests on a table (probe and meter at room temperature, 0.5 s sampling, laptop on battery); field recordings from colleagues' machines (SF-1 with 4.7 mm RTD, Probatone II 5k, Neuhaus Neotec RFB Signum, Mill City 500 g North) and the author's own roaster. No coffee roasted for the main results."
topics: [measurement-and-artisan, rate-of-rise]
novelty: novel
corroborates: []
kb_status: new
---

# S0068 — MaKoMo: "On Idle Noise" (Artisan RoR noise and delay)

**Author:** MaKoMo (works on Artisan) · **Type:** blog article with measurements · **Grade:** B · **Heat context:** n/a (measurement system) · [Original](https://artisan-roasterscope.blogspot.com/2019/03/on-idle-noise.html)

## Summary
The author measured how much noise different probe-and-meter combinations put into the rate-of-rise (RoR) when nothing is happening ("idle noise"), by recording two minutes at 0.5 s sampling and taking the standard deviation of the RoR. He argues that smoothing, a longer delta-span and a longer sampling interval are the same trade (cleaner curve, more delay), and that it is better to cut noise at the source with a quiet meter, an RTD probe, high-resolution signals and no ground loops. His own change (3 mm PT100 RTD on a Phidget TMP1200) dropped idle-noise StdDev from 2.64 to 0.09, allowing a 1 s delta-span with no software smoothing. He also criticises the hot-water speed test in Hoos's thermocouple article (S0067).

## Key claims
1. **C1** — The RoR is a derivative of the temperature signal, so it magnifies noise.
   > "This computation unavoidably amplifies any noise of the temperature signal dramatically as differentiation degrades the signal-to-noise ratio."
   — *The Problem*
2. **C2** — A longer RoR interval (delta-span), averaging smoothing and a longer sampling interval all have the same effect: smoother, but later.
   > "Larger RoR intervals, the application of average smoothing and increased sampling intervals all have the exact same effects: smoother signals and large time lags!"
   — *Fine? No!*
3. **C3** — The lag from computing the RoR is half the delta-span; smoothing during recording adds more.
   > "the time lag produced by computing the RoR is half of the delta-span interval"
   — *RoR lags in time - always!*
4. **C4** — Rao's suggested maximum rolling interval is 15 s; the author runs a 1 s delta-span and no smoothing.
   > "Scott suggests to set the rolling-average intervals to no more than 15 seconds. I rather go without any smoothing and use a 1sec delta-span adding only a minimal delay of max 0.5sec at a sampling interval of 1sec."
   — *Online smoothing delays signals*
5. **C5** — Measured idle noise: most field machines were not bad, but one machine with its motors on was almost useless; delta-spans of 10-20 s removed the noise on the quiet machines, while even 30 s (Artisan's maximum) left the noisy one at StdDev 1.38.
   > "Only the Mill City with motors on is problematic."
   > "The motors induce a considerable noise into the signal, rendering it mostly useless."
   > "A delta-span of 10sec reduces the StdDev of the SF-1 to 0.16 and a delta-span of 20sec reduces it to 0.09."
   — *In Situ*
6. **C6** — Drum-roast bean temperature rarely rises faster than 30 C/min (0.5 C/s) after dry end, so a measuring system need not be faster than that; faster systems only add noise and need more filtering.
   > "I found values from 15C/min up to 30C/min at DRY"
   > "all those systems are fast enough to record all details needed to catch any change in RoR after DRY"
   — *Reactivity; Meters*
7. **C7** — Both RTD meters had a much lower noise floor than all thermocouple meters tested.
   > "The two RTD meters, marked in green, produce a significant lower noise floor than all those TC meters."
   — *Results*
8. **C8** — Probe diameter: a 3 mm probe is the author's compromise; thinner probes break sooner and need more smoothing; the shield's thermal mass acts as a helpful analog filter; "RTDs are slower than thermocouples" is misleading.
   > "To me a 3mm PT100 probe gives the best compromise between speed, noise and durability."
   > "The common wisdom that RTDs have a slower response time than TCs is misleading."
   — *Probes; Meters*
9. **C9** — Resolution matters: low-resolution (zero or one decimal) readings create digital noise when the RoR is computed.
   > "Digital noise is caused by computing the RoR over low resolution signals and can be addressed by choosing meters generating high-resolution signals."
   — *An alternative Path*
10. **C10** — Idle-noise measurement is a starting point for choosing smoothing; real roasts may need more.
    > "Measuring idle noise can help to find a first good setup for the roasting software smoothing parameters."
    > "Note that your actual smoothing settings might need to be increased further due to further noise produced during roasting."
    — *Closing section*
11. **C11** — The author questions the method of the hot-water test in S0067.
    > "used either hot water to test the speed with potentially some uneven cooling effect of the remaining water on the probe after removal"
    — *Closing section*

12. **C12** — Artisan's optimal smoothing, which avoids the time shift, can only be applied while not recording.
    > "but (obviously) only while not recording (offline)"
    — *Online smoothing delays signals*

## Numbers & parameters
| Parameter | Value | Context (machine, batch size, unit) | Claim |
|---|---|---|---|
| Idle-noise StdDev of RoR (no smoothing, 0.5 s) | 1.36 / 1.95 / 2.91 / 2.13 | SF-1 4.7 mm RTD / Probatone II 5k std TC / Neuhaus Neotec RFB Signum with Phidget 1048 / Mill City 500 g North 5 mm TC, motors off | C5 |
| Same, Mill City motors on | 54.35 | 5 mm TC, Phidget 1048 | C5 |
| StdDev after delta-span 10 s / 20 s | 0.16 / 0.09 | SF-1 | C5 |
| StdDev after delta-span 30 s | 1.38 | Mill City, motors on | C5 |
| Author's old vs new setup, motors on | 2.64 vs 0.09 | 3 mm K-type TC + Phidget TMP1101 vs 3 mm PT100 RTD + Phidget TMP1200 | C5 |
| Fastest RoR a system can record | 6.75 / 7.90 / 2.60 / 1.00 C/s | Phidget 1048 + 2 mm TC / TMP1101 + 2 mm TC / TMP1101 + 3 mm TC / TMP1200 + 3 mm RTD (ice-water test) | C6 |
| Needed speed | 0.25-0.5 C/s | max BT RoR after dry end in his own and published profiles (15-30 C/min) | C6 |
| Delta-span lag | half the delta-span | Artisan, online | C3 |
| Rao's suggested maximum interval | 15 s | as quoted by the author | C4 |

## Relevance to Skywalker (IR, 350 g)
*Gatherer judgement:* This gives the owner a method (record two minutes of idle noise with the roaster on and the heater off, then pick the smallest delta-span that removes it) and a rule (the RoR is late by half the delta-span, so a 15 s span means the owner sees the roast 7.5 s ago). It says nothing about the Skywalker's own probe type; S0017 and S0046 describe the V1 stream as noisy, and the blog's main finding that motor and electrical interference can swamp a thermocouple (the 54.35 case) may or may not apply to a lamp heater and fan (untested). The numbers are for drum roasters, not 350 g on a lamp.

## Gatherer notes
- The page text was read to the end of the main body (including updates of 20 and 29 March 2019 and the Appendix heading); the Appendix proof and the tables/figures (images) were not extracted.
- The author's contrasting stance is stated as personal: "Don't believe everything". Rao's claims about RoR are relayed, not tested here.
- Home-Barista discussion thread: S0069.
