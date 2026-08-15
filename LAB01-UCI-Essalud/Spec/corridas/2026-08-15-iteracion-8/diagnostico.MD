# Diagnóstico — 2026-08-15-iteracion-8

Evidencia de la agregación. Los 176 veredictos de cada persona viven en su propio archivo
—`veredicto-rodrigo.MD`, `veredicto-milagros.MD`, `veredicto-carmen.MD`, `veredicto-anibal.MD`—,
que es lo que hace diffeable una corrida contra la siguiente. Aquí se agregan los que producen
efecto: todo RF que al menos un agente marcó **Estorba** o **Ambiguo**. Un RF que las cuatro
personas marcan Sirve o Indiferente no mueve ningún puntaje por sí solo; su efecto se lee en la
matriz de cobertura.

## Precondiciones

Cuatro evaluaciones presentes, 176 filas cada una, mismo conjunto y mismo orden de identificadores,
vocabulario cerrado sin veredictos inválidos. Ninguna omisión que contar como Ambiguo. D1 es
computable.

| Persona | Sirve | Indiferente | Estorba | Ambiguo | Total | Percibida |
|---|---:|---:|---:|---:|---:|---:|
| Rodrigo | 48 | 120 | 5 | 3 | 176 | 78 |
| Milagros | 80 | 93 | 1 | 2 | 176 | 85 |
| Carmen | 82 | 90 | 2 | 2 | 176 | 85 |
| Aníbal | 73 | 98 | 2 | 3 | 176 | 88 |

## Veredictos agregados

| RF | Rodrigo | Milagros | Carmen | Aníbal | Efecto en D1 |
|---|---|---|---|---|---|
| RF-TUR-06 | Sirve | Indiferente | **Estorba** | Indiferente | Traza a la tarea 3 de Carmen: no entra en `X_Carmen`; la mantiene en 3 |
| RF-TUR-10 | Indiferente | Indiferente | **Ambiguo** | Indiferente | Traza a la tarea 1 de Carmen: la mantiene en 3 |
| RF-TUR-17 | **Estorba** | Indiferente | Sirve | Indiferente | Fuera de las seis tareas de Rodrigo: `X_Rodrigo` −2 |
| RF-TUR-28 | Indiferente | **Estorba** | **Ambiguo** | Indiferente | Fuera de las seis tareas de Milagros: `X_Milagros` −2. Para Carmen traza a la tarea 1 y sostiene el paso 12 de su flujo |
| RF-TUR-31 | **Estorba** | Indiferente | Sirve | Indiferente | Fuera de las seis tareas de Rodrigo: `X_Rodrigo` −2 |
| RF-TUR-33 | **Estorba** | Indiferente | Sirve | Indiferente | Fuera de las seis tareas de Rodrigo: `X_Rodrigo` −2 |
| RF-DIA-29 | **Estorba** | Sirve | Indiferente | Indiferente | Traza a la tarea 1 de Rodrigo: no entra en `X_Rodrigo` |
| RF-DIA-32 | Sirve | Indiferente | Indiferente | **Ambiguo** | Fuera de las seis tareas de Aníbal en la matriz; roza su tarea 3, que queda en 3 |
| RF-DIA-34 | **Ambiguo** | Indiferente | Sirve | Indiferente | Traza a la tarea 6 de Rodrigo: la mantiene en 3 y apoya dos pasos de su flujo |
| RF-DIA-42 | Sirve | Indiferente | Indiferente | **Ambiguo** | Idéntico a RF-DIA-32 |
| RF-DIA-44 | **Estorba** | Indiferente | Sirve | Indiferente | Fuera de las seis tareas de Rodrigo: `X_Rodrigo` −2 |
| RF-ESC-16 | Indiferente | **Ambiguo** | Indiferente | Sirve | Traza a la tarea 1 de Aníbal (Sirve) y sostiene la rama del flujo de Milagros |
| RF-ESC-25 | Indiferente | Sirve | Indiferente | **Estorba** | Fuera de las seis tareas de Aníbal: `X_Aníbal` −2 |
| RF-ESC-30 | Indiferente | Sirve | Sirve | **Estorba** | Traza a la tarea 5 de Aníbal: no entra en `X_Aníbal`; la mantiene en 3 |
| RF-ESC-32 | Indiferente | Sirve | **Estorba** | Sirve | Fuera de las seis tareas de Carmen: `X_Carmen` −2 |
| RF-REG-02 | **Ambiguo** | Sirve | Indiferente | Sirve | Fuera de las seis tareas de Rodrigo en la matriz; apoya el paso de las 23:50 de su flujo |
| RF-REG-14 | Sirve | **Ambiguo** | Indiferente | Sirve | Fuera de las seis tareas de Milagros en la matriz; sostiene la rama de su flujo |
| RF-IAM-12 | Indiferente | Indiferente | Indiferente | **Ambiguo** | Traza a la tarea 1 de Aníbal, que se sostiene en otros diez RF Sirve: no la baja |
| RF-IAM-15 | **Ambiguo** | Sirve | Sirve | Indiferente | Traza a la tarea 3 de Rodrigo: la mantiene en 3 y apoya el paso de las 23:50 de su flujo |

