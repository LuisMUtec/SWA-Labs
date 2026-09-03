# Diagnóstico — corrida 2026-08-15-iteracion-10

Evaluado: `Requirements/ReqFunc.MD` @ `42c00ba` (195 RF vigentes; `RF-DIA-44` y `RF-DIA-49` fueron
retirados y no existen). Rúbrica: `Spec/Eval-Spec.MD` @ `b492237`. Instrumento no modificado.

## Precondiciones

Las cuatro evaluaciones están presentes, cada una con un veredicto para los 195 RF vigentes, en el
mismo conjunto y orden de identificadores, y con vocabulario cerrado. Ninguna omisión y ningún
veredicto inválido. Reparto declarado y comprobado: Rodrigo 62/122/7/4, Milagros 84/105/3/3,
Carmen 94/95/3/3, Aníbal 78/114/1/2 (Sirve/Indiferente/Estorba/Ambiguo). Cobertura percibida: 80 en
las cuatro.

## Veredictos agregados

La columna «Efecto en D1» registra únicamente los veredictos que mueven el puntaje: un **Estorba**
que no traza a ninguna de las seis tareas de esa persona resta 2 en su `X_p`; uno que sí traza baja
la tarea que lo traza; un **Ambiguo** puede bajar una tarea o el flujo. Un Sirve no sube nada por sí
solo y un Indiferente no cuenta.

