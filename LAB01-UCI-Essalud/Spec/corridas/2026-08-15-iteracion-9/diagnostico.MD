# Diagnóstico — corrida 2026-08-15-iteracion-9

Evidencia de la medición de `Requirements/ReqFunc.MD` @ `f21fc52` contra `Spec/Eval-Spec.MD` @
`b492237`. El resumen vive en `Spec/Eval-Report.MD`; los números, en `corrida.json`.

## Precondiciones

Las cuatro evaluaciones están presentes, cada una con 177 filas, el mismo conjunto y orden de
identificadores y vocabulario cerrado. La serie DIA no tiene `RF-DIA-44`, retirado. No hay veredictos
ausentes ni inválidos, de modo que D1 es computable y ningún RF se cuenta como Ambiguo por omisión.

| Persona | Sirve | Indiferente | Estorba | Ambiguo | Percibida |
|---|---:|---:|---:|---:|---:|
| Rodrigo | 61 | 109 | 4 | 3 | 85 % |
| Milagros | 77 | 95 | 3 | 2 | 80 % |
| Carmen | 85 | 87 | 1 | 4 | 85 % |
| Aníbal | 75 | 97 | 3 | 2 | 80 % |

## Veredictos agregados

La columna **Efecto en D1** distingue lo que descuenta de lo que solo se anota: un **Estorba** que no
traza a ninguna de las seis tareas de esa persona resta 2 puntos por `X_p`; uno que sí traza no resta
por esa vía, pero pesa en el estado de la tarea; un **Ambiguo** no resta por sí mismo y decide entre
5, 3 y 1 en la tarea que traza, y entre 4 y 2 en el flujo.

