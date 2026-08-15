# Evaluación de Requerimientos Funcionales — Sistema UCI Essalud

| | |
|---|---|
| Corrida | 2026-08-15-iteracion-5 |
| Rama | `eval/iteracion-5` |
| Modelo | claude-opus-5 |
| Evaluado | `Requirements/ReqFunc.MD` @ `be8c4ed` |
| Rúbrica | `Spec/Eval-Spec.MD` @ `b492237` |
| Personas | `Personas/` @ `6340172` |
| Agentes | `Agents/` @ `34877c7` |
| Instrumento modificado | no |

## Puntaje global: 68,9 %

| Dimensión | Puntaje | Peso | Aporte |
|---|---:|---:|---:|
| D1 Satisfacción de las personas | 41,0 | 30 % | 12,300 |
| D2 Cobertura de problemas críticos | 66,7 | 25 % | 16,675 |
| D3 Verificabilidad y forma | 98,4 | 20 % | 19,680 |
| D4 Trazabilidad | 100,0 | 10 % | 10,000 |
| D5 Consistencia y tensiones | 60,0 | 10 % | 6,000 |
| D6 Priorización | 85,0 | 5 % | 4,250 |

Suma de los aportes: 12,300 + 16,675 + 19,680 + 10,000 + 6,000 + 4,250 = **68,905 → 68,9 %**.

## Veredicto: FAILED

| # | Condición | Umbral | Obtenido | Cumple |
|---|---|---:|---:|:---:|
| 1 | Puntaje global | ≥ 80,0 % | 68,9 % | ✗ |
| 2 | D1 | ≥ 80,0 | 41,0 | ✗ |
| 3 | Persona más baja | ≥ 7,0/10 | 2,8 | ✗ |
| 4 | D2 | ≥ 80,0 | 66,7 | ✗ |
| 5 | Controles de `verificar.sh` | 9/9 | 9/9 | ✓ |

## Puntajes por persona

| Persona | Tareas /30 | Estorba fuera | Necesidades /6 | Flujo /4 | Puntaje /10 | Percibida | Δ |
|---|---:|---:|---:|---:|---:|---:|---:|
| Rodrigo | 20 | 3 | 2,8 | 0 | 2,8 | 78 | +50 |
| Milagros | 22 | 3 | 3,2 | 2 | 5,2 | 80 | +28 |
| Carmen | 18 | 0 | 3,6 | 0 | 3,6 | 75 | +39 |
| Aníbal | 20 | 3 | 2,8 | 2 | 4,8 | 80 | +32 |
| **PROMEDIO** | **20,0** | **2,25** | **3,1** | **1,0** | **4,1** | **78,3** | **+37,3** |

La forma de la falla está en las tres últimas columnas. El documento es formalmente sólido —98,4 % de
RF conformes, trazabilidad completa, cinco tensiones decididas— y aun así ninguna persona llega a la
mitad de su escala. Ninguna de las 24 tareas críticas quedó descubierta, pero solo cuatro llegaron a
**cubierta**: las otras veinte están **incompletas** y una es apenas **aparente**. Dos de los cuatro
recorridos se interrumpen en un paso que ningún RF sostiene. La desviación entre lo autoinformado y
lo computado supera el umbral de 20 puntos en las cuatro personas y siempre en el mismo sentido: los
agentes describen la falla con precisión y no la descuentan al puntuarse. Prevalece el valor
computado.

## Brechas encontradas

Las 39 brechas, con origen y severidad, están en
[`corridas/2026-08-15-iteracion-5/diagnostico.MD`](corridas/2026-08-15-iteracion-5/diagnostico.MD).
Aquí las de severidad alta.

