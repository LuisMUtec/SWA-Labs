# Evaluación de Requerimientos Funcionales — Sistema UCI Essalud

| | |
|---|---|
| Corrida | 2026-08-14-iteracion-4 |
| Rama | `eval/iteracion-4` |
| Modelo | claude-opus-5 |
| Evaluado | `Requirements/ReqFunc.MD` @ `f4cc4cf` |
| Rúbrica | `Spec/Eval-Spec.MD` @ `b492237` |
| Personas | `Personas/` @ `6340172` |
| Agentes | `Agents/` @ `34877c7` |
| Instrumento modificado | no |

## Puntaje global: 64,7 %

| Dimensión | Puntaje | Peso | Aporte |
|---|---:|---:|---:|
| D1 Satisfacción de las personas | 48,0 | 30 % | 14,40 |
| D2 Cobertura de problemas críticos | 50,0 | 25 % | 12,50 |
| D3 Verificabilidad y forma | 97,5 | 20 % | 19,50 |
| D4 Trazabilidad | 80,0 | 10 % | 8,00 |
| D5 Consistencia y tensiones | 60,0 | 10 % | 6,00 |
| D6 Priorización | 85,0 | 5 % | 4,25 |
| **Global** | | | **64,65 → 64,7** |

## Veredicto: FAILED

| # | Condición | Umbral | Obtenido | Cumple |
|---|---|---:|---:|:---:|
| 1 | Puntaje global | ≥ 80,0 % | 64,7 % | no |
| 2 | D1 | ≥ 80,0 | 48,0 | no |
| 3 | Persona más baja | ≥ 7,0/10 | 4,4 | no |
| 4 | D2 | ≥ 80,0 | 50,0 | no |
| 5 | Controles de `verificar.sh` | 9/9 | 9/9 | sí |

## Puntajes por persona

| Persona | Tareas /30 | Estorba fuera | Necesidades /6 | Flujo /4 | Puntaje /10 | Percibida | Δ |
|---|---:|---:|---:|---:|---:|---:|---:|
| Rodrigo | 20 | 4 | 2,4 | 2 | 4,4 | 70 | 26 |
| Milagros | 20 | 2 | 3,2 | 2 | 5,2 | 78 | 26 |
| Carmen | 20 | 3 | 2,8 | 2 | 4,8 | 70 | 22 |
| Aníbal | 20 | 3 | 2,8 | 2 | 4,8 | 80 | 32 |
| **PROMEDIO** | **20** | **3** | **2,8** | **2** | **4,8** | **74,5** | **26,5** |

Ninguna de las 24 tareas críticas queda descubierta y ninguna llega a 5 salvo cinco: los
requerimientos abordan todo y no terminan casi nada. Las cuatro coberturas percibidas superan lo
computado por más del umbral de 20 puntos; prevalece el valor computado en los cuatro casos.

## Estado de los problemas críticos

| Problema | Puntos | Tramo sin RF |
|---|---:|---|
| P1 — Rotación de doctor | 50 | La cadena entera cuelga de la asignación médica de camas que solo RF-DIA-18 produce y que el enunciado pone en una coordinadora de jornada 08:00–16:00; ningún RF declara qué ocurre sin ella |
| P2 — Medianoche | 50 | Ningún RF declara el acto por el que una cama adquiere su responsable clínico vigente, que es el destinatario entero de RF-ESC-01 y el primer eslabón de RF-ESC-23 |
| P3 — Actualizaciones en tiempo real | 50 | El único RF que alcanza a varios destinatarios, RF-ESC-13, declara que la actualización aguarda la consulta de sus destinatarios: no notifica, espera |

## Brechas encontradas

Las 44 filas completas están en `Spec/corridas/2026-08-14-iteracion-4/diagnostico.MD`. Las críticas:

| # | Persona o problema afectado | Brecha | Origen | Severidad |
|---|---|---|---|---|
| 1 | Milagros, Carmen, Rodrigo · P2 | Ningún RF declara cómo una cama adquiere su responsable clínico vigente; RF-ESC-01, RF-ESC-08 y RF-ESC-23 lo presuponen | `veredicto-milagros`, `veredicto-carmen`, `veredicto-rodrigo` | Crítica |
| 2 | Rodrigo, Carmen · P1 | RF-DIA-18 y RF-DIA-19 ponen la asignación de camas de cada turno de las 24 horas en la coordinadora y ningún RF declara la vía alterna cuando no ocurrió | `veredicto-carmen`, `veredicto-rodrigo`, `auditoría` | Crítica |
| 3 | Milagros, Aníbal, Rodrigo · P3 | Ningún RF alcanza proactivamente a médicos y enfermeras ante una indicación nueva o un resultado crítico | `veredicto-milagros`, `veredicto-anibal`, `auditoría` | Crítica |
| 4 | Carmen · P1 | Ningún RF permite cerrar por autoridad una franja descubierta si ningún candidato acepta | `veredicto-carmen` | Crítica |
| 5 | Carmen · P1 | RF-TUR-35 contradice a RF-TUR-39 y a RF-TUR-01 sobre la misma aceptación de cobertura | `auditoría`, `veredicto-carmen` | Alta |
| 8 | Rodrigo · P1 | Ningún RF declara que la entrega médica se componga sin transcripción, como RF-DIA-08 y RF-DIA-11 sí declaran para enfermería | `veredicto-rodrigo` | Alta |
| 16 | Carmen · P1 | Ningún RF declara quién define el patrón de cobertura requerido de la unidad | `veredicto-carmen` | Alta |
| 17 | Carmen · P1 | Ningún RF declara de dónde salen las reglas de jornada y descanso que RF-TUR-02 y RF-TUR-03 invocan | `veredicto-carmen` | Alta |

## Acciones recomendadas (priorizadas)

1. **Declarar el responsable clínico vigente.** Escribir el RF que constituye, para cada cama y
   franja, el profesional médico que responde por ella derivándolo de la programación vigente, y
   reconciliarlo con la enumeración de RF-IAM-02, que hoy lo trata como cosa distinta de la asignación
   médica. Es el eslabón que le falta a P2, a la tarea 2 y a la tarea 3 de Milagros y al paso 8 del
   escenario de Rodrigo, y lo declararon tres agentes por separado.
2. **Sacar la asignación de camas del horario administrativo.** RF-DIA-18 y RF-DIA-19 son la
   precondición silenciosa de RF-DIA-01, RF-DIA-02, RF-DIA-21 y RF-IAM-02, y hoy dependen de una
   persona que a las 19:00 de un sábado no está. Hace falta un RF de borde que declare qué ocurre
   cuando un turno inicia sin asignación registrada.
3. **Convertir la actualización informativa en alcance.** RF-ESC-13 es el único RF de P3 para varios
   destinatarios y su enunciado dice que aguarda la consulta. Declarar el alcance proactivo de la
   indicación nueva y del resultado crítico a las enfermeras asignadas y al responsable médico, como
   RF-ESC-22 ya lo declara para quien emitió un escalamiento.
4. **Cerrar el circuito de cobertura de Carmen.** Un RF que le permita asignar por autoridad una
   franja descubierta sin aceptación del candidato, y la condición que falta en el enunciado de
   RF-TUR-35 para que deje de contradecir a RF-TUR-01 y a RF-TUR-39.
5. **Declarar los insumos que hoy se presuponen:** el patrón de cobertura requerido de la unidad
   (RF-TUR-09), las reglas de jornada y el vínculo laboral vigente (RF-TUR-02, RF-TUR-03), la
   incorporación del resultado de un estudio al episodio (RF-REG-06) y el alcance de la autorización
   reutilizable (RF-TUR-13).
6. **Equilibrar la tensión de adopción.** Declarar para la entrega médica la composición sin
   transcripción que RF-DIA-08 y RF-DIA-11 ya declaran para enfermería: hoy la tensión «Adopción
   voluntaria» está decidida a favor de Milagros y de la programación, y en contra de Rodrigo, que es
   la persona ancla de P1.
7. **Limpiar forma y consistencia:** los tres RF no conformes en D3 (RF-TUR-16, RF-TUR-39, RF-DIA-02),
   la lápida de RF-TUR-20, el duplicado encubierto RF-DIA-02 / RF-DIA-21, las dos filas de matriz
   desfasadas y los tres MUST no reservados (RF-DIA-03, RF-DIA-05, RF-ESC-19).

## Evidencia

`Spec/corridas/2026-08-14-iteracion-4/` — diagnóstico completo, los cuatro veredictos de persona,
`corrida.json` y la salida de los controles.