| RF | Rodrigo | Milagros | Carmen | Aníbal | Efecto en D1 |
|---|---|---|---|---|---|
| RF-TUR-01 | Indiferente | Indiferente | Sirve | Indiferente | — |
| RF-TUR-02 | Indiferente | Indiferente | Sirve | Indiferente | — |
| RF-TUR-03 | Indiferente | Indiferente | Sirve | Indiferente | — |
| RF-TUR-04 | Indiferente | Sirve | Sirve | Sirve | — |
| RF-TUR-05 | Indiferente | Indiferente | Sirve | Sirve | — |
| RF-TUR-06 | Sirve | Indiferente | Estorba | Indiferente | baja la tarea de Carmen que lo traza |
| RF-TUR-07 | Indiferente | Indiferente | Sirve | Sirve | — |
| RF-TUR-08 | Indiferente | Sirve | Sirve | Indiferente | — |
| RF-TUR-09 | Indiferente | Indiferente | Sirve | Indiferente | — |
| RF-TUR-10 | Indiferente | Indiferente | Sirve | Indiferente | — |
| RF-TUR-11 | Indiferente | Indiferente | Sirve | Indiferente | — |
| RF-TUR-12 | Indiferente | Indiferente | Sirve | Indiferente | — |
| RF-TUR-13 | Sirve | Indiferente | Sirve | Indiferente | — |
| RF-TUR-14 | Indiferente | Indiferente | Sirve | Indiferente | — |
| RF-TUR-15 | Estorba | Indiferente | Sirve | Indiferente | −2 en X_Rodrigo (no traza) |
| RF-TUR-16 | Indiferente | Indiferente | Sirve | Indiferente | — |
| RF-TUR-17 | Estorba | Indiferente | Sirve | Indiferente | −2 en X_Rodrigo (no traza) |
| RF-TUR-18 | Indiferente | Indiferente | Sirve | Indiferente | — |
| RF-TUR-19 | Indiferente | Indiferente | Sirve | Indiferente | — |
| RF-TUR-20 | Indiferente | Indiferente | Sirve | Indiferente | — |
| RF-TUR-21 | Indiferente | Indiferente | Sirve | Indiferente | — |
| RF-TUR-22 | Indiferente | Indiferente | Sirve | Indiferente | — |
| RF-TUR-23 | Indiferente | Indiferente | Ambiguo | Indiferente | Ambiguo para Carmen |
| RF-TUR-24 | Indiferente | Indiferente | Sirve | Indiferente | — |
| RF-TUR-25 | Indiferente | Indiferente | Sirve | Indiferente | — |
| RF-TUR-26 | Indiferente | Indiferente | Sirve | Sirve | — |
| RF-TUR-27 | Indiferente | Sirve | Sirve | Sirve | — |
| RF-TUR-28 | Indiferente | Estorba | Sirve | Indiferente | −2 en X_Milagros (no traza) |
| RF-TUR-29 | Indiferente | Indiferente | Sirve | Indiferente | — |
| RF-TUR-30 | Indiferente | Indiferente | Sirve | Indiferente | — |
| RF-TUR-31 | Estorba | Indiferente | Sirve | Indiferente | −2 en X_Rodrigo (no traza) |
| RF-TUR-32 | Sirve | Indiferente | Sirve | Indiferente | — |
| RF-TUR-33 | Sirve | Indiferente | Sirve | Indiferente | — |
| RF-TUR-34 | Indiferente | Indiferente | Sirve | Indiferente | — |
| RF-TUR-35 | Indiferente | Indiferente | Sirve | Indiferente | — |
| RF-TUR-36 | Indiferente | Indiferente | Sirve | Indiferente | — |
| RF-TUR-37 | Indiferente | Indiferente | Sirve | Indiferente | — |
| RF-TUR-38 | Indiferente | Indiferente | Sirve | Indiferente | — |
| RF-TUR-39 | Indiferente | Indiferente | Sirve | Indiferente | — |
| RF-TUR-40 | Indiferente | Indiferente | Sirve | Indiferente | — |
| RF-TUR-41 | Indiferente | Sirve | Sirve | Indiferente | — |
| RF-TUR-42 | Sirve | Sirve | Sirve | Indiferente | — |
| RF-TUR-43 | Indiferente | Indiferente | Indiferente | Indiferente | — |
| RF-TUR-44 | Indiferente | Indiferente | Sirve | Indiferente | — |
| RF-TUR-45 | Indiferente | Indiferente | Sirve | Indiferente | — |
| RF-TUR-46 | Indiferente | Indiferente | Sirve | Indiferente | — |
| RF-TUR-47 | Indiferente | Indiferente | Sirve | Indiferente | — |
| RF-TUR-48 | Indiferente | Indiferente | Sirve | Indiferente | — |
| RF-TUR-49 | Indiferente | Indiferente | Sirve | Indiferente | — |
| RF-TUR-50 | Sirve | Sirve | Sirve | Indiferente | — |
| RF-TUR-51 | Estorba | Indiferente | Sirve | Indiferente | −2 en X_Rodrigo (no traza) |
| RF-TUR-52 | Indiferente | Indiferente | Sirve | Indiferente | — |
| RF-DIA-01 | Sirve | Indiferente | Sirve | Sirve | — |
| RF-DIA-02 | Sirve | Indiferente | Indiferente | Indiferente | — |
| RF-DIA-03 | Sirve | Indiferente | Indiferente | Indiferente | — |
| RF-DIA-04 | Sirve | Indiferente | Sirve | Indiferente | — |
| RF-DIA-05 | Sirve | Indiferente | Indiferente | Sirve | — |
| RF-DIA-06 | Sirve | Sirve | Indiferente | Indiferente | — |
| RF-DIA-07 | Sirve | Indiferente | Sirve | Sirve | — |
| RF-DIA-08 | Indiferente | Sirve | Sirve | Indiferente | — |
| RF-DIA-09 | Sirve | Indiferente | Indiferente | Indiferente | — |
| RF-DIA-10 | Sirve | Indiferente | Indiferente | Indiferente | — |
| RF-DIA-11 | Indiferente | Sirve | Indiferente | Indiferente | — |
| RF-DIA-12 | Sirve | Indiferente | Sirve | Indiferente | — |
| RF-DIA-13 | Sirve | Indiferente | Indiferente | Sirve | — |
| RF-DIA-14 | Sirve | Indiferente | Indiferente | Sirve | — |
| RF-DIA-15 | Sirve | Indiferente | Indiferente | Indiferente | — |
| RF-DIA-16 | Sirve | Indiferente | Indiferente | Indiferente | — |
| RF-DIA-17 | Sirve | Indiferente | Indiferente | Indiferente | — |
| RF-DIA-18 | Sirve | Indiferente | Estorba | Indiferente | −2 en X_Carmen (no traza) |
| RF-DIA-19 | Indiferente | Sirve | Estorba | Indiferente | −2 en X_Carmen (no traza) |
| RF-DIA-20 | Sirve | Indiferente | Ambiguo | Indiferente | Ambiguo para Carmen |
| RF-DIA-21 | Sirve | Indiferente | Indiferente | Indiferente | — |
| RF-DIA-22 | Sirve | Sirve | Indiferente | Indiferente | — |
| RF-DIA-23 | Sirve | Sirve | Indiferente | Sirve | — |
| RF-DIA-24 | Indiferente | Indiferente | Sirve | Indiferente | — |
| RF-DIA-25 | Indiferente | Sirve | Indiferente | Indiferente | — |
| RF-DIA-26 | Indiferente | Sirve | Indiferente | Indiferente | — |
| RF-DIA-27 | Indiferente | Sirve | Sirve | Indiferente | — |
| RF-DIA-28 | Sirve | Indiferente | Sirve | Sirve | — |
| RF-DIA-29 | Sirve | Sirve | Indiferente | Indiferente | — |
| RF-DIA-30 | Indiferente | Sirve | Sirve | Indiferente | — |
| RF-DIA-31 | Sirve | Indiferente | Sirve | Indiferente | — |
| RF-DIA-32 | Sirve | Indiferente | Indiferente | Indiferente | — |
| RF-DIA-33 | Indiferente | Sirve | Indiferente | Indiferente | — |
| RF-DIA-34 | Sirve | Indiferente | Indiferente | Indiferente | — |
| RF-DIA-35 | Sirve | Indiferente | Indiferente | Indiferente | — |
| RF-DIA-36 | Indiferente | Indiferente | Sirve | Indiferente | — |
| RF-DIA-37 | Indiferente | Sirve | Indiferente | Indiferente | — |
| RF-DIA-38 | Indiferente | Ambiguo | Indiferente | Indiferente | Ambiguo para Milagros |
| RF-DIA-39 | Sirve | Indiferente | Indiferente | Indiferente | — |
| RF-DIA-40 | Sirve | Indiferente | Sirve | Sirve | — |
| RF-DIA-41 | Sirve | Ambiguo | Indiferente | Indiferente | Ambiguo para Milagros |
| RF-DIA-42 | Sirve | Indiferente | Indiferente | Indiferente | — |
| RF-DIA-43 | Sirve | Indiferente | Indiferente | Indiferente | — |
| RF-DIA-45 | Indiferente | Indiferente | Indiferente | Sirve | — |
| RF-DIA-46 | Indiferente | Indiferente | Sirve | Indiferente | — |
| RF-DIA-47 | Sirve | Indiferente | Sirve | Indiferente | — |
| RF-DIA-48 | Sirve | Indiferente | Indiferente | Indiferente | — |
| RF-DIA-50 | Indiferente | Sirve | Indiferente | Indiferente | — |
| RF-DIA-51 | Indiferente | Sirve | Indiferente | Indiferente | — |
| RF-ESC-01 | Sirve | Sirve | Indiferente | Sirve | — |
| RF-ESC-02 | Indiferente | Sirve | Indiferente | Sirve | — |
| RF-ESC-03 | Sirve | Sirve | Indiferente | Sirve | — |
| RF-ESC-04 | Indiferente | Sirve | Indiferente | Sirve | — |
| RF-ESC-05 | Indiferente | Sirve | Indiferente | Indiferente | — |
| RF-ESC-06 | Indiferente | Sirve | Indiferente | Sirve | — |
| RF-ESC-07 | Estorba | Sirve | Sirve | Sirve | −2 en X_Rodrigo (no traza) |
| RF-ESC-08 | Indiferente | Sirve | Sirve | Sirve | — |
| RF-ESC-09 | Indiferente | Sirve | Sirve | Sirve | — |
| RF-ESC-10 | Indiferente | Indiferente | Indiferente | Sirve | — |
| RF-ESC-11 | Indiferente | Sirve | Indiferente | Sirve | — |
| RF-ESC-12 | Indiferente | Sirve | Indiferente | Sirve | — |
| RF-ESC-13 | Ambiguo | Indiferente | Indiferente | Sirve | Ambiguo para Rodrigo |
| RF-ESC-14 | Indiferente | Sirve | Indiferente | Sirve | — |
| RF-ESC-15 | Indiferente | Sirve | Indiferente | Sirve | — |
| RF-ESC-16 | Ambiguo | Sirve | Indiferente | Sirve | Ambiguo para Rodrigo |
| RF-ESC-17 | Indiferente | Sirve | Indiferente | Sirve | — |
| RF-ESC-18 | Indiferente | Sirve | Indiferente | Sirve | — |
| RF-ESC-19 | Indiferente | Sirve | Indiferente | Sirve | — |
| RF-ESC-20 | Indiferente | Sirve | Indiferente | Indiferente | — |
| RF-ESC-21 | Indiferente | Sirve | Indiferente | Sirve | — |
| RF-ESC-22 | Indiferente | Sirve | Indiferente | Indiferente | — |
| RF-ESC-23 | Indiferente | Sirve | Sirve | Sirve | — |
| RF-ESC-24 | Ambiguo | Sirve | Indiferente | Sirve | Ambiguo para Rodrigo |
| RF-ESC-25 | Indiferente | Sirve | Indiferente | Estorba | −2 en X_Aníbal (no traza) |
| RF-ESC-26 | Indiferente | Indiferente | Sirve | Indiferente | — |
| RF-ESC-27 | Sirve | Sirve | Sirve | Sirve | — |
| RF-ESC-28 | Indiferente | Sirve | Indiferente | Sirve | — |
| RF-ESC-29 | Sirve | Sirve | Indiferente | Sirve | — |
| RF-ESC-30 | Indiferente | Sirve | Sirve | Sirve | — |
| RF-ESC-31 | Indiferente | Indiferente | Sirve | Indiferente | — |
| RF-ESC-32 | Indiferente | Sirve | Sirve | Sirve | — |
| RF-ESC-33 | Indiferente | Indiferente | Sirve | Sirve | — |
| RF-ESC-34 | Indiferente | Indiferente | Indiferente | Sirve | — |
| RF-ESC-35 | Indiferente | Sirve | Indiferente | Sirve | — |
| RF-ESC-36 | Indiferente | Estorba | Indiferente | Sirve | baja la tarea de Milagros que lo traza |
| RF-ESC-37 | Indiferente | Sirve | Indiferente | Sirve | — |
| RF-ESC-38 | Indiferente | Sirve | Indiferente | Sirve | — |
| RF-ESC-39 | Indiferente | Sirve | Indiferente | Indiferente | — |
| RF-ESC-40 | Indiferente | Sirve | Indiferente | Sirve | — |
| RF-ESC-41 | Indiferente | Sirve | Indiferente | Indiferente | — |
| RF-ESC-42 | Indiferente | Indiferente | Indiferente | Sirve | — |
| RF-ESC-43 | Indiferente | Sirve | Sirve | Sirve | — |
| RF-ESC-44 | Indiferente | Sirve | Sirve | Indiferente | — |
| RF-ESC-45 | Indiferente | Sirve | Ambiguo | Sirve | Ambiguo para Carmen |
| RF-ESC-46 | Indiferente | Sirve | Sirve | Indiferente | — |
| RF-ESC-47 | Indiferente | Sirve | Sirve | Indiferente | — |
| RF-ESC-48 | Indiferente | Indiferente | Sirve | Sirve | — |
| RF-REG-01 | Indiferente | Sirve | Indiferente | Sirve | — |
| RF-REG-02 | Sirve | Sirve | Indiferente | Sirve | — |
| RF-REG-03 | Sirve | Sirve | Indiferente | Sirve | — |
| RF-REG-04 | Indiferente | Sirve | Indiferente | Sirve | — |
| RF-REG-05 | Indiferente | Sirve | Indiferente | Sirve | — |
| RF-REG-06 | Sirve | Indiferente | Indiferente | Sirve | — |
| RF-REG-07 | Indiferente | Sirve | Indiferente | Sirve | — |
| RF-REG-08 | Sirve | Indiferente | Indiferente | Sirve | — |
| RF-REG-09 | Indiferente | Sirve | Indiferente | Sirve | — |
| RF-REG-10 | Sirve | Indiferente | Indiferente | Sirve | — |
| RF-REG-11 | Indiferente | Sirve | Indiferente | Sirve | — |
| RF-REG-12 | Sirve | Indiferente | Indiferente | Indiferente | — |
| RF-REG-13 | Sirve | Sirve | Indiferente | Sirve | — |
| RF-REG-14 | Sirve | Sirve | Indiferente | Sirve | — |
| RF-REG-15 | Sirve | Sirve | Indiferente | Sirve | — |
| RF-REG-16 | Sirve | Sirve | Indiferente | Sirve | — |
| RF-IAM-01 | Sirve | Sirve | Sirve | Sirve | — |
| RF-IAM-02 | Estorba | Ambiguo | Sirve | Sirve | baja la tarea de Rodrigo que lo traza; Ambiguo para Milagros |
| RF-IAM-03 | Indiferente | Indiferente | Sirve | Indiferente | — |
| RF-IAM-04 | Indiferente | Indiferente | Indiferente | Sirve | — |
| RF-IAM-05 | Indiferente | Indiferente | Indiferente | Sirve | — |
| RF-IAM-06 | Indiferente | Indiferente | Sirve | Indiferente | — |
| RF-IAM-07 | Indiferente | Indiferente | Indiferente | Sirve | — |
| RF-IAM-08 | Sirve | Sirve | Indiferente | Sirve | — |
| RF-IAM-09 | Indiferente | Sirve | Indiferente | Sirve | — |
| RF-IAM-10 | Sirve | Sirve | Indiferente | Indiferente | — |
| RF-IAM-11 | Indiferente | Sirve | Sirve | Sirve | — |
| RF-IAM-12 | Indiferente | Indiferente | Sirve | Sirve | — |
| RF-IAM-13 | Indiferente | Indiferente | Sirve | Indiferente | — |
| RF-IAM-14 | Sirve | Sirve | Indiferente | Indiferente | — |
| RF-IAM-15 | Sirve | Estorba | Sirve | Indiferente | baja la tarea de Milagros que lo traza |
| RF-IAM-16 | Sirve | Sirve | Indiferente | Sirve | — |
| RF-IAM-17 | Sirve | Sirve | Indiferente | Indiferente | — |
| RF-IAM-18 | Sirve | Sirve | Sirve | Indiferente | — |
| RF-IAM-19 | Sirve | Sirve | Indiferente | Indiferente | — |
| RF-IAM-20 | Indiferente | Indiferente | Indiferente | Sirve | — |
| RF-IAM-21 | Indiferente | Indiferente | Indiferente | Ambiguo | Ambiguo para Aníbal |
| RF-IAM-22 | Indiferente | Indiferente | Indiferente | Ambiguo | Ambiguo para Aníbal |
| RF-SUP-01 | Ambiguo | Indiferente | Sirve | Indiferente | Ambiguo para Rodrigo |
| RF-SUP-02 | Indiferente | Indiferente | Sirve | Indiferente | — |
| RF-SUP-03 | Indiferente | Sirve | Indiferente | Sirve | — |
| RF-SUP-04 | Indiferente | Sirve | Sirve | Indiferente | — |
| RF-SUP-05 | Indiferente | Indiferente | Sirve | Indiferente | — |
| RF-SUP-06 | Indiferente | Indiferente | Sirve | Indiferente | — |
| RF-SUP-07 | Indiferente | Indiferente | Sirve | Indiferente | — |
| RF-SUP-08 | Estorba | Indiferente | Sirve | Indiferente | baja la tarea de Rodrigo que lo traza |

