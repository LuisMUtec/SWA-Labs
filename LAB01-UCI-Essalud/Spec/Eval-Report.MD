# Evaluación de Requerimientos Funcionales — Sistema UCI Essalud

| | |
|---|---|
| Corrida | 2026-08-15-iteracion-11 |
| Rama | `eval/iteracion-11` |
| Modelo | claude-opus-5 |
| Evaluado | `Requirements/ReqFunc.MD` @ `4eb06c0` |
| Rúbrica | `Spec/Eval-Spec.MD` @ `b492237` |
| Personas | `Personas/` @ `6340172` |
| Agentes | `Agents/` @ `34877c7` |
| Instrumento modificado | no |

## Puntaje global: 72,7 %

| Dimensión | Puntaje | Peso | Aporte |
|---|---:|---:|---:|
| D1 Satisfacción de las personas | 52,0 | 30 % | 15,600 |
| D2 Cobertura de problemas críticos | 66,7 | 25 % | 16,675 |
| D3 Verificabilidad y forma | 99,5 | 20 % | 19,900 |
| D4 Trazabilidad | 100,0 | 10 % | 10,000 |
| D5 Consistencia y tensiones | 60,0 | 10 % | 6,000 |
| D6 Priorización | 90,0 | 5 % | 4,500 |
| **Suma de aportes** | | | **72,675 → 72,7** |

## Veredicto: FAILED

| # | Condición | Umbral | Obtenido | Cumple |
|---|---|---:|---:|:---:|
| 1 | Puntaje global | ≥ 80,0 % | 72,7 % | ✗ |
| 2 | D1 | ≥ 80,0 | 52,0 | ✗ |
| 3 | Persona más baja | ≥ 7,0/10 | 2,8 (Milagros) | ✗ |
| 4 | D2 | ≥ 80,0 | 66,7 | ✗ |
| 5 | Controles de `verificar.sh` | 9/9 | 9/9 | ✓ |

Fallan cuatro de las cinco. El único control en verde es el mecánico: la forma de los RF y la
aritmética están bien; lo que no está resuelto es a quién sirven.

## Puntajes por persona

| Persona | Tareas /30 | Estorba fuera | Necesidades /6 | Flujo /4 | Puntaje /10 | Percibida | Δ |
|---|---:|---:|---:|---:|---:|---:|---:|
| Rodrigo | 20 | 1 | 3,6 | 4 | 7,6 | 85 | +9 |
| Milagros | 20 | 3 | 2,8 | 0 | 2,8 | 85 | +57 |
| Carmen | 20 | 2 | 3,2 | 2 | 5,2 | 85 | +33 |
| Aníbal | 22 | 3 | 3,2 | 2 | 5,2 | 80 | +28 |
| **PROMEDIO** | **20,5** | **2,25** | **3,2** | **2,0** | **5,2** | **83,8** | **+31,8** |

`Puntaje_p = máx(0, Σ tareas_p − 2 × X_p) / 5 + Flujo_p`; `D1 = 5,2 × 10 = 52,0`.

Tres de las cuatro discrepancias superan los 20 puntos y prevalece el valor computado.

## Brechas encontradas

