# Reporte de Evaluación de Requerimientos Funcionales
## Sistema de Gestión UCI — Essalud

| | |
|---|---|
| Corrida | 2026-08-13-additional-v2 |
| Rama | `eval/additional-v2` |
| Modelo | `claude-opus-5[1m]` |
| Evaluado | `Requirements/ReqFunc.MD` @ `a1df636` |
| Rúbrica | `Spec/Eval-Spec.MD` @ `8af38e9` |
| Personas | `Personas/` @ `6340172` |
| Agentes | `Agents/` @ `fb5856c` |
| Instrumento modificado en el Paso 0 | no |

## Puntaje global: 58,7 %

| Dimensión | Puntaje | Peso | Aporte |
|---|---:|---:|---:|
| D1 Satisfacción de las personas | 61,0 | 30 % | 18,30 |
| D2 Cobertura de problemas críticos | 66,7 | 25 % | 16,68 |
| D3 Verificabilidad y forma | 54,8 | 20 % | 10,96 |
| D4 Trazabilidad | 40,0 | 10 % | 4,00 |
| D5 Consistencia y tensiones | 40,0 | 10 % | 4,00 |
| D6 Priorización | 95,0 | 5 % | 4,75 |

Suma de aportes: 18,30 + 16,68 + 10,96 + 4,00 + 4,00 + 4,75 = **58,7**.

## Veredicto: FAILED

| # | Condición | Umbral | Obtenido | Cumple |
|---|---|---:|---:|:---:|
| 1 | Puntaje global | ≥ 80,0 % | 58,7 % | ✗ |
| 2 | D1 | ≥ 80,0 | 61,0 | ✗ |
| 3 | Persona más baja | ≥ 7,0/10 | 4,4 | ✗ |
| 4 | D2 | ≥ 80,0 | 66,7 | ✗ |
| 5 | Controles de `verificar.sh` | 9/9 | 9/9 | ✓ |

Los nueve controles mecánicos devuelven vacío, C1 incluido: la aritmética cierra y el veredicto
declarado es el que producen las cinco condiciones. El FAILED no viene de la forma detectable por
script, sino del contenido.

## Puntajes por persona

| Persona | Tareas /30 | Estorba fuera | Necesidades /6 | Flujo /4 | Puntaje /10 | Percibida | Δ |
|---|---:|---:|---:|---:|---:|---:|---:|
| Rodrigo | 26 | 2 | 4,4 | 0 | 4,4 | 100 % | 56,0 |
| Milagros | 24 | 0 | 4,8 | 4 | 8,8 | 100 % | 12,0 |
| Carmen | 22 | 0 | 4,4 | 0 | 4,4 | 100 % | 56,0 |
| Aníbal | 24 | 0 | 4,8 | 2 | 6,8 | 100 % | 32,0 |
| **PROMEDIO** | **24,0** | **0,5** | **4,6** | **1,5** | **6,1** | **100 %** | **39,0** |

Milagros es la única persona a la que el conjunto satisface: su escenario clave se recorre entero y
cada paso se sostiene en un RF explícito. Rodrigo y Carmen quedan por debajo de la mitad de la escala
por la misma causa —el sistema declara qué hace con un registro que nunca declara aceptar— y no por
falta de requerimientos.

## Brechas encontradas