## Daño fuera de tarea — `X_p`, RF por RF

`X_p` cuenta los RF que el agente marcó **Estorba** y que **no** figuran en ninguna de las seis filas
de esa persona en la matriz de trazabilidad de `ReqFunc.MD` (§Matriz de trazabilidad, líneas 3287 a
3310). Cada uno resta 2. La comprobación es fila por fila, no estimada.

### Rodrigo — 7 Estorba, `X_Rodrigo = 5`

| RF marcado Estorba | ¿Figura en alguna fila de Rodrigo? | Dónde | Resta |
|---|---|---|---:|
| RF-TUR-15 | **No** | solo traza a Carmen (persona declarada: Carmen) | −2 |
| RF-TUR-17 | **No** | fila «Carmen · Aprobar o rechazar intercambios y permisos» | −2 |
| RF-TUR-31 | **No** | fila «Carmen · Aprobar o rechazar intercambios y permisos» | −2 |
| RF-TUR-51 | **No** | fila «Carmen · Elaborar y publicar la programación mensual» | −2 |
| RF-ESC-07 | **No** | fila «Aníbal · Marcarse temporalmente indisponible y delegar» | −2 |
| RF-IAM-02 | Sí | fila «Rodrigo · Registrar nota de evolución y diagnóstico por paciente» | 0 |
| RF-SUP-08 | Sí | fila «Rodrigo · Cerrar y firmar la entrega de turno» | 0 |

Los cinco que no trazan son fricción pura para un rotante: dos convierten el mero hecho de abrir una
pantalla en su confirmación de lectura sobre una PC compartida (RF-TUR-15, RF-TUR-51), dos le
devuelven a la coordinadora cada intercambio que pacta con un colega (RF-TUR-17, RF-TUR-31) y uno le
permite ser nombrado delegado sin haberlo aceptado (RF-ESC-07). `X_Rodrigo = 5` → **−10 puntos de
tarea**, el término que más pesa en toda la corrida.

