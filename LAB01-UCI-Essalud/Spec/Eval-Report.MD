# Evaluación de Requerimientos Funcionales — Sistema UCI Essalud

| | |
|---|---|
| Corrida | 2026-08-15-iteracion-9 |
| Rama | `eval/iteracion-9` |
| Modelo | claude-opus-5 |
| Evaluado | `Requirements/ReqFunc.MD` @ `f21fc52` |
| Rúbrica | `Spec/Eval-Spec.MD` @ `b492237` |
| Personas | `Personas/` @ `6340172` |
| Agentes | `Agents/` @ `34877c7` |
| Instrumento modificado | no |

## Puntaje global: 80,9 %

| Dimensión | Puntaje | Peso | Aporte |
|---|---:|---:|---:|
| D1 Satisfacción de las personas | 63,0 | 30 % | 18,90 |
| D2 Cobertura de problemas críticos | 83,3 | 25 % | 20,83 |
| D3 Verificabilidad y forma | 98,3 | 20 % | 19,66 |
| D4 Trazabilidad | 100,0 | 10 % | 10,00 |
| D5 Consistencia y tensiones | 70,0 | 10 % | 7,00 |
| D6 Priorización | 90,0 | 5 % | 4,50 |
| | | | **80,89 → 80,9** |

## Veredicto: FAILED

| # | Condición | Umbral | Obtenido | Cumple |
|---|---|---:|---:|:---:|
| 1 | Puntaje global | ≥ 80,0 % | 80,9 % | ✅ |
| 2 | D1 | ≥ 80,0 | 63,0 | ❌ |
| 3 | Persona más baja | ≥ 7,0/10 | 4,8 (Rodrigo) | ❌ |
| 4 | D2 | ≥ 80,0 | 83,3 | ✅ |
| 5 | Controles de `verificar.sh` | 9/9 | 9/9 | ✅ |

Fallan dos de las cinco condiciones y el resultado es **FAILED**. El global atraviesa el umbral por
0,9 puntos, y eso no lo salva: el porcentaje ponderado alto lo sostienen las dimensiones de
auditoría —forma, trazabilidad, priorización, que suman 35 % del peso y promedian 96— mientras la
dimensión que responde la única pregunta que importa, si los requerimientos satisfacen a las personas
que van a usar el sistema, se queda a 17 puntos de su umbral. Un documento impecablemente escrito que
deja a su persona ancla en 4,8/10 no está aprobado.

## Puntajes por persona

| Persona | Tareas /30 | Estorba fuera | Necesidades /6 | Flujo /4 | Puntaje /10 | Percibida | Δ |
|---|---:|---:|---:|---:|---:|---:|---:|
| Rodrigo | 18 | 2 | 2,8 | 2 | 4,8 | 85 | −37 |
| Milagros | 22 | 2 | 3,6 | 2 | 5,6 | 80 | −24 |
| Carmen | 24 | 1 | 4,4 | 4 | 8,4 | 85 | −1 |
| Aníbal | 26 | 2 | 4,4 | 2 | 6,4 | 80 | −16 |
| **PROMEDIO** | **22,5** | **1,75** | **3,8** | **2,5** | **6,3** | **82,5** | **−19,5** |

`Puntaje_p = máx(0, Σ tareas_p − 2 × X_p) / 5 + Flujo_p`; `D1 = 6,3 × 10 = 63,0`.

Dos discrepancias superan los 20 puntos —Rodrigo (37) y Milagros (24)—. En ambas prevalece el valor
computado y lo que falla es el autoinforme: los dos agentes leen su cobertura percibida sobre la
densidad de veredictos *Sirve* del documento entero (61 y 77 de 177) y no sobre la completitud de sus
seis tareas, y ninguno de los dos descuenta los RF que marcó **Estorba** fuera de ellas.

## Brechas encontradas

