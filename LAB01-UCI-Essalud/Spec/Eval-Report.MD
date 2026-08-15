# Evaluación de Requerimientos Funcionales — Sistema UCI Essalud

| | |
|---|---|
| Corrida | 2026-08-15-iteracion-8 |
| Rama | `eval/iteracion-8` |
| Modelo | claude-opus-5 |
| Evaluado | `Requirements/ReqFunc.MD` @ `df4ec25` |
| Rúbrica | `Spec/Eval-Spec.MD` @ `b492237` |
| Personas | `Personas/` @ `6340172` |
| Agentes | `Agents/` @ `34877c7` |
| Instrumento modificado | no |

## Puntaje global: 79,9 %

| Dimensión | Puntaje | Peso | Aporte |
|---|---:|---:|---:|
| D1 Satisfacción de las personas | 66,0 | 30 % | 19,80 |
| D2 Cobertura de problemas críticos | 83,3 | 25 % | 20,83 |
| D3 Verificabilidad y forma | 98,9 | 20 % | 19,78 |
| D4 Trazabilidad | 90,0 | 10 % | 9,00 |
| D5 Consistencia y tensiones | 60,0 | 10 % | 6,00 |
| D6 Priorización | 90,0 | 5 % | 4,50 |
| **Suma de aportes** | | | **79,9** |

## Veredicto: FAILED

| # | Condición | Umbral | Obtenido | Cumple |
|---|---|---:|---:|:---:|
| 1 | Puntaje global | ≥ 80,0 % | 79,9 | ✗ |
| 2 | D1 | ≥ 80,0 | 66,0 | ✗ |
| 3 | Persona más baja | ≥ 7,0/10 | 4,8 (Rodrigo) | ✗ |
| 4 | D2 | ≥ 80,0 | 83,3 | ✓ |
| 5 | Controles de `verificar.sh` | 9/9 | 9/9 | ✓ |

Tres condiciones de cinco quedan sin cumplir. El global se queda a 0,1 punto del umbral y **no se
redondea hacia arriba**: 66,0 × 0,30 + 83,3 × 0,25 + 98,9 × 0,20 + 90,0 × 0,10 + 60,0 × 0,10 +
90,0 × 0,05 = 79,905, que con un decimal es 79,9. Aun cruzándolo, las condiciones 2 y 3 lo dejarían
en FAILED: el documento está bien escrito y mal repartido, y quien más lo paga es la persona ancla
de P1.

## Puntajes por persona

| Persona | Tareas /30 | Estorba fuera | Necesidades /6 | Flujo /4 | Puntaje /10 | Percibida | Δ |
|---|---:|---:|---:|---:|---:|---:|---:|
| Rodrigo | 22 | 4 | 2,8 | 2 | 4,8 | 78 | −30 |
| Milagros | 26 | 1 | 4,8 | 2 | 6,8 | 85 | −17 |
| Carmen | 22 | 1 | 4,0 | 2 | 6,0 | 85 | −25 |
| Aníbal | 26 | 1 | 4,8 | 4 | 8,8 | 88 | 0 |
| **PROMEDIO** | **24,0** | **1,75** | **4,1** | **2,5** | **6,6** | **84** | **−18** |

`Puntaje_p = máx(0, Σ tareas_p − 2 × X_p) / 5 + Flujo_p`; `D1 = 6,6 × 10 = 66,0`.

## Brechas encontradas