### Milagros — 3 Estorba, `X_Milagros = 1`

| RF | ¿Traza? | Dónde | Resta |
|---|---|---|---:|
| RF-TUR-28 | **No** | ninguna fila de Milagros | −2 |
| RF-ESC-36 | Sí | fila «Ver y confirmar indicaciones médicas vigentes» | 0 |
| RF-IAM-15 | Sí | fila «Registrar eventos y administración de medicamentos» | 0 |

### Carmen — 3 Estorba, `X_Carmen = 2`

| RF | ¿Traza? | Dónde | Resta |
|---|---|---|---:|
| RF-TUR-06 | Sí | fila «Aprobar o rechazar intercambios y permisos» | 0 |
| RF-DIA-18 | **No** | ninguna fila de Carmen | −2 |
| RF-DIA-19 | **No** | ninguna fila de Carmen | −2 |

### Aníbal — 1 Estorba, `X_Aníbal = 1`

| RF | ¿Traza? | Dónde | Resta |
|---|---|---|---:|
| RF-ESC-25 | **No** | ninguna fila de Aníbal | −2 |

## Matriz de cobertura

Escala: 5 cubierta · 3 incompleta · 1 aparente · 0 descubierta. El texto de la tarea es el literal de
`Personas/*.MD`; los RF son los de la matriz de trazabilidad de `ReqFunc.MD`.

| Persona | Tarea crítica | RF que la cubre (extracto) | Veredicto | Puntos | Estado |
|---|---|---|---|---:|---|
| Rodrigo | Recibir el handoff estructurado de todas las camas asignadas | RF-DIA-02, 03, 09, 10, 17, 18, 28, 29, 32, 35, 39, 42, 48 | 13 Sirve | 3 | Incompleta — RF-DIA-18 le obliga a declarar camas y RF-DIA-28 solo repone al inicio del turno: entra sin saber si responde por cuatro o por diez hasta que alguien declare. Su criterio «el handoff incluye decisiones y su justificación» no queda satisfecho |
| Rodrigo | Consultar la evolución y el diagnóstico del turno anterior | RF-DIA-02, 05, 07, 10, 13, 14, 15, 21, 23, 40, 42, 43 | 12 Sirve | 3 | Incompleta — ningún enunciado obliga a que la decisión clínica exista: RF-DIA-40 exige el fundamento solo si se registra y RF-DIA-34 declara que su ausencia no condiciona la firma |
| Rodrigo | Registrar nota de evolución y diagnóstico por paciente | RF-DIA-07, 13, 14, 15, 16, 40, RF-REG-02, RF-IAM-01, 02, 09, 10, 14, 15, 17, 18, 19 | 14 Sirve · RF-IAM-02 **Estorba** · RF-IAM-09 Indiferente | 3 | Incompleta — RF-IAM-02 le rechaza el registro sobre una cama ajena ante un deterioro que nadie escaló todavía, y RF-IAM-09 solo abre esa puerta después de una toma del caso |
| Rodrigo | Marcar pacientes inestables o con pendientes críticos | RF-DIA-06, 22, 41 | 3 Sirve | 5 | Cubierta — marca, permanencia, consulta y aviso de retiro están declarados; el agente la da por cubierta |
| Rodrigo | Consultar resultados de laboratorio e imágenes | RF-REG-06, 10, 12, 14, 15, 16, RF-ESC-29 | 7 Sirve | 5 | Cubierta — el agente declara «aquí no veo hueco» |
| Rodrigo | Cerrar y firmar la entrega de turno | RF-DIA-01, 04, 12, 20, 24, 31, 34, 47, RF-TUR-42, 50, RF-SUP-01, 08 | 9 Sirve · RF-SUP-01 **Ambiguo** · RF-SUP-08 **Estorba** · RF-DIA-24 Indiferente | 3 | Incompleta — RF-SUP-08 rotula con su nombre ante la jefatura cada cierre posterior al término, que es la vía que RF-DIA-20 y RF-DIA-47 le conceden como normal; RF-SUP-01 habla de datos obligatorios en plural |
| Milagros | Registrar signos vitales y balance por paciente | RF-REG-01, 02, RF-IAM-01, 08, 16 | 5 Sirve | 3 | Incompleta — RF-IAM-16 promete no exigirle otro dispositivo ni apartarse de la cama, pero ningún enunciado declara cuál es el dispositivo de pie de cama del que esa promesa depende |
| Milagros | Escalar un deterioro clínico al médico responsable | RF-ESC-01, 06, 11, 14, 15, 20, 21, 22, 23, 25, 27, 35, 37, 39, 40, 43, 44, 46, 47, RF-DIA-29, RF-IAM-16 | 21 Sirve | 5 | Cubierta — emisión junto a la cama sin clasificar, cadena compuesta, avance automático, agotamiento con destinatario y preservación sin conexión; sus cuatro criterios relacionados quedan satisfechos |
| Milagros | Consultar quién está de guardia y su estado de disponibilidad | RF-ESC-08, 27, 32, 35, 41, 43 | 6 Sirve | 3 | Incompleta — nada le avisa cuando el responsable clínico cambia por delegación, revocación o vencimiento; RF-ESC-41 solo la alcanza cuando la cama queda sin ninguno |
| Milagros | Ver y confirmar indicaciones médicas vigentes | RF-REG-03, 04, 13, RF-ESC-28, 36, 38, RF-IAM-16 | 6 Sirve · RF-ESC-36 **Estorba** | 3 | Incompleta — RF-ESC-36 mete en el mismo canal de alcance junto a la cama cada solicitud de estudio (RF-REG-14) y cada resultado no crítico (RF-REG-16) de las diez camas |
| Milagros | Registrar eventos y administración de medicamentos | RF-REG-05, RF-IAM-02, 08, 10, 14, 15, 16, 17, 18, 19 | 8 Sirve · RF-IAM-02 **Ambiguo** · RF-IAM-15 **Estorba** | 3 | Incompleta — RF-IAM-02 condiciona su registro a un «turno de enfermería en curso» que ningún enunciado constituye, y RF-IAM-15 deja el dato clínico fuera del episodio |
| Milagros | Recibir y entregar el turno de enfermería | RF-DIA-08, 11, 19, 25, 26, 27, 30, 33, 37, 38, 50, 51, RF-SUP-07 | 11 Sirve · RF-DIA-38 **Ambiguo** · RF-SUP-07 Indiferente | 3 | Incompleta — las marcas vigentes de inestabilidad y de pendiente crítico no integran la enumeración de su entrega, y RF-DIA-38 no declara por dónde le llega el aviso |
| Carmen | Elaborar y publicar la programación mensual de turnos | RF-TUR-04, 09, 10, 11, 27, 28, 46, 51, 52, RF-IAM-13 | 10 Sirve | 3 | Incompleta — RF-TUR-03 se dispara al solicitar cobertura y no al armar la propuesta, y RF-TUR-10 solo declara qué ocurre con una propuesta completa: publicar con franjas sin nombre no está cubierto |
| Carmen | Validar que no existan cruces ni franjas descubiertas | RF-TUR-01, 02, 07, 42, 45, 48, 50, RF-ESC-26, 30, 31, 33, 45, 48, RF-DIA-46, RF-IAM-12 | 14 Sirve · RF-ESC-45 **Ambiguo** | 3 | Incompleta — sus dos criterios se cumplen (RF-TUR-01 impide, RF-TUR-07 muestra el horizonte), pero RF-ESC-45 dirige la solicitud a todos los elegibles a la vez sin declarar qué ocurre si más de uno acepta, que es un cruce que ella tendría que desenredar |
| Carmen | Aprobar o rechazar intercambios y permisos | RF-TUR-06, 12, 13, 17, 21, 22, 29, 30, 31, 32, 33, 34 | 11 Sirve · RF-TUR-06 **Estorba** | 3 | Incompleta — el permiso le queda íntegro; el intercambio, partido: RF-TUR-06 aplica sin ella lo que su autorización cubre y RF-TUR-34 se lo cuenta después |
| Carmen | Reasignar cobertura ante una ausencia imprevista | RF-TUR-03, 05, 18, 19, 20, 25, 26, 35, 36, 37, 38, 39, 40, 41, 43, 44, 47, RF-DIA-36, RF-IAM-13 | 18 Sirve · RF-TUR-43 Indiferente | 3 | Incompleta — su criterio «cubrir una ausencia toma minutos» no se cumple: RF-TUR-20 dirige la solicitud de a un candidato y RF-TUR-44 exige que ninguna solicitud permanezca vigente antes de habilitarla a asignar |
| Carmen | Monitorear cumplimiento y completitud de entregas de turno | RF-DIA-12, 24, RF-SUP-01, 07, 08 | 5 Sirve | 3 | Incompleta — acepta el camino alterno (RF-DIA-01 impide el cierre incompleto), pero declara no saber qué mide su cumplimiento porque RF-DIA-20, que marcó **Ambiguo**, admite la firma dentro del propio turno |
| Carmen | Generar indicadores de cobertura para la Dirección de Red | RF-SUP-02, 05 | 2 Sirve | 5 | Cubierta — RF-SUP-02 declara «sin transcripción manual» y el glosario define qué mide cada indicador (ver refutación más abajo) |
| Aníbal | Recibir la alerta de escalamiento con contexto clínico adjunto | RF-ESC-03, 16, 24, RF-IAM-04, 05, 07, 08, 11, 12, 16, 20, 21, 22 | 11 Sirve · RF-IAM-21 y RF-IAM-22 **Ambiguo** | 3 | Incompleta — RF-ESC-03 le entrega los nueve componentes, pero ningún enunciado le presenta a él de qué camas quedó responsable por RF-ESC-43: esa lista va a la jefatura (RF-TUR-49, RF-DIA-46) |
| Aníbal | Confirmar recepción y tomar el caso | RF-ESC-04, 12, 14, 19 | 4 Sirve | 5 | Cubierta — acuse, toma, devolución inmediata a quien escaló y cierre con desenlace; el agente no reclama nada aquí |
| Aníbal | Consultar tendencia de signos, ventilación y última evolución | RF-REG-08, RF-DIA-05, 45 | 3 Sirve | 3 | Incompleta — el contenido está entero, pero su criterio relacionado «decidir si acude con el contexto ya recibido» traza en el propio documento a RF-IAM-21 y RF-IAM-22, que él marcó Ambiguos |
| Aníbal | Registrar la indicación dada de forma remota | RF-REG-07, 09, 11, 13, 14, RF-ESC-37, RF-IAM-02, 05, 07, 08, 09, 16 | 12 Sirve | 5 | Cubierta — el agente la declara «la tarea mejor resuelta de las seis»: registro con autoría desde el dispositivo personal, alcance a enfermería y devolución de la confirmación |
| Aníbal | Marcarse temporalmente indisponible y delegar | RF-ESC-07, 17, 30, 31, 32, 34, 35, 40, 42, 45, 48 | 11 Sirve | 3 | Incompleta — marcarse está resuelto; delegar no: RF-ESC-30 CA-2 describe la noche en que él es el único asignado y entonces ningún delegado es admisible |
| Aníbal | Revisar en la mañana lo ocurrido durante la noche | RF-SUP-03 | 1 Sirve | 5 | Cubierta — RF-SUP-03 CA-1 le da en un solo lugar eventos, escalamientos con recorrido y desenlace, indicaciones a distancia e ingresos y egresos de las dos sedes (ver refutación más abajo) |

