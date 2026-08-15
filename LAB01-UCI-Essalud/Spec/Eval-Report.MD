# Evaluación de Requerimientos Funcionales — Sistema UCI Essalud

| | |
|---|---|
| Corrida | 2026-08-15-iteracion-7 |
| Rama | `eval/iteracion-7` |
| Modelo | claude-opus-5 |
| Evaluado | `Requirements/ReqFunc.MD` @ `c923c7f` |
| Rúbrica | `Spec/Eval-Spec.MD` @ `b492237` |
| Personas | `Personas/` @ `6340172` |
| Agentes | `Agents/` @ `34877c7` |
| Instrumento modificado | no |

## Puntaje global: 77,8 %

| Dimensión | Puntaje | Peso | Aporte |
|---|---:|---:|---:|
| D1 Satisfacción de las personas | 60,0 | 30 % | 18,00 |
| D2 Cobertura de problemas críticos | 83,3 | 25 % | 20,83 |
| D3 Verificabilidad y forma | 96,3 | 20 % | 19,26 |
| D4 Trazabilidad | 100,0 | 10 % | 10,00 |
| D5 Consistencia y tensiones | 60,0 | 10 % | 6,00 |
| D6 Priorización | 75,0 | 5 % | 3,75 |
| **Suma de aportes** | | | **77,84 → 77,8** |

## Veredicto: FAILED

| # | Condición | Umbral | Obtenido | Cumple |
|---|---|---:|---:|:---:|
| 1 | Puntaje global | ≥ 80,0 % | 77,8 % | no |
| 2 | D1 | ≥ 80,0 | 60,0 | no |
| 3 | Persona más baja | ≥ 7,0/10 | 5,6 (Rodrigo y Carmen) | no |
| 4 | D2 | ≥ 80,0 | 83,3 | sí |
| 5 | Controles de `scripts/verificar.sh` | 9/9 | 9/9 | sí |

Fallan tres de las cinco. El documento está bien formado y bien trazado —D3 y D4 son las dimensiones
altas— y sigue sin satisfacer a las personas: ninguna de las cuatro alcanza 7,0/10 y ninguna de las 24
tareas críticas llega a 5 por la misma causa repetida, que es la ausencia de garantía sobre el
contenido que cada tarea necesita.

## Puntajes por persona

| Persona | Tareas /30 | Estorba fuera | Necesidades /6 | Flujo /4 | Puntaje /10 | Percibida | Δ |
|---|---:|---:|---:|---:|---:|---:|---:|
| Rodrigo | 22 | 2 | 3,6 | 2 | 5,6 | 75 | −19 |
| Milagros | 20 | 0 | 4,0 | 2 | 6,0 | 85 | −25 |
| Carmen | 20 | 1 | 3,6 | 2 | 5,6 | 80 | −24 |
| Aníbal | 26 | 1 | 4,8 | 2 | 6,8 | 85 | −17 |
| **PROMEDIO** | **22,0** | **1,0** | **4,0** | **2,0** | **6,0** | **81,3** | **−21,3** |

`Puntaje_p = máx(0, Σ tareas_p − 2 × X_p) / 5 + Flujo_p`; `D1 = promedio × 10 = 60,0`.
Milagros (Δ −25) y Carmen (Δ −24) superan los 20 puntos de desviación: en ambos casos falla el agente,
no el enunciado de las tareas críticas. Detalle en `Spec/corridas/2026-08-15-iteracion-7/diagnostico.MD`.

## Brechas encontradas

