# Evaluación de Requerimientos Funcionales — Sistema UCI Essalud

| | |
|---|---|
| Corrida | 2026-08-15-iteracion-6 |
| Rama | `eval/iteracion-6` |
| Modelo | claude-opus-5 |
| Evaluado | `Requirements/ReqFunc.MD` @ `4b277e9` |
| Rúbrica | `Spec/Eval-Spec.MD` @ `b492237` |
| Personas | `Personas/` @ `6340172` |
| Agentes | `Agents/` @ `34877c7` |
| Instrumento modificado | no |

## Puntaje global: 71,5 %

| Dimensión | Puntaje | Peso | Aporte |
|---|---:|---:|---:|
| D1 Satisfacción de las personas | 49,0 | 30 % | 14,700 |
| D2 Cobertura de problemas críticos | 66,7 | 25 % | 16,675 |
| D3 Verificabilidad y forma | 97,9 | 20 % | 19,580 |
| D4 Trazabilidad | 100,0 | 10 % | 10,000 |
| D5 Consistencia y tensiones | 60,0 | 10 % | 6,000 |
| D6 Priorización | 90,0 | 5 % | 4,500 |
| **Suma de aportes** | | | **71,455 → 71,5** |

## Veredicto: FAILED

| # | Condición | Umbral | Obtenido | Cumple |
|---|---|---:|---:|:---:|
| 1 | Puntaje global | ≥ 80,0 % | 71,5 % | no |
| 2 | D1 | ≥ 80,0 | 49,0 | no |
| 3 | Persona más baja | ≥ 7,0/10 | 3,2 | no |
| 4 | D2 | ≥ 80,0 | 66,7 | no |
| 5 | Controles de `verificar.sh` | 9/9 | 9/9 | sí |

## Puntajes por persona

| Persona | Tareas /30 | Estorba fuera | Necesidades /6 | Flujo /4 | Puntaje /10 | Percibida | Δ |
|---|---:|---:|---:|---:|---:|---:|---:|
| Rodrigo | 20 | 4 | 2,4 | 2 | 4,4 | 78 | 34 |
| Milagros | 20 | 2 | 3,2 | 0 | 3,2 | 80 | 48 |
| Carmen | 22 | 2 | 3,6 | 2 | 5,6 | 82 | 26 |
| Aníbal | 24 | 1 | 4,4 | 2 | 6,4 | 80 | 16 |
| **PROMEDIO** | **21,5** | **2,25** | **3,4** | **1,5** | **4,9** | **80** | **31** |

La forma es sólida y la satisfacción no la sigue. Los 146 RF están bien escritos, trazados y
priorizados —D3 97,9, D4 100, D6 90—, y aun así ninguna persona llega a 7/10. La distancia la
producen tres cosas: el escenario de Milagros se corta antes del final, nueve requerimientos estorban
a una persona fuera de sus tareas críticas y diecisiete de las veinticuatro tareas quedan incompletas
por un comportamiento que el conjunto no declara. Tres de los cuatro agentes se autoinforman más de
20 puntos por encima de lo computado; prevalece el cómputo.

## Brechas encontradas

Las treinta brechas, con su origen y severidad, están en
[`Spec/corridas/2026-08-15-iteracion-6/diagnostico.MD`](corridas/2026-08-15-iteracion-6/diagnostico.MD).
Las de severidad alta:

| # | Persona o problema afectado | Brecha | Origen | Severidad |
|---|---|---|---|---|
| 1 | Milagros · P3 | La decisión de acudir se incorpora al episodio por RF-REG-11 y ningún RF la hace llegar a quien escaló: corta su escenario en el paso 8 | veredicto-milagros | Alta |
| 2 | Milagros · P3 | La suspensión o el cambio de una indicación vigente no la alcanza junto a la cama; RF-ESC-28 sólo declara la indicación nueva | veredicto-milagros · auditoría | Alta |
| 3 | Milagros · P2 | Una noche cubierta sólo por guardia localizable deja las camas sin responsable clínico vigente (RF-DIA-28 CA-2), y RF-ESC-01, RF-ESC-08 y RF-ESC-23 lo presuponen | veredicto-milagros · auditoría | Alta |
| 4 | P2 | La indisponibilidad declarada no altera la cadena: por RF-ESC-27 y RF-ESC-23 el indisponible sigue encabezándola y quema un plazo entero | auditoría · veredicto-milagros | Alta |
| 5 | Aníbal · P2 | No existe indisponibilidad registrada cuando sí se indica delegado; RF-ESC-08 enumera un estado que nadie constituye y RF-ESC-31 devuelve al titular a la cabeza de la cadena | veredicto-anibal | Alta |
| 6 | Carmen · P2 | La indisponibilidad sin delegado no devuelve la franja a las descubiertas de RF-TUR-07 ni la habilita para RF-TUR-44 | veredicto-carmen | Alta |
| 7 | P2 | RF-ESC-09 termina la cadena en la jefatura y ningún RF declara qué ocurre si ella tampoco acusa | veredicto-milagros · auditoría | Alta |
| 8 | Aníbal · P2 | RF-ESC-06 aplica la cadena de la severidad y RF-ESC-23 la compone sin mirarla: contradicción entre dos RF | veredicto-anibal · auditoría | Alta |
| 9 | Rodrigo · P1 | La atribución del registro en la PC compartida no la declara ningún RF; RF-IAM-08 sólo cubre el dispositivo personal | veredicto-rodrigo | Alta |
| 10 | Milagros · P2 | No puede registrar ni escalar sobre la cama de su colega sin un relevo declarado previo (RF-IAM-02, RF-IAM-10) | veredicto-milagros | Alta |
| 11 | Milagros · P3 | Nada la alcanza junto a la cama cuando su cama se queda sin responsable clínico vigente | veredicto-milagros | Alta |
| 12 | Carmen · P1 | El vínculo laboral y las reglas de jornada del personal de planta no los constituye ningún RF; RF-IAM-06 sólo cubre al rotante | veredicto-carmen | Alta |
| 13 | ReqFunc.MD | Cinco RF conservan un bloque «*Cambio:*» que narra la historia de la iteración y cita la evaluación; RF-DIA-05 remite a una sección `## GLOSARIO` inexistente | auditoría | Alta |

## Acciones recomendadas (priorizadas)

1. **Cerrar el corte de Milagros.** Un RF que haga llegar a quien emitió el escalamiento la decisión
   de acudir o de no acudir que RF-REG-11 ya incorpora al episodio. Es el único flujo interrumpido de
   la corrida y vale por sí solo 2 de los 4 puntos de flujo de su persona.
2. **Constituir la indisponibilidad como estado que la cadena mira.** Un RF que registre la
   indisponibilidad declarada también cuando hay delegado, y otro que la haga desplazar al declarado
   indisponible de la cabeza de la cadena. Cierra las brechas 4, 5 y 6 y desbloquea el tramo de P2 que
   hoy vale 50.
3. **Resolver la contradicción RF-ESC-06 ↔ RF-ESC-23** declarando si la cadena depende de la
   severidad o si sólo el plazo lo hace. Es el Ambiguo que le cuesta a Aníbal sus 2 puntos de flujo.
4. **Declarar la verificación de identidad en el equipo compartido.** RF-IAM-08 la constituye sólo en
   el dispositivo personal; es el par de Ambiguos que le cuesta a Rodrigo sus 2 puntos de flujo y la
   restricción explícita de su persona.
5. **Constituir el vínculo laboral y las reglas de jornada del personal de planta**, de los que
   dependen RF-TUR-02 y RF-TUR-03. Es el único Ambiguo del recorrido de Carmen.
6. **Retirar de `ReqFunc.MD` los cinco bloques «*Cambio:*»** y la referencia rota a `## GLOSARIO`: el
   documento no registra cómo se llegó al enunciado vigente ni habla de la rúbrica que lo mide.
7. **Revisar los nueve RF que estorban fuera de tarea** —RF-TUR-17, RF-TUR-31, RF-TUR-44 y RF-SUP-01
   para Rodrigo; RF-TUR-28 y RF-DIA-36 para Milagros; RF-DIA-29 y RF-ESC-32 para Carmen; RF-ESC-25
   para Aníbal—. Cuestan 18 de los 30 puntos de tarea que la corrida descuenta.

## Evidencia

[`Spec/corridas/2026-08-15-iteracion-6/`](corridas/2026-08-15-iteracion-6/) — diagnóstico con la
matriz de veredictos de los 146 RF, la matriz de cobertura de las 24 tareas, la aritmética de D1 a D6
desarrollada, las treinta brechas y los cuatro veredictos de persona.