| # | Persona o problema afectado | Brecha | Origen | Severidad |
|---|---|---|---|---|
| 1 | Rodrigo · P1 · P3 | Ningún RF declara el acto por el que un resultado de laboratorio o de imágenes se incorpora al episodio: RF-REG-06 presenta los «disponibles», RF-REG-10 cuenta los pendientes y RF-ESC-29 se dispara «cuando se incorpora» | veredicto-rodrigo · auditoría | Alta |
| 2 | Rodrigo · P1 | RF-DIA-05 ancla el «último contacto» al último registro clínico y no a la última consulta, de modo que a las 23:40 vuelve a recibir tres semanas de cambios | veredicto-rodrigo | Media |
| 3 | Rodrigo · P1 | Las imágenes no figuran entre los cambios que RF-DIA-05 enumera: una placa nueva no aparece en lo que cambió | veredicto-rodrigo | Media |
| 4 | Rodrigo · Milagros · Carmen · P1 | Ningún enunciado declara si declarar camas (RF-DIA-18, RF-DIA-19) sustituye o se suma a la incorporación automática (RF-DIA-28, RF-DIA-30); tres de los cuatro agentes lo marcaron Ambiguo por esa misma razón | veredicto-rodrigo · veredicto-milagros · veredicto-carmen | Alta |
| 5 | Rodrigo · P1 | Nada declara que el equipo compartido muestre bajo qué identidad se está escribiendo antes de guardar; RF-IAM-15 preserva sin declarar cómo distingue al autor | veredicto-rodrigo | Alta |
| 6 | Milagros · P1 | No existe para enfermería el equivalente de RF-DIA-09: ningún RF registra la aceptación de su entrega por la enfermera entrante | veredicto-milagros | Media |
| 7 | Milagros · P2 | Al escalar no obtiene por qué medio de contacto se alcanza al médico ni si está vigente; RF-IAM-12 presenta esa carencia al profesional y a la jefatura, nunca a ella | veredicto-milagros | Media |
| 8 | Milagros · P2 | RF-ESC-23 compone la cadena encabezada por el responsable clínico vigente sin declarar cómo se compone cuando no existe | veredicto-milagros | Media |
| 9 | Milagros · P3 | Ningún RF declara que se le presente la condición de un registro suyo preservado fuera del episodio por RF-IAM-15 | veredicto-milagros · auditoría | Alta |
| 10 | Milagros · P2 | La cadena agotada termina en la jefatura (RF-ESC-09) sin respuesta exigible declarada ni condición presentada a quien escaló | veredicto-milagros | Media |
| 11 | Carmen · P1 | El cumplimiento y la completitud de las entregas de enfermería no se le presentan: RF-SUP-01 solo alcanza el turno médico | veredicto-carmen | Media |
| 12 | Carmen · P1 | RF-TUR-07 lista solo franjas sin profesional asignado: la franja cuyo profesional declaró indisponibilidad vigente (RF-ESC-32) le sigue figurando cubierta | veredicto-carmen | Alta |
| 13 | Carmen · P1 | No hay confirmación de lectura de la programación mensual publicada; RF-TUR-15 y RF-TUR-25 solo cubren los cambios posteriores | veredicto-carmen | Media |
| 14 | Carmen · P1 | Ningún RF avisa a la jefatura cuando la asignación médica de una cama cambia de manos durante la franja: RF-DIA-35 avisa solo al médico desplazado | veredicto-carmen | Media |
| 15 | Carmen · P1 | RF-DIA-34 señala al propio médico las camas sin decisión clínica y no traslada ese faltante a nadie: responde por un registro cuya integridad no puede ver | veredicto-carmen | Media |
| 16 | Aníbal · P2 | Ningún enunciado le presenta de cuántas y cuáles camas es responsable clínico vigente esta noche en cada sede: RF-TUR-49 y RF-DIA-46 se lo presentan a la jefatura, RF-ESC-41 a enfermería | veredicto-anibal | Alta |
| 17 | Aníbal · P2 | Nada le avisa en el instante en que una cama pasa a ser suya por RF-DIA-36 seguido de RF-ESC-43 | veredicto-anibal | Alta |
| 18 | Aníbal · P3 | Con la toma del caso de una cama que no es de su responsabilidad no recibe su actualización informativa: RF-ESC-13 la entrega solo a la consulta del responsable clínico vigente | veredicto-anibal | Media |
| 19 | Aníbal · P2 | Nada declara qué ocurre cuando dos cadenas de sedes distintas lo alcanzan en el mismo minuto: RF-ESC-23 compone por unidad | veredicto-anibal | Media |
| 20 | D3 | RF-IAM-12 pega dos disparadores en una respuesta, RF-IAM-15 pega dos respuestas con disparadores distintos y RF-REG-14 enuncia una segunda respuesta en cláusula relativa | auditoría | Media |
| 21 | D5 | El rol supervisor se designa de tres formas —«la coordinadora» (70), «el coordinador» (2) y «la jefatura de la unidad» (38)— y el glosario solo fija la tercera | auditoría | Media |
| 22 | D6 | RF-ESC-38 y RF-ESC-45 llevan MUST sin que su ausencia deje descubierta una tarea crítica ni sin resolver un problema crítico | auditoría | Baja |