Nueve de los diez veredictos negativos de Rodrigo caen sobre RF que otra persona marca Sirve. No es
casualidad ni error de un agente: es el conjunto decidiendo tensiones en contra suya. La agregación
lo hace visible y ningún agente por separado podía verlo.

## Matriz de cobertura

`persona × tarea crítica → RF → veredicto → puntos`. La columna RF reproduce la fila de la matriz de
trazabilidad de `ReqFunc.MD`; el veredicto es el del agente de esa persona.

| Persona | Tarea crítica | RF que la cubre | Veredicto | Puntos | Estado |
|---|---|---|---|---:|---|
| Rodrigo | Recibir el handoff estructurado de todas las camas asignadas | DIA-02, 03, 09, 10, 17, 18, 28, 32, 35, 39, 42 Sirve · DIA-29 Estorba | 11 Sirve, 1 Estorba | 3 | Incompleta — hay vista por cama, ordenada y disponible sin el saliente, pero su criterio «el handoff incluye decisiones y su justificación» no queda satisfecho: RF-DIA-02 CA-4 declara la decisión *no registrada* cuando el turno saliente no la registró, y nada obliga a que exista |
| Rodrigo | Consultar la evolución y el diagnóstico del turno anterior | DIA-02, 05, 07, 10, 13, 14, 15, 21, 23, 40, 42, 43 | 12 Sirve | 5 | Cubierta — RF-DIA-05 satisface literalmente «ver qué cambió desde su último contacto», incluido el caso de tres semanas sin pisar la unidad |
| Rodrigo | Registrar nota de evolución y diagnóstico por paciente | DIA-07, 13, 14, 15, 16, 40, IAM-01, 02, 14 Sirve · IAM-09, 10 Indiferente · IAM-15 Ambiguo | 9 Sirve, 1 Ambiguo | 3 | Incompleta — su criterio «registrar le toma menos de lo que le tomaba a mano» no lo sostiene ningún enunciado: RF-DIA-31 abarata la entrega, no el acto de registrar. RF-IAM-15 deja sin decidir qué pasa con la nota retenida |
| Rodrigo | Marcar pacientes inestables o con pendientes críticos | DIA-06, 22, 41 | 3 Sirve | 3 | Incompleta — la marca no trae autor, instante ni motivo, de modo que su objetivo de identificar de inmediato al inestable lo obliga igual a abrir el episodio entero |
| Rodrigo | Consultar resultados de laboratorio e imágenes | REG-06, 10, 12, 14, ESC-29 | 5 Sirve | 5 | Cubierta — la mejor cubierta de las seis según su propio agente; corta la repetición de exámenes |
| Rodrigo | Cerrar y firmar la entrega de turno | DIA-01, 04, 12, 20, 31, 47, TUR-42 Sirve · DIA-24, SUP-01 Indiferente · DIA-34 Ambiguo | 7 Sirve, 1 Ambiguo | 3 | Incompleta — el cierre exige un solo dato por cama, pero RF-DIA-34 no deja saber si a las 07:00 hay una puerta más antes de firmar |
| Milagros | Registrar signos vitales y balance por paciente | REG-01, 02, IAM-01, 08, 16 | 5 Sirve | 5 | Cubierta — registro junto a la cama, identidad en ese mismo dispositivo y preservación sin conexión: sus dos criterios quedan satisfechos |
| Milagros | Escalar un deterioro clínico al médico responsable | ESC-01, 06, 11, 15, 20, 21, 22, 23, 25, 27, 35, 37, 39, 40, 43, 44, DIA-29, IAM-16 | 18 Sirve | 5 | Cubierta — escala sin clasificar, sin apartarse de la cama, con contexto adjunto, y la cadena avanza sola de punta a punta |
| Milagros | Consultar quién está de guardia y su estado de disponibilidad | ESC-08, 27, 32, 35, 41, 43 | 6 Sirve | 3 | Incompleta — la tarea es «quién está de guardia **y cómo contactarlo**»: RF-IAM-11 registra los medios de contacto y ningún enunciado declara que ella pueda consultarlos |
| Milagros | Ver y confirmar indicaciones médicas vigentes | REG-03, 04, 13, ESC-28, 36, 38, IAM-16 Sirve · ESC-13 Indiferente | 7 Sirve | 3 | Incompleta — la solicitud de estudio hecha a distancia no la alcanza junto a la cama y es ella quien toma la muestra a las 03:20 (RF-REG-14) |
| Milagros | Registrar eventos y administración de medicamentos | REG-05, IAM-02, 08, 10, 14, 15, 16 | 7 Sirve | 5 | Cubierta — registra junto a la cama, sobre camas que no son suyas mientras cursa turno, con relevo declarado y autoría cierta en el equipo compartido |
| Milagros | Recibir y entregar el turno de enfermería | DIA-08, 11, 19, 25, 26, 27, 30, 33, 37, 38 | 10 Sirve | 5 | Cubierta — compone y recibe reutilizando lo registrado, cubre el turno concluido sin cerrar y firma el cierre: deja de transcribir a las 06:30 |
| Carmen | Elaborar y publicar la programación mensual de turnos | TUR-04, 09, 11, 27, 46, IAM-13 Sirve · TUR-10, 28 Ambiguo | 6 Sirve, 2 Ambiguo | 3 | Incompleta — RF-TUR-10 solo resuelve la propuesta completa y sin infracciones, y así no publica ella casi ningún mes; ningún enunciado declara la forma imprimible para la pared |
| Carmen | Validar que no existan cruces ni franjas descubiertas | TUR-01, 02, 07, 42, 45, 48, ESC-26, 30, 31, 33, DIA-46 | 11 Sirve | 3 | Incompleta — su criterio «el sistema impide y no solo advierte» queda satisfecho, pero una franja con médico indisponible sin delegado sigue figurando cubierta (RF-ESC-32) y nunca ve el acumulado de horas del mes |
| Carmen | Aprobar o rechazar intercambios y permisos | TUR-12, 13, 17, 21, 22, 29, 30, 31, 32, 33, 34 Sirve · TUR-06 Estorba | 11 Sirve, 1 Estorba | 3 | Incompleta — su dolor documentado «enterarse de un intercambio después de que ocurrió» sigue vivo: RF-TUR-06 aplica el intercambio sin que vea el par concreto y RF-TUR-34 le avisa después |
| Carmen | Reasignar cobertura ante una ausencia imprevista | TUR-03, 05, 18, 19, 20, 25, 26, 35, 36, 37, 38, 39, 40, 41, 43, 44, 47, DIA-36, IAM-13 | 19 Sirve | 3 | Incompleta — el camino existe, pero en su propio escenario, a 27 horas de la franja, RF-TUR-44 puede no habilitarla y la cobertura queda colgada de que un colega acepte |
| Carmen | Monitorear cumplimiento y completitud de entregas de turno | DIA-12, 24, 44, SUP-01 | 4 Sirve | 5 | Cubierta — su criterio «saber qué entregas se cerraron sin diagnóstico» queda mejor que pedido: con RF-DIA-01 no se cierran |
| Carmen | Generar indicadores de cobertura para la Dirección de Red | SUP-02, 05 | 2 Sirve | 5 | Cubierta — su criterio «sin trabajo manual» está enunciado con todas sus letras, y el glosario fija qué mide cada indicador |
| Aníbal | Recibir la alerta de escalamiento con contexto clínico adjunto | ESC-03, 16, 24, IAM-04, 05, 07, 08, 11, 16 Sirve · IAM-12 Ambiguo | 9 Sirve, 1 Ambiguo | 5 | Cubierta — RF-ESC-03 enumera las seis cosas que hoy pide por teléfono y declara no registrado lo que falte; RF-IAM-04 protege el celular personal |
| Aníbal | Confirmar recepción y tomar el caso | ESC-04, 12, 14, 19 | 4 Sirve | 5 | Cubierta — acuse y toma con autoría e instante, y quien escaló lo ve junto a la cama sin consultar |
| Aníbal | Consultar tendencia de signos, ventilación y última evolución | REG-08, DIA-05, 45 | 3 Sirve | 3 | Incompleta — falta la vía de recuperar por consulta lo que decidió el turno diurno cerrado sin entrega: RF-DIA-32 y RF-DIA-42 hablan de un «médico entrante» indefinido para un localizable |
| Aníbal | Registrar la indicación dada de forma remota | REG-07, 09, 11, 13, ESC-37, IAM-02, 05, 07, 08, 09, 16 | 11 Sirve | 5 | Cubierta — verifica identidad en su celular, indica, suspende, pide un estudio, y la enfermera se entera junto a la cama |
| Aníbal | Marcarse temporalmente indisponible y delegar | ESC-07, 17, 32, 34, 35, 40, 42 Sirve · ESC-31 Indiferente · ESC-30 Estorba | 7 Sirve, 1 Estorba | 3 | Incompleta — la mitad de indisponibilidad está entera; la de delegar exige un médico asignado a esa unidad en el intervalo, que en su noche habitual no existe |
| Aníbal | Revisar en la mañana lo ocurrido durante la noche | SUP-03 | 1 Sirve | 5 | Cubierta — su criterio literal: un solo lugar, las dos sedes, con cadena, acuses, tomas y desenlace |