| RF | Rodrigo | Milagros | Carmen | Aníbal | Efecto en D1 |
|---|---|---|---|---|---|
| RF-TUR-01 | Sirve | Estorba | Sirve | Sirve | Estorba Milagros fuera de tarea: −2 |
| RF-TUR-02 | Indiferente | Indiferente | Sirve | Indiferente | — |
| RF-TUR-03 | Indiferente | Indiferente | Sirve | Indiferente | — |
| RF-TUR-04 | Indiferente | Sirve | Sirve | Sirve | — |
| RF-TUR-05 | Sirve | Indiferente | Sirve | Sirve | — |
| RF-TUR-06 | Sirve | Indiferente | Sirve | Indiferente | — |
| RF-TUR-07 | Indiferente | Indiferente | Sirve | Indiferente | — |
| RF-TUR-08 | Indiferente | Sirve | Sirve | Sirve | — |
| RF-TUR-09 | Indiferente | Indiferente | Sirve | Indiferente | — |
| RF-TUR-10 | Indiferente | Indiferente | Sirve | Indiferente | — |
| RF-TUR-11 | Indiferente | Indiferente | Sirve | Indiferente | — |
| RF-TUR-12 | Indiferente | Indiferente | Sirve | Indiferente | — |
| RF-TUR-13 | Sirve | Indiferente | Sirve | Indiferente | — |
| RF-TUR-14 | Indiferente | Indiferente | Sirve | Indiferente | — |
| RF-TUR-15 | Indiferente | Indiferente | Sirve | Indiferente | — |
| RF-TUR-16 | Indiferente | Indiferente | Indiferente | Indiferente | — |
| RF-TUR-17 | Estorba | Indiferente | Sirve | Indiferente | Estorba Rodrigo fuera de tarea: −2 |
| RF-TUR-18 | Indiferente | Indiferente | Sirve | Indiferente | — |
| RF-TUR-19 | Indiferente | Sirve | Sirve | Indiferente | — |
| RF-TUR-20 | Sirve | Indiferente | Sirve | Indiferente | — |
| RF-TUR-21 | Indiferente | Indiferente | Sirve | Indiferente | — |
| RF-TUR-22 | Indiferente | Indiferente | Sirve | Indiferente | — |
| RF-TUR-23 | Indiferente | Indiferente | Sirve | Indiferente | — |
| RF-TUR-24 | Indiferente | Indiferente | Sirve | Indiferente | — |
| RF-TUR-25 | Indiferente | Indiferente | Sirve | Indiferente | — |
| RF-TUR-26 | Sirve | Indiferente | Sirve | Sirve | — |
| RF-TUR-27 | Sirve | Indiferente | Sirve | Indiferente | — |
| RF-TUR-28 | Indiferente | Estorba | Sirve | Indiferente | Estorba Milagros fuera de tarea: −2 |
| RF-TUR-29 | Indiferente | Indiferente | Sirve | Indiferente | — |
| RF-TUR-30 | Indiferente | Indiferente | Sirve | Indiferente | — |
| RF-TUR-31 | Estorba | Indiferente | Sirve | Indiferente | Estorba Rodrigo fuera de tarea: −2 |
| RF-TUR-32 | Sirve | Indiferente | Sirve | Indiferente | — |
| RF-TUR-33 | Sirve | Indiferente | Sirve | Indiferente | — |
| RF-TUR-34 | Indiferente | Indiferente | Sirve | Indiferente | — |
| RF-TUR-35 | Sirve | Indiferente | Sirve | Indiferente | — |
| RF-TUR-36 | Indiferente | Indiferente | Sirve | Indiferente | — |
| RF-TUR-37 | Indiferente | Indiferente | Sirve | Indiferente | — |
| RF-TUR-38 | Indiferente | Indiferente | Sirve | Indiferente | — |
| RF-TUR-39 | Indiferente | Indiferente | Sirve | Indiferente | — |
| RF-TUR-40 | Indiferente | Indiferente | Sirve | Indiferente | — |
| RF-TUR-41 | Indiferente | Sirve | Sirve | Sirve | — |
| RF-TUR-42 | Sirve | Sirve | Sirve | Sirve | — |
| RF-TUR-43 | Sirve | Indiferente | Indiferente | Indiferente | — |
| RF-TUR-44 | Indiferente | Indiferente | Sirve | Indiferente | — |
| RF-TUR-45 | Indiferente | Indiferente | Sirve | Indiferente | — |
| RF-TUR-46 | Indiferente | Indiferente | Sirve | Indiferente | — |
| RF-TUR-47 | Indiferente | Indiferente | Sirve | Indiferente | — |
| RF-TUR-48 | Indiferente | Indiferente | Sirve | Indiferente | — |
| RF-TUR-49 | Indiferente | Indiferente | Sirve | Indiferente | — |
| RF-TUR-50 | Sirve | Sirve | Sirve | Sirve | — |
| RF-DIA-01 | Sirve | Indiferente | Sirve | Sirve | — |
| RF-DIA-02 | Sirve | Indiferente | Indiferente | Indiferente | — |
| RF-DIA-03 | Sirve | Indiferente | Indiferente | Indiferente | — |
| RF-DIA-04 | Sirve | Indiferente | Sirve | Indiferente | — |
| RF-DIA-05 | Sirve | Indiferente | Indiferente | Sirve | — |
| RF-DIA-06 | Sirve | Sirve | Indiferente | Indiferente | — |
| RF-DIA-07 | Sirve | Indiferente | Sirve | Sirve | — |
| RF-DIA-08 | Indiferente | Sirve | Indiferente | Indiferente | — |
| RF-DIA-09 | Sirve | Indiferente | Indiferente | Indiferente | — |
| RF-DIA-10 | Sirve | Indiferente | Indiferente | Indiferente | — |
| RF-DIA-11 | Indiferente | Sirve | Indiferente | Indiferente | — |
| RF-DIA-12 | Sirve | Indiferente | Sirve | Indiferente | — |
| RF-DIA-13 | Sirve | Indiferente | Indiferente | Sirve | — |
| RF-DIA-14 | Sirve | Indiferente | Indiferente | Sirve | — |
| RF-DIA-15 | Sirve | Indiferente | Indiferente | Indiferente | — |
| RF-DIA-16 | Sirve | Indiferente | Indiferente | Indiferente | — |
| RF-DIA-17 | Sirve | Indiferente | Indiferente | Indiferente | — |
| RF-DIA-18 | Ambiguo | Sirve | Ambiguo | Indiferente | Ambiguo Rodrigo en tarea; Ambiguo Carmen |
| RF-DIA-19 | Indiferente | Ambiguo | Indiferente | Indiferente | Ambiguo Milagros en tarea |
| RF-DIA-20 | Sirve | Indiferente | Sirve | Indiferente | — |
| RF-DIA-21 | Sirve | Indiferente | Indiferente | Indiferente | — |
| RF-DIA-22 | Sirve | Indiferente | Indiferente | Indiferente | — |
| RF-DIA-23 | Sirve | Sirve | Indiferente | Sirve | — |
| RF-DIA-24 | Estorba | Indiferente | Sirve | Indiferente | Estorba Rodrigo en tarea |
| RF-DIA-25 | Indiferente | Sirve | Indiferente | Indiferente | — |
| RF-DIA-26 | Indiferente | Sirve | Indiferente | Indiferente | — |
| RF-DIA-27 | Indiferente | Sirve | Indiferente | Indiferente | — |
| RF-DIA-28 | Sirve | Indiferente | Sirve | Sirve | — |
| RF-DIA-29 | Sirve | Sirve | Sirve | Indiferente | — |
| RF-DIA-30 | Indiferente | Sirve | Indiferente | Indiferente | — |
| RF-DIA-31 | Sirve | Indiferente | Sirve | Indiferente | — |
| RF-DIA-32 | Sirve | Indiferente | Indiferente | Indiferente | — |
| RF-DIA-33 | Indiferente | Sirve | Indiferente | Indiferente | — |
| RF-DIA-34 | Sirve | Indiferente | Estorba | Indiferente | Estorba Carmen fuera de tarea: −2 |
| RF-DIA-35 | Sirve | Indiferente | Indiferente | Indiferente | — |
| RF-DIA-36 | Indiferente | Sirve | Sirve | Estorba | Estorba Aníbal fuera de tarea: −2 |
| RF-DIA-37 | Indiferente | Sirve | Indiferente | Indiferente | — |
| RF-DIA-38 | Indiferente | Sirve | Indiferente | Indiferente | — |
| RF-DIA-39 | Sirve | Indiferente | Indiferente | Indiferente | — |
| RF-DIA-40 | Sirve | Indiferente | Sirve | Sirve | — |
| RF-DIA-41 | Sirve | Sirve | Indiferente | Indiferente | — |
| RF-DIA-42 | Sirve | Indiferente | Indiferente | Indiferente | — |
| RF-DIA-43 | Sirve | Indiferente | Indiferente | Indiferente | — |
| RF-DIA-45 | Indiferente | Indiferente | Indiferente | Sirve | — |
| RF-DIA-46 | Indiferente | Indiferente | Sirve | Indiferente | — |
| RF-DIA-47 | Sirve | Indiferente | Ambiguo | Indiferente | Ambiguo Carmen |
| RF-ESC-01 | Indiferente | Sirve | Indiferente | Sirve | — |
| RF-ESC-02 | Indiferente | Sirve | Indiferente | Sirve | — |
| RF-ESC-03 | Sirve | Sirve | Indiferente | Sirve | — |
| RF-ESC-04 | Indiferente | Sirve | Indiferente | Sirve | — |
| RF-ESC-05 | Indiferente | Ambiguo | Indiferente | Indiferente | Ambiguo Milagros |
| RF-ESC-06 | Indiferente | Sirve | Indiferente | Sirve | — |
| RF-ESC-07 | Indiferente | Sirve | Sirve | Sirve | — |
| RF-ESC-08 | Indiferente | Sirve | Sirve | Sirve | — |
| RF-ESC-09 | Indiferente | Sirve | Sirve | Sirve | — |
| RF-ESC-10 | Indiferente | Indiferente | Indiferente | Sirve | — |
| RF-ESC-11 | Indiferente | Sirve | Indiferente | Sirve | — |
| RF-ESC-12 | Indiferente | Sirve | Indiferente | Sirve | — |
| RF-ESC-13 | Sirve | Indiferente | Indiferente | Sirve | — |
| RF-ESC-14 | Indiferente | Sirve | Indiferente | Sirve | — |
| RF-ESC-15 | Indiferente | Sirve | Indiferente | Sirve | — |
| RF-ESC-16 | Sirve | Sirve | Indiferente | Sirve | — |
| RF-ESC-17 | Indiferente | Sirve | Indiferente | Sirve | — |
| RF-ESC-18 | Indiferente | Sirve | Indiferente | Sirve | — |
| RF-ESC-19 | Indiferente | Sirve | Indiferente | Sirve | — |
| RF-ESC-20 | Indiferente | Sirve | Indiferente | Indiferente | — |
| RF-ESC-21 | Indiferente | Sirve | Indiferente | Sirve | — |
| RF-ESC-22 | Indiferente | Sirve | Indiferente | Indiferente | — |
| RF-ESC-23 | Indiferente | Sirve | Sirve | Sirve | — |
| RF-ESC-24 | Sirve | Sirve | Indiferente | Sirve | — |
| RF-ESC-25 | Indiferente | Sirve | Indiferente | Estorba | Estorba Aníbal fuera de tarea: −2 |
| RF-ESC-26 | Indiferente | Indiferente | Sirve | Indiferente | — |
| RF-ESC-27 | Sirve | Sirve | Sirve | Sirve | — |
| RF-ESC-28 | Indiferente | Sirve | Indiferente | Sirve | — |
| RF-ESC-29 | Sirve | Sirve | Indiferente | Sirve | — |
| RF-ESC-30 | Indiferente | Sirve | Sirve | Sirve | — |
| RF-ESC-31 | Indiferente | Indiferente | Sirve | Estorba | Estorba Aníbal en tarea |
| RF-ESC-32 | Indiferente | Sirve | Sirve | Sirve | — |
| RF-ESC-33 | Indiferente | Indiferente | Sirve | Sirve | — |
| RF-ESC-34 | Indiferente | Indiferente | Indiferente | Sirve | — |
| RF-ESC-35 | Indiferente | Sirve | Indiferente | Sirve | — |
| RF-ESC-36 | Indiferente | Sirve | Indiferente | Sirve | — |
| RF-ESC-37 | Indiferente | Sirve | Indiferente | Sirve | — |
| RF-ESC-38 | Indiferente | Sirve | Indiferente | Sirve | — |
| RF-ESC-39 | Indiferente | Sirve | Indiferente | Indiferente | — |
| RF-ESC-40 | Indiferente | Sirve | Indiferente | Sirve | — |
| RF-ESC-41 | Indiferente | Sirve | Indiferente | Indiferente | — |
| RF-ESC-42 | Indiferente | Indiferente | Indiferente | Sirve | — |
| RF-ESC-43 | Indiferente | Sirve | Sirve | Sirve | — |
| RF-ESC-44 | Indiferente | Sirve | Sirve | Ambiguo | Ambiguo Aníbal |
| RF-ESC-45 | Indiferente | Sirve | Ambiguo | Sirve | Ambiguo Carmen en tarea |
| RF-REG-01 | Indiferente | Sirve | Indiferente | Sirve | — |
| RF-REG-02 | Sirve | Sirve | Indiferente | Sirve | — |
| RF-REG-03 | Sirve | Sirve | Indiferente | Sirve | — |
| RF-REG-04 | Indiferente | Sirve | Indiferente | Sirve | — |
| RF-REG-05 | Indiferente | Sirve | Indiferente | Sirve | — |
| RF-REG-06 | Ambiguo | Indiferente | Indiferente | Sirve | Ambiguo Rodrigo en tarea |
| RF-REG-07 | Indiferente | Sirve | Indiferente | Sirve | — |
| RF-REG-08 | Sirve | Indiferente | Indiferente | Sirve | — |
| RF-REG-09 | Indiferente | Indiferente | Indiferente | Sirve | — |
| RF-REG-10 | Sirve | Indiferente | Indiferente | Indiferente | — |
| RF-REG-11 | Indiferente | Sirve | Indiferente | Sirve | — |
| RF-REG-12 | Sirve | Indiferente | Indiferente | Indiferente | — |
| RF-REG-13 | Indiferente | Sirve | Indiferente | Sirve | — |
| RF-REG-14 | Sirve | Sirve | Indiferente | Sirve | — |
| RF-IAM-01 | Sirve | Sirve | Sirve | Sirve | — |
| RF-IAM-02 | Sirve | Sirve | Sirve | Sirve | — |
| RF-IAM-03 | Indiferente | Indiferente | Sirve | Indiferente | — |
| RF-IAM-04 | Indiferente | Indiferente | Indiferente | Sirve | — |
| RF-IAM-05 | Indiferente | Indiferente | Indiferente | Ambiguo | Ambiguo Aníbal en tarea |
| RF-IAM-06 | Indiferente | Indiferente | Sirve | Indiferente | — |
| RF-IAM-07 | Indiferente | Indiferente | Indiferente | Sirve | — |
| RF-IAM-08 | Sirve | Sirve | Indiferente | Sirve | — |
| RF-IAM-09 | Indiferente | Sirve | Indiferente | Sirve | — |
| RF-IAM-10 | Indiferente | Sirve | Indiferente | Indiferente | — |
| RF-IAM-11 | Indiferente | Sirve | Sirve | Sirve | — |
| RF-IAM-12 | Indiferente | Indiferente | Sirve | Sirve | — |
| RF-IAM-13 | Indiferente | Indiferente | Sirve | Indiferente | — |
| RF-IAM-14 | Sirve | Sirve | Sirve | Indiferente | — |
| RF-IAM-15 | Ambiguo | Estorba | Sirve | Indiferente | Ambiguo Rodrigo en tarea; Estorba Milagros en tarea |
| RF-IAM-16 | Sirve | Sirve | Indiferente | Sirve | — |
| RF-SUP-01 | Estorba | Indiferente | Sirve | Indiferente | Estorba Rodrigo en tarea |
| RF-SUP-02 | Indiferente | Indiferente | Sirve | Indiferente | — |
| RF-SUP-03 | Indiferente | Sirve | Ambiguo | Sirve | Ambiguo Carmen |
| RF-SUP-04 | Indiferente | Sirve | Indiferente | Indiferente | — |
| RF-SUP-05 | Indiferente | Indiferente | Sirve | Indiferente | — |
| RF-SUP-06 | Indiferente | Indiferente | Sirve | Indiferente | — |

