# Agents

Una definición de agente por cada persona / usuario modelo de [`/Personas`](../Personas).
Base normativa: [`_TEMPLATE.md`](_TEMPLATE.md).

| Agente | Archivo | Persona | Problema que ancla |
|---|---|---|---|
| Rodrigo Salazar | [`agent-rodrigo.MD`](agent-rodrigo.MD) | [`../Personas/Rodrigo.MD`](../Personas/Rodrigo.MD) | P1 |
| Milagros Chávez | [`agent-milagros.MD`](agent-milagros.MD) | [`../Personas/Milagros.MD`](../Personas/Milagros.MD) | P2 · P3 |
| Carmen Rojas | [`agent-carmen.MD`](agent-carmen.MD) | [`../Personas/Carmen.MD`](../Personas/Carmen.MD) | P1 |
| Aníbal Quispe | [`agent-anibal.MD`](agent-anibal.MD) | [`../Personas/Anibal.MD`](../Personas/Anibal.MD) | P2 |

Cada agente sostiene su lado de las tensiones de
[`../Personas/README.md`](../Personas/README.md): no cede para quedar conforme. Que los cuatro queden
satisfechos a la vez es señal de que una tensión se esquivó, y `Eval-Spec` lo penaliza.

## El estándar

Un agente tiene diez secciones en este orden. Las siete primeras dependen de la persona; las tres
últimas son texto fijo.

| Sección | Deriva de | Varía entre agentes |
|---|---|---|
| Identidad | perfil y contexto de la persona | sí |
| Contexto operativo | restricciones de la persona | sí |
| Tu escenario clave | escenario clave de la persona | sí |
| Tus tareas críticas | tabla de tareas críticas de la persona | sí |
| Lo que te importa | criterios de éxito de la persona | sí |
| Lo que te frustra | frustraciones de la persona | sí |
| Tu lado de las tensiones | `../Personas/README.md` | sí |
| Tarea | el estándar | **no** |
| Formato de salida | el estándar | **no** |
| Reglas | el estándar | **no** |

**El bloque fijo es idéntico en los cuatro archivos.** Lo único que cambia es el nombre de la persona
y el archivo donde se archiva su evaluación. Se copia desde `_TEMPLATE.md`, que es su fuente: corregir
el bloque en un solo agente lo desalinea de los otros tres y convierte cuatro instrumentos
equivalentes en cuatro instrumentos distintos.

Ese bloque es lo que hace comparables las cuatro evaluaciones: mismo vocabulario de veredicto, mismos
dos recorridos, mismo formato de salida. La perspectiva es lo que cambia, no la vara.

### Por qué la tabla de tareas se copia

`Personas/‹Nombre›.MD` es la única dueña de las tareas críticas, y `Eval-Spec` construye su matriz de
cobertura desde ahí, no desde el agente. La copia existe porque el agente se adopta como un todo y
necesita tener a la vista lo que va a recorrer. Es una derivación declarada, no una segunda fuente: si
las dos difieren, la desviada es la copia.

## Las tensiones y quién las sostiene

Las cinco tensiones de [`../Personas/README.md`](../Personas/README.md), y el agente que declara cada
lado:

| Tensión | Lado | Lado |
|---|---|---|
| Velocidad frente a completitud del registro | Rodrigo | Carmen |
| Autonomía de intercambio de turnos | Rodrigo | Carmen |
| Sensibilidad del escalamiento | Milagros | Aníbal |
| Adopción voluntaria | Rodrigo · Milagros | Carmen |
| Movilidad frente a control de datos | Aníbal | Ley N.° 29733 |

Dos asimetrías son deliberadas y no son omisiones. **Aníbal no declara la adopción voluntaria**: la
tensión corre entre Carmen y quienes registran a pie de cama, y él ni registra en volumen ni responde
por el registro de otros. **La movilidad frente al control de datos no tiene un agente enfrente**: su
contraparte es una norma, y una norma no negocia — por eso Aníbal la marca ambigua cuando un RF no
resuelve ninguno de los dos lados.

## Cómo se ejecutan

Las cuatro evaluaciones son independientes por diseño: ningún agente ve el veredicto de otro, y el
conflicto entre ellos es justamente lo que `Eval-Spec` tiene que resolver. Por eso se lanzan **en
paralelo, un subagente por persona**, cada uno con su archivo de agente, `Requirements/ReqFunc.MD` y
su `Personas/‹Nombre›.MD`.

Ejecutarlas en un solo contexto las contamina: el cuarto veredicto se escribe sabiendo lo que
dijeron los tres anteriores, y la coincidencia deja de ser evidencia. El aislamiento no es una
optimización de velocidad; es lo que hace que las cuatro lecturas signifiquen algo al agregarse.

El agente emite veredictos; no calcula puntajes. La escala que traduce esos veredictos a puntos vive
en [`../Spec/Eval-Spec.MD`](../Spec/Eval-Spec.MD), de modo que ningún agente puede subir su propia
nota. El procedimiento completo de una corrida está en esa rúbrica.

## Conformidad

Antes de evaluar se comprueba el instrumento. Un agente que se desvía de su persona mide otra cosa que
la que la rúbrica supone, y el porcentaje deja de significar lo que dice.

```
- [ ] Existen exactamente cuatro agentes, uno por persona, enlazados en la tabla de arriba
- [ ] Identidad, contexto, escenario, tareas, criterios y frustraciones derivan solo de su persona
- [ ] Ninguna tarea, necesidad o restricción que su persona no documente
- [ ] Nada de otra persona, y ningún RNF convertido en necesidad personal
- [ ] Las seis tareas coinciden con las de `Personas/‹Nombre›.MD`
- [ ] El bloque fijo es idéntico en los cuatro, salvo el nombre y el archivo de destino
- [ ] Cada tensión de `Personas/README.md` tiene declarados los lados que la tabla de arriba le asigna
```

Lo que se desvíe se corrige **en el agente**. Si la necesidad es legítima pero falta en la persona, no
se agrega al agente: `Personas/*` es la fuente, y se reporta como bloqueo. Se interviene solo sobre la
desviación concreta — no se reescribe un agente que ya cumple, ni se ajusta ninguno en función de los
RF que va a evaluar.

Corregir un agente cambia el instrumento: la corrida lo registra en `instrumento_modificado` y el
resultado no es comparable con el de una corrida anterior.

## Corridas

Ejecutar los cuatro agentes sobre [`ReqFunc.MD`](../Requirements/ReqFunc.MD) produce una corrida. Las
cuatro evaluaciones son insumo obligatorio del agente evaluador global,
[`../Spec/Eval-Spec.MD`](../Spec/Eval-Spec.MD): de ellas computa D1 —satisfacción de las personas, 30 %
del puntaje—. Sin las cuatro no hay porcentaje global. Una evaluación que omite un RF cuenta ese RF
como ambiguo y penaliza.

Cuando se archivan, viven en `Spec/corridas/‹id›/veredicto-‹nombre›.MD`, según
[`../Spec/corridas/_ESQUEMA.MD`](../Spec/corridas/_ESQUEMA.MD).
