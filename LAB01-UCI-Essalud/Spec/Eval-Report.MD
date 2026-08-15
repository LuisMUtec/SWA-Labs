# Evaluación de Requerimientos Funcionales — Sistema UCI Essalud

| | |
|---|---|
| Corrida | 2026-08-15-iteracion-10 |
| Rama | `eval/iteracion-10` |
| Modelo | claude-opus-5 |
| Evaluado | `Requirements/ReqFunc.MD` @ `42c00babb090c3e48b789017bf977a3e1ff24489` |
| Rúbrica | `Spec/Eval-Spec.MD` @ `b492237b254baa5c538b9d68803e1b0bd456112a` |
| Personas | `Personas/` @ `6340172da2d8c0b4ccabfc93880446cce9025732` |
| Agentes | `Agents/` @ `34877c7cc8316f7222914b8f03b0b548fb5d2806` |
| Instrumento modificado | no |

## Puntaje global: 77,4 %

| Dimensión | Puntaje | Peso | Aporte |
|---|---:|---:|---:|
| D1 Satisfacción de las personas | 54,0 | 30 % | 16,200 |
| D2 Cobertura de problemas críticos | 83,3 | 25 % | 20,825 |
| D3 Verificabilidad y forma | 99,5 | 20 % | 19,900 |
| D4 Trazabilidad | 100,0 | 10 % | 10,000 |
| D5 Consistencia y tensiones | 60,0 | 10 % | 6,000 |
| D6 Priorización | 90,0 | 5 % | 4,500 |
| | | | **77,425 → 77,4** |

## Veredicto: FAILED

| # | Condición | Umbral | Obtenido | Cumple |
|---|---|---:|---:|:---:|
| 1 | Puntaje global | ≥ 80,0 % | 77,4 % | ✗ |
| 2 | D1 | ≥ 80,0 | 54,0 | ✗ |
| 3 | Persona más baja | ≥ 7,0/10 | 4,4 | ✗ |
| 4 | D2 | ≥ 80,0 | 83,3 | ✓ |
| 5 | Controles de `verificar.sh` | 9/9 | 8/9 | ✗ |

C1 queda en rojo por un artefacto de ordenamiento del propio control, no por una discrepancia
aritmética: `verificar-puntaje.sh` identifica la última corrida ordenando los directorios como texto,
y `iteracion-10` ordena antes que `iteracion-5`, de modo que compara el porcentaje del README contra
`iteracion-9`. Corregirlo exige tocar `scripts/`, que es de solo lectura durante una corrida; queda
registrado en `Spec/corridas/2026-08-15-iteracion-10/bloqueos.MD`. El veredicto es FAILED con o sin
ese control: las condiciones 1, 2 y 3 ya no se cumplen.

El documento es formalmente excelente —D3 99,5, D4 100,0— y resuelve P1 y P2 de extremo a extremo. Lo
que no consigue es satisfacer a las personas: las 24 tareas críticas suman 86 de 120 puntos posibles,
ningún flujo llega a 4 porque los cuatro escenarios se apoyan en algún RF que su propio agente marcó
Ambiguo, y Rodrigo carga cinco requerimientos que le estorban fuera de sus seis tareas.

## Puntajes por persona

| Persona | Tareas /30 | Estorba fuera | Necesidades /6 | Flujo /4 | Puntaje /10 | Percibida | Δ |
|---|---:|---:|---:|---:|---:|---:|---:|
| Rodrigo | 22 | 5 | 2,4 | 2 | 4,4 | 80 | 36 |
| Milagros | 20 | 1 | 3,6 | 2 | 5,6 | 80 | 24 |
| Carmen | 20 | 2 | 3,2 | 2 | 5,2 | 80 | 28 |
| Aníbal | 24 | 1 | 4,4 | 2 | 6,4 | 80 | 16 |
| **PROMEDIO** | **21,5** | **2,25** | **3,4** | **2** | **5,4** | **80** | **26** |

`D1 = 5,4 × 10 = 54,0`. Tres de las cuatro discrepancias percibido/computado superan los 20 puntos; en
las tres prevalece el valor computado y falla el autoinforme del agente, no el enunciado de las tareas.

## Brechas encontradas

