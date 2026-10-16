---
title: Airflow
---

# Airflow

!!! abstract "In short"
    - On the Skywalker, air doesn't deliver heat to the beans — it removes it. `conf: medium`
    - Airflow changes alter roast dynamics a lot; even a kitchen hood above the roaster is noticeable.

## Concepts
- In a radiant roaster the air is cooler than the beans and takes heat from them [S0003](../sources/S0003-skywiki-renatoa-words-of-wisdom.md); it is
  not the main heat carrier [S0001](../sources/S0001-skywiki-infrared-roaster.md). `conf: medium`

## In practice
- Avoid changing airflow casually: any change "will change dramatically the roast dynamics";
  one owner could detect the speed setting of a hood ~0.5 m above the machine. `conf: low` [S0003](../sources/S0003-skywiki-renatoa-words-of-wisdom.md)
- The built-in program P11 raises fan to 90 % while dropping heater to 40 % at ~170 °C
  (observed in an empty-machine test). [S0001](../sources/S0001-skywiki-infrared-roaster.md)

## On the Skywalker (IR)
- Keep fan %, hood and windows the same across roasts you compare; note them in Artisan.
- **Inference — test it:** because the fan cools rather than heats, raising the fan should act as
  a fast brake on RoR compared with lamp power (which lags). Worth testing carefully.

## Open questions
- Fan's role in chaff/smoke removal vs heat; recommended fan curves from Skywalker owners.