| # | Persona o problema afectado | Brecha | Origen | Severidad |
|---|---|---|---|---|
| 1 | Rodrigo | La marca de inestabilidad o de pendiente crítico no trae autor, instante ni motivo al consultarla: sabe qué cama está marcada, no por qué | veredicto-rodrigo | Alta |
| 2 | Rodrigo · P1 | Nada obliga a que la decisión clínica y su fundamento existan en la entrega recibida: el cierre solo exige el diagnóstico del turno | veredicto-rodrigo | Alta |
| 3 | Rodrigo · P1 | La cama señalada sin diagnóstico del turno anterior solo se repara si el médico que ya se fue vuelve a registrarlo (RF-DIA-47) | veredicto-rodrigo | Alta |
| 4 | Rodrigo | El médico desplazado de una cama (RF-DIA-29) no puede registrar lo que ya observó en ella | veredicto-rodrigo | Media |
| 5 | Rodrigo | No se declara qué ocurre con la nota retenida por RF-IAM-15, ni con la escrita desde la estación al caer la red: RF-REG-02 solo cubre el registro a pie de cama | veredicto-rodrigo · auditoría | Alta |
| 6 | Milagros · P2 | Ningún enunciado declara que pueda consultar los medios de contacto vigentes que RF-IAM-11 registra | veredicto-milagros | Alta |
| 7 | Milagros | El cambio de responsable clínico vigente no la alcanza junto a la cama salvo que la cama quede sin ninguno (RF-ESC-41) | veredicto-milagros | Media |
| 8 | Milagros | La indisponibilidad declarada del responsable de su cama no la alcanza: RF-ESC-33 informa a la jefatura | veredicto-milagros | Media |
| 9 | Milagros | La solicitud de un estudio hecha a distancia no la alcanza junto a la cama, y es ella quien toma la muestra (RF-REG-14) | veredicto-milagros | Media |
| 10 | Carmen | Ningún enunciado declara que el reflejo pueda entregarse en forma imprimible para la pared de la unidad, restricción documentada de su persona | veredicto-carmen | Alta |
| 11 | Carmen | No se declara qué ocurre al publicar la programación mensual con franjas sin cubrir: RF-TUR-10 solo resuelve la propuesta completa | veredicto-carmen | Alta |
| 12 | Carmen | No puede asignar directamente una franja descubierta cuyo inicio queda fuera del horizonte de urgencia (RF-TUR-44) | veredicto-carmen | Alta |
| 13 | Carmen | No se le presenta el acumulado de horas del mes de cada profesional: solo la exclusión del candidato | veredicto-carmen | Media |
| 14 | Carmen · Aníbal · P2 | La condición de profesional asignado sin medio de contacto vigente se presenta solo a él (RF-IAM-12): ni la jefatura ni la enfermera se enteran | veredicto-carmen · veredicto-anibal | Alta |
| 15 | Carmen | La confirmación de lectura del rol solo se persigue en el cambio urgente (RF-TUR-25, RF-TUR-26) | veredicto-carmen | Baja |
| 16 | Carmen · P2 | Una franja cuyo médico declaró indisponibilidad sin delegado sigue figurando cubierta en RF-TUR-07 (RF-ESC-32) | veredicto-carmen | Alta |
| 17 | Aníbal · P2 | Nadie le comunica de qué camas queda respondiendo al iniciar su bloque: RF-TUR-49 y RF-DIA-46 van a la jefatura | veredicto-anibal | Alta |
| 18 | Aníbal · P2 | No se entera durante la noche de que una cama pasó a ser suya: RF-DIA-36 la libera y RF-ESC-41 alcanza a enfermería | veredicto-anibal | Alta |
| 19 | Aníbal | No puede recuperar por consulta lo que decidió el turno diurno cerrado sin entrega: RF-DIA-32 y RF-DIA-42 hablan del «médico entrante de esa cama», indefinido para un localizable | veredicto-anibal | Media |
| 20 | Aníbal · P2 | No puede delegar cuando ningún médico está asignado a esa unidad en el intervalo (RF-ESC-30), y ningún RF ofrece otra vía de traspaso | veredicto-anibal | Alta |
| 21 | P1 · forma | RF-DIA-02 CA-3 exige en la entrega un cultivo pendiente que la composición cerrada de «estado clínico de una cama» no comprende | auditoría | Alta |
| 22 | Milagros · P3 | RF-ESC-16 ordena cuatro clases que no comprenden la tercera clase de aviso clínico que fija el glosario | auditoría · veredicto-milagros | Alta |
| 23 | Rodrigo · Milagros | RF-IAM-01 y RF-IAM-15 se contradicen: IAM-15 presupone una atribución que IAM-01 impide | auditoría | Media |
| 24 | Vocabulario | RF-DIA-23 enumera «el responsable clínico vigente de esa cama, su delegado activo» cuando el glosario ya constituye al delegado en responsable vigente | auditoría | Baja |
| 25 | Forma | RF-TUR-42 enuncia dos respuestas: conservar la asignación de la franja y conservar la asignación médica de camas | auditoría | Media |
| 26 | Trazabilidad | La fila «Milagros / Ver y confirmar indicaciones médicas vigentes» cita RF-ESC-13, que entrega una actualización informativa a la consulta del responsable clínico y no a la enfermera | auditoría | Media |
| 27 | Priorización | RF-DIA-04 y RF-ESC-44 llevan MUST sin que su ausencia deje descubierta una tarea crítica ni sin resolver un problema | auditoría | Baja |

Dos necesidades declaradas por los agentes quedan **refutadas por escrito** y no abren brecha: que
ningún enunciado diga qué mide cada indicador (`docs/GLOSARIO.md` define «indicador de cobertura de
turnos» e «indicador de cumplimiento de entrega») y que ninguno defina el cambio del estado de
atención (el glosario fija ese estado con exactamente seis valores).

## Acciones recomendadas (priorizadas)

1. **Devolverle a Rodrigo los cuatro Estorba que caen fuera de sus tareas.** Ocho de sus treinta
   puntos se pierden ahí, y ninguno le compensa nada: RF-TUR-17, RF-TUR-31 y RF-TUR-33 le devuelven
   a la coordinadora un intercambio que él ya pactó, y RF-DIA-44 lleva a la jefatura cada cama
   estable sin decisión registrada. Decidir la tensión «autonomía de intercambio» sin dejarlo
   colgado de una resolución individual, y acotar RF-DIA-44 a las camas marcadas, sube su puntaje
   más que cualquier RF nuevo.
2. **Cerrar los tres Ambiguo que le cuestan el flujo a Rodrigo.** RF-DIA-34 debe decir si el
   señalamiento condiciona la firma o solo la informa; RF-IAM-15, qué ocurre con el acto retenido si
   la verificación no llega; RF-REG-02, si su alcance es el registro a pie de cama o todo registro
   clínico sin conexión. Los tres son de redacción, no de comportamiento nuevo.
3. **Dar salida a la indisponibilidad sin delegado posible (RF-ESC-30).** Es el tramo de P2 que
   ningún RF cubre y el único motivo por el que P2 queda en 50: en la noche habitual de Aníbal —
   único localizable de dos UCIs— no existe delegado admisible, y el sistema solo sabe agotar la
   cadena hasta la jefatura.
4. Declarar la consulta de los medios de contacto vigentes por quien escala, y presentar la
   condición de RF-IAM-12 también a la jefatura: son las dos mitades del agujero por el que hoy no
   se ubica al médico.
5. Corregir los cuatro hallazgos de consistencia (brechas 21 a 24) y la fila desfasada de la matriz
   (brecha 26): D5 está en 60 con el tramo de consistencia agotado, y es la dimensión que menos
   cuesta recuperar.

## Evidencia

`Spec/corridas/2026-08-15-iteracion-8/` — diagnóstico completo, los cuatro veredictos de persona y
`corrida.json`.
