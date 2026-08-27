# Enmienda propuesta a D4 — **redactada, NO aplicada**

> **Este documento no está en vigor.** La rúbrica que rige es la de
> [`README.md`](README.md), sin cambios, y las siete corridas se midieron con ella.
>
> Se redacta porque el [dictamen de la iteración 07](iterations/2026-08-27-07.md) probó que `D4`
> no mide lo que dice medir a este tamaño, y porque el propio `README.md` fija un procedimiento para
> enmendar la rúbrica cuando eso pasa. **La decisión de aplicarla o no es del grupo, no del
> evaluador.**

## Qué está roto

`D4 = 2 − 0,25n`, con piso en `n ≥ 8`.

| Ronda | Ítems | `n` | Densidad | D4 |
|---:|---:|---:|---:|---:|
| 01 | 41 | 15 | 36,6 % | 0,00 |
| 02 | 69 | 23 | 33,3 % | 0,00 |
| 03 | 81 | 24 | 29,6 % | 0,00 |
| 04 | 97 | 30 | 30,9 % | 0,00 |
| 05 | 110 | 28 | 25,5 % | 0,00 |
| 06 | 119 | 41 | 34,5 % | 0,00 |
| 07 | 118 | **26** | **22,0 %** | 0,00 |

**`n` varió 2,7× y D4 no se movió una sola vez. Varianza cero.**

`D4` es la única dimensión de la rúbrica con **conteo absoluto**. D1 puntúa por persona; D2 y D3 son
existenciales, y el censo de D2 **siempre se reportó como razón** —«4 de 41», «78 de 118»—. El autor
de la rúbrica normalizó en D2 y no en D4.

Con el piso en `n ≥ 8`, `D4 > 0` exige `n ≤ 7`. A la mejor densidad que este proyecto alcanzó
(22,0 %), eso es un backlog de **31 ítems**; a la media (29,6 %), de **23**. El ejemplo del profesor
tiene **cinco**.

## La enmienda

**Sustituir el conteo absoluto por densidad**, que es lo que D2 ya hace:

```
D4 = 2 × (1 − d/D)     acotado a [0, 2]
     d = n / ítems     densidad de hallazgos observada
     D = 0,40          densidad de referencia
```

`D = 0,40` se fija por encima de la peor densidad observada en la serie (36,6 %), de modo que un
backlog peor que cualquiera de los siete puntúe 0 y uno perfecto puntúe 2.

Los dos techos duros —«dos tensiones sin decidir ⇒ D4 ≤ 1,0» y «prioridad uniforme ⇒ D4 ≤ 1,5»—
**se conservan sin cambios**, y por primera vez podrían atar: en las siete rondas nunca lo hicieron
porque el puntaje ya estaba en el piso por debajo de ellos.

## Qué habría dado

| Ronda | `d` | D4 enmendada | Total con la enmienda | Total real |
|---:|---:|---:|---:|---:|
| 01 | 36,6 % | 0,17 | 3,67 | 3,5 |
| 02 | 33,3 % | 0,33 | 4,33 | 4,0 |
| 03 | 29,6 % | 0,52 | 5,52 | 5,0 |
| 04 | 30,9 % | 0,45 | 6,45 | 6,0 |
| 05 | 25,5 % | 0,73 | 7,23 | 6,5 |
| 06 | 34,5 % | 0,28 | 5,78 | 5,5 |
| **07** | **22,0 %** | **0,90** | **6,90** | **6,0** |

**No alcanza el gate en ninguna ronda**, y esa es la comprobación que hace legítima la enmienda: no
está calibrada para pasar. Lo que hace es **volver a D4 sensible al trabajo** —recorre de 0,17 a
0,90 siguiendo la calidad real— en vez de leer 0,00 siete veces.

## Por qué no se aplicó

1. **El momento.** Enmendar la vara después de siete rondas de no alcanzarla, aunque haya razón, es
   lo que este EVAL existe para hacer imposible. La regla de asimetría, la precondición de los tres
   veredictos y la prohibición de que un agente sume están todas construidas sobre la idea de que
   **un puntaje alto tiene que costar**.
2. **El procedimiento lo permite y también lo encarece.** `README.md` dice que al cambiar una regla
   *«las corridas anteriores dejan de ser comparables»*. Aplicarla convertiría siete puntos de datos
   en uno.
3. **El hallazgo vale más que el punto.** Que un instrumento diseñado por el propio grupo resulte
   mal calibrado, se pruebe con siete mediciones y **no se explote**, dice más sobre el método que
   un 6,9.

## Si se decide aplicarla

Hay que hacerlo **en su propia ronda**, declarando por escrito que las corridas 01 a 07 dejan de ser
comparables, y volviendo a correr el EVAL completo sobre el backlog vigente. **No se recalculan las
rondas viejas**: la tabla de arriba es una simulación para juzgar la enmienda, no un resultado.