| # | Persona o problema afectado | Brecha | Origen | Severidad |
|---|---|---|---|---|
| 1 | Rodrigo · P1 | El contexto de la entrega puede llegar entero declarado «no registrado»: solo el diagnóstico condiciona el cierre y ningún RF obliga a registrar decisión, esquema o estado de la familia | veredicto-rodrigo | Alta |
| 2 | Rodrigo, Carmen · P1 | Una cama puede llegar sin diagnóstico del turno anterior: `RF-DIA-24` admite expresamente que un turno concluya sin entrega cerrada y `RF-DIA-01` solo bloquea el cierre | veredicto-rodrigo | Alta |
| 3 | P1 | `RF-DIA-01` no alcanza al turno médico sin asignación médica vigente: una noche cubierta solo por guardia localizable puede transcurrir sin ningún diagnóstico exigible | auditoría | Alta |
| 4 | Rodrigo | Ningún enunciado exige verificar identidad antes de registrar en el equipo compartido; `RF-IAM-01` atribuye a la identidad verificada, pero no la reclama | veredicto-rodrigo | Alta |
| 5 | Rodrigo | Ningún RF constituye la solicitud de un estudio, de modo que el señalamiento de `RF-REG-10` puede quedar vacío para todo cultivo pedido como se pide hoy | veredicto-rodrigo | Media |
| 6 | Milagros · P2 | `RF-ESC-08` no declara que la consulta de la cobertura clínica pueda hacerse junto a la cama, a diferencia de `RF-ESC-20` y `RF-REG-01`; es la consulta que hace ante cada escalamiento | veredicto-milagros | Alta |
| 7 | Milagros | La indisponibilidad declarada sin delegado solo alcanza a la jefatura (`RF-ESC-33`), que de madrugada no está en la unidad | veredicto-milagros | Media |
| 8 | Milagros, Carmen | La ausencia de medio de contacto vigente solo se le presenta al propio profesional (`RF-IAM-12`); ni quien va a escalar hacia él ni quien lo asignó se enteran | veredicto-milagros, veredicto-carmen | Media |
| 9 | Milagros | Ningún enunciado declara el dispositivo con el que ella trabaja junto a la cama; `RF-IAM-08` habla del dispositivo personal sin decir si la alcanza | veredicto-milagros | Alta |
| 10 | Milagros | `RF-DIA-30` la carga sin límite con todas las camas sin asignación de cuidado y `RF-DIA-37` deja cada cama en manos de la última que la declara: los dos que marcó Estorba caen dentro de su tarea 6 | veredicto-milagros | Alta |
| 11 | Milagros | No existe para enfermería el orden de camas al iniciar el turno que `RF-DIA-39` le da al médico | veredicto-milagros | Baja |
| 12 | Milagros · P3 | `RF-ESC-16` ordena los avisos de «un destinatario» sin declarar si la enfermera es una de ellas | veredicto-milagros | Baja |
| 13 | Carmen | Ningún enunciado declara el formato imprimible del reflejo; `RF-TUR-28` entrega contenido e instante y la restricción de la persona es explícita | veredicto-carmen | Media |
| 14 | Carmen | No hay forma de ver las horas acumuladas y el margen de cada profesional antes de asignarle; `RF-TUR-02` solo rechaza al guardar | veredicto-carmen | Media |
| 15 | Carmen | Ningún RF constituye la modificación de una asignación de la programación **vigente** fuera de ausencia, permiso, intercambio o urgencia, aunque la CA-1 de `RF-TUR-04` invoque «modificación válida» | veredicto-carmen | Alta |
| 16 | Carmen | `RF-TUR-03` no excluye de los candidatos a quien tiene una ausencia imprevista registrada: el mismo profesional retirado reaparece como elegible | veredicto-carmen | Alta |
| 17 | Carmen | `RF-TUR-02` solo actúa sobre una regla asociada a un vínculo laboral vigente: al profesional cuyo vínculo nadie registró no hay tope que pueda infringir | auditoría | Media |
| 18 | Carmen | No existe consulta de la agenda de un profesional a través de todas las sedes de la Red | veredicto-carmen | Baja |
| 19 | Carmen | El cambio de responsable de una cama por segunda declaración solo se avisa al médico desplazado (`RF-DIA-35`) | veredicto-carmen | Baja |
| 20 | Carmen | `RF-SUP-05` entrega franjas descubiertas y entregas cerradas, que por glosario son el insumo y no el indicador que su propio enunciado nombra | veredicto-carmen, auditoría | Alta |
| 21 | Aníbal · P2 | El esquema terapéutico vigente con su día solo viaja en el paquete del escalamiento: `RF-DIA-21` lo condiciona a una asignación médica que el localizable nunca tiene | veredicto-anibal | Alta |
| 22 | Aníbal | `RF-REG-13` no declara el dispositivo personal, a diferencia de `RF-REG-07` y `RF-REG-11`: la suspensión es el único acto remoto de su noche sin dispositivo declarado | veredicto-anibal | Media |
| 23 | Aníbal, Milagros, Carmen · P2 | `RF-ESC-09` descansa en una «delegación activa de la jefatura» que ningún RF constituye; es el eslabón que existe para los casos que a nadie alcanzaron | veredicto-anibal, veredicto-carmen | Alta |
| 24 | Aníbal | `RF-TUR-05` avisa el cambio de programación sin la identificación que `RF-TUR-26` sí exige en la reiteración: un aviso administrativo llega indistinguible de uno clínico | veredicto-anibal | Media |
| 25 | Todas | `RF-ESC-08` y `RF-ESC-25` llevan entre título y enunciado una nota editorial dirigida al integrador que contradice el enunciado y deja la corrección sin cerrar | auditoría, veredicto-rodrigo, veredicto-carmen | Alta |
| 26 | Todas | `RF-TUR-08`, `RF-DIA-39`, `RF-DIA-40`, `RF-ESC-37` y `RF-REG-13` llevan notas de proceso dentro del requerimiento: `CONVENCIONES` §2 «cero lápidas» y §10 «el documento registra el estado vigente» | auditoría | Media |
| 27 | Carmen, Rodrigo | `RF-TUR-13` no declara qué compone un «alcance», y de esa delimitación depende íntegro el control de la coordinadora sobre los intercambios | veredicto-carmen | Alta |
| 28 | Milagros, Carmen · P2 | `RF-ESC-23` no fija en qué orden van los demás médicos de la franja, y una cadena es por glosario una secuencia ordenada | veredicto-carmen, auditoría | Media |
| 29 | Carmen | `RF-TUR-16` acuña «condición no operativa» frente a la «condición no editable» de `RF-TUR-28`, sin que el glosario la recoja | auditoría | Baja |