| # | Persona o problema afectado | Brecha | Origen | Severidad |
|---|---|---|---|---|
| 1 | Milagros · P2 | Tras la reiteración de `RF-ESC-47`, si el alcanzado por el agotamiento tampoco acusa, ningún RF continúa la cadena | veredicto-milagros + auditoría | Crítica |
| 2 | Aníbal · P2 | El acuse de recibo y la toma del caso no figuran en el conjunto cerrado de actos que `RF-IAM-16` admite en el dispositivo personal | veredicto-anibal + auditoría | Crítica |
| 3 | Rodrigo · P1 | `RF-DIA-47` admite el registro tardío del diagnóstico y `RF-IAM-02` ordena rechazarlo; ningún enunciado dice cuál manda | veredicto-rodrigo + auditoría | Alta |
| 4 | Rodrigo, Milagros, Aníbal · P3 | `RF-ESC-13` y `RF-ESC-49` fijan cortes distintos para el mismo acto de consultar la actualización informativa | veredicto-rodrigo, -milagros, -anibal + auditoría | Alta |
| 5 | Todos · D3 | `RF-ESC-13` enuncia dos respuestas: la incorporación del hecho y lo que la consulta entrega | auditoría | Alta |
| 6 | Milagros | `RF-ESC-08` no declara qué entrega por una cama que no cuenta con responsable clínico vigente | veredicto-milagros | Alta |
| 7 | Milagros | `RF-IAM-08` no declara si la identidad se verifica junto a la cama con la unidad sin conexión | veredicto-milagros | Alta |
| 8 | Carmen | Ningún RF le avisa de que un candidato aceptó la cobertura; `RF-TUR-36` y `RF-TUR-40` cubren rechazo y vencimiento | veredicto-carmen + auditoría | Alta |
| 9 | Carmen | `RF-TUR-03` no excluye la indisponibilidad declarada vigente que `RF-ESC-45` sí excluye de su lista | veredicto-carmen + auditoría | Alta |
| 10 | Aníbal | Ningún RF declara qué expone el aviso en un dispositivo no institucional cuando sí hay identidad verificada vigente; `RF-IAM-04` solo fija el caso contrario | veredicto-anibal | Alta |
| 11 | Rodrigo | La marca de `RF-DIA-06` no lleva el pendiente concreto que la motivó | veredicto-rodrigo | Media |
| 12 | Milagros | Ningún enunciado declara que recibir, firmar y aceptar la entrega de enfermería se hagan junto a la cama | veredicto-milagros | Media |
| 13 | Carmen | No puede cerrar por sí misma una franja descubierta fuera del horizonte de urgencia (`RF-TUR-44`, `RF-TUR-47`) | veredicto-carmen | Media |
| 14 | Carmen | No puede dejar sin efecto una solicitud de cobertura vigente antes del vencimiento de su plazo | veredicto-carmen | Media |
| 15 | Carmen | No se entera de los cambios que el sistema produce sobre su programación vigente sin intervención suya (`RF-ESC-45`) | veredicto-carmen | Media |
| 16 | Carmen | `RF-TUR-16` y `RF-TUR-28` no declaran que el reflejo sea imprimible, que es su restricción documentada | veredicto-carmen | Media |
| 17 | Aníbal | `RF-SUP-03` no comprende las indicaciones suspendidas ni las decisiones de acudir o de no acudir | veredicto-anibal | Media |
| 18 | Aníbal | La solicitud de estudio hecha a distancia no tiene alcance junto a la cama (`RF-REG-14`, `RF-REG-17`) | veredicto-anibal | Media |
| 19 | Consistencia | `RF-ESC-49` y `RF-REG-17` llevan un bloque «Por qué existe» que narra cómo se llegó al RF y cita dimensiones de la rúbrica | auditoría | Media |
| 20 | Rodrigo · P1 | Ningún enunciado declara qué recibe el entrante cuando el turno saliente no registró nada en el sistema | veredicto-rodrigo | Baja |

Cinco necesidades declaradas por los agentes quedan **refutadas por escrito** en el diagnóstico: las
cuatro que invocan un «título de consulta» no declarado y la que reclama la composición de los
indicadores. El glosario define ambos términos y los agentes no lo aplicaron.

## Acciones recomendadas (priorizadas)

1. **Cerrar la cadena de escalamiento.** Declarar qué ocurre cuando el profesional alcanzado por el
   agotamiento no acusa la reiteración de `RF-ESC-47`. Es el único punto donde el escenario clave de
   una persona se interrumpe, y arrastra el flujo de Milagros a 0 y P2 a 50.
2. **Resolver las dos contradicciones que bloquean comportamiento declarado.** `RF-DIA-47` frente a
   `RF-IAM-02` —el cierre tardío, que sostiene P1— y `RF-ESC-13` frente a `RF-ESC-49` —la
   actualización informativa—. La segunda exige además separar `RF-ESC-13` en dos RF: es el único RF
   no conforme de D3.
3. **Abrir el conjunto cerrado de `RF-IAM-16`** para que comprenda el acuse de recibo y la toma del
   caso. Es la tarea crítica peor sostenida del documento (Aníbal, tarea 2, 1/5) y la única que baja
   de 3.
4. **Alinear la elegibilidad**: `RF-TUR-03` y `RF-ESC-45` deben aplicar el mismo conjunto de
   condiciones, y el glosario es su dueño.
5. **Sacar de `ReqFunc.MD` los bloques «Por qué existe»** de `RF-ESC-49` y `RF-REG-17`: registran
   cómo se llegó al requerimiento y citan la rúbrica que lo puntúa. Su lector es `git log`.
6. **Revisar la prioridad de `RF-TUR-04` y `RF-IAM-19`**: ausentes, ninguna tarea crítica queda
   descubierta ni ningún problema crítico sin resolver. Son SHOULD.

## Evidencia

`Spec/corridas/2026-08-15-iteracion-11/` — diagnóstico, los cuatro veredictos de persona y
`corrida.json`.