## Matriz de cobertura

24 tareas críticas con su texto literal de `Personas/*.MD`, cruzadas con la matriz de trazabilidad de
`ReqFunc.MD` y con los veredictos. Se cita el RF que sostiene el estado, no la fila entera.

| Persona | Tarea crítica | RF que la cubre | Veredicto | Puntos | Estado |
|---|---|---|---|---:|---|
| Rodrigo | Recibir el handoff estructurado de todas las camas asignadas | RF-DIA-02, 03, 09, 10, 17, 28, 29, 32, 35, 39, 42 · **RF-DIA-18** | Sirve (11) · Ambiguo (1) | 3 | Incompleta — RF-DIA-18, única vía para acotar las camas cuando la franja se comparte, quedó Ambiguo, y ningún enunciado declara cómo devolver las que RF-DIA-28 incorpora |
| Rodrigo | Consultar la evolución y el diagnóstico del turno anterior | RF-DIA-02, 05, 07, 10, 13, 14, 15, 21, 23, 40, 42, 43 | Sirve (12) | 3 | Incompleta — el criterio de éxito «ver qué cambió desde su último contacto» no queda satisfecho: RF-DIA-05 ancla el contacto al último registro y no a la última consulta |
| Rodrigo | Registrar nota de evolución y diagnóstico por paciente | RF-DIA-07, 13, 14, 15, 16, 40, RF-REG-02, RF-IAM-01, 02, 14 · **RF-IAM-15** | Sirve (10) · Indiferente (2) · Ambiguo (1) | 3 | Incompleta — el rescate de lo escrito sin identidad verificada propia se apoya en RF-IAM-15, Ambiguo, y nada declara bajo qué identidad se está escribiendo antes de guardar |
| Rodrigo | Marcar pacientes inestables o con pendientes críticos | RF-DIA-06, 22, 41 | Sirve (3) | 5 | Cubierta — la marca se crea, permanece vigente, se consulta agrupada y su retiro se avisa a quien la dejó |
| Rodrigo | Consultar resultados de laboratorio e imágenes | **RF-REG-06** · RF-REG-10, 12, 14, RF-ESC-29 | Ambiguo (1) · Sirve (4) | 1 | Aparente — el único RF que entrega los resultados del episodio en curso es Ambiguo, y la cobertura depende de un acto —la incorporación del resultado al episodio— que ningún enunciado declara |
| Rodrigo | Cerrar y firmar la entrega de turno | RF-DIA-01, 04, 12, 20, 31, 34, 47, RF-TUR-42, 50 · **RF-DIA-24**, **RF-SUP-01** | Sirve (9) · Estorba (2) | 3 | Incompleta — dos RF implicados llevan Estorba y el cierre posterior al registro tardío de RF-DIA-47 no se declara en el enunciado |
| Milagros | Registrar signos vitales y balance por paciente | RF-REG-01, 02, RF-IAM-01, 08, 16 | Sirve (5) | 5 | Cubierta — registro junto a la cama con una sola mano libre, atribuido, y preservado cuando cae el WiFi |
| Milagros | Escalar un deterioro clínico al médico responsable | RF-ESC-01, 06, 11, 15, 20, 21, 22, 23, 25, 27, 35, 37, 39, 40, 43, 44, RF-DIA-29, RF-IAM-16 | Sirve (18) | 3 | Incompleta — RF-ESC-23 no declara cómo se compone la cadena cuando la cama no tiene responsable, y la cadena agotada muere en la jefatura sin respuesta exigible ni condición presentada a quien escaló |
| Milagros | Consultar quién está de guardia y su estado de disponibilidad | RF-ESC-08, 27, 32, 35, 41, 43 | Sirve (6) | 3 | Incompleta — obtiene quién responde, no cómo se lo alcanza: el medio de contacto vigente no se le presenta y RF-IAM-12 lleva esa carencia al profesional y a la jefatura |
| Milagros | Ver y confirmar indicaciones médicas vigentes | RF-REG-03, 04, 13, RF-ESC-28, 36, 38, RF-IAM-16 | Sirve (7) | 5 | Cubierta — la indicación nueva y su suspensión la alcanzan junto a la cama, las ve vigentes con autor e instante y confirma sin apartarse |
| Milagros | Registrar eventos y administración de medicamentos | RF-REG-05, RF-IAM-02, 08, 10, 14, 16 · **RF-IAM-15** | Sirve (6) · Estorba (1) | 3 | Incompleta — RF-IAM-15 deja su registro fuera del episodio hasta que vuelva a identificarse en ese equipo y ningún RF le presenta esa condición |
| Milagros | Recibir y entregar el turno de enfermería | RF-DIA-08, 11, 25, 26, 27, 30, 33, 37, 38 · **RF-DIA-19** | Sirve (9) · Ambiguo (1) | 3 | Incompleta — no existe para enfermería el equivalente de RF-DIA-09: la aceptación de su entrega por la entrante no se registra |
| Carmen | Elaborar y publicar la programación mensual de turnos | RF-TUR-04, 09, 10, 11, 27, 28, 46, RF-IAM-13 | Sirve (8) | 3 | Incompleta — falta la confirmación de lectura de la publicación mensual; RF-TUR-15 y RF-TUR-25 solo cubren los cambios posteriores |
| Carmen | Validar que no existan cruces ni franjas descubiertas | RF-TUR-01, 02, 07, 42, 45, 48, 50, RF-ESC-26, 30, 31, 33, RF-DIA-46, RF-IAM-12 · **RF-ESC-45** | Sirve (13) · Ambiguo (1) | 3 | Incompleta — RF-TUR-07 solo lista franjas sin profesional asignado: la cubierta por un indisponible declarado le sigue figurando cubierta |
| Carmen | Aprobar o rechazar intercambios y permisos | RF-TUR-06, 12, 13, 17, 21, 22, 29, 30, 31, 32, 33, 34 | Sirve (12) | 5 | Cubierta — el circuito entero, con la decisión de la tensión a su favor: nada se aplica sin autorización suya previa o resolución expresa |
| Carmen | Reasignar cobertura ante una ausencia imprevista | RF-TUR-03, 05, 18, 19, 20, 25, 26, 35, 36, 37, 38, 39, 40, 41, 44, 47, RF-DIA-36, RF-IAM-13 · RF-TUR-43 | Sirve (18) · Indiferente (1) | 5 | Cubierta — el recorrido existe entero; la única reserva del agente es el plazo de RF-TUR-44, que pertenece a `ReqNoFunc.MD` y no se puntúa aquí |
| Carmen | Monitorear cumplimiento y completitud de entregas de turno | RF-DIA-12, RF-SUP-01, RF-DIA-24 | Sirve (3) | 3 | Incompleta — el cumplimiento de las entregas de enfermería no se le presenta, RF-DIA-34 no le traslada el faltante de decisión clínica y RF-DIA-47 no declara qué cambia en RF-SUP-01 |
| Carmen | Generar indicadores de cobertura para la Dirección de Red | RF-SUP-02, 05 | Sirve (2) | 5 | Cubierta — los indicadores salen de los registros vigentes sin transcripción manual |
| Aníbal | Recibir la alerta de escalamiento con contexto clínico adjunto | RF-ESC-03, 16, 24, RF-IAM-04, 07, 08, 11, 12, 16 · **RF-IAM-05** | Sirve (9) · Ambiguo (1) | 3 | Incompleta — la alerta llega completa, pero el paso del aviso al contexto queda sujeto a RF-IAM-05, Ambiguo |
| Aníbal | Confirmar recepción y tomar el caso | RF-ESC-04, 12, 14, 19 | Sirve (4) | 5 | Cubierta — el acuse y la toma quedan registrados y quien escaló los ve de inmediato |
| Aníbal | Consultar tendencia de signos, ventilación y última evolución | RF-REG-08, RF-DIA-05, 45 | Sirve (3) | 5 | Cubierta — seis horas de signos, balance, vasoactivo con dosis, los cinco parámetros del ventilador y la última evolución |
| Aníbal | Registrar la indicación dada de forma remota | RF-REG-07, 09, 11, 13, RF-ESC-37, RF-IAM-02, 07, 08, 09, 16 · RF-IAM-05 | Sirve (10) · Ambiguo (1) | 5 | Cubierta — cubierto de punta a punta incluida la vuelta: la enfermera queda alcanzada junto a la cama y su confirmación de ejecución vuelve al autor |
| Aníbal | Marcarse temporalmente indisponible y delegar | RF-ESC-07, 17, 30, 32, 34, 35, 40, 42, 45 · **RF-ESC-31** | Sirve (9) · Estorba (1) | 3 | Incompleta — RF-ESC-31 permite revocar la delegación sin condicionarla a que el titular haya vuelto a estar disponible |
| Aníbal | Revisar en la mañana lo ocurrido durante la noche | RF-SUP-03 | Sirve (1) | 5 | Cubierta — alcanza las dos unidades que cubrió, con escalamientos, eventos, indicaciones a distancia e ingresos y egresos; el «ámbito de responsabilidad» que define su alcance lo fija el glosario |