Ninguna de las 24 tareas queda en 0 ni en 1: las 24 obtienen al menos 1 punto, que es la proporción
que D4 recompensa. Diez quedan en 5 y catorce en 3. **Ninguna de las catorce está en 3 por falta de
requerimientos**: en todas hay RF Sirve que las abordan, y lo que falta es un tramo de
comportamiento o un criterio de éxito que el conjunto deja fuera.

### Daño fuera de tarea (`X_p`)

| Persona | Estorba | Traza a alguna de sus seis tareas | No traza — cuenta en `X_p` | `X_p` |
|---|---|---|---|---:|
| Rodrigo | TUR-17, TUR-31, TUR-33, DIA-29, DIA-44 | DIA-29 (tarea 1) | TUR-17, TUR-31, TUR-33, DIA-44 | **4** |
| Milagros | TUR-28 | — | TUR-28 | **1** |
| Carmen | TUR-06, ESC-32 | TUR-06 (tarea 3) | ESC-32 | **1** |
| Aníbal | ESC-25, ESC-30 | ESC-30 (tarea 5) | ESC-25 | **1** |

## Recorrido del escenario clave

| Persona | Recorrido | Apoyo en Ambiguo | Flujo |
|---|---|---|---:|
| Rodrigo | Completo, sin corte, de las 19:00 a las 07:00 | RF-DIA-34 (23:40 y cierre), RF-IAM-15 y RF-REG-02 (registro de las 23:50) | **2** |
| Milagros | Completo, sin corte | RF-REG-14 y RF-ESC-16 en la rama del paso «Resuelve» | **2** |
| Carmen | Completo, sin corte, del viernes 15:40 al sábado 19:00 | RF-TUR-28 en el paso 12 | **2** |
| Aníbal | Completo y en orden, cada paso sostenido en un RF explícito | ninguno de forma necesaria | **4** |

