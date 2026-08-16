# Caso de Estudio #1 — Sistema de Gestión UCI (Essalud)

**Arquitectura de Software · UTEC · 2026-II**

**Repositorio: https://github.com/LuisMUtec/SWA-LAB01-UCI-Essalud**

Luis Maquera ([@LuisMUtec](https://github.com/LuisMUtec)) · Johar Barzola
([@Joharjbe](https://github.com/Joharjbe)) · Fernando Aguilar ([@LordFernan](https://github.com/LordFernan))

---

Todo lo pedido está en el repo: `README.md` (problema y usuarios/clientes), `/Personas` (4),
`/Requirements` (194 RF + RNF), `/Agents` (un agente por persona), `/Spec` (`Eval-Spec.MD` con la
rúbrica, `Eval-Report.MD` y `HISTORIAL.MD` con las 11 corridas).

## Resultado

```
it1 58,7 → it2 71,4 → it3 59,0 → it4 64,7 → it5 68,9 → it6 71,5
→ it7 77,8 → it8 79,9 → it9 80,9 ← mejor → it10 77,4 → it11 72,7
```

**Mejor corrida: it9 — 80,9 %**, y el mínimo de brechas abiertas (22). it10 e it11 retroceden porque
las correcciones para levantar D1 abrieron brechas en D2 y D5 más rápido de lo que cerraban las de D1.

## Sobre el PASSED

El enunciado pide que `Eval-Spec` devuelva un % y no fija umbral. Bajo ese criterio, **it9 = 80,9 %**.

El `FAILED` de las once corridas es el veredicto de **nuestra rúbrica**, deliberadamente más estricta:
exige cinco condiciones a la vez. it9 cumple tres —global 80,9 %, D2 83,3 y los 9/9 controles— y falla
las dos de personas: D1 63,0 (umbral 80) y persona más baja 4,8/10 (umbral 7,0).

**El cuello de botella es siempre D1, la satisfacción de las personas — nunca la forma:** D3 y D4 se
sostienen sobre 90 desde it5. Un documento impecablemente escrito puede dejar a su persona ancla en
4,8/10.

> El ejemplo del enunciado rotula `PROMEDIO 3/10 - PASSED` con puntajes 7/10 y 8/10, que promedian
> 7,5. Asumimos que el `3/10` es una errata y que el umbral implícito es ≈7/10.