| # | Persona o problema afectado | Brecha | Origen | Severidad |
|---|---|---|---|---|
| 1 | Rodrigo · P1 | Ningún enunciado obliga a que exista la decisión clínica y su fundamento: RF-DIA-40 los exige solo si la decisión se registra y RF-DIA-34 declara que su ausencia no condiciona la firma | veredicto-rodrigo | Alta |
| 2 | Rodrigo | Ningún RF le señala, antes de firmar, qué camas de su asignación no llegó a revisar; RF-DIA-34 señala la falta de decisión registrada, que no es lo mismo | veredicto-rodrigo | Media |
| 3 | Rodrigo · P1 · P3 | La nota retenida por RF-IAM-15 no llega nunca al médico entrante: RF-IAM-19 solo la presenta en esa máquina y RF-DIA-32 no comprende lo retenido fuera del episodio | veredicto-rodrigo | Alta |
| 4 | Rodrigo | Nada declara qué ocurre con la entrega y con la asignación médica de camas cuando el turno siguiente no tiene médico asignado a esa unidad | veredicto-rodrigo | Media |
| 5 | Rodrigo · P2 | Ningún enunciado le deja registrar sobre una cama ajena ante un deterioro que nadie escaló todavía: RF-IAM-02 lo rechaza y RF-IAM-09 solo abre la puerta tras la toma del caso | veredicto-rodrigo | Media |
| 6 | Milagros · P3 | Ningún RF declara con qué dispositivo trabaja junto a la cama; RF-IAM-08 y RF-IAM-16 prometen no exigirle apartarse de ella sobre un equipo que el documento no menciona | veredicto-milagros | Alta |
| 7 | Milagros | Ningún RF declara el acto por el que su turno de enfermería queda en curso ni por el que concluye, y de ese estado dependen RF-DIA-30 y RF-IAM-02 | veredicto-milagros | Alta |
| 8 | Milagros · Carmen · P3 | Ningún RF reincorpora a una asignación de cuidado las camas que salen de la suya al declarar (RF-DIA-19), porque RF-DIA-30 solo actúa al iniciar el turno: esas camas dejan de recibir RF-ESC-28, RF-ESC-38 y RF-ESC-41 | veredicto-milagros · veredicto-carmen | Alta |
| 9 | Milagros · P2 | Ningún RF le avisa cuando cambia el responsable clínico de una cama por delegación, revocación o vencimiento: RF-ESC-26, 33, 34 y 42 informan a la jefatura, al titular y al delegado | veredicto-milagros | Media |
| 10 | Milagros · P1 | Ningún RF incluye las marcas vigentes de inestabilidad ni de pendiente crítico entre los componentes de su entrega de enfermería | veredicto-milagros | Media |
| 11 | Milagros · P2 · P3 | Ningún RF le da un canal cuando el escalamiento no alcanza a nadie porque la unidad está sin conexión: RF-ESC-39 presenta la condición y nada declara qué hacer entretanto | veredicto-milagros | Alta |
| 12 | Carmen · P1 | No puede obtener la lista de candidatos elegibles ordenada por rotación mientras arma la propuesta mensual: RF-TUR-03 se dispara al solicitar cobertura | veredicto-carmen | Media |
| 13 | Carmen · P1 | No puede publicar la programación mensual con alguna franja todavía sin nombre: RF-TUR-10 solo declara qué ocurre con una propuesta completa | veredicto-carmen | Media |
| 14 | Carmen · P1 | No puede dirigir una misma solicitud de cobertura a varios candidatos a la vez: RF-TUR-20 la dirige de a uno y RF-TUR-44 exige que ninguna permanezca vigente antes de habilitarla a asignar | veredicto-carmen | Alta |
| 15 | Carmen · P1 | Al vencer una solicitud, RF-TUR-39 y RF-TUR-40 la dejan sin efecto y le avisan, pero ningún RF pasa al siguiente candidato: el ciclo vuelve a empezar por su mano | veredicto-carmen | Media |
| 16 | Carmen · P2 | Nada declara qué ocurre si ella, último eslabón de una cadena agotada, no acusa ni siquiera tras la reiteración de RF-ESC-47 | veredicto-carmen | Media |
| 17 | Carmen | Ningún enunciado declara que el reflejo de RF-TUR-28 y RF-TUR-16 sea imprimible, que es la restricción con la que ella convive | veredicto-carmen | Baja |
| 18 | Carmen | No puede revisar en conjunto los intercambios aplicados bajo una autorización reutilizable durante un periodo: RF-TUR-34 le avisa de a uno | veredicto-carmen | Baja |
| 19 | Aníbal · P2 | Ningún RF le presenta a él de qué camas quedó responsable esa noche en cada sede: RF-ESC-43 se las adjudica y RF-TUR-49 y RF-DIA-46 las presentan a la jefatura | veredicto-anibal | Alta |
| 20 | Aníbal · P2 | No puede delegar cuando es el único médico que la programación vigente asigna a esa unidad en ese intervalo: RF-ESC-30 CA-2 rechaza a cualquier delegado | veredicto-anibal | Alta |
| 21 | Aníbal · P2 | Ningún RF le alcanza el agotamiento de una cadena en la que él era el último integrante: se entera recién con RF-SUP-03 en la mañana | veredicto-anibal | Media |
| 22 | P3 | La persistencia con disponibilidad permanente queda a medias: ningún RF lleva al episodio el registro retenido por RF-IAM-15 cuyo autor no lo reclama en ese mismo equipo, y ninguno declara qué ocurre mientras un escalamiento no alcanza a nadie por falta de conexión | auditoría | Alta |
| 23 | Consistencia | Titularidad inconsistente del acto de consultar una cama: RF-REG-06, RF-REG-10 y RF-DIA-22 admiten a «un profesional» sin restricción; RF-DIA-21, RF-DIA-23, RF-DIA-45 y RF-REG-12 admiten cuatro conjuntos distintos de titulares | auditoría | Media |
| 24 | Consistencia · P3 | La actualización informativa es el único artefacto con contrato abierto: RF-ESC-13 la constituye con tres clases de cambio sin decir «exactamente», y RF-REG-14 y RF-REG-16 le incorporan contenido sin que ningún enunciado declare el conjunto | auditoría | Media |
| 25 | Consistencia · Carmen | RF-SUP-01 habla de «cada cama y dato obligatorio ausente» en plural, contra el glosario, que fija uno solo: el diagnóstico de ese turno | auditoría | Baja |
| 26 | Consistencia · Carmen | RF-TUR-44 y RF-TUR-47 atribuyen a «la jefatura de la unidad» funciones que el glosario reserva a «la coordinadora»: procurar la cobertura de sus franjas y editar la programación vigente | auditoría | Baja |
| 27 | Forma (D3) | RF-REG-14 enuncia dos respuestas —incorporar la solicitud al episodio y a la actualización informativa—, y RF-REG-16 demuestra que la segunda es un RF aparte | control-M/auditoría | Baja |
| 28 | Prioridad (D6) | RF-DIA-19 es MUST sin serlo, y la escala queda invertida: la garantía constitutiva (RF-DIA-30) es SHOULD y la partición optativa es MUST, al revés que en el lado médico (RF-DIA-28, MUST) | auditoría | Media |
| 29 | Prioridad (D6) | RF-IAM-15 es MUST sin serlo: su origen declarado es normativo (SUSALUD) y no una tarea crítica, y su rango es lo que hace dura una retención que dos agentes marcan Estorba | auditoría | Media |

