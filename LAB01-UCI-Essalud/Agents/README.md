# Agents

Una definición de agente por cada persona / usuario modelo de [`/Personas`](../Personas).
Base: [`_TEMPLATE.md`](_TEMPLATE.md).

| Agente | Archivo | Persona | Problema que ancla |
|---|---|---|---|
| Rodrigo Salazar | [`agent-rodrigo.MD`](agent-rodrigo.MD) | [`../Personas/Rodrigo.MD`](../Personas/Rodrigo.MD) | P1 |
| Milagros Chávez | [`agent-milagros.MD`](agent-milagros.MD) | [`../Personas/Milagros.MD`](../Personas/Milagros.MD) | P2 · P3 |
| Carmen Rojas | [`agent-carmen.MD`](agent-carmen.MD) | [`../Personas/Carmen.MD`](../Personas/Carmen.MD) | P1 |
| Aníbal Quispe | [`agent-anibal.MD`](agent-anibal.MD) | [`../Personas/Anibal.MD`](../Personas/Anibal.MD) | P2 |

Cada agente sostiene su lado de las tensiones de
[`../Personas/README.md`](../Personas/README.md): no cede para quedar conforme. Que los cuatro queden
satisfechos a la vez es señal de que una tensión se esquivó, y `Eval-Spec` lo penaliza.

## Corridas

Ejecutar un agente sobre [`ReqFunc.MD`](../Requirements/ReqFunc.MD) produce una corrida con el formato
de salida del template. Cuando se archiva, vive en `Veredictos/veredicto-‹nombre›.MD`.

Las cuatro corridas son insumo obligatorio del agente evaluador global, que vive aparte en
[`/Spec/Eval-Spec.MD`](../Spec/Eval-Spec.MD): de ellas computa D1 —satisfacción de las personas, 30 %
del puntaje—. Sin las cuatro no hay porcentaje global. Una corrida que omite un RF cuenta ese RF como
ambiguo y penaliza.

El agente emite veredictos; no calcula puntajes. La escala que traduce esos veredictos a puntos vive
en `Eval-Spec`, de modo que ningún agente puede subir su propia nota.
