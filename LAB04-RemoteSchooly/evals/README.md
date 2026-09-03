# EVAL — backlog de requerimientos de RemoteSchooly

Aparato de evaluación del paso **R** de [R.E.D.A.L.E.](../redale/README.md). Se corre a mano.

El [enunciado](../docs/LAB-04-ARQ-2026.2.md) pide un *Requirements Eval* y su pipeline no deja pasar
al diagrama sin **`Score > 8`**. La rúbrica del caso paga **2 puntos por el gate** y 3 por los
requerimientos. Eso decide el alcance de este documento: **se puntúa el backlog, y nada más.**

## Entradas

| Entrada | Papel |
|---|---|
| [`redale/R-requerimientos/backlog.md`](../redale/R-requerimientos/backlog.md) | **Lo único puntuado.** El único documento con autoridad sobre qué debe hacer el sistema |
| `personas/*.MD` | Las lee cada agente de persona: la suya y el backlog, nada más |
| [`personas/README.md`](../personas/README.md) | La lee el agregador. De ahí salen las tensiones que D4 exige decididas |
| [`docs/LAB-04-ARQ-2026.2.md`](../docs/LAB-04-ARQ-2026.2.md) | La lee el agregador. Fija el problema contra el que mide D2 y nombra las dos exigencias que cuenta D3 |
| [`.specify/memory/constitution.md`](../.specify/memory/constitution.md) | La lee el agregador. El enunciado dice cuál es el problema; la constitución dice **qué se hace con un ítem que no lo ataca** |

### Los demás pasos de R.E.D.A.L.E. no se puntúan

`E`, `D`, `A`, `L` y `E` son entregable exigido, no puntaje — y en este caso son además donde está
el grueso de la nota, que se califica aparte, contra el diagrama.

Lo que impide que diverjan del backlog no es puntuarlos, sino **una regla de dirección: los
requerimientos bajan, nunca suben.** Ningún paso aguas abajo puede introducir un comportamiento que
el backlog no declare. Si `D` diseña un endpoint que responde algo que ningún título exige, o `A`
guarda un campo que ningún título obliga a conocer, el defecto **es del backlog** y se cobra en D4
como *decisión sin requerimiento*. La corrección va arriba, nunca abajo.

## Rúbrica — 10 puntos

| Dim | Pts | Qué mide | Juzga |
|---|---|---|---|
| **D1** Satisfacción de las personas | 3 | El flujo principal de cada persona corre de extremo a extremo en el backlog, **incluido cuando sale mal**. 1 pt por persona, **solo deducciones** | Los agentes de persona |
| **D2** Ajuste al problema | 3 | Ataca *este* problema —material educativo que llega a un pueblo con internet limitado, y un costo de tokens que hay que bajar 40 %— y no un aula virtual genérica | Agregador |
| **D3** Cobertura de las dos exigencias del enunciado | 2 | Que los cursos **lleguen correctamente** y que el gasto de tokens baje **≥ 40 %**, las dos con medida y no como adjetivo | Agregador |
| **D4** Coherencia del backlog | 2 | Sin huérfanos ni duplicados encubiertos; títulos atómicos y entendibles **sin descripción**; tensiones entre personas decididas; prioridad asignada | Agregador |

**Gate: ≥ 8/10.** Se pueden perder dos puntos, no más. Un puntaje por debajo del gate **no baja la
vara**: se corrige el backlog y se vuelve a evaluar.

> **D3 mide lo que el enunciado exige, no lo que excluye.** El caso dice que no hace falta asegurar
> 100 % de disponibilidad ni usar mecanismos de confiabilidad *todavía*. Un ítem sobre replicación
> activa-activa no suma en D3: gasta presupuesto de backlog en algo que el enunciado sacó del
> alcance. Lo que sí exige, y con la misma frase, es que **los cursos lleguen correctamente**.

## La regla de asimetría

**Un agente de persona solo puede restar de D1. Nunca sumar.** Si ninguno objeta, D1 vale 3.

No es cortesía metodológica, es consecuencia de qué puede observar cada quien. Un agente lee su
persona y el backlog: ve un ángulo del problema y no ve el conjunto. Si además pudiera sumar, una
lectura entusiasta compraría puntos que ninguna otra lectura está en condiciones de contestar, y D1
terminaría midiendo la generosidad del agente en lugar de la calidad del backlog.

## Quién juzga qué

| Pregunta | Quién responde | Por qué |
|---|---|---|
| ¿Este backlog le resuelve el día a esta persona? | Su agente | Solo quien opera desde esa posición reconoce si el comportamiento enunciado le sirve |
| ¿Ataca el problema del enunciado o uno genérico? | Agregador | Cada persona ve un rasgo del problema; ninguna ve el conjunto |
| ¿Las dos exigencias están enunciadas con medida? | Agregador | La forma del enunciado es ajena a la perspectiva de cualquier persona |
| ¿Hay huérfanos, duplicados encubiertos o títulos comodín? | Agregador | Requiere el conjunto entero a la vista |
| ¿Las tensiones están decididas? | Agregador | Cada agente ve su lado de la tensión y lo da por bueno; ninguno ve el conflicto |
| ¿Algún paso aguas abajo afirma lo viejo? | Agregador | La propagación solo es visible desde fuera del paso corregido |