### Milagros — por qué 2 y no 4 ni 0

Su agente declara que el camino principal no se apoya en ningún Ambiguo y sitúa los dos apoyos
ambiguos en una rama, y señala además dos puntos donde «se corta». Las tres lecturas se deciden así:

- **No es 0.** Ninguno de los dos cortes que declara es un paso que ningún RF sostenga. El primero
  —consultar el medio de contacto para llamar por teléfono en vez de esperar— no es un paso del
  escenario sino la práctica manual que el sistema viene a reemplazar: lo que `Personas/Milagros.MD`
  le exige garantizar al sistema es que el escalamiento llegue a alguien que pueda responder, que
  ella vea que fue recibido y que la cadena avance sola, y eso está sostenido por RF-ESC-01,
  RF-ESC-14 y RF-ESC-02. El segundo —la espera con la unidad sin conexión— está sostenido por
  RF-ESC-21 y RF-ESC-39, que ella misma marcó Sirve: el escalamiento se preserva con su instante y
  ella obtiene la condición de no alcanzado sin apartarse de la cama. El flujo se demora, no se
  interrumpe por falta de enunciado.
- **No es 4.** La escala dice «al menos un paso se sostiene en un RF que el agente marcó Ambiguo», y
  no distingue camino principal de rama. Su propio texto lo enuncia como apoyo: «ese paso se apoya
  en RF-REG-14». La rama es el paso «Resuelve» del mismo escenario —el médico que ella despertó
  responde pidiendo un estudio en vez de indicando—, y es ella quien tiene que tomar la muestra a
  las 03:20. RF-ESC-16 agrava lo mismo cuando le caen varios avisos a la vez, que su persona declara
  como condición habitual (0–4 escalamientos por turno, alarmas constantes).
- **Queda en 2.** Completo, con un paso apoyado en un Ambiguo.

### Aníbal — por qué 4 y no 2