**Σ por persona:** Rodrigo 3+3+3+5+1+3 = **18** · Milagros 5+3+3+5+3+3 = **22** · Carmen 3+3+5+5+3+5 = **24** · Aníbal 3+5+5+5+3+5 = **26**.

Ninguna persona tiene tarea alguna en 0, de modo que el techo de 50 sobre D1 no se aplica. Las 24
tareas obtienen al menos 1 punto, dato que alimenta el segundo tramo de D4.

## Daño fuera de tarea — `X_p`

`X_p` cuenta los RF **Estorba** que no trazan a ninguna de las seis tareas de esa persona en la matriz
de trazabilidad de `ReqFunc.MD`. Cada uno resta 2 puntos.

| Persona | RF con Estorba | Cuentan en `X_p` | No cuentan (trazan a una tarea suya) | `X_p` |
|---|---|---|---|---:|
| Rodrigo | RF-TUR-17, RF-TUR-31, RF-DIA-24, RF-SUP-01 | **RF-TUR-17**, **RF-TUR-31** | RF-DIA-24 y RF-SUP-01 (tarea 6, cerrar y firmar) | 2 |
| Milagros | RF-TUR-01, RF-TUR-28, RF-IAM-15 | **RF-TUR-01**, **RF-TUR-28** | RF-IAM-15 (tarea 5, registrar eventos) | 2 |
| Carmen | RF-DIA-34 | **RF-DIA-34** | — | 1 |
| Aníbal | RF-DIA-36, RF-ESC-25, RF-ESC-31 | **RF-DIA-36**, **RF-ESC-25** | RF-ESC-31 (tarea 5, indisponibilidad y delegación) | 2 |

