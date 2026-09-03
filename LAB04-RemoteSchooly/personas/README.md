# Personas / usuarios modelo

Base para una nueva: [`_TEMPLATE.MD`](_TEMPLATE.MD).

El enunciado del [Caso #4](../docs/LAB-04-ARQ-2026.2.md) no nombra a nadie, así que las cuatro van
`status: proto` y **toda afirmación inventada se marca con `[ASSUMPTION: ...]`**.

| Persona | Archivo | Rol | Qué ancla |
|---|---|---|---|
| **Nayra** | [`Nayra.MD`](Nayra.MD) | Alumna del pueblo remoto. **Usuario modelo** | Que el material de la semana esté, completo y sin conexión activa. Es quien sufre el enlace |
| **Rómulo** | [`Romulo.MD`](Romulo.MD) | Docente que dicta en el pueblo | Que la clase ocurra. Es el único que está a los dos lados: recibe de Lima y le da la cara al aula |
| **Marisol** | [`Marisol.MD`](Marisol.MD) | Autora de materiales en la central de Lima | La producción con IA — y el gasto que el enunciado manda bajar |
| **Aurelio** | [`Aurelio.MD`](Aurelio.MD) | Coordinador del programa; responde ante el gobierno | El presupuesto y la cobertura. Es quien paga la factura que Marisol genera |

**Nayra es el usuario modelo.** El enunciado empieza por ella —*"se necesita que los alumnos tengan
acceso a los materiales para la semana"*— y las otras tres existen en función de que eso ocurra:
Marisol produce lo que ella recibe, Rómulo lo dicta, Aurelio responde por que llegue.

## A quién nombra el enunciado, y cómo se resolvió

El texto menciona tres posiciones sin darles nombre, más una cuarta que aparece dos veces sin figura.
Quién es persona y quién es restricción fue una decisión del caso, no un dato:

| En el enunciado | Cómo entró | Decisión |
|---|---|---|
| *"los alumnos"* | **Nayra** | — |
| *"los profesores puedan enseñar sin problema"* | **Rómulo** | [`D-04`](../docs/DECISIONES.md) — no es el mismo que genera el material |
| *"los profesores que generan los materiales… usan demasiado la IA"* | **Marisol** | [`D-04`](../docs/DECISIONES.md) — produce en la central, no en el pueblo |
| *"el gobierno de Perú"* / *"una central de Lima"* | **Aurelio** | [`D-03`](../docs/DECISIONES.md) — entra como persona con agente, no como restricción |

La razón de [`D-03`](../docs/DECISIONES.md) en una línea: **quien causa el gasto no es quien lo
sufre**. Sin Aurelio, el −40 % es un número sin nadie que pueda reclamarlo.

## Tensiones entre personas

Cada fila es un choque que el backlog tiene que **decidir**, no esquivar. Las cobra D4.

| # | Tensión | Entre quiénes | Decidida en | Qué se pierde |
|---|---|---|---|---|
| `T1` | Riqueza del material ↔ peso del paquete | Marisol ↔ Nayra | _(se llena al proyectar el backlog)_ | |
| `T2` | Libertad de regenerar con IA ↔ techo de gasto | Marisol ↔ Aurelio | _(idem)_ | |
| `T3` | Corregir el material tarde ↔ la semana ya congelada y en camino | Marisol ↔ Rómulo | _(idem)_ | |
| `T4` | Cobertura de la región más lejana ↔ presupuesto finito | Aurelio ↔ Nayra | _(idem)_ | |

**Regla de asimetría:** un agente de persona solo puede **restar** de D1, nunca sumar. Su función es
detectar la falla, no certificar el acierto. Ver [`../evals/README.md`](../evals/README.md).

## Cobertura de las dos exigencias del enunciado

| Exigencia | Quién la ancla | Ángulo |
|---|---|---|
| Que los cursos **lleguen correctamente** | **Rómulo**, con **Nayra** de contraparte | Él es quien lo verifica antes de la clase y quien distingue «no llegó» de «llegó incompleto» de «llegó lo viejo». Ella es quien paga el costo de que falle |
| Reducir el gasto de tokens **≥ 40 %** | **Aurelio**, con **Marisol** de contraparte | Él responde por la cifra y la tiene que poder mostrar contra una línea base; ella es donde el gasto se produce y donde el comportamiento tiene que cambiar |

Ninguna de las dos exigencias descansa en una sola persona: cada una tiene quien la reclame y quien
la ejerza. Es lo que impide que el backlog la enuncie sin que nadie la pueda verificar.