Cuatro necesidades declaradas por los agentes **no** figuran aquí porque quedan refutadas por escrito
en `diagnostico.MD` §Necesidades refutadas: las tres que el glosario ya resuelve —«estado clínico»,
«último contacto» y «ámbito de responsabilidad»— y el cierre de la entrega tras el registro tardío de
RF-DIA-47, que RF-DIA-20 admite. Lo que Milagros declina reclamar —los 30 segundos, el número de
pasos, la forma del aviso en una unidad con alarmas— pertenece a `ReqNoFunc.MD` y no es brecha.

## Acciones recomendadas (priorizadas)

1. **Declarar el acto de incorporación de resultados al episodio** (brecha 1). Es el único punto del
   documento del que cuelgan tres RF sin dueño, deja la quinta tarea crítica de Rodrigo en 1 punto —el
   único «Aparente» de la corrida— y es la razón por la que P3 queda en 50. Un solo RF nuevo mueve D1,
   D2 y D5 a la vez.
2. **Cerrar la composición de la asignación médica y de cuidado** (brecha 4). Declarar si la
   declaración de camas de RF-DIA-18 y RF-DIA-19 sustituye la asignación vigente o se suma a ella, y
   por qué vía se devuelve una cama incorporada. Tres agentes aislados marcaron Ambiguo el mismo
   punto: la coincidencia es evidencia, no ruido.
3. **Constituir el paso del aviso al contexto clínico en el dispositivo personal** (RF-IAM-05,
   Ambiguo para Aníbal). Es el paso 5 de su recorrido y el tramo donde se juegan sus tres minutos; hoy
   ningún enunciado constituye el estado de identificación que RF-IAM-04 presupone.
4. **Dar a cada persona la vista de aquello por lo que responde**: a Aníbal las camas de las que es
   responsable clínico vigente y el aviso de cuándo una pasa a serlo (brechas 16 y 17); a Milagros el
   medio de contacto por el que se alcanza al médico y el destino del escalamiento agotado (7 y 10); a
   Carmen la franja cubierta por un indisponible y el faltante de decisión clínica (12 y 15).
5. **Unificar el vocabulario del rol supervisor** (brecha 21) y **revisar los dos MUST no reservados**
   (brecha 22). Son las correcciones más baratas del conjunto y son las únicas que suben D5 y D6.

## Evidencia

`Spec/corridas/2026-08-15-iteracion-9/` — `diagnostico.MD` (matriz de cobertura, recorridos, auditoría
de D2 a D6), los cuatro `veredicto-*.MD` y `corrida.json`.