## Recorrido del escenario clave

| Persona | Pasos | Corte | Apoyos en Ambiguo | Flujo |
|---|---:|---|---|---:|
| Rodrigo | 14 | ninguno | RF-REG-06 (paso 7) · RF-DIA-18 (paso 2) y RF-IAM-15 (paso 12), evitables | **2** |
| Milagros | 15 | ninguno | RF-DIA-19 (paso 1) · RF-ESC-05 (paso 8) | **2** |
| Carmen | 11 | ninguno | ninguno en el escenario que su persona describe | **4** |
| Aníbal | 11 | ninguno | RF-IAM-05 (paso 5) | **2** |

**Rodrigo — 2, no 0.** El agente declara «un corte real de contenido en el paso 7». Se comprueba y no
lo es: el paso del escenario que `Personas/Rodrigo.MD` enuncia es literalmente «si hubo un cultivo
pendiente», y eso lo sostiene RF-REG-10, que marcó **Sirve** y que le señala los estudios solicitados
sin resultado con su autoría y su hora. Lo que se apoya en el Ambiguo RF-REG-06 es el resultado del
cultivo si ya volvió, que es una extensión de ese paso y no el paso. Ningún paso queda sin RF que lo
sostenga, de modo que la escala no admite 0; y el apoyo en un Ambiguo dentro de un paso del recorrido
impide el 4. Los otros dos apoyos —RF-DIA-18 y RF-IAM-15— el propio agente los declara evitables en su
escenario (esa noche está solo y se verificó en el equipo en el paso 1), y no habrían cambiado el
resultado: con RF-REG-06 basta para bajar de 4 a 2.

**Milagros — 2.** Recorre los quince pasos sin cortarse. Dos apoyos ambiguos, ninguno de ellos
detiene el flujo: RF-DIA-19 en el paso 1 decide sobre qué camas la alcanzan los avisos junto a la cama
de los pasos 8, 11 y 12, y RF-ESC-05 en el paso 8 es una consulta que RF-ESC-22 y RF-ESC-14 suplen. La
escala no premia que el apoyo sea inocuo: el 4 exige que **ningún** paso se apoye en un Ambiguo.

**Carmen — 4, no 2.** El agente afirma que los pasos 1 a 9 son su escenario propiamente dicho y que la
cola —pasos 10 y 11, apoyados en RF-DIA-18 y RF-DIA-47— cae fuera. Se contrasta contra
`Personas/Carmen.MD`, que es la fuente y manda: su escenario clave es el viernes a las 15:40, el
descanso médico del internista del sábado y la búsqueda de reemplazo, y lo que el sistema debe
garantizar son exactamente tres cosas —«que Carmen vea candidatos elegibles y libres de conflicto, que
el sistema rechace una asignación que genere cruce, y que la publicación del cambio llegue a todos los
afectados con confirmación de lectura»—, las tres resueltas en los pasos 4, 6 y 8. El sábado a las
19:00 aparece en su persona como el desenlace que quiere evitar, no como un tramo que ella recorra: la
prevención ocurre en el paso 6 con RF-TUR-01. Los pasos 10 y 11 son el turno del reemplazo y el cierre
de su entrega —el escenario de Rodrigo, no el de ella—, y puntuarlos aquí la penalizaría por un
recorrido que su persona no describe. Se verificó además que ninguno de los 32 RF citados en los pasos
1 a 9 lleva veredicto Ambiguo de Carmen. **Flujo 4.**

**Aníbal — 2.** Once pasos sin corte. El paso 5 —del aviso al contexto clínico en su celular— se apoya
en RF-IAM-05, Ambiguo, y es el tramo del que dependen los tres minutos con que decide si indica o si
maneja cuarenta. RF-IAM-08 y RF-IAM-07 sostienen el paso; lo que RF-IAM-05 no resuelve es si basta con
abrir el aviso o si antes hay que identificarse ante el dispositivo, estado que RF-IAM-04 presupone y
que ningún enunciado constituye.

## Cómputo de D1 — cada operación

```
Rodrigo   máx(0, 18 − 2 × 2) / 5 + 2 = máx(0, 14) / 5 + 2 = 2,8 + 2 = 4,8
Milagros  máx(0, 22 − 2 × 2) / 5 + 2 = máx(0, 18) / 5 + 2 = 3,6 + 2 = 5,6
Carmen    máx(0, 24 − 2 × 1) / 5 + 4 = máx(0, 22) / 5 + 4 = 4,4 + 4 = 8,4
Aníbal    máx(0, 26 − 2 × 2) / 5 + 2 = máx(0, 22) / 5 + 2 = 4,4 + 2 = 6,4

promedio  (4,8 + 5,6 + 8,4 + 6,4) / 4 = 25,2 / 4 = 6,3
D1        6,3 × 10 = 63,0
```

## Cobertura de P1, P2 y P3