Σ tareas: **Rodrigo 22 · Milagros 20 · Carmen 20 · Aníbal 24**. Ninguna tarea en 0 en ninguna persona,
de modo que el techo de D1 ≤ 50 no se activa.

## Recorrido del escenario clave y puntaje de flujo

Escala: 4 = recorrido entero y ningún paso apoyado en un RF Ambiguo · 2 = completo pero algún paso se
apoya en un Ambiguo · 0 = se interrumpe.

| Persona | Recorrido | Paso exacto | RF | Flujo |
|---|---|---|---|---:|
| Rodrigo | Completo, 15 pasos, sin cortes | Paso 14 — «me llegan los resultados» | RF-ESC-13 vía RF-REG-16 | **2** |
| Milagros | Completo, 14 pasos, sin cortes | Paso 2 — registrar signos y evento junto a la cama | RF-IAM-02 | **2** |
| Carmen | Completo, 12 pasos, sin cortes | Paso 5 — obtener los candidatos elegibles | RF-TUR-23 | **2** |
| Aníbal | Completo, 12 pasos, sin cortes | Paso 5 — abrir el aviso en el celular personal | RF-IAM-21 y RF-IAM-22 | **2** |

**Rodrigo — por qué 2 y no 4.** El agente declara que el apoyo en RF-ESC-13 «no es indispensable»
porque el resultado llega igual por RF-REG-06. La sustitución no es equivalente: RF-REG-06 entrega
los resultados **cuando un profesional consulta la cama**, mientras que el paso 14 tal como él lo
recorre es el alcance del resultado sin consultarlo, agrupado en la actualización informativa —que es
justamente la conducta que RF-ESC-13 declara y que él no puede leer de una sola manera («lo nuevo
desde mi última mirada o todo lo acumulado»). El paso sigue apoyado en un Ambiguo aunque exista una
vía más costosa que no lo esté; la escala no admite excepción por prescindibilidad, y ante la duda se
penaliza. **Flujo 2.**

**Carmen — por qué 2 y no 4.** El agente acota el apoyo ambiguo al caso en que el reemplazo es un
rotante y declara limpio el paso con personal de planta. La acotación no lo salva: su propia persona
fija que «Carmen no tiene autoridad sobre los rotantes que asigna la Red; los recibe como un dato»,
y ella misma sitúa el apoyo ambiguo «en el caso más frecuente de mi unidad». Un flujo que solo es
limpio en la rama favorable de una bifurcación que el propio agente declara minoritaria no cumple
«cada paso se sostiene en un RF explícito». **Flujo 2.**

## Cómputo de D1 — cada operación