| # | Persona o problema afectado | Brecha | Origen | Severidad |
|---|---|---|---|---|
| 1 | Rodrigo · P1 | Ningún RF obliga a registrar la decisión clínica y su fundamento; RF-DIA-01 condiciona el cierre solo al diagnóstico | veredicto-rodrigo | Alta |
| 2 | Rodrigo · P1 | Un turno puede concluir sin cerrar su entrega y ningún RF devuelve el contexto de la cama: corte del recorrido de Rodrigo y tramo que baja P1 a 50 | veredicto-rodrigo · auditoría | Alta |
| 3 | Milagros | Enfermería carece del equivalente de RF-DIA-17 para la entrega no cerrada | veredicto-milagros | Alta |
| 4 | Carmen | Ningún RF permite asignar directamente sobre la programación vigente cuando nadie acepta la cobertura: corte del recorrido de Carmen | veredicto-carmen | Alta |
| 5 | Carmen | RF-TUR-09 presupone «las franjas de cobertura requeridas» sin que ningún RF las constituya | veredicto-carmen | Alta |
| 6 | Aníbal · Milagros | El «ámbito de responsabilidad» de RF-SUP-03 no queda constituido para la guardia localizable ni para enfermería | veredicto-anibal · veredicto-milagros · auditoría | Alta |
| 7 | Aníbal · P2 | No hay enunciado para declararse indisponible cuando ningún delegado resulta admisible | veredicto-anibal | Alta |
| 8 | Aníbal · P2 | Ningún RF comunica al titular el vencimiento o la revocación de su delegación | veredicto-anibal | Alta |
| 9 | Aníbal · P3 | RF-ESC-29 no alcanza al médico con toma del caso vigente | veredicto-anibal | Alta |
| 10 | Milagros · Aníbal · P3 | RF-ESC-13 no declara si la actualización informativa alcanza sin consulta previa: tramo que baja P3 a 50 | veredicto-milagros · veredicto-anibal | Alta |
| 11 | Rodrigo · Milagros | RF-IAM-02 rechaza el registro sobre una cama fuera de la asignación propia sin escalamiento de por medio | veredicto-rodrigo · veredicto-milagros | Alta |
| 12 | Rodrigo · Carmen | RF-DIA-18 («exactamente») contradice RF-DIA-28, que agrega toda cama huérfana a la misma asignación | auditoría · veredicto-rodrigo | Alta |
| 13 | Rodrigo · Carmen | RF-DIA-29 no decide en el enunciado la segunda declaración sobre una cama; su criterio desplaza al primer médico sin avisarle | auditoría · veredicto-carmen | Alta |
| 14 | Rodrigo | RF-IAM-06 constituye y extingue la responsabilidad clínica por una vía distinta de RF-ESC-27 y contra RF-TUR-42 | auditoría · veredicto-rodrigo | Alta |
| 15 | Aníbal | RF-TUR-01, leído con el glosario, rechazaría la guardia localizable simultánea en dos sedes que la persona declara vigente | veredicto-anibal · auditoría | Alta |
| 16 | Rodrigo | El diferencial de RF-DIA-05 se vacía en cuanto consulta la cama una vez: el glosario cuenta la consulta como contacto | veredicto-rodrigo · auditoría | Alta |

## Acciones recomendadas (priorizadas)

1. **Cerrar los dos cortes de recorrido**, que son lo que más hunde D1. Para Rodrigo: un RF que
   declare qué obtiene el médico entrante cuando el turno anterior concluyó sin entrega cerrada, y
   RF-DIA-17 elevado a MUST. Para Carmen: un RF que le permita asignar directamente a un profesional
   sobre la programación vigente cuando la solicitud vence o la lista de candidatos se agota.
2. **Hacer exigible el contenido del handoff.** RF-DIA-02 promete decisiones con su fundamento,
   esquema con su día y estado de la familia, y ningún RF obliga a registrarlos. Mientras el cierre
   dependa solo del diagnóstico, el handoff seguirá siendo lo que el saliente quiera dejar — que es
   literalmente el problema P1.
3. **Deshacer la contradicción triple sobre la asignación médica**: RF-DIA-18 «exactamente» frente a
   RF-DIA-28; RF-DIA-29 sin regla de resolución en el enunciado y sin aviso al desplazado; RF-IAM-06
   constituyendo la responsabilidad clínica por un segundo camino, contra RF-TUR-42.
4. **Constituir el «ámbito de responsabilidad»** para el médico de guardia localizable y para la
   asignación de cuidado de enfermería, o desdoblar RF-SUP-03: hoy es el único RF de la tarea 6 de
   Aníbal y el glosario lo deja sin alcance.
5. **Decidir la entrega de la actualización informativa** (RF-ESC-13) con el vocabulario de RF-ESC-22,
   28 y 29 —«alcanzar sin que deban consultarlo», o su negación explícita— y extender RF-ESC-29 al
   médico con toma del caso vigente. Son los dos tramos que mantienen P3 en 50.
6. **Abrir el registro a quien cubre sin ser titular** (RF-IAM-02): el médico llamado a una cama ajena
   y la enfermera que cubre a su colega vuelven hoy al papel, que es la fuga por donde se degrada
   todo el registro que la Red exige.
7. **Completar la delegación** (RF-ESC-07, RF-ESC-30, RF-ESC-31): indisponibilidad sin delegado
   admisible, revocación por el propio titular y aviso del retorno de la responsabilidad a su nombre.

## Evidencia

[`Spec/corridas/2026-08-15-iteracion-5/`](corridas/2026-08-15-iteracion-5/) — `diagnostico.MD` con las
tablas de evidencia y la aritmética desarrollada, `corrida.json`, `controles.txt` y los cuatro
veredictos de persona.