| Problema | RF asociados | Comportamiento que lo resuelve | Puntos |
|---|---|---|---:|
| **P1** Rotación de doctor | 110 RF; el núcleo son RF-DIA-07, 13, 40 (registro con fundamento exigido en el acto), RF-DIA-01 y 12 (el cierre se impide y se dice qué falta), RF-DIA-20 y 04 (la entrega cerrada y su firma), RF-DIA-10 y 02 (el entrante la obtiene sin el saliente presente), RF-DIA-03 (se le señala la cama sin diagnóstico antes de aceptar), RF-DIA-17, 32 y 42 (qué obtiene si el turno anterior no cerró), RF-DIA-47 (registro tardío), RF-SUP-01 y RF-DIA-24 (supervisión) | El diagnóstico existe porque el cierre no ocurre sin él, y está disponible antes del cambio de turno sin depender de nadie. El caso degradado también está resuelto: del turno que no cerró entrega el entrante obtiene lo que sí se registró, con cada componente ausente declarado no registrado. Registrado el faltante por RF-DIA-47, la firma produce el cierre por RF-DIA-20, y el glosario admite ese registro «después de concluido este mientras su entrega no esté cerrada». No queda tramo sin RF | **100** |
| **P2** Medianoche | 60 RF; RF-ESC-20, 11, 25 (escala junto a la cama sin clasificar y sin castigo de plazo), RF-ESC-23, 43, 27, 35 (la cadena y quién la encabeza), RF-ESC-01, 21, 40 (alcanza, sobrevive a la desconexión, saltea al indisponible), RF-ESC-03 y RF-IAM-04 (el contexto y lo que se ve antes de identificarse), RF-ESC-04, 12, 14 (acuse, toma y su devolución), RF-ESC-02, 09, 18 (avance solo, agotamiento, registro), RF-ESC-07, 30, 32, 33, 34, 42, 45, 17 (indisponibilidad y delegación), RF-REG-07, 11, 13 (conducta remota) | Las dos mitades del enunciado están resueltas de extremo a extremo. «Contactar rápido al médico encargado»: la cadena se compone sola, siempre tiene cabeza —RF-ESC-43 constituye responsable al localizable de la franja aunque ninguna asignación médica comprenda la cama— y avanza sin que la enfermera intervenga. «Manejar su indisponibilidad»: se declara con instante de término, se delega solo en quien la programación asigna a esa unidad, el rechazo dice quiénes sí, la cadena saltea al indisponible, la jefatura se entera y el sistema sale a buscar cobertura | **100** |
| **P3** Actualizaciones en tiempo real | 21 RF; RF-ESC-28, 36, 38, 29, 41, 22 (alcance junto a la cama sin consulta previa), RF-ESC-13 y 16 (agrupación y orden), RF-REG-01 a 05 y 13, RF-REG-02 y RF-ESC-21 (preservación sin conexión), RF-IAM-15 | La mitad de las notificaciones a múltiples médicos y enfermeras está resuelta: cinco clases de aviso ordenadas, el propio aviso declara a cuál corresponde, y cuatro hechos alcanzan sin consulta previa a quien debe obrar. La mitad de la persistencia deja **dos tramos sin RF**. Primero: ningún enunciado declara el acto por el que un resultado de laboratorio o de imágenes se incorpora al episodio, y de ese acto cuelgan RF-REG-06 («los disponibles»), RF-REG-10 («cuyo resultado aún no incorpora») y RF-ESC-29 («cuando se incorpora»). Segundo: RF-IAM-15 deja un registro clínico —una nota de evolución, según su propio CA-1— fuera del episodio por tiempo indefinido, sin que ningún RF presente esa condición a su autor ni a nadie más, de modo que lo registrado existe pero no está disponible | **50** |

`D2 = (100 + 100 + 50) / 3 = 83,3`. Ningún problema queda en 0, de modo que el techo de 60 no se
aplica.

## D3 — las ocho condiciones sobre los 177 RF

Los controles mecánicos M1, M2 y M3 devuelven vacío, de modo que las condiciones 1, 3, 4 y 5 —patrón
EARS, sistema como sujeto del DEBE, garantía y no mecanismo, ausencia de interfaz y tecnología— se
cumplen en los 177. E2 devuelve vacío: los 177 declaran enunciado, prioridad, persona, problema y
criterios, de modo que la condición 6 se cumple. La condición 7 se verificó enunciado por enunciado:
ningún criterio de aceptación del documento contiene más de un par Cuando/Entonces.

Las condiciones 2 y 8 se auditaron a mano. La 8 no produce hallazgos: los criterios que parecían
ampliar el contrato lo demuestran, porque `docs/GLOSARIO.md` cierra los términos de los que dependen
—«estado clínico de una cama» como conjunto cerrado de seis componentes con el ausente en condición de
no registrado (RF-DIA-02 CA-4, RF-DIA-32 CA-1), «último contacto» con sus dos casos de defecto
(RF-DIA-05 CA-2 y CA-3), «cruce de turnos» excluyendo la guardia localizable (RF-TUR-01 CA-2)—.

| ID | Condición de D3 incumplida | Corrección propuesta |
|---|---|---|
| RF-IAM-12 | **2** — dos disparadores pegados a una respuesta. «DEBE presentar esa condición a ese profesional **cuando emplee el sistema** y a la jefatura de esa unidad»: son dos momentos distintos, y CA-1 y CA-2 lo confirman con dos Cuando distintos —«cuando emplea el sistema» y «cuando la programación vigente le asigna esa guardia»— | Partir en dos RF, uno por destinatario y disparador |
| RF-IAM-15 | **2** — dos respuestas con disparadores distintos. «DEBE preservarlo … fuera del episodio hasta incorporarlo a él … **cuando ese profesional verifique en ese equipo su identidad**»: preservar rige desde la producción; incorporar se dispara con un acto voluntario posterior, y CA-1 y CA-2 los demuestran por separado. No es el caso de RF-REG-02 ni de RF-ESC-21, cuya incorporación se dispara con el mismo hecho que cierra la preservación | Separar la preservación de la incorporación en dos RF |
| RF-REG-14 | **2** — segunda respuesta en cláusula relativa. «DEBE incorporar esa solicitud … a ese episodio y a la actualización informativa de esa cama, **que alcanza junto a la cama a las profesionales de enfermería con asignación de cuidado de enfermería vigente sobre ella**», y CA-3 demuestra ese alcance como resultado propio | Suprimir la cláusula: el alcance ya es el contrato de RF-ESC-36 |

`D3 = 174 / 177 × 100 = 98,3`.

## D4 — Trazabilidad

- **70 puntos por la proporción de RF que declaran persona y problema, ambos existentes.** Los 177
  declaran ambos campos; las personas citadas son las cuatro modeladas y los problemas, P1, P2 y P3.
  Ningún huérfano. `177/177 × 70 = 70,0`.