Su agente declara que no se apoya de forma necesaria en ningún Ambiguo pero sí en un Estorba,
RF-ESC-25, en el paso 3. La escala enumera exactamente tres estados y solo nombra el Ambiguo:
bajarlo a 2 por un Estorba sería aplicar una penalización que la escala no define. RF-ESC-25
sostiene el paso 3 de forma explícita —dice qué plazo corresponde a la severidad por confirmar—, y
que ese plazo le perjudique ya está cobrado en otro lugar: RF-ESC-25 no traza a ninguna de sus seis
tareas y por eso resta 2 puntos en `X_Aníbal`. El roce con RF-DIA-32 y RF-DIA-42 en el paso 9 no es
un apoyo: ese paso lo sostienen RF-REG-08, RF-DIA-45, RF-DIA-23, RF-REG-03, RF-REG-06, RF-DIA-05 y
RF-REG-10, todos Sirve, y el par ambiguo es una vía alternativa a lo que RF-ESC-03 ya adjuntó.

## Cómputo de D1

```
Rodrigo   Σ tareas = 3+5+3+3+5+3 = 22   X = 4   máx(0, 22 − 2×4)/5 = 14/5 = 2,8   + 2 = 4,8
Milagros  Σ tareas = 5+5+3+3+5+5 = 26   X = 1   máx(0, 26 − 2×1)/5 = 24/5 = 4,8   + 2 = 6,8
Carmen    Σ tareas = 3+3+3+3+5+5 = 22   X = 1   máx(0, 22 − 2×1)/5 = 20/5 = 4,0   + 2 = 6,0
Aníbal    Σ tareas = 5+5+3+5+3+5 = 26   X = 1   máx(0, 26 − 2×1)/5 = 24/5 = 4,8   + 4 = 8,8

promedio = (4,8 + 6,8 + 6,0 + 8,8) / 4 = 26,4 / 4 = 6,6
D1       = 6,6 × 10 = 66,0
```

Ninguna persona tiene sus seis tareas en 0, de modo que el techo de 50 no se activa.

## Cobertura de P1, P2 y P3

| Problema | RF asociados | Comportamiento que lo resuelve | Puntos |
|---|---|---|---:|
| **P1** — El diagnóstico del médico previo debe estar disponible antes del cambio de turno | DIA-01, 02, 03, 07, 10, 12, 17, 20, 24, 31, 32, 42, 47, SUP-01 | Extremo a extremo: RF-DIA-07 lo registra como versión con autoría; RF-DIA-01 impide cerrar la entrega si a alguna cama le falta y RF-DIA-12 dice cuáles; RF-DIA-10 lo entrega al entrante sin depender del saliente y RF-DIA-02 con el estado clínico completo; RF-DIA-03 señala la cama sin diagnóstico antes de la aceptación; RF-DIA-17, 32 y 42 cubren el turno concluido sin cerrar; RF-DIA-47 admite el registro posterior y RF-DIA-24 y RF-SUP-01 lo llevan a la jefatura. Ningún tramo queda sin enunciado, incluido el tramo de falla | **100** |
| **P2** — Un paciente se agrava en turno noche: contactar rápido al médico encargado y manejar su indisponibilidad | ESC-01, 02, 03, 04, 07, 08, 09, 11, 12, 20, 21, 23, 25, 27, 30, 32, 33, 35, 40, 43, 44, IAM-08, 11 | La mitad de «contactar rápido» está resuelta: RF-ESC-23 compone la cadena, RF-ESC-43 y RF-ESC-27 constituyen al responsable, RF-ESC-01 lo alcanza por sus medios vigentes, RF-ESC-03 adjunta el contexto y RF-ESC-02 avanza sola. La mitad de «manejar su indisponibilidad» queda **sin un tramo**: RF-ESC-30 rechaza la delegación cuando ningún médico está asignado a esa unidad en el intervalo —la noche habitual del único localizable de dos UCIs— y ningún RF ofrece otra forma de traspasar la responsabilidad; el sistema solo sabe agotar la cadena hasta la jefatura (RF-ESC-09). Se suma que la condición «asignado sin ningún medio de contacto vigente» se presenta solo al propio profesional (RF-IAM-12), de modo que el agujero por el que hoy no lo ubican sigue abierto para quien tendría que cerrarlo | **50** |
| **P3** — Notificaciones a múltiples médicos y enfermeras, y persistencia del diagnóstico con disponibilidad permanente | ESC-13, 16, 22, 28, 29, 36, 37, 38, 41, REG-01, 02, 03, 04, 05, DIA-07, 37, IAM-01, 16 | Los avisos alcanzan a varios destinatarios a la vez sin consulta previa —RF-ESC-29 al responsable, al que tomó el caso y a la enfermería; RF-ESC-28 y 38 a toda la enfermería con cuidado vigente— y RF-ESC-22 y RF-ESC-37 cierran el circuito hacia quien escaló. La persistencia está resuelta por RF-DIA-07 como versión, RF-REG-02 y RF-ESC-21 sin pérdida ni duplicación ante la caída, y RF-DIA-10 y RF-DIA-17 en la disponibilidad de la entrega. El umbral de disponibilidad permanente es RNF y no se puntúa aquí | **100** |