Tres necesidades declaradas quedan **refutadas por escrito** y no abren brecha: el medio por el que
sale el escalamiento (Milagros) es mecanismo y `CONVENCIONES` §5 lo excluye del RF; enterarse de
noche de un deterioro que nadie escaló (Aníbal) queda fuera de sus seis tareas, cuya sexta es
justamente revisar en la mañana; la interfaz idéntica y sin capacitación (Rodrigo) pertenece a
`ReqNoFunc.MD`, como el propio agente declara.

## Acciones recomendadas (priorizadas)

1. **Sacar las notas editoriales de `RF-ESC-08` y `RF-ESC-25`** y cerrar la decisión que discuten. Un
   requerimiento cuyo margen contradice su cuerpo no se puede construir ni evaluar: los dos son MUST y
   los dos cuestan hoy dos veredictos Ambiguo. Con ellos, las notas de proceso de `RF-TUR-08`,
   `RF-DIA-39`, `RF-DIA-40`, `RF-ESC-37` y `RF-REG-13`.
2. **Exigir el contenido de la entrega, no solo su forma.** Mientras únicamente el diagnóstico
   condicione el cierre y `RF-DIA-24` admita el turno sin entrega cerrada, las tareas 1 y 2 de Rodrigo
   —el corazón de P1— no pasan de 3 y su escenario sigue terminando en una llamada por WhatsApp.
   Alcanzar también al turno cubierto solo por guardia localizable.
3. **Declarar dónde trabaja Milagros.** Tres de sus seis tareas se detienen en el mismo punto: ningún
   enunciado dice con qué dispositivo registra junto a la cama ni que pueda consultar allí la cobertura
   clínica. Es un enunciado, no una capacidad nueva.
4. **Constituir lo que otros RF invocan:** la delegación de la jefatura de `RF-ESC-09`, la solicitud de
   estudio de `RF-REG-10` y la modificación de la programación vigente que invoca la CA-1 de
   `RF-TUR-04`.
5. **Cerrar los tres contratos abiertos** que hoy cuestan D3: el «alcance» de `RF-TUR-13`, el orden de
   la cadena en `RF-ESC-23` y la elegibilidad sin reglas registradas de `RF-TUR-03`; y entregar en
   `RF-SUP-05` el indicador que su enunciado nombra.
6. **Poner límite a `RF-DIA-30`** y decidir el reparto de camas de enfermería, que hoy queda en manos
   de quién tocó la pantalla al final (`RF-DIA-37`).

## Evidencia

`Spec/corridas/2026-08-15-iteracion-7/` — `diagnostico.MD`, `corrida.json` y los cuatro
`veredicto-‹persona›.MD`.
