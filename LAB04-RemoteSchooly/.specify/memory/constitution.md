# Constitución de RemoteSchooly

Los principios que gobiernan el diseño de este caso. La lee el agregador del
[EVAL](../../evals/README.md): el [enunciado](../../docs/LAB-04-ARQ-2026.2.md) dice cuál es el
problema, y **la constitución dice qué se hace con un ítem que no lo ataca**.

## Core Principles

### I. La entrega se verifica en el destino, no en el origen (NEGOCIABLE: NO)

Un material se da por entregado cuando **el destino confirma que lo tiene completo**, nunca cuando la
central lo despachó. «Enviado» y «llegado» son dos hechos distintos y el sistema no puede confundirlos
en un solo estado.

El enunciado exime de asegurar 100 % de disponibilidad, pero exige con la misma frase *"que los cursos
lleguen correctamente"*. Ese «correctamente» es este principio: completo, íntegro, y de la semana que
corresponde.

**Consecuencia operativa:** todo estado del sistema que afirme una entrega tiene que poder decir quién
la confirmó y cuándo. Un tablero que muestre despachos y los llame cobertura contradice la
constitución.

### II. El pueblo funciona sin preguntar

Todo lo que ocurre del lado del pueblo —abrir el material, ver qué compone la semana, saber si está
completo— **tiene que ocurrir sin conexión activa en ese momento**. El enlace limitado es premisa del
caso, no falla que se maneje.

**Consecuencia operativa:** cualquier diseño que exija una llamada a Lima en el instante en que Nayra
abre una lectura está descartado, aunque funcione en la demo.

### III. Cada no funcional lleva su medida

*"Rápido", "seguro", "escalable" y "confiable" no son requerimientos.* Un no funcional sin número no
entra al backlog, y no se rescata reescribiéndolo mejor: se le pone medida o se retira.

Es el criterio que el profesor dictó en clase el 2026-08-25 `[11:49]` —*"los no funcionales son todas
las limitaciones técnicas del sistema: el sistema soportará máximo un megabyte de archivo de texto"*—
y el que respondió, por escrito, a los no funcionales del Caso #1: *"demasiado genéricos y parecen
demasiado ajustados para que sean evaluados/leídos por una IA más que una persona"*.

### IV. La cobertura manda sobre el volumen

El backlog se mide por **cuántos flujos de personas cierra de extremo a extremo, incluido cuando salen
mal** — no por cuántos ítems tiene. Un título que no cierra un paso del flujo de alguien no entra,
aunque sea verdadero y esté bien escrito.

El Caso #1 llegó a 194 requerimientos y el profesor lo objetó tres veces; el Caso #3 llegó a 236.
[`D-05`](../../docs/DECISIONES.md) fija el techo de este caso en ~26 + ~7.

**Consecuencia operativa:** frente a un ítem que no ataca el problema del enunciado —un aula virtual
genérica, una funcionalidad razonable que nadie pidió— **se retira**. No se conserva por si acaso.

### V. Los requerimientos bajan, nunca suben

La cadena de autoridad es `constitución → spec → backlog → E · D · A · L`
([`D-01`](../../docs/DECISIONES.md)). Ningún paso aguas abajo puede introducir un comportamiento que
el backlog no declare.

Si `D` diseña una ruta que responde algo que ningún título exige, o `A` guarda un campo que ningún
título obliga a conocer, **el defecto es del backlog** y la corrección va arriba: se agrega el
requerimiento en el spec, se reproyecta, y se vuelve a puntuar. Nunca se arregla abajo.

## Restricciones del caso

Lo que el enunciado fija y ningún diseño puede contradecir:

| Restricción | Origen |
|---|---|
| Los materiales salen de **una central en Lima** y llegan a todas las regiones | Enunciado |
| El internet de los pueblos es **limitado** — premisa, no avería | Enunciado |
| La unidad de entrega es **la semana** | Enunciado: *"los materiales para la semana"* |
| El gasto de tokens baja **al menos 40 %** | Enunciado. Única cifra dura del caso. Unidad y línea base en [`D-07`](../../docs/DECISIONES.md) |
| **Fuera de alcance:** asegurar 100 % de disponibilidad | Enunciado |
| **Fuera de alcance:** mecanismos de confiabilidad | Enunciado |

**Un principio que exija lo que el enunciado excluyó contradice esta constitución.** Un ítem sobre
replicación activa-activa no suma en D3: gasta presupuesto de backlog en algo que el caso sacó del
alcance. Se retira igual que un ítem que no ataca el problema.

## Proceso

| Regla | Qué fija |
|---|---|
| **El EVAL puntúa el backlog, y nada más** | `E`, `D`, `A`, `L` y `E` son entregable exigido, no puntaje. Lo que impide que diverjan es el principio V, no puntuarlos |
| **Gate ≥ 8/10, y no se alcanza bajando la vara** | Un puntaje bajo el gate se corrige en el spec y se reproyecta. La rúbrica no se mueve para pasar |
| **Medir y corregir no ocurren a la vez** | Una ronda mide; la corrección va entre rondas. Corregir a mitad de una corrida invalida el puntaje |
| **Un ID no se reutiliza** | `RF`, `RNF` y `BR` retirados se declaran muertos y su número queda quemado |
| **La ambigüedad se marca, no se resuelve en silencio** | `[CLARIFY: ...]` para lo que falta decidir, `[ASSUMPTION: ...]` para lo que decidimos nosotros. El profesor deja la ambigüedad a propósito `[14:08]` |

## Governance

Esta constitución **prevalece sobre cualquier otra práctica del repositorio**. Un documento que la
contradiga está mal, aunque sea posterior.

**Enmiendas.** Se enmienda registrando la enmienda en [`../../docs/DECISIONES.md`](../../docs/DECISIONES.md)
con su alternativa descartada y sus consecuencias en los dos sentidos. Una enmienda escrita **después**
de conocer el puntaje que produciría es inadmisible.

**Verificación.** Cada corrida del EVAL comprueba el cumplimiento: el agregador lee esta constitución
para D2 y para decidir qué hacer con un ítem que no ataca el problema.

**Versionado.** `MAYOR.MENOR.PARCHE` — mayor si se retira o se invierte un principio, menor si se
agrega uno o una sección, parche si se aclara la redacción sin cambiar lo que obliga.

**Version**: 1.0.0 | **Ratified**: 2026-09-02 | **Last Amended**: 2026-09-02