`D2 = (100 + 50 + 100) / 3 = 83,3`. Ningún problema queda en 0, de modo que el techo de 60 no se
activa.

## Verificabilidad y forma (D3)

Los controles M1, M2 y M3 devuelven vacío sobre los 176 RF: las condiciones 1, 3, 4 y 5 quedan
mecánicamente satisfechas. E2 devuelve vacío: los 176 declaran enunciado, prioridad, persona,
problema y criterios, con lo que la condición 6 se satisface. Ningún criterio de aceptación del
documento contiene dos pares Cuando/Entonces —comprobado sobre las 176 fichas—, con lo que la
condición 7 se satisface. Quedan las condiciones 2 y 8, que exigen lectura:

`D3 = 174 / 176 × 100 = 98,9`.

## Requerimientos mal formados

| ID | Condición de D3 incumplida | Corrección propuesta |
|---|---|---|
| RF-DIA-02 | 8 — un criterio amplía el contrato que el enunciado declara | El enunciado presenta «exactamente el estado clínico de esa cama», cuya composición el glosario cierra en seis componentes que no comprenden un estudio solicitado sin resultado. CA-3 exige que un cultivo pendiente figure en la entrega. O el criterio se reescribe sobre los pendientes críticos marcados, o el estudio solicitado sin resultado se incorpora al término del glosario y el enunciado lo enumera |
| RF-TUR-42 | 2 — enuncia dos respuestas | «Conservar la asignación de esa franja» y «conservar la asignación médica de camas» son dos garantías con vidas propias: la primera mantiene al rotante en la programación vigente, la segunda mantiene las camas a su cargo. Se separan en dos RF, y el segundo cita al primero como puntero |

## Requerimientos mal ubicados

| ID | Por qué no es funcional | Documento que le corresponde |
|---|---|---|
| — | Ninguno. Los RF que invocan un plazo —RF-ESC-06, RF-ESC-25, RF-ESC-02, RF-TUR-26, RF-TUR-39— enuncian el comportamiento y remiten el umbral a `ReqNoFunc.MD`, que es exactamente lo que la rúbrica exige. Ninguno enuncia solo un umbral | — |

## Requerimientos huérfanos

| ID | Por qué no traza a nadie |
|---|---|
| — | Ninguno. Los 176 declaran persona y problema, las cuatro personas nombradas existen y los tres problemas existen: 176/176 en el tramo de 70 puntos de D4 |

## Trazabilidad (D4)

- **70 × 176/176 = 70,0** — todos los RF declaran persona y problema, ambos existentes.
- **30 × 24/24 = 30,0** — las 24 tareas críticas obtuvieron al menos 1 punto en D1.
- **−10 × 1 = −10,0** — una fila de matriz interna no coincide con el cuerpo.

`D4 = 90,0`.

### Fila de matriz desfasada

| Matriz | Fila | Por qué no coincide con el cuerpo |
|---|---|---|
| Matriz de trazabilidad | Milagros · Ver y confirmar indicaciones médicas vigentes | Cita RF-ESC-13, cuyo cuerpo incorpora los cambios a «una única actualización informativa de esa cama **entregada a la consulta del responsable clínico vigente**». Ni el objeto ni el destinatario coinciden: el glosario distingue expresamente la actualización informativa de la indicación, y el destinatario es un médico, no la enfermera. Su propio agente lo marcó Indiferente por esa razón. Se corrige quitando RF-ESC-13 de esa fila |

Las demás matrices coinciden: las tres filas de cobertura de problemas críticos reproducen
exactamente el campo `Problema` de los 176 RF —110 en P1, 59 en P2, 20 en P3, sin sobrantes ni
faltantes—; la distribución de prioridad declara 66/108/2 y el documento tiene 66 MUST, 108 SHOULD y
2 COULD; las 24 filas de trazabilidad citan personas que el cuerpo de cada RF declara; y E3 no
encuentra identificadores inexistentes.

## Tensiones sin decidir

| Tensión | Por qué ningún RF la resuelve |
|---|---|
| — | Ninguna. Las cinco de `Personas/README.md` se deciden en RF y la decisión está enunciada |

Las cinco, con la decisión que las cierra:

