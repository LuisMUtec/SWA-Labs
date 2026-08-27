# Iteraciones del diseño

El enunciado exige **mostrar claramente las iteraciones**. Esta es la bitácora.

Hay **dos clases de iteración** y confundirlas arruina el entregable. Ambas viven acá, en tablas
separadas, porque una fuerza a la otra.

| Clase | Qué es | Qué la hace avanzar | Dónde se ve |
|---|---|---|---|
| **Del diseño** (*top-down*) | El **mismo diagrama de componentes**, dibujado otra vez y más abierto | Un ítem del backlog que el diagrama actual no explica | [`L-listar-componentes/`](L-listar-componentes/) |
| **Del EVAL** | Una pasada de evaluación que **cambia una decisión** del backlog | Un puntaje bajo el gate, o un veredicto de persona | [`../evals/iterations/`](../evals/iterations/) |

La que el enunciado pide mostrar es la **primera** — así la mostró el profesor en clase (ver
[`../docs/EJEMPLO-CLASE-TOP-DOWN.md`](../docs/EJEMPLO-CLASE-TOP-DOWN.md)). La segunda es cómo se
llega a un backlog que valga la pena diagramar.

---

## Iteraciones del diseño

Cada fila es una pasada del diagrama. La regla que las gobierna: **no se dibuja el diagrama final y
después se inventan las iteraciones previas.** La primera es un cuadrado; lo que fuerza la
siguiente es un ítem del backlog que el cuadrado no explica.

| # | Qué muestra | Qué ítem del backlog la forzó | Ítems que quedan `DONE` |
|---|---|---|---|
| 1 | — | — | — |
| 2 | — | — | — |
| 3 | — | — | — |

La trazabilidad completa —qué ítem cubre qué iteración— vive en
[`L-listar-componentes/`](L-listar-componentes/), no acá. Esta tabla dice **por qué** hubo otra
pasada; aquella dice **qué** quedó cubierto.

---

## Iteraciones del EVAL

Una fila por corrida. El detalle de cada una en [`../evals/iterations/`](../evals/iterations/) y el
resumen en [`../evals/HISTORY.md`](../evals/HISTORY.md).

| # | Fecha | Pasos tocados | Qué la forzó | Qué cambió | Total /10 |
|---|---|---|---|---|---|
| 01 | — | — | — | — | — |

---

## Cómo se registra una iteración del diseño

1. **Qué ítem del backlog no explicaba el diagrama anterior.** Ese es el motivo, y es el único
   motivo válido. Un componente que aparece sin un ítem que lo pida es un huérfano, y el
   [agregador](../evals/README.md) lo cobra.
2. **Qué se abrió.** Qué caja de la pasada anterior dejó de ser una caja.
3. **Qué ítems quedan `DONE`** al cerrar la pasada.
4. **Qué quedó sin cubrir**, que es lo que va a forzar la siguiente.

## Cómo se registra una iteración del EVAL

Una iteración es una pasada que **cambia una decisión**, no una corrección de redacción. Se abre
cuando algo obliga a volver atrás: el EVAL quedó bajo el gate, una estimación no cierra contra los
requerimientos, el modelo de datos no soporta un flujo, o una persona no puede completar su día.

1. **Qué la forzó** — el hallazgo concreto, con su origen (una deducción del agregador, el veredicto
   de una persona, una contradicción entre dos pasos).
2. **Qué paso se corrigió** y qué decisión reemplazó a cuál.
3. **La propagación** — qué pasos aguas abajo quedaron afirmando lo viejo. Este es el punto:
   corregir `R` sin volver a mirar `E`, `D`, `A` y `L` deja el diseño incoherente, y el defecto
   reaparece dos iteraciones después disfrazado de otra cosa.
4. **El puntaje** de esa ronda.

---

## La propagación, que es el defecto que hay que vigilar

En el proyecto hermano ([Caso #2](https://github.com/LuisMUtec/SWA-LAB02-Lease)), nueve rondas de
evaluación encontraron que el modo de falla dominante **no era la sustancia sino la propagación**:
se enmendaba un requisito y quedaban la decisión que lo generó, la entidad, el flujo o el criterio
afirmando lo viejo. Tres rondas seguidas encontraron la misma forma con distinto disfraz.

En R.E.D.A.L.E. pega más fuerte, porque los pasos están encadenados por construcción: una
estimación se calcula **contra** unos requerimientos, un modelo de datos se arma **para** un
servicio diseñado, y un diagrama dibuja **lo que** el modelo de datos sostiene. Tocar `R` invalida
aguas abajo, siempre.

Las cuatro variantes que el Caso #2 encontró, que acá se buscan **por nombre**:

| Variante | En qué consiste | Cómo se cierra |
|---|---|---|
| **Cifra sin productor** | Un requisito se apoya en un número que nada produce | Dándole un productor a la cifra, nunca reescribiendo el criterio que la usa |
| **Acto sin consumidor** | Algo se puede registrar, guardar y recuperar, y no le llega a nadie ni puede responderse | Dándole un destinatario y un cierre |
| **Reparación en la altitud equivocada** | Se corrige el ítem y no la decisión que lo generó, que sigue diciendo lo contrario | Subiendo la corrección al documento que gobierna |
| **Estado sin terminador** | Algo se abre y nada lo cierra — acá, típicamente: una retención | Dándole un plazo que se vence solo |