- **30 puntos por la proporción de las 24 tareas críticas con al menos 1 punto en D1.** Ninguna quedó
  en 0; la más baja es la quinta de Rodrigo, con 1. `24/24 × 30 = 30,0`.
- **Filas de matriz desfasadas: 0.** Se comprobó fila por fila que cada RF citado en la matriz de
  trazabilidad (24 filas) y en la de cobertura de criterios de éxito (23 filas) declara en su cuerpo
  la persona de esa fila, y que la matriz de cobertura de problemas críticos coincide exactamente con
  el campo `Problema` de los 177: P1 110, P2 60 y P3 21, sin sobrantes ni faltantes en ninguno de los
  tres sentidos. La distribución de prioridad declarada —65 MUST, 110 SHOULD, 2 COULD, 36,7 %, 62,1 %
  y 1,1 %— coincide con el recuento del cuerpo. Los 24 textos de tarea coinciden literalmente con
  `Personas/*.MD`.

`D4 = 70 + 30 − 0 = 100,0`.

## D5 — Consistencia y tensiones decididas

### Tensiones sin decidir

| Tensión | Por qué ningún RF la resuelve |
|---|---|
| — | Ninguna. Las cinco de `Personas/README.md` están decididas en RF, con la decisión enunciada |

Las cinco suman 60 de 60. La comprobación no es que la tabla exista, sino que cada decisión se
sostenga en el articulado y que alguien haya perdido: **cada una de las cinco deja a una persona
marcando Estorba o resistiendo el resultado**, que es la señal de que se decidió en lugar de
esquivarse. Velocidad frente a completitud (RF-DIA-01, 31, 34, 40, 47): Carmen marca **Estorba** el
RF-DIA-34 que protege a Rodrigo. Sensibilidad del escalamiento (RF-ESC-11, 24, 25, 16): Aníbal marca
**Estorba** el RF-ESC-25 que protege a Milagros. Autonomía de intercambio (RF-TUR-06, 13, 17, 31):
Rodrigo marca **Estorba** RF-TUR-17 y RF-TUR-31, que dan la razón a Carmen. Adopción voluntaria
(RF-TUR-08, 16, 27, 28): Milagros marca **Estorba** el reflejo impreso de RF-TUR-28. Movilidad frente
a control de datos (RF-IAM-04, 05, 07, 08, 16): Aníbal marca **Ambiguo** RF-IAM-05, justo donde la
norma le cobra el precio. Ninguna cobertura percibida alcanza el 90 %, de modo que el techo de 40 por
conformidad unánime no se activa; el repositorio tiene glosario, de modo que el techo de 80 tampoco.

### Segundo tramo — 40 menos 10 por hallazgo independiente

| # | Hallazgo | Categoría | Resta |
|---|---|---|---:|
| 1 | **Duplicado encubierto.** RF-REG-14 reenuncia el contrato de RF-ESC-36 —«alcanza junto a la cama a las profesionales de enfermería con asignación de cuidado de enfermería vigente sobre ella»— y su CA-3 lo demuestra por segunda vez. Dos copias de una regla se corrigen por separado hasta contradecirse | duplicado | −10 |
| 2 | **Vocabulario inconsistente en el rol supervisor.** El documento lo designa de tres formas: «la coordinadora» (70 apariciones, RF-TUR-* y RF-SUP-05), «el coordinador» (2, RF-SUP-01 y RF-SUP-04) y «la jefatura de la unidad» (38, RF-TUR-44 a 49, RF-DIA-24 y 46, RF-ESC-26, 31 y 33, RF-SUP-06). El glosario fija solo la tercera; nada declara si las tres denotan el mismo rol, y los actos de supervisión se reparten entre ellas sin regla —RF-TUR-46 la llama jefatura para definir franjas y RF-TUR-09 coordinadora para programarlas sobre esas mismas franjas— | vocabulario | −10 |
| 3 | **Contrato abierto, único en el documento.** RF-REG-06 presenta «los resultados de laboratorio e imágenes **disponibles** del episodio»: sin «exactamente», sin enumeración y con un adjetivo que el glosario no fija, mientras sus pares cierran el suyo (RF-REG-03 «exactamente las vigentes», RF-REG-08 y RF-REG-10 «exactamente…»). De ese contrato abierto depende una tarea crítica entera y es la razón de que su agente lo marcara Ambiguo | vocabulario · contrato | −10 |

`40 − 30 = 10`. `D5 = 60 + 10 = 70,0`.

No se computa un cuarto hallazgo por la composición indeterminada entre RF-DIA-18/RF-DIA-19 y
RF-DIA-28/RF-DIA-30: leídos al pie de la letra no se contradicen —«incorporar exactamente las camas
declaradas» dice qué se incorpora, no en qué queda la asignación—, y lo que hay es una incompletitud,
ya penalizada en D1 y registrada como brecha 4. Tampoco se computa ningún requerimiento mal ubicado:
no hay RNF alojado en `ReqFunc.MD`, y los umbrales que los enunciados invocan —«dentro del plazo
definido para la severidad», «el horizonte de urgencia»— quedan expresamente remitidos a
`ReqNoFunc.MD` en la cabecera del documento.

## D6 — Priorización realista

Los 177 declaran prioridad y los tres valores pertenecen al vocabulario MUST/SHOULD/COULD: **0
descuentos** por ese concepto. La distribución es 65 MUST, 110 SHOULD y 2 COULD, de modo que
`prioridad_uniforme` es `false` y el techo de 60 no se aplica.

Se auditaron los 65 MUST contra el criterio de reserva —su ausencia deja sin resolver un problema
crítico o descubierta una tarea crítica—. Dos no lo pasan:

| ID | Por qué no está reservado | Resta |
|---|---|---:|
| RF-ESC-38 | Alcance junto a la cama de la suspensión de una indicación. Ausente, la cuarta tarea crítica de Milagros sigue cubierta por RF-REG-03, RF-REG-04 y RF-REG-13 desde el dispositivo que ya emplea junto a la cama (RF-IAM-16), y P3 sigue resuelto por los otros cuatro alcances sin consulta previa. La asimetría lo delata: RF-ESC-29, que alcanza un resultado crítico, es SHOULD | −5 |
| RF-ESC-45 | Solicitud de cobertura ante una indisponibilidad declarada sin delegado. Ausente, la quinta tarea crítica de Aníbal sigue cubierta por RF-ESC-32, 07, 30, 33, 34, 35 y 42, y el hueco de cobertura llega igualmente a la jefatura por RF-ESC-33, que lo resuelve por la vía de RF-TUR-03, 20 y 44. Sus seis RF hermanos del mismo circuito son todos SHOULD | −5 |

