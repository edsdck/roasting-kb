---
id: S0071
title: "New to Artisan, RoR curve help please (Home-Barista thread t92299, Feb 2024)"
url: "https://www.home-barista.com/roasting/new-to-artisan-ror-curve-help-please-t92299.html"
type: forum
author: "H175Driver (OP), rmongiovi, Ben N, TheCopyCat"
author_credentials: "Home-Barista members describing their own use of Artisan; OP had just bought a Kaleido M2 (five roasts in). 6 posts, 13-21 February 2024. No formal credentials stated."
published: 2024-02-13
accessed: 2026-10-19
language: en
grade: C
heat: IR
machine: "OP: Kaleido M2 (a hybrid heater, see S0070 notes), 5th roast, cheap Rwandan beans, batch size not stated."
topics: [measurement-and-artisan, rate-of-rise]
novelty: corroborating
corroborates: [S0068]
kb_status: integrated
---

# S0071 — Home-Barista: spiky RoR on a Kaleido M2 in Artisan

**Author:** H175Driver and others · **Type:** forum thread (6 posts, all read) · **Grade:** C · **Heat context:** IR/hybrid (Kaleido M2) · [Original](https://www.home-barista.com/roasting/new-to-artisan-ror-curve-help-please-t92299.html)

## Summary
A new Kaleido M2 owner finds his Artisan RoR curve "far too spiky". Two replies say it looks normal because the RoR is a derivative that magnifies noise, and that smoothing delays the values. A third gives a specific Artisan setting that removed the noise on his curve. A short, low-evidence thread, but one of few that ties Artisan filter settings to an IR-type roaster.

## Key claims
1. **C1** — A spiky RoR is normal: it is the derivative of a noisy temperature curve.
   > "Since it's the derivative of the temperature curve the RoR curve magnifies the variability in the data."
   — *post #2, rmongiovi*
2. **C2** — Smoothing makes the RoR values late; the advice is as little smoothing as possible.
   > "Artisan can smooth the data, but that means the RoR values reported will be delayed from reality by the smoothing algorithm."
   > "In general, I believe the recommendation is the less smoothing the better."
   — *post #2, rmongiovi*
3. **C3** — Judge the general shape and look through the jaggedness.
   > "Watch the general shape, imagine out the jaggedy."
   — *post #3, Ben N*
4. **C4** — One user's setting that removed the noise: a 20 s / 40 filter on the Delta BT with polyfit and optimal smoothing.
   > "found a setting of 20s/40 with polyfit and optimal smoothing on made a curve that removed the measurement noise"
   — *post #5, TheCopyCat*

## Numbers & parameters
| Parameter | Value | Context (machine, batch size, unit) | Claim |
|---|---|---|---|
| Delta BT filter | 20 s / 40 with polyfit and optimal smoothing | Kaleido M2 in Artisan; "time and value" of the Delta BT rate-of-rise filter | C4 |
| Recommended smoothing | as little as possible | rmongiovi | C2 |

## Relevance to Skywalker (IR, 350 g)
*Gatherer judgement:* Shows what an IR-type roaster's Artisan curve looks like to its owners (spiky, and accepted as normal) and one setting someone used. A 20 s filter implies about 10 s of lag by S0068's reasoning (lag is half the span), and "optimal smoothing" in Artisan is an offline algorithm per S0068, so the setting cannot be used live without delay; whether TheCopyCat applied it after the roast is not said. Untested on a Skywalker (gap 15).

## Gatherer notes
- The OP's screenshots were not recorded; no roast data are given.
- TheCopyCat's post is a single anecdote and the thread ends with the OP saying he will try it; no result is reported.
- The half-span lag and the offline-only nature of optimal smoothing come from S0068 (MaKoMo's statement about Artisan), not from this thread.