| # | Persona o problema afectado | Brecha | Origen | Severidad |
|---|---|---|---|---|
| B-01 | Rodrigo · P1 | Ningún enunciado declara que el sistema incorpore la nota de evolución ni el diagnóstico que el médico produce. `RF-DIA-01` bloquea el cierre si falta y `RF-DIA-07` conserva «cada versión registrada»: ambos presuponen el acto | `veredicto-rodrigo` | Crítica |
| B-02 | Rodrigo | El contrato cerrado de `RF-DIA-02` omite el esquema terapéutico en curso con su día de tratamiento, primer dato que el escenario de la cama 6 exige | `veredicto-rodrigo` | Alta |
| B-03 | Rodrigo | La aceptación de la entrega de turno se invoca en `RF-DIA-03` pero ningún RF la declara como comportamiento del sistema | `veredicto-rodrigo` | Media |
| B-04 | Milagros | Ningún RF declara que el registro pueda producirse a pie de cama; `RF-REG-02` regula la falta de conexión, que es su consecuencia | `veredicto-milagros` | Alta |
| B-05 | Milagros | `RF-DIA-08` declara entregar el turno de enfermería, no recibirlo; la mitad de su tarea 6 queda sin enunciado | `veredicto-milagros` | Alta |
| B-06 | Milagros | `RF-ESC-06` impone clasificar la severidad antes de escalar y ningún RF prevé escalar primero con un valor por defecto para la duda clínica | `veredicto-milagros` | Alta |
| B-07 | Carmen · P1 | Ningún enunciado declara el acto de asignar un profesional a una franja ni el de elaborar y publicar una programación. `RF-TUR-01` a `RF-TUR-05` presuponen los dos | `veredicto-carmen` | Crítica |
| B-08 | Carmen | El circuito de permisos no tiene ningún RF: `RF-TUR-03` los usa como dato preexistente | `veredicto-carmen` | Alta |
| B-09 | Carmen | `RF-TUR-06` declara que la propuesta de intercambio no tiene efecto hasta la resolución, pero no qué ocurre al resolverla | `veredicto-carmen` | Media |
| B-10 | Carmen | La rotación como criterio de reparto, que su escenario invoca, no aparece en `RF-TUR-03` | `veredicto-carmen` | Baja |
| B-11 | Aníbal | Los parámetros del ventilador no figuran en el contrato cerrado de `RF-ESC-03` ni en `RF-REG-08`, siendo una frustración documentada de la persona | `veredicto-anibal` | Alta |
| B-12 | Aníbal | «Tomar el caso» no lo declara ningún RF: `RF-ESC-04` declara el acuse | `veredicto-anibal` | Media |
| B-13 | Aníbal | `RF-ESC-03` adjunta «la última evolución registrada», que no es la decisión del turno diurno con su fundamento que `RF-DIA-02` sí declara para el médico presencial | `veredicto-anibal` | Media |
| B-14 | P3 | Ningún RF declara la actualización de un evento clínico a múltiples destinatarios. `RF-ESC-02` es secuencial, `RF-ESC-05` es una consulta y `RF-TUR-05` alcanza por cambios de programación | auditoría | Crítica |
| B-15 | D3 | 19 de 42 RF incumplen alguna de las ocho condiciones de forma: 6 enuncian dos respuestas independientes, 11 llevan criterios que amplían el contrato del enunciado, 1 declara el mecanismo y 1 nombra tecnología | auditoría | Alta |
| B-16 | D4 | Seis filas de las matrices internas afirman una cobertura que ningún RF citado declara | auditoría | Alta |
| B-17 | D5 | La tensión de adopción voluntaria se declara decidida por `RF-TUR-08` —un COULD— y por dos RNF que esta rúbrica no puntúa: ningún RF vinculante la decide | auditoría | Crítica |
| B-18 | D5 | «Un profesional» no distingue médico de enfermería en `RF-DIA-01`, `RF-DIA-02` y `RF-DIA-04`; `RF-IAM-02` y `RF-REG-07` usan dos vocabularios distintos para el mismo permiso | auditoría · `veredicto-milagros` · `veredicto-anibal` | Alta |
| B-19 | Instrumento | La definición de cobertura percibida que comparten los cuatro agentes devuelve 100 % siempre que cada tarea reciba un solo «Sirve», por parcial que sea. Las cuatro percibidas valen 100 y tres superan los 20 puntos de desviación | auditoría | Media |

## Acciones recomendadas (priorizadas)

1. **Decidir la tensión de adopción voluntaria en un RF vinculante** (B-17). Mientras quede sin
   decidir y las cuatro coberturas percibidas alcancen el 90 %, el contraste de conformidad unánime
   fija D5 ≤ 40 y ninguna otra corrección de consistencia puede subirla.
2. **Declarar los actos que el documento presupone** (B-01, B-07): registrar un diagnóstico o una
   nota de evolución, y asignar un profesional a una franja. Son los dos huecos que cortan el
   escenario clave de Rodrigo y el de Carmen, y los que dejan P1 en 50.
3. **Declarar la actualización clínica a múltiples destinatarios** (B-14), que es el tramo de P3 que
   el enunciado del caso exige y ningún RF cubre.
4. **Cerrar las tareas incompletas de Milagros y Aníbal** (B-04, B-05, B-06, B-11, B-12): registro a
   pie de cama, recepción de la entrega de enfermería, escalamiento sin clasificación previa,
   parámetros del ventilador y toma del caso.
5. **Corregir la forma de los 19 RF no conformes** (B-15): separar los seis de doble respuesta y
   llevar al enunciado el comportamiento que hoy solo vive en un criterio de aceptación.
6. **Realinear las matrices internas con el cuerpo** (B-16) una vez declarados los actos del punto 2.
7. **Unificar el vocabulario** (B-18): distinguir profesional médico de profesional de enfermería, y
   emplear un solo criterio de permiso entre `RF-IAM-02` y `RF-REG-07`.
8. **Completar los circuitos menores** (B-02, B-03, B-08, B-09, B-10, B-13).

## Evidencia

- [`corridas/2026-08-13-additional-v2/iteracion-1/`](corridas/2026-08-13-additional-v2/iteracion-1/)
  — cuatro veredictos de persona y `diagnostico.MD` con las matrices de cobertura, P1–P3, el
  inventario de D3, las tensiones y las discrepancias.
- [`corridas/2026-08-13-additional-v2/controles.txt`](corridas/2026-08-13-additional-v2/controles.txt)
  — salida literal de `scripts/verificar.sh --sin-agentes`, código de salida 0.
- [`corridas/2026-08-13-additional-v2/corrida.json`](corridas/2026-08-13-additional-v2/corrida.json)
  — los mismos puntajes como datos, recomputados por C1.

## Resultado final: 58,7 %

La corrida se cierra en la iteración 1 por decisión del equipo: la Fase D habría reescrito
`Requirements/ReqFunc.MD` con una docena de requerimientos nuevos, y ese documento se consensúa en
grupo antes de modificarse. Las tres iteraciones que el protocolo admite no se agotaron; el 58,7 %
es el estado real del documento evaluado, no el resultado de un ciclo de corrección incompleto.

- Iteraciones ejecutadas: 1 de 3 admitidas — corrida cerrada por decisión, sin Fase D
- Veredicto final: FAILED
- Promedio final de personas: 6,1/10
- Puntaje global final: 58,7 %
- Brechas abiertas: 14 de necesidad no cubierta, más 5 de forma, trazabilidad, consistencia e
  instrumento