| Tensión | RF que la decide | Suma |
|---|---|---:|
| Velocidad frente a completitud del registro | RF-DIA-01 exige un solo dato al cerrar; RF-DIA-31 compone lo demás sin reingreso; RF-DIA-40 pide el fundamento en el acto y no en el cierre; RF-DIA-34 señala sin condicionar; RF-DIA-24 y RF-DIA-44 llevan lo que faltó a la jefatura | 12 |
| Sensibilidad del escalamiento | RF-ESC-11 y RF-ESC-25 dejan escalar ante la duda con el plazo del deterioro inmediato; la selectividad se preserva en la presentación (RF-ESC-16, RF-ESC-24) y no en el plazo | 12 |
| Autonomía de intercambio de turnos | RF-TUR-13 y RF-TUR-06 aplican por anticipado lo que la autorización cubre; RF-TUR-31, 32 y 33 reservan a la coordinadora lo que no cubre; RF-TUR-34 le avisa | 12 |
| Adopción voluntaria | RF-TUR-08 hace del sistema la única fuente editable, y RF-TUR-28 y RF-TUR-16 conceden el reflejo no editable para emplearse fuera de él | 12 |
| Movilidad frente a control de datos | RF-IAM-04 recorta el aviso antes de la identificación; RF-IAM-08 e RF-IAM-16 admiten el dispositivo personal sin equipo institucional; RF-IAM-07 cierra el contexto sin identidad vigente | 12 |

`tensiones_sin_decidir = 0`. Las cuatro coberturas percibidas son 78, 85, 85 y 88: no alcanzan el
90 %, de modo que el techo de 40 por conformidad unánime no se activa. El repositorio tiene glosario,
de modo que el techo de 80 tampoco.

## Consistencia (D5)

- **60/60** por las cinco tensiones decididas.
- **40 − 10 × 5 = 0**, con piso 0, por cinco hallazgos independientes:

| # | Hallazgo | Clase |
|---|---|---|
| 1 | RF-DIA-02 CA-3 exige en la entrega un cultivo pendiente que la composición cerrada de «estado clínico de una cama» no comprende, y el glosario declara que esa composición «no varía» | Vocabulario inconsistente |
| 2 | RF-ESC-16 ordena los avisos clínicos pendientes en cuatro clases que comprenden el escalamiento y la actualización informativa, pero no la tercera clase que el glosario fija —«un hecho de esa cama que reclama su obrar inmediato»—, que es justamente la de RF-ESC-28, RF-ESC-38, RF-ESC-29 y RF-ESC-41 | Vocabulario inconsistente |
| 3 | RF-IAM-01 atribuye todo registro a la identidad verificada vigente del profesional en ese dispositivo; RF-IAM-15 presupone un acto «cuya autoría el sistema atribuye sin haber verificado en ese equipo su identidad», estado que RF-IAM-01 no admite | Contradicción |
| 4 | RF-REG-02 ata la preservación sin conexión al «registro a pie de cama», que el glosario define como la anotación tomada junto a la cama, mientras RF-IAM-16 y RF-REG-01 admiten registros en cualquier dispositivo con identidad vigente: el mismo acto queda dentro o fuera de la garantía según dónde se produzca | Vocabulario inconsistente |
| 5 | RF-DIA-23 enumera como destinatarios «el responsable clínico vigente de esa cama, su delegado activo», cuando el glosario ya constituye al delegado en responsable clínico vigente mientras la delegación alcanza esa cama | Vocabulario inconsistente |

`D5 = 60 + 0 = 60,0`.

## Priorización (D6)

Ningún RF sin prioridad ni con prioridad fuera del vocabulario: E2 verde y la distribución
verificada es 66 MUST, 108 SHOULD y 2 COULD, de modo que `prioridad_uniforme = false` y el techo de
60 no se activa.

| MUST no reservado | Por qué su ausencia no deja descubierta una tarea ni sin resolver un problema |
|---|---|
| RF-DIA-04 | RF-DIA-20 —también MUST— registra la entrega como cerrada cuando el saliente firma. Lo que RF-DIA-04 añade es la autoría y el instante de esa firma: trazabilidad de origen normativo (SUSALUD), no la cobertura de una tarea ni la resolución de P1. Corresponde SHOULD |
| RF-ESC-44 | El último eslabón de la cadena lo garantiza RF-ESC-09, que es SHOULD y ya alcanza a la jefatura vigente. RF-ESC-44 solo habilita a esa jefatura a delegar su responsabilidad; sin él ninguna tarea queda descubierta y P2 conserva su terminal. El gradiente está invertido: la garantía terminal es SHOULD y su delegación optativa es MUST |

`D6 = 100 − 5 × 2 = 90,0`.