```
Puntaje_p = máx(0, Σ tareas_p − 2 × X_p) / 5 + Flujo_p

Rodrigo   = máx(0, 22 − 2×5) / 5 + 2 = máx(0, 12) / 5 + 2 = 2,4 + 2 = 4,4
Milagros  = máx(0, 20 − 2×1) / 5 + 2 = máx(0, 18) / 5 + 2 = 3,6 + 2 = 5,6
Carmen    = máx(0, 20 − 2×2) / 5 + 2 = máx(0, 16) / 5 + 2 = 3,2 + 2 = 5,2
Aníbal    = máx(0, 24 − 2×1) / 5 + 2 = máx(0, 22) / 5 + 2 = 4,4 + 2 = 6,4

promedio  = (4,4 + 5,6 + 5,2 + 6,4) / 4 = 21,6 / 4 = 5,4
D1        = 5,4 × 10 = 54,0
```

## Cobertura de P1, P2 y P3 — D2

| Problema | RF asociados | Comportamiento que lo resuelve | Puntos |
|---|---|---|---:|
| P1 — Rotación de doctor | 121 RF declaran P1; el núcleo es RF-DIA-01, 02, 03, 07, 10, 12, 17, 20, 24, 31, 32, 42, 47 y RF-SUP-01, 08 | RF-DIA-07 registra el diagnóstico con autoría e instante y RF-DIA-01 impide cerrar la entrega si falta el de alguna cama asignada; RF-DIA-31 compone el resto sin transcripción; RF-DIA-10 lo entrega al entrante sin depender del saliente y RF-DIA-17 impide confundir una entrega vieja con la ausente. Las ramas de falla también tienen enunciado: RF-DIA-12 dice qué cama bloquea, RF-DIA-32 y RF-DIA-42 rescatan lo registrado en un turno cerrado sin entrega, RF-DIA-47 admite el registro tardío, RF-DIA-24 advierte a la jefatura y RF-SUP-08 informa el cierre posterior. Ningún tramo queda sin RF | **100** |
| P2 — Medianoche | 66 RF declaran P2; el núcleo es RF-ESC-01, 02, 03, 04, 06, 07, 08, 09, 12, 20, 23, 25, 27, 32, 33, 40, 43, 45, 46, 47 y RF-IAM-04, 05, 07, 08, 11, 16 | Contactar rápido: RF-ESC-20 emite junto a la cama, RF-ESC-23 compone la cadena con la programación vigente y el orden de rotación, RF-ESC-27, 35 y 43 constituyen al responsable y RF-IAM-11 fija los medios de contacto vigentes. Manejar la indisponibilidad: RF-ESC-32 la registra aun sin delegado, RF-ESC-07 activa la delegación, RF-ESC-40 saltea al indisponible, RF-ESC-02 avanza la cadena sin intervención, RF-ESC-45 sale a buscar cobertura, RF-ESC-09 y 44 cierran en la jefatura o su delegado y RF-ESC-46 y 47 cubren la cadena vacía y la reiteración. Ningún tramo queda sin RF; la ambigüedad de RF-IAM-21 y RF-IAM-22 se penaliza en D1 y no aquí | **100** |
| P3 — Actualizaciones en tiempo real | 25 RF declaran P3; el núcleo es RF-ESC-13, 22, 28, 29, 36, 38, 41 y RF-REG-01 a 05, 13 a 16, RF-IAM-16, 18, 19 | El aviso a varios está resuelto: RF-ESC-28, 29, 36, 38 y 41 alcanzan junto a la cama a enfermería y al responsable sin que deban consultarlo, y RF-ESC-16 y 24 ordenan e identifican las clases. **La persistencia con disponibilidad permanente queda a medias:** RF-IAM-15 retiene fuera del episodio, por tiempo indefinido, todo registro producido en el equipo compartido sin identidad verificada propia, y el único enunciado que lo rescata —RF-IAM-18— exige que su autor lo declare propio **en ese mismo equipo**; si el autor se fue, RF-IAM-19 solo presenta la condición en esa máquina y ningún RF lleva ese dato clínico al episodio. Dos agentes lo declaran de forma independiente (Rodrigo: «una nota retenida no llega nunca al médico entrante»; Milagros: «ese dato no está en la cama cuando el médico la consulta minutos después»). Además, cuando la unidad está sin conexión RF-ESC-39 presenta la condición de escalamiento no alcanzado pero ningún RF declara qué ocurre entretanto. Tramo sin RF que lo cubra | **50** |

```
D2 = (100 + 100 + 50) / 3 = 250 / 3 = 83,3
```

Ningún problema queda en 0, de modo que el techo de D2 ≤ 60 no se activa.

## D3 — Verificabilidad y forma

Los ocho controles de `scripts/verificar.sh` devuelven vacío: M1 (auxiliar DEBE), M2 (sujeto del
DEBE), M3 (mecanismo o producto nombrado) y M4 pasan, y E2 confirma que los 195 RF declaran
enunciado, prioridad, persona, problema y criterios. Eso deja las condiciones 1, 3, 4, 5 y 6
satisfechas en los 195. La condición 7 se comprobó de forma exhaustiva: ningún criterio de aceptación
del documento contiene más de un par Cuando/Entonces. Quedan por juzgar a mano las condiciones 2 y 8.

| ID | Condición de D3 incumplida | Corrección propuesta |
|---|---|---|
| RF-REG-14 | **2 — una sola respuesta.** El enunciado incorpora la solicitud de un estudio a dos artefactos distintos: «a ese episodio **y** a la actualización informativa de esa cama». Son dos comportamientos separables, y el propio documento lo demuestra: RF-REG-16 dedica un RF entero a la segunda incorporación para el caso del resultado no crítico. CA-1 y CA-2 demuestran la primera respuesta y CA-3 la segunda por separado | Partir en dos: un RF que incorpore la solicitud al episodio con su autoría e instante, y otro que la incorpore a la actualización informativa de esa cama, con el mismo disparador |

Se examinaron y se dan por conformes los demás candidatos: los criterios negativos que demuestran que
la regla no dispara fuera de su condición (RF-DIA-01 CA-2, RF-DIA-03 CA-2, RF-DIA-28 CA-2, RF-TUR-01
CA-2, RF-TUR-05 CA-2, RF-TUR-38 CA-2, RF-TUR-39 CA-2, RF-TUR-51 CA-2, RF-ESC-02 CA-2, RF-ESC-40 CA-2,
RF-ESC-47 CA-2, RF-ESC-48 CA-2, RF-REG-06 CA-2, RF-REG-10 CA-2, RF-REG-16 CA-2, RF-IAM-19 CA-2) son
pruebas de borde de un contrato que el enunciado declara cerrado, no ampliaciones; los enunciados con
punto y coma (RF-ESC-03, RF-REG-08, RF-SUP-03) separan elementos de una enumeración cerrada bajo una
sola respuesta, no condiciones; y las enumeraciones que los criterios de RF-DIA-02, RF-DIA-21,
RF-DIA-31 y RF-DIA-05 despliegan están fijadas en `docs/GLOSARIO.md` bajo «Estado clínico de una
cama» y «Último contacto», de modo que demuestran el contrato en vez de ampliarlo.

```
D3 = 194 / 195 × 100 = 99,5
```

## D4 — Trazabilidad

- **70 × proporción de RF con persona y problema existentes.** Los 195 declaran ambos campos; las
  personas citadas pertenecen a las cuatro modeladas y los problemas a {P1, P2, P3}. 195/195 → **70**.