Dos necesidades declaradas por los agentes quedan **refutadas por escrito** en el diagnóstico y no
figuran aquí: la de Carmen sobre qué mide el indicador de cobertura (lo define `docs/GLOSARIO.md`) y
la de Aníbal sobre enterarse de un evento que nadie le escaló (RF-SUP-03 presenta lo ocurrido en las
unidades de su ámbito, que el glosario declara comprensivo de la unidad de su turno).

## Acciones recomendadas (priorizadas)

1. **Obligar a que el razonamiento exista, no solo su formato.** Es la brecha que abre el escenario de
   Rodrigo y la que más pesa: el documento garantiza que toda decisión registrada venga con su
   fundamento, pero admite que un turno entero cierre sin ninguna. Un RF que exija al menos una
   decisión clínica registrada por cama con episodio abierto y por turno cerraría a la vez la brecha 1
   y su tarea 2.
2. **Bajar `X_Rodrigo` de 5 a 0.** Cinco RF le añaden fricción fuera de sus seis tareas y le cuestan
   diez puntos, más que ninguna otra causa de esta corrida. Convertir la consulta de una pantalla en
   confirmación de lectura solo cuando media un acto deliberado (RF-TUR-15, RF-TUR-51), y exigir la
   aceptación del delegado antes de activar la delegación (RF-ESC-07), son cambios acotados de alto
   rendimiento.
3. **Desambiguar los cuatro apoyos que impiden que algún flujo llegue a 4:** RF-ESC-13 (qué obtiene
   quien consulta la actualización informativa), RF-IAM-02 (qué acto pone en curso el turno de
   enfermería), RF-TUR-23 frente a RF-IAM-06 (si elegibilidad y vínculo laboral son la misma cosa) y
   RF-IAM-21 con RF-IAM-22 (qué es y cuándo cesa la identificación ante el dispositivo). Los cuatro
   flujos pasarían de 2 a 4 y D1 subiría ocho puntos sin tocar una sola tarea.
4. **Cerrar el hueco de la asignación de cuidado de enfermería** (brecha 8): elevar RF-DIA-30 a MUST y
   hacerlo actuar durante el turno y no solo al iniciarlo. Es la única brecha que tres garantías de
   tiempo real —RF-ESC-28, RF-ESC-38 y RF-ESC-41— presuponen resuelta.
5. **Recuperar los registros retenidos hacia el episodio** (brechas 3 y 22): un RF que los incorpore
   al episodio cuando su autor no los reclama antes de concluir su turno llevaría P3 de 50 a 100 y
   sumaría 4,2 puntos al global por sí solo.

## Evidencia

`Spec/corridas/2026-08-15-iteracion-10/` — `diagnostico.MD` (veredictos agregados de los 195 RF,
matriz de cobertura, `X_p` RF por RF, cómputo de D1 a D6, contrastes cruzados), los cuatro
`veredicto-‹persona›.MD` y `corrida.json`.
