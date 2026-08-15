# Evaluación de Requerimientos Funcionales — Sistema UCI Essalud

| | |
|---|---|
| Corrida | 2026-08-14-iteracion-3 |
| Rama | `eval/iteracion-3` |
| Modelo | claude-opus-5 |
| Evaluado | `Requirements/ReqFunc.MD` @ `f50cf90` |
| Rúbrica | `Spec/Eval-Spec.MD` @ `b492237` |
| Personas | `Personas/` @ `6340172` |
| Agentes | `Agents/` @ `34877c7` |
| Instrumento modificado | no |

## Puntaje global: 59,0 %

| Dimensión | Puntaje | Peso | Aporte |
|---|---:|---:|---:|
| D1 Satisfacción de las personas | 29,0 | 30 % | 8,70 |
| D2 Cobertura de problemas críticos | 50,0 | 25 % | 12,50 |
| D3 Verificabilidad y forma | 93,8 | 20 % | 18,76 |
| D4 Trazabilidad | 90,0 | 10 % | 9,00 |
| D5 Consistencia y tensiones | 60,0 | 10 % | 6,00 |
| D6 Priorización | 80,0 | 5 % | 4,00 |
| **Suma de aportes** | | | **58,96 → 59,0** |

## Veredicto: FAILED

| # | Condición | Umbral | Obtenido | Cumple |
|---|---|---:|---:|:---:|
| 1 | Puntaje global | ≥ 80,0 % | 59,0 % | ✗ |
| 2 | D1 | ≥ 80,0 | 29,0 | ✗ |
| 3 | Persona más baja | ≥ 7,0/10 | 2,0 | ✗ |
| 4 | D2 | ≥ 80,0 | 50,0 | ✗ |
| 5 | Controles de `verificar.sh` | 9/9 | 9/9 | ✓ |

El documento está bien escrito y mal repartido. La forma es sólida —76 de 81 RF conformes, los ocho
controles mecánicos en verde, las cinco tensiones decididas, ningún huérfano y ningún RNF infiltrado—
y sin embargo ninguna de las cuatro personas recorre su escenario clave de extremo a extremo. Esa es
la distancia entre 93,8 en D3 y 29,0 en D1: los requerimientos declaran muy bien lo que declaran, y
lo que falta es el acto que los enlaza.

## Puntajes por persona

| Persona | Tareas /30 | Estorba fuera | Necesidades /6 | Flujo /4 | Puntaje /10 | Percibida | Δ |
|---|---:|---:|---:|---:|---:|---:|---:|
| Rodrigo | 20 | 1 | 3,6 | 0 | 3,6 | 70 | −34 |
| Milagros | 16 | 3 | 2,0 | 0 | 2,0 | 70 | −50 |
| Carmen | 14 | 2 | 2,0 | 0 | 2,0 | 70 | −50 |
| Aníbal | 22 | 1 | 4,0 | 0 | 4,0 | 78 | −38 |
| **PROMEDIO** | **18** | **1,75** | **2,9** | **0** | **2,9** | **72** | **−43** |

Las cuatro desviaciones superan el umbral de 20 puntos y las cuatro tienen el mismo signo: la
cobertura percibida está por encima de la computada. Prevalece el valor computado. La coincidencia de
las cuatro lecturas —producidas en aislamiento— descarta que el problema esté en el enunciado de las
tareas críticas: si lo estuviera, la desviación se concentraría en una persona. El autoinforme mide
qué proporción de los RF le sirve al agente; la rúbrica mide si sus seis tareas quedan cubiertas y si
su escenario se recorre entero.

**Los cuatro flujos quedaron en 0**, y en los cuatro casos por el mismo motivo: un paso del escenario
clave que ningún RF sostiene.

| Persona | Paso exacto |
|---|---|
| Rodrigo | 23:40, la cama 6 se descompensa: ningún RF permite volver a abrir la decisión fundamentada, el esquema con su día y el estado de la familia fuera del inicio de turno |
| Milagros | 02:15, decide escalar: ningún RF declara el acto de emisión. Y la indicación remota de las 02:40 le llega sin aviso |
| Carmen | Viernes 15:40, asigna al reemplazo: ningún RF declara que el candidato acepte antes de quedar asignado, y sigue llamando por teléfono |
| Aníbal | 03:20, indicó noradrenalina: ningún RF le devuelve la confirmación de ejecución que RF-REG-04 registra |

## Brechas encontradas

44 brechas abiertas; el detalle completo, con su severidad y su origen, está en
`Spec/corridas/2026-08-14-iteracion-3/diagnostico.MD`. Las nueve críticas:

| # | Persona o problema afectado | Brecha | Origen | Severidad |
|---:|---|---|---|---|
| 1 | Rodrigo, Carmen · P1 | Ningún RF declara cómo se asignan las camas a un médico: RF-DIA-01, RF-DIA-02, RF-DIA-10 y RF-IAM-02 dan ese estado por existente y la programación asigna franjas, no camas | veredicto-rodrigo, veredicto-carmen, auditoría | Crítica |
| 2 | Rodrigo · P1 | No hay consulta a demanda del bloque de decisión, esquema y familia en medio del turno | veredicto-rodrigo | Crítica |
| 7 | Milagros · P2 | Ningún RF declara el acto de emisión del escalamiento ni desde qué dispositivo | veredicto-milagros, auditoría | Crítica |
| 13 | Milagros · P3 | Ningún RF avisa de una indicación médica nueva: la lista de RF-ESC-13 no la contempla | veredicto-milagros, auditoría | Crítica |
| 15 | Carmen · P1 | Ningún RF declara que alguien pueda consultar la programación vigente | veredicto-carmen | Crítica |
| 25 | Aníbal, Milagros · P2 | Ningún RF declara cómo se obtiene o renueva la identidad verificada en el celular a las 03:20; sin ella RF-IAM-07 devuelve el flujo al teléfono | veredicto-anibal, veredicto-milagros | Crítica |
| 27 | Aníbal, Rodrigo · P2 | RF-IAM-02 no declara si tomar un caso por avance de cadena habilita a registrar sobre esa cama | veredicto-anibal, veredicto-rodrigo, veredicto-milagros | Crítica |
| 32 | P1 | Ningún RF declara qué acto produce una «entrega confirmada», condición de RF-DIA-10 y RF-DIA-17, mientras conviven firma, aceptación, cierre y entrega confirmada | auditoría, veredicto-rodrigo | Crítica |
| 44 | Las cuatro | Cinco coberturas únicas de tarea crítica están en SHOULD —RF-DIA-05, RF-DIA-08, RF-REG-08, RF-SUP-02, RF-SUP-03— con 60 MUST asignados al resto | auditoría, los cuatro veredictos | Alta |

Ninguna brecha proviene de un control mecánico: los ocho controles de forma y estructura devuelven
vacío. Todas salen de los cuatro veredictos o de la auditoría, que es donde vive lo que un script no
puede ver.

## Acciones recomendadas (priorizadas)

1. **Declarar los actos que el documento presupone.** Cuatro estados sostienen la mitad de los
   enunciados y ninguno tiene RF que los produzca: la asignación de camas a un médico y a una
   enfermera, la «entrega confirmada», el pendiente de cuidado de enfermería y la composición de la
   cadena de escalamiento. Sin ellos, RF-DIA-01, RF-DIA-02, RF-DIA-10, RF-DIA-17, RF-DIA-08,
   RF-DIA-11, RF-IAM-02, RF-ESC-01 y RF-ESC-09 arrancan de un supuesto. Es la corrección que más sube
   D1 y D2 a la vez.
2. **Cerrar los cuatro pasos que interrumpen los escenarios clave**: consulta a demanda del bloque
   clínico fuera del inicio de turno (Rodrigo), acto de emisión del escalamiento a pie de cama y aviso
   de indicación nueva (Milagros), aceptación del candidato antes de la asignación (Carmen), y retorno
   al indicador de la confirmación de ejecución (Aníbal). Cada uno vale 4 puntos de 10 en su persona.
3. **Declarar la recuperación de la identidad verificada en el dispositivo personal** y qué se expone
   en pantalla bloqueada cuando la identidad está vigente. Hoy RF-IAM-07 corta el contexto sin ruta de
   salida declarada y devuelve el escalamiento al teléfono, que es la falla que P2 nombra.
4. **Hacer visible la programación vigente**: un RF que declare su consulta y otro que declare la copia
   imprimible del periodo en curso. Sin ellos, RF-TUR-08 convierte al sistema en fuente única de un rol
   que nadie puede leer, y la foto por WhatsApp sobrevive con las tres versiones que el sistema venía a
   eliminar.
5. **Corregir los cinco RF no conformes de D3** —RF-ESC-06 y RF-REG-06 enuncian dos respuestas;
   RF-REG-02, RF-REG-08 y RF-SUP-02 tienen criterios que amplían su contrato— y **reparar la fila P2 de
   la matriz de cobertura de problemas**, que incluye RF-ESC-13 (declara P3) y omite RF-DIA-13
   (declara P2).
6. **Rehacer el gradiente de prioridad.** Bajar a SHOULD los cuatro MUST no justificados —RF-TUR-08,
   RF-TUR-21, RF-TUR-25, RF-DIA-16— y subir a MUST las coberturas únicas de tarea crítica que hoy son
   SHOULD. Resolver antes el duplicado RF-TUR-03 / RF-TUR-21 y definir «cambio urgente», del que
   dependen RF-TUR-25 y RF-TUR-26.

## Evidencia

`Spec/corridas/2026-08-14-iteracion-3/` — diagnóstico completo, los cuatro veredictos de persona,
`corrida.json` y la salida literal de los controles.
