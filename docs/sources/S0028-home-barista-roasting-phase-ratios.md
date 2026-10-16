---
id: S0028
title: "Roasting phase ratios (Home-Barista)"
url: "https://www.home-barista.com/roasting/roasting-phase-ratios-t102598.html"
type: forum
author: "Mathwiz (OP), EddyQ, LBIespresso, mkane, BeWe, CarefreeBuzzBuzz"
author_credentials: "Home-Barista roasting-forum regulars; EddyQ mentions a North 1K and a Quest M3s; LBIespresso a Cormorant; Mathwiz's machine not stated in this thread. Experience levels not stated."
published: 2026-01-19
accessed: 2026-10-16
language: en
grade: C
heat: gas-drum
machine: "EddyQ: North 1K (gas) and Quest M3s (electric); LBIespresso: Cormorant (gas); BeWe: direct-heat drum similar to BC-2; Mathwiz: drum with manual damper (Pa gauge)"
topics: [roast-phases, airflow, rate-of-rise, myths-and-contested]
novelty: mixed
corroborates: [S0011]
kb_status: new
---

# S0028 — Roasting phase ratios (Home-Barista)

**Author:** Mathwiz and others · **Type:** forum thread (15 posts, 2 pages, 2026-01-19 to 2026-01-22) · **Grade:** C · **Heat context:** gas-drum (plus one electric air-type roaster) · [Original](https://www.home-barista.com/roasting/roasting-phase-ratios-t102598.html)

## Summary
Mathwiz notes he finally hit a 45-35-20 phase split. Replies question phase percentages, share simple RoR rules (30/20/10 °F per minute at checkpoints), and drift into airflow strategy. EddyQ argues ratios hide what changed and that lower airflow raises the inlet air temperature on some roasters (relaying Rob Hoos), a point he has not tested for flavour. Others describe how they avoid the crash and flick around first crack. No profiles or cup results are shown.

## Key claims
1. **C1** — Phase percentages can hide the real change: two roasts with equal dry and development times but different middle phases give very different-looking ratios.
   > "I have two roasts with matching dry times, matching development times but significantly different middle phase lengths. The ratios computed were 48%/33%/19% and 40%/43%/16%." — *post #7, EddyQ*
   > "Looking at these ratios it is impossible to see that I only lengthened the middle phase." — *post #7, EddyQ*
2. **C2** — EddyQ tracks the turning point (reveals whether the charge temperature suits the batch) and the inlet air temperature (too hot risks tipping or scorching).
   > "I also watch my turning point temperatures since at that point it usually tells me if my charge temperature is at the right temp for the amount of beans being charged." — *post #7, EddyQ*
   > "I watch closely the input air temperature since if too hot I likely will get tipping or scorching with some beans." — *post #7, EddyQ*
3. **C3** — Second-hand report of Hoos's airflow finding: lower airflow raises inlet air temperature and dries faster; EddyQ's North 1K behaves that way, his Quest M3s does not, and no one reports a flavour test.
   > "I think on Rob's roaster, lower airflow results in higher input air temperature which results in faster drying (hence difference in the cup)." — *post #10, EddyQ*
   > "my Quest M3s, input air doesn't change much with different airflows" — *post #10, EddyQ*
   > "How this effects the flavors? I have no idea." — *post #15, EddyQ*
4. **C4** — LBIespresso finds "lower airflow gives faster drying" counter-intuitive unless the relationship is non-linear.
   > "Lower airflow making dry time faster is counter-intuitive. Unless it is not a linear relationship." — *post #12, LBIespresso*
5. **C5** — Airflow practice: Mathwiz holds a nearly static airflow (about 7 Pa), low in drying, raised very slowly after dry end to 7–8 Pa; BeWe says raising airflow in development is hard to control on a direct-heat drum because of its high conduction share.
   > "I find that I achieve the best control over my roasts when I maintain a static airflow, typically around 7 Pa." — *post #9, Mathwiz*
   > "increasing airflow during the development phase makes it very difficult to control the ROR. This is due to the very high conduction ratio." — *post #13, BeWe*
6. **C6** — Avoiding the flick and crash around first crack: have the right energy just before FC; LBIespresso cuts gas hard 30–40 s before FC; Mathwiz wants ending RoR no lower than about 8 °F/min.
   > "If my energy is where it should be just before FC, it seems to minimize the flick-and-crash issue." — *post #6, Mathwiz*
   > "I have (mostly) solved the pre-FC hump/Crash/Flick with a very aggressive gas cut about 30-40 seconds before FC." — *post #8, LBIespresso*
7. **C7** — Rules of thumb used: 45-35-20 phase split; 30-20-10 (°F/min) RoR checkpoints, which "leaves some energy for the end of the roast".
   > "I am always aiming for that 30/20/10 ROR since it leaves some energy for the end of the roast if needed." — *post #5, LBIespresso*

## Numbers & parameters
| Parameter | Value | Context (machine, batch size, unit) | Claim |
|---|---|---|---|
| Phase split reached | 45-35-20 % | Mathwiz, one roast | C7 |
| Phase splits compared | 48/33/19 % vs 40/43/16 % | EddyQ, equal dry and development times | C1 |
| Airflow | ~7 Pa static; 7–8 Pa after dry end | Mathwiz, drum with manual damper | C5 |
| Ending RoR | ≥ ~8 °F/min | Mathwiz, target | C6 |
| Gas cut before FC | ~30–40 s before FC | LBIespresso, Cormorant | C6 |

## Relevance to Skywalker (IR, 350 g)
*Gatherer judgement:* Modest. C1 supports the existing KB view (S0011/S0012) that phase percentages hide what happened and the owner should compare times as well as ratios. The airflow remarks apply to gas drum roasters where air carries heat; on the Skywalker, owners say air mainly cools (S0015, S0016), so the inlet-temperature mechanism may not apply. C6's pre-FC power reduction resembles the stepwise power cuts Skywalker owners describe (S0015–S0017), though those owners use an IR lamp rather than gas.

## Gatherer notes
- EddyQ's Hoos reference matches S0025 (airflow tastes different, weight-loss curve changes); nobody in this thread has tested the flavour effect.
- Units: RoR numbers here are °F/min as stated in the thread.