## Cobertura contra un título

Los títulos no se describen. Eso deja al agente de persona con un problema real: ¿qué significa que
un título *cubra* un paso de mi flujo, si el título es todo lo que hay?

**Un título cubre un paso cuando pasa las tres pruebas y, leído contra ese paso, lo decide.**

| Prueba | Pasa | No pasa |
|---|---|---|
| **Nombra un hecho, no un área** | «Entregar al alumno el material de la semana sin conexión activa» | «Gestión de contenidos» — un sistema que no hace nada de eso también podría llevar ese título |
| **Es negable** | Se puede describir un sistema concreto que lo incumple | «Optimización del uso de IA» — ningún sistema lo incumple y ninguno lo cumple |
| **Una sola lectura** | Dos lectores del enunciado y de las personas lo entienden igual | «Sincronizar los materiales» — con o sin verificación de integridad son dos sistemas distintos |

Si el título determina el paso solo en parte, la cobertura es parcial y el veredicto no puede ser
mejor que `Funciona con reservas`.

### Título comodín

Un título que falla la prueba 1 o la 2 es un **comodín**: cubre cualquier cosa y por lo tanto no
cubre ninguna. Frente a él el agente hace dos cosas, y las dos:

1. **Cuenta el paso como no cubierto.** Un comodín no es cobertura débil; es ausencia de cobertura
   con apariencia de presencia, que es peor, porque nadie va a buscar el requerimiento que falta.
2. **Lo reporta por su nombre**, con el identificador. El agregador lo cobra en D4 como *título no
   entendible*.

Un título que falla la prueba 3 no es comodín sino **ambigüedad no marcada**. También lo cobra D4, y
su corrección no es reescribirlo mejor sino marcarlo con `[CLARIFY: …]` y decidirlo.

## Protocolo del agente de persona

Se corre **una vez por persona, por separado**. Cada agente vive en
[`.claude/agents/`](../.claude/agents/) y lee **exactamente dos archivos**: el suyo en
[`personas/`](../personas/) y el [backlog](../redale/R-requerimientos/backlog.md). Nada más: ni las
otras personas, ni `personas/README.md`, ni los veredictos ajenos, ni el historial.

La exclusión de `personas/README.md` es la que más importa: ese archivo contiene las tensiones y el
ángulo de las otras personas. Un agente que lo lee deja de reclamar y empieza a negociar, y ahí se
pierde la única señal que el agente existe para producir.

Cada agente responde, en este orden:

1. **¿Mi flujo principal corre de extremo a extremo, incluido cuando sale mal?** Citando ítems por
   su identificador. Un flujo cubierto solo en su camino feliz no aprueba esta pregunta.
2. **¿Qué me frustra?** Lo que el backlog decide en mi contra, lo que deja sin decidir para que lo
   absorba yo, y cualquier título que rompa mis permisos.
3. **Veredicto.**

| Veredicto | Resta | Se emite cuando |
|---|---|---|
| `Funciona` | 0 | Cada paso del flujo y el *cuando sale mal* están sostenidos por títulos que pasan las tres pruebas |
| `Funciona con reservas` | 0,5 | El flujo corre entero, pero al menos un paso se sostiene en un comodín o en cobertura parcial |
| `No funciona` | 1 | Un paso del flujo principal no lo sostiene ningún título; o el *cuando sale mal* no está cubierto; o un título le concede a alguien algo que su archivo declara «nunca debe» |

**Un veredicto sin cita al backlog es inadmisible y cuenta como `No funciona`.** Una cita a un
identificador que no existe tampoco es cita.

**Precondición: sin todos los veredictos no se emite total.** Si falta uno, D1 se declara no
computable, se informan D2, D3 y D4, y el total queda en blanco.

## Cómo se corre una iteración

1. Se corre cada agente de persona por separado sobre el backlog vigente.
2. Se corre el agregador, que lee el conjunto y puntúa D2, D3 y D4.
3. Se escribe el informe en [`iterations/`](iterations/) con nombre `AAAA-MM-DD-NN.md`.
4. Se agrega la fila a [`HISTORY.md`](HISTORY.md).
5. Si el total quedó bajo 8, se corrige **el backlog** —nunca la rúbrica— y se vuelve a 1.

## Cómo se enmienda la rúbrica

Se puede enmendar una dimensión que **no mide lo que dice medir**. Nunca para alcanzar el gate.
La enmienda se escribe antes de conocer el puntaje que produciría, se justifica contra datos de
rondas anteriores, y se registra en [`../docs/DECISIONES.md`](../docs/DECISIONES.md).
