# Caso de Estudio #1 — Sistema de Gestión UCI (Essalud)

**Arquitectura de Software · UTEC · 2026-II · 20 ptos**

## Repositorio

**https://github.com/LuisMUtec/SWA-LAB01-UCI-Essalud**

## Equipo

| Nombre | GitHub |
|---|---|
| Luis Maquera | [@LuisMUtec](https://github.com/LuisMUtec) |
| Johar Barzola | [@Joharjbe](https://github.com/Joharjbe) |
| Fernando Aguilar | [@LordFernan](https://github.com/LordFernan) |

## Entregables

| Pedido en el enunciado | Dónde está |
|---|---|
| Usuarios / Clientes | [`README.md`](README.md) §2 — clientes, usuarios directos, indirectos y reguladores |
| Definición del Problema | [`README.md`](README.md) §1 — problemáticas críticas P1–P3, escalamiento y metas |
| Personas / Usuarios modelo | [`/Personas`](Personas) — `Rodrigo.MD`, `Milagros.MD`, `Carmen.MD`, `Anibal.MD` |
| Requerimientos Funcionales | [`Requirements/ReqFunc.MD`](Requirements/ReqFunc.MD) — **194 RF** en patrón EARS |
| Requerimientos No Funcionales | [`Requirements/ReqNoFunc.MD`](Requirements/ReqNoFunc.MD) |
| Agente por persona | [`/Agents`](Agents) — un `agent-*.MD` por persona, más el estándar común |
| Prompt de evaluación | [`README.md`](README.md) §3 — repartido entre `Agents/` y `Spec/Eval-Spec.MD` |
| Agente `Eval-Spec.MD` | [`Spec/Eval-Spec.MD`](Spec/Eval-Spec.MD) — rúbrica D1–D6, pesos y veredicto |
| Rúbrica de evaluación | [`Spec/Eval-Spec.MD`](Spec/Eval-Spec.MD) §Rúbrica |
| Reporte e iteraciones | [`Spec/HISTORIAL.MD`](Spec/HISTORIAL.MD) — **11 corridas** · [`Spec/Eval-Report.MD`](Spec/Eval-Report.MD) — última |

Evidencia por corrida en [`Spec/corridas/<id>/`](Spec/corridas): cuatro veredictos de persona,
`diagnostico.MD`, `controles.txt` y `corrida.json`.

## Resultado

Once corridas sobre estados sucesivos de `ReqFunc.MD`:

```
it1 58,7 → it2 71,4 → it3 59,0 → it4 64,7 → it5 68,9 → it6 71,5
→ it7 77,8 → it8 79,9 → it9 80,9 ← mejor → it10 77,4 → it11 72,7
```

**La iteración más exitosa fue la 9: 80,9 % global y 22 brechas abiertas**, el mínimo de la serie.
Cierra la progresión monótona it6 → it9. Las dos siguientes retroceden porque las correcciones que
buscaban levantar D1 abrieron brechas en D2 y D5 más rápido de lo que cerraban las de D1.

## Sobre el veredicto PASSED

El enunciado no fija umbral: pide que `Eval-Spec` **«devuelva un % indicando la calidad de los
requerimientos»**. Bajo ese criterio literal, **it9 entrega 80,9 %**.

El `FAILED` que reportan las once corridas es el veredicto de **nuestra propia rúbrica**, que fijamos
deliberadamente más estricta que la pedida: exige cinco condiciones a la vez.

| # | Condición | Umbral | it9 | |
|---|---|---:|---:|:---:|
| 1 | Puntaje global | ≥ 80,0 % | 80,9 % | ✅ |
| 2 | D1 · satisfacción de personas | ≥ 80,0 | 63,0 | ❌ |
| 3 | Persona más baja | ≥ 7,0/10 | 4,8 | ❌ |
| 4 | D2 · problemas críticos | ≥ 80,0 | 83,3 | ✅ |
| 5 | Controles de `verificar.sh` | 9/9 | 9/9 | ✅ |

it9 cumple tres de cinco. **El cuello de botella de toda la serie es D1** —si los requerimientos
satisfacen a las personas—, nunca la forma: D3 y D4 se sostienen sobre 90 desde it5. Es el hallazgo
que nos parece más honesto reportar: un documento impecablemente escrito puede dejar a su persona
ancla en 4,8/10.

> **Nota sobre el enunciado.** El ejemplo de la sección *Additional* rotula `PROMEDIO 3/10 - PASSED`
> en la iteración #2, pero sus puntajes (7/10 y 8/10) promedian 7,5/10. El `3/10` parece heredado de
> la iteración #1. Asumimos que el umbral implícito de PASSED es ≈ 7/10 de promedio por persona.

## Verificación

```bash
bash scripts/verificar.sh --sin-agentes    # 9/9 controles, exit 0
```

Nueve controles mecánicos sobre forma de los RF, identificadores duplicados, matrices que citan IDs
inexistentes y aritmética del puntaje. Sin los nueve en verde no se declara `PASSED`, por alto que
sea el porcentaje.