Dos SHOULD quedan por debajo de lo que sostienen y conviene revisarlos en la próxima iteración,
aunque la rúbrica no descuente por ello: **RF-DIA-03** es el criterio de éxito literal de Rodrigo
—que el sistema señale la cama sin diagnóstico antes de que él acepte la entrega— y **RF-ESC-09** es
el que impide que un aviso no llegue a nadie.

## Discrepancias entre agente y cómputo

| Persona | Δ | Qué falla: el agente o las tareas críticas |
|---|---:|---|
| Rodrigo | −30 | **El agente, por complaciente en el agregado y honesto en el detalle.** Su prosa declara con precisión cada carencia —la marca sin motivo, la decisión que puede no existir, la nota retenida— y después las resume en un 78 % que ninguna de sus seis tareas sostiene. Prevalece el computado: 48. Cuatro de sus cinco Estorba caen fuera de sus tareas y le cuestan 8 de 30 puntos, y su percibida no los descuenta |
| Milagros | −17 | Dentro del margen de 20. No se reporta discrepancia |
| Carmen | −25 | **El agente.** Marca 82 RF como Sirve —la cifra más alta de las cuatro— y declara seis necesidades no cubiertas que afectan a cuatro de sus seis tareas. La percibida recoge la amplitud de lo que le sirve y no la profundidad de lo que le falta; el cómputo pesa lo segundo. Prevalece el computado: 60 |
| Aníbal | 0 | Coincidencia exacta. Es el único agente cuya autoevaluación resiste el cómputo, y también el único cuyo escenario clave recorre entero sin apoyarse en un ambiguo |

Las tres discrepancias apuntan en la misma dirección —percibida por encima de computada— y ninguna
en la contraria. No hay señal de tareas críticas mal enunciadas en las personas; hay señal de
agentes que resumen mejor de lo que detallan.

## Contrastes cruzados

1. **Discrepancia percibido/computado.** Dos personas superan los 20 puntos de desviación —Rodrigo
   con 30 y Carmen con 25— y en ambos casos falla el agente, no el enunciado de sus tareas críticas.
   Prevalece el valor computado en las dos.
2. **Conformidad unánime.** Las cuatro percibidas son 78, 85, 85 y 88: ninguna alcanza el 90 % y las
   cinco tensiones están decididas, de modo que el techo de 40 sobre D5 no se activa. El conjunto no
   dejó conformes a las cuatro personas a la vez: dejó conforme a Aníbal, razonablemente conformes a
   Milagros y Carmen, y decidió tres tensiones en contra de Rodrigo, que es la única persona cuyo
   puntaje computado cae por debajo de 5.
3. **Necesidad no cubierta sin brecha.** Las veinte necesidades que los cuatro agentes declaran
   figuran como filas 1 a 20 de la tabla de brechas del informe. Dos quedan **refutadas por
   escrito** y no abren brecha: que ningún enunciado declare qué mide cada indicador —el glosario
   define «indicador de cobertura de turnos» como la relación entre franjas descubiertas y
   requeridas, y «indicador de cumplimiento de entrega» como la relación entre entregas cerradas y
   turnos concluidos— y que ninguno defina el cambio del estado de atención de un escalamiento —el
   glosario fija ese estado con exactamente seis valores—.

## Cálculo global

```
D1  66,0 × 0,30 = 19,80
D2  83,3 × 0,25 = 20,83
D3  98,9 × 0,20 = 19,78
D4  90,0 × 0,10 =  9,00
D5  60,0 × 0,10 =  6,00
D6  90,0 × 0,05 =  4,50
                  ─────
                  79,91  →  79,9
```

## Veredicto

| # | Condición | Umbral | Obtenido | Cumple |
|---|---|---:|---:|:---:|
| 1 | Puntaje global | ≥ 80,0 % | 79,9 | ✗ |
| 2 | D1 | ≥ 80,0 | 66,0 | ✗ |
| 3 | Persona más baja | ≥ 7,0/10 | 4,8 | ✗ |
| 4 | D2 | ≥ 80,0 | 83,3 | ✓ |
| 5 | Controles de `verificar.sh` | 9/9 | 9/9 | ✓ |

**FAILED.** El global queda a 0,095 de punto del umbral y no se redondea hacia arriba; aunque lo
cruzara, las condiciones 2 y 3 lo dejarían en FAILED. La corrida no corrige `ReqFunc.MD`: emite su
veredicto y termina.

## Evaluaciones de agente ausentes o inválidas

| Persona | Qué falta |
|---|---|
| — | Ninguna. Las cuatro evaluaciones están presentes, completas sobre los 176 RF y dentro del vocabulario cerrado |