- **30 × proporción de las 24 tareas con al menos 1 punto en D1.** Las 24 obtuvieron 3 o 5. 24/24 →
  **30**.
- **−10 por cada fila de matriz interna desfasada.** Se comprobaron las siete matrices del documento:
  la de trazabilidad (24 filas; el texto de cada tarea es literal al de `Personas/*.MD` y todo RF
  citado declara esa persona en su campo `Persona`), la de criterios de éxito (23 filas, misma
  comprobación), la de problemas críticos (P1 121, P2 66, P3 25 — coinciden exactamente, sin sobrantes
  ni faltantes, con los RF cuyo campo `Problema` declara ese problema), la de preguntas del enunciado,
  la de origen normativo, la de decisión de tensiones y la de distribución de prioridad (65 + 128 + 2 =
  195; 33,3 % / 65,6 % / 1,0 %). Las referencias a `RNF-USA-01`, `RNF-USA-02`, `RNF-SEG-03`,
  `RNF-DIS-01` y `RNF-DIS-02` existen en `ReqNoFunc.MD`. **Ninguna fila desfasada: −0**.

```
D4 = 70 + 30 − 0 = 100,0
```

## Requerimientos huérfanos

| ID | Por qué no traza a nadie |
|---|---|
| — | Ninguno. Los 195 RF declaran persona y problema existentes |

## Requerimientos mal ubicados

| ID | Por qué no es funcional | Documento que le corresponde |
|---|---|---|
| — | Ninguno. Ningún RF enuncia solo un umbral: los plazos que los enunciados invocan («dentro del plazo definido para la severidad», «el horizonte definido para la urgencia») se declaran expresamente remitidos a `ReqNoFunc.MD`, y el comportamiento queda en este documento | — |

## D5 — Consistencia y tensiones decididas

### Tensiones sin decidir

| Tensión | Por qué ningún RF la resuelve |
|---|---|
| — | Ninguna. Las cinco están decididas en RF, y la decisión adoptada está enunciada en §Decisión de tensiones |

Comprobación una por una: **Velocidad frente a completitud** se decide en RF-DIA-01 (el cierre exige
el diagnóstico y ningún otro dato), RF-DIA-31 (el resto se compone sin transcripción), RF-DIA-40 (el
fundamento se exige en el acto que registra la decisión, no en el cierre) y RF-DIA-34 (el señalamiento
no condiciona la firma). **Sensibilidad del escalamiento** se decide en RF-ESC-11 y RF-ESC-25
(escalar sin clasificar, con el plazo del deterioro inmediato: el lado de Milagros) contra RF-ESC-24 y
RF-ESC-16 (la selectividad se preserva en la presentación, no en el plazo: el lado de Aníbal).
**Autonomía de intercambio** se decide en RF-TUR-13 y RF-TUR-06 frente a RF-TUR-31. **Adopción
voluntaria** se decide en RF-TUR-08 y en los dos reflejos no editables de RF-TUR-28 y RF-TUR-16.
**Movilidad frente a control de datos** se decide en RF-IAM-04 (el aviso previo sin nombre ni
documento), RF-IAM-08, RF-IAM-16, RF-IAM-21 y RF-IAM-22. **60/60**.

Los dos techos duros no se activan: el repositorio **tiene** glosario (`docs/GLOSARIO.md`, 94
términos), de modo que D5 no queda limitada a 80; y las cuatro coberturas percibidas son 80, por
debajo de 90, de modo que el contraste de conformidad unánime no aplica el techo de 40.

### Hallazgos independientes del segundo tramo — 40 − 10 por cada uno

| # | Hallazgo | Evidencia |
|---|---|---|
| 1 | **Titularidad inconsistente del acto de consultar una cama.** Cinco RF del mismo acto admiten cinco conjuntos distintos de titulares: RF-REG-06 y RF-REG-10 admiten a «un profesional» sin restricción; RF-DIA-22 igual; RF-DIA-21 solo al médico «de su asignación médica vigente»; RF-DIA-23 al responsable clínico, al médico con asignación y al alcanzado por un escalamiento; RF-DIA-45 al responsable clínico, al de toma del caso y al alcanzado; RF-REG-12 al responsable clínico, al de asignación y al de toma, pero no al alcanzado | uso inconsistente del vocabulario que RF-IAM-02 y el glosario fijan |
| 2 | **La asignación de cuidado de enfermería se puede vaciar durante el turno y ningún RF la repone.** RF-DIA-19 permite a la enfermera acotar su asignación a las camas que declara; RF-DIA-30 solo actúa al iniciar el turno. Las camas que salen dejan de recibir RF-ESC-28, RF-ESC-38 y RF-ESC-41, cuyas garantías están redactadas «a las profesionales de enfermería con asignación de cuidado vigente sobre ella»: sin ninguna, la garantía se evapora sin que ningún enunciado lo declare | contradicción funcional; declarada de forma independiente por Milagros (necesidad no cubierta y riesgo) y por Carmen (RF-DIA-19 Estorba) |
| 3 | **La actualización informativa es el único artefacto del documento con contrato abierto.** RF-ESC-13 la constituye con tres clases de cambio sin decir «exactamente», RF-REG-14 le incorpora las solicitudes de estudio y RF-REG-16 los resultados no críticos; ningún enunciado declara el conjunto ni qué obtiene quien la consulta. `docs/CONVENCIONES.md` §2 exige contratos cerrados y el resto del documento los cierra | Rodrigo lo marca Ambiguo en RF-ESC-13 por exactamente esta razón |
| 4 | **RF-SUP-01 habla de «cada cama y dato obligatorio ausente» en plural.** El glosario fija «Dato obligatorio de la entrega médica … es uno solo: el diagnóstico de ese turno de esa cama» | uso inconsistente del vocabulario; Rodrigo lo marca Ambiguo por esto |
| 5 | **RF-TUR-44 y RF-TUR-47 atribuyen a «la jefatura de la unidad» funciones que el glosario reserva a «la coordinadora».** El glosario asigna a la coordinadora «elaborar y publicar su programación vigente … y procurar la cobertura de sus franjas», y reserva la denominación de jefatura para la conducción; ambos RF hacen que la jefatura asigne cobertura y sustituya profesionales sobre la programación vigente | uso inconsistente del vocabulario |

```
Segundo tramo = máx(0, 40 − 5 × 10) = 0
D5 = 60 + 0 = 60,0
```

## D6 — Priorización realista

- **Resta 10 por cada RF sin prioridad o con prioridad fuera de MUST/SHOULD/COULD:** ninguno. La
  distribución es 65 MUST (33,3 %) + 128 SHOULD (65,6 %) + 2 COULD (1,0 %) = 195, con gradiente real,
  de modo que `prioridad_uniforme` es `false` y el techo de D6 ≤ 60 no se activa. **−0**.
- **Resta 5 por cada MUST no reservado:** se recorrieron los 65. Sesenta y tres resisten la prueba —su
  ausencia dejaría un problema crítico sin resolver o una tarea crítica descubierta—. Dos no:

| MUST no reservado | Por qué su ausencia no deja descubierta ninguna tarea ni sin resolver ningún problema |
|---|---|
| RF-DIA-19 | Sin él ninguna enfermera podría acotar su asignación de cuidado, pero RF-DIA-30 ya la constituye al iniciar el turno sobre toda cama con episodio abierto sin responsable, RF-DIA-37 resuelve la segunda declaración y RF-IAM-02 CA-2 admite el registro de la enfermera con turno en curso sobre cualquier cama de su unidad. La tarea «Recibir y entregar el turno de enfermería» sigue cubierta por RF-DIA-08, 11, 27, 50 y 51. El documento además invierte la escala: la garantía constitutiva (RF-DIA-30) es SHOULD y la partición optativa (RF-DIA-19) es MUST, al revés que en el lado médico, donde RF-DIA-28 es MUST |
| RF-IAM-15 | Su ausencia haría que el registro producido en un equipo compartido sin identidad propia quedara atribuido a la identidad vigente en él por RF-IAM-01 —un defecto de atribución grave, pero ni P1 ni P3 quedan sin resolver por eso (el diagnóstico sigue disponible) ni ninguna tarea crítica queda descubierta: Rodrigo y Milagros ejercen las suyas verificando su identidad, que RF-IAM-08 y RF-IAM-14 garantizan. El propio documento lo declara de origen normativo (SUSALUD — atribución cierta del registro clínico) y no de una tarea crítica. Es además el MUST que dos agentes marcan Estorba, y su rango es lo que hace dura la retención |

```
D6 = 100 − 0 − 5 × 2 = 90,0
```

## Contrastes cruzados

### Discrepancia percibido/computado

| Persona | Percibida | Computada (Puntaje × 10) | Δ | Qué falla: el agente o las tareas críticas |
|---|---:|---:|---:|---|
| Rodrigo | 80 | 44 | **36** | El agente. Su tabla es rigurosa y sus siete Estorba están bien fundados, pero su autoinforme del 80 % pondera solo lo que le sirve dentro de sus seis tareas y no descuenta la fricción que él mismo documenta fuera de ellas —cinco Estorba que no trazan a ninguna—. Sus tareas críticas están bien enunciadas: son observables y la matriz las cubre |
| Milagros | 80 | 56 | **24** | El agente. Declara 84 Sirve y una percibida del 80 %, pero sus propias necesidades no cubiertas alcanzan a cuatro de sus seis tareas. La percibida está por encima de lo que su propio texto sostiene |
| Carmen | 80 | 52 | **28** | El agente. Es la persona con más Sirve (94) y la que más gaps declara (ocho necesidades no cubiertas). Su percibida refleja el volumen de RF que la sirven, no el estado de sus tareas |
| Aníbal | 80 | 64 | **16** | Sin discrepancia reportable (Δ ≤ 20) |

Tres de las cuatro superan los 20 puntos. En las tres prevalece el valor computado. El patrón —cuatro
percibidas idénticas en 80 y tres desviaciones al alza— sugiere que la cobertura percibida se está
declarando como una cifra de convención y no como una medición, y conviene revisarlo en el
instrumento antes de la próxima corrida.

### Conformidad unánime

Las cuatro percibidas son 80, por debajo del umbral de 90, y además ninguna tensión queda sin decidir.
El contraste no se activa y D5 no queda limitada a 40. Aun así se deja constancia de que el
documento **no** esquivó las tensiones: RF-ESC-25 y RF-ESC-36 son Estorba para Aníbal y para Milagros
respectivamente, y RF-TUR-06, RF-DIA-18 y RF-DIA-19 lo son para Carmen. Que cada tensión deje a
alguien inconforme es la señal de que se decidió.

### Necesidad no cubierta sin brecha

Las 23 necesidades no cubiertas que los cuatro agentes declaran están todas resueltas: 21 aparecen
como fila de la tabla de brechas de `Spec/Eval-Report.MD` y 2 quedan refutadas aquí por escrito.

| Necesidad declarada | Refutación |
|---|---|
| Carmen: «Conocer qué mide el indicador de cobertura de turnos que RF-SUP-02 produce y RF-SUP-05 me entrega» | `docs/GLOSARIO.md` lo define: «Indicador de cobertura de turnos: Relación entre las franjas descubiertas y las franjas requeridas de una unidad en un periodo», y define igualmente el de cumplimiento de entrega. Los términos del dominio se emplean en `ReqFunc.MD` con el significado que el glosario fija, según declara su propia cabecera |
| Aníbal: «Enterarme de un evento nocturno que se resolvió sin escalarme» | `docs/GLOSARIO.md` define «Ámbito de responsabilidad» comprendiendo las unidades de sus turnos, y añade expresamente que «un turno comprende la unidad de su franja aunque no comprenda ninguna asignación de camas». RF-SUP-03 presenta «los eventos clínicos … ocurridos en **las unidades** que ese ámbito comprendía en ese periodo», no solo lo que le fue escalado. Los eventos resueltos sin alcanzarlo están comprendidos |

## Cálculo global

| Dimensión | Puntaje | Peso | Aporte |
|---|---:|---:|---:|
| D1 Satisfacción de las personas | 54,0 | 30 % | 16,200 |
| D2 Cobertura de problemas críticos | 83,3 | 25 % | 20,825 |
| D3 Verificabilidad y forma | 99,5 | 20 % | 19,900 |
| D4 Trazabilidad | 100,0 | 10 % | 10,000 |
| D5 Consistencia y tensiones | 60,0 | 10 % | 6,000 |
| D6 Priorización | 90,0 | 5 % | 4,500 |
| **Suma de aportes** | | | **77,425 → 77,4** |

## Veredicto

| # | Condición | Umbral | Obtenido | Cumple |
|---|---|---:|---:|:---:|
| 1 | Puntaje global | ≥ 80,0 % | 77,4 % | ✗ |
| 2 | D1 | ≥ 80,0 | 54,0 | ✗ |
| 3 | Persona más baja | ≥ 7,0/10 | 4,4 (Rodrigo) | ✗ |
| 4 | D2 | ≥ 80,0 | 83,3 | ✓ |
| 5 | Controles de `verificar.sh` | 9/9 | 8/9 | ✗ |

M1 a M4 y E1 a E4 devuelven vacío. C1 queda en rojo por un artefacto de ordenamiento del propio
control —identifica la última corrida ordenando los nombres de directorio como texto, y
`iteracion-10` ordena antes que `iteracion-5`, de modo que compara el porcentaje del README contra
`iteracion-9`, que cerró en 80,9—. No es una discrepancia aritmética: las seis comprobaciones de
fórmula y los cinco techos duros pasan sobre `corrida.json`. La corrección cae en `scripts/`, que es
de solo lectura durante una corrida, y queda registrada en `bloqueos.MD`.

**FAILED.** Fallan cuatro de las cinco. El global no se redondeó hacia arriba en ningún tramo: D2 se
declara 83,3 (recomputado 83,333), D3 se declara 99,5 (recomputado 99,487) y el global 77,4
(recomputado 77,425), todos por debajo del recomputado o dentro de la tolerancia del control.

## Evaluaciones de agente ausentes o inválidas

| Persona | Qué falta |
|---|---|
| — | Ninguna. Las cuatro evaluaciones están completas, con 195 veredictos cada una y vocabulario cerrado |