No se descuenta por RF-DIA-18 ni RF-DIA-19 pese a que RF-DIA-28 y RF-DIA-30 cubren la cama sin
responsable: son los actos que constituyen la asignación médica y la de cuidado, conceptos de los que
dependen RF-DIA-01, 02, 03, 12, 20, 21, 31, 34, 35 y 39, RF-ESC-27, 28, 36, 38 y 41 y RF-IAM-02.
Tampoco por RF-REG-14: sin él ninguna solicitud de estudio existe nunca, y RF-REG-10 y RF-ESC-29 se
quedan sin disparador.

`D6 = 100 − 0 − 5 × 2 = 90,0`.

## Contrastes cruzados

### Discrepancias entre agente y cómputo

| Persona | Δ | Qué falla: el agente o las tareas críticas |
|---|---:|---|
| Rodrigo | 48 vs 85 → **−37** | **El agente.** Sus tareas críticas están bien enunciadas —son acciones observables, con frecuencia y criticidad— y su propio texto documenta una carencia declarada en cinco de las seis. El 85 % lee la densidad de *Sirve* del documento entero (61 de 177) y el alivio frente al papel, no la completitud de lo suyo; y no descuenta los dos Estorba que caen fuera de sus tareas, RF-TUR-17 y RF-TUR-31, que él mismo describe como la razón por la que seguirá arreglando cambios de turno por WhatsApp. Prevalece el computado |
| Milagros | 56 vs 80 → **−24** | **El agente**, por la misma vía: 77 *Sirve* sobre 177 sostienen la impresión global, mientras cuatro de sus seis tareas cierran con una necesidad no cubierta declarada por ella misma, y RF-TUR-01 y RF-TUR-28 —Estorba fuera de sus tareas— no entran en su porcentaje. Prevalece el computado |
| Carmen | 84 vs 85 → −1 | Dentro de tolerancia. Su autoinforme y el cómputo miden lo mismo |
| Aníbal | 64 vs 80 → −16 | Dentro de tolerancia |

### Conformidad unánime

No se activa. Las cuatro percibidas son 85, 80, 85 y 80: ninguna alcanza el 90 %, y además no hay
tensión sin decidir, de modo que las dos condiciones del techo de 40 sobre D5 fallan por separado. La
comprobación deja además un resultado con signo positivo: los cuatro agentes **no** quedan conformes a
la vez —hay siete veredictos Estorba y once Ambiguo repartidos entre los cuatro, y cada tensión deja a
alguien perdiendo—, que es lo contrario del patrón que `Personas/README.md` advierte.

### Necesidad no cubierta sin brecha

Las 18 necesidades no cubiertas que los cuatro agentes declaran están todas resueltas: 14 figuran como
filas de la tabla de brechas de `Spec/Eval-Report.MD` y 4 quedan refutadas por escrito más abajo. La
que Milagros declara expresamente no reclamar —el umbral de 30 segundos, el número de pasos y la forma
del aviso en una unidad con ruido de alarmas— pertenece a `ReqNoFunc.MD` y no es brecha de este
documento.

## Necesidades refutadas

| Persona | Necesidad declarada | Por qué no es brecha |
|---|---|---|
| Rodrigo | «Registrado después del turno el diagnóstico que faltaba según RF-DIA-47, ningún enunciado declara que yo pueda entonces cerrar y firmar esa entrega» | RF-DIA-20 no restringe la firma al transcurso del turno: «CUANDO el médico saliente firma una entrega cuyas camas cuentan todas con diagnóstico de ese turno, el sistema DEBE registrar esa entrega como entrega cerrada». El glosario admite el diagnóstico de ese turno «registrada dentro de ese turno o después de concluido este mientras su entrega no esté cerrada». Registrado el faltante, la firma produce el cierre |
| Rodrigo | «RF-DIA-02 promete el estado clínico sin enumerarlo en el enunciado, mientras RF-ESC-03 sí enumera» | El glosario cierra «estado clínico de una cama» como conjunto cerrado de seis componentes cuya composición no varía, con el componente ausente integrado en condición de no registrado. La entrega no puede llegarle más pobre que un escalamiento: llega con otro conjunto, igualmente cerrado |
| Aníbal | «Lo que define el alcance de RF-SUP-03 —su ámbito de responsabilidad— no lo constituye ningún enunciado de este documento» | Lo constituye el glosario, que `ReqFunc.MD` declara vinculante en su cabecera: el ámbito resulta de los turnos, asignaciones médicas, asignaciones de cuidado, delegaciones activas y responsabilidad de jefatura vigentes en el periodo, y un turno comprende la unidad de su franja aunque no comprenda camas — que es exactamente su caso de localizable sin asignación médica, el que CA-1 demuestra |
| Carmen | RF-SUP-03 Ambiguo: «no declara si mi jefatura constituye un ámbito de responsabilidad» | La misma entrada del glosario nombra la responsabilidad de jefatura entre los títulos que componen el ámbito |

## Requerimientos huérfanos

| ID | Por qué no traza a nadie |
|---|---|
| — | Ninguno. Los 177 declaran persona y problema, ambos existentes |

## Requerimientos mal ubicados

| ID | Por qué no es funcional | Documento que le corresponde |
|---|---|---|
| — | Ninguno. Ningún RF enuncia solo un umbral; los plazos que invocan quedan remitidos a `ReqNoFunc.MD` en la cabecera del documento | — |

## Evaluaciones de agente ausentes o inválidas

| Persona | Qué falta |
|---|---|
| — | Ninguna. Las cuatro presentes, con 177 filas cada una y vocabulario cerrado |

## Cálculo global y veredicto

```
D1 63,0 × 0,30 = 18,900
D2 83,3 × 0,25 = 20,825
D3 98,3 × 0,20 = 19,660
D4 100,0 × 0,10 = 10,000
D5 70,0 × 0,10 =  7,000
D6 90,0 × 0,05 =  4,500
                 ───────
Global           80,885 → 80,9 %
```

| # | Condición | Umbral | Obtenido | Cumple |
|---|---|---:|---:|:---:|
| 1 | Puntaje global | ≥ 80,0 % | 80,9 | sí |
| 2 | D1 | ≥ 80,0 | 63,0 | **no** |
| 3 | Persona más baja | ≥ 7,0/10 | 4,8 | **no** |
| 4 | D2 | ≥ 80,0 | 83,3 | sí |
| 5 | Controles de `verificar.sh` | 9/9 | 9/9 | sí |

**FAILED.** El global cruza su umbral y no basta: fallan la segunda y la tercera condición, y las
cinco se exigen a la vez. El 80,9 % lo sostienen las tres dimensiones de auditoría —D3, D4 y D6, que
pesan 35 % y promedian 96,1—, es decir, la forma del documento. La dimensión que mide si los
requerimientos satisfacen a las personas que van a usar el sistema pesa 30 % y vale 63,0, y la persona
ancla del problema que el enunciado marca como causa raíz cierra en 4,8 sobre 10. Un porcentaje que
sube mientras D1 baja está midiendo la redacción, no el producto; el veredicto existe para no
confundir las dos cosas.
