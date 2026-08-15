# Diagnóstico global — 2026-08-14-iteracion-2

## Resultado

**Global: 71,4 % — FAILED**

Las cuatro evaluaciones son válidas: cada una contiene 59 veredictos y usa exclusivamente `Sirve`, `Indiferente`, `Estorba` y `Ambiguo`.

| Persona | Sirve | Indiferente | Estorba | Ambiguo |
|---|---:|---:|---:|---:|
| Rodrigo | 29 | 23 | 3 | 4 |
| Milagros | 29 | 25 | 3 | 2 |
| Carmen | 31 | 26 | 1 | 1 |
| Aníbal | 29 | 27 | 2 | 1 |

## D1 — Satisfacción de las personas: 42,0

| Persona | Puntos de las seis tareas | `X_p` | Flujo | Operación | Puntaje |
|---|---:|---:|---:|---|---:|
| Rodrigo | 24 | 3 | 0 | `máx(0, 24 − 2×3)/5 + 0` | 3,6 |
| Milagros | 20 | 2 | 2 | `máx(0, 20 − 2×2)/5 + 2` | 5,2 |
| Carmen | 24 | 0 | 0 | `máx(0, 24 − 2×0)/5 + 0` | 4,8 |
| Aníbal | 20 | 2 | 0 | `máx(0, 20 − 2×2)/5 + 0` | 3,2 |

`D1 = (3,6 + 5,2 + 4,8 + 3,2) / 4 × 10 = 42,0`

### Matriz persona × tarea

| Persona | Tarea | RF principales y veredicto | Puntos | Estado |
|---|---|---|---:|---|
| Rodrigo | Handoff estructurado | DIA-02 A; DIA-03/09/10 S | 3 | Incompleta: faltan productores y vigencia inmediata |
| Rodrigo | Evolución y diagnóstico anterior | DIA-02/05 A; DIA-07/10 S | 3 | Incompleta |
| Rodrigo | Registrar evolución y diagnóstico | DIA-07, IAM-01/06 S | 5 | Cubierta |
| Rodrigo | Marcar inestables y pendientes | DIA-06 S | 5 | Cubierta |
| Rodrigo | Laboratorio e imágenes | REG-06 S | 5 | Cubierta |
| Rodrigo | Cerrar y firmar entrega | DIA-01/04/09 S | 3 | Falta firma explícita |
| Milagros | Signos y balance | REG-01/02 S | 5 | Cubierta |
| Milagros | Escalar deterioro | ESC-01/11 S; ESC-06 E | 3 | Incompleta por fricción de severidad |
| Milagros | Guardia y disponibilidad | ESC-08 A | 1 | Aparente |
| Milagros | Ver y confirmar indicaciones | REG-03/04 S | 5 | Cubierta |
| Milagros | Eventos y medicamentos | REG-05 S | 3 | No garantiza registro junto a cama |
| Milagros | Entrega de enfermería | DIA-08/11 S | 3 | No garantiza reutilización sin transcripción |
| Carmen | Elaborar y publicar programación | TUR-04/09/10 S | 5 | Cubierta |
| Carmen | Cruces y franjas descubiertas | TUR-01/02/07 S | 5 | Cubierta |
| Carmen | Intercambios y permisos | TUR-06 E; TUR-12/13 S | 3 | Falta efecto operativo del permiso |
| Carmen | Reasignar ausencia | TUR-03 A; TUR-05/11 e IAM-06 S | 3 | Falta flujo sobre programación vigente |
| Carmen | Monitorear entregas | SUP-01 S | 3 | No distingue bloqueos por falta de diagnóstico |
| Carmen | Indicadores de cobertura | SUP-02 S | 5 | Cubierta |
| Aníbal | Alerta con contexto | ESC-03 e IAM-04/05 S | 3 | Falta identidad inequívoca y laboratorio requerido |
| Aníbal | Acusar y tomar caso | ESC-04/12/14 S | 5 | Cubierta |
| Aníbal | Tendencia, ventilación y evolución | REG-08 S | 5 | Cubierta |
| Aníbal | Indicación remota | REG-07 e IAM-02 S | 3 | No garantiza escritura desde celular personal |
| Aníbal | Indisponibilidad y delegación | ESC-07 A | 1 | Aparente: falta expiración o revocación |
| Aníbal | Revisión matutina | SUP-03 S | 3 | Resumen incompleto |

### Flujo

- **Rodrigo, 0/4:** se corta en DIA-02 porque se presentan decisiones y fundamentos cuyo registro no está declarado; DIA-10 puede devolver una entrega antigua.
- **Milagros, 2/4:** el recorrido existe, pero depende del ambiguo ESC-08 para conocer disponibilidad real.
- **Carmen, 0/4:** se corta al registrar la ausencia y sustituir al ausente directamente en la programación vigente.
- **Aníbal, 0/4:** el paquete recibido no garantiza paciente inequívoco ni el laboratorio relevante; tampoco se declara la escritura desde el dispositivo personal.

### Estorba fuera de tarea

- Rodrigo: TUR-13, IAM-04, IAM-05.
- Milagros: TUR-16, IAM-05. ESC-06 estorba, pero traza a su tarea de escalamiento.
- Carmen: ninguno; TUR-06 traza a intercambios.
- Aníbal: ESC-11 y ESC-13.

### Discrepancias percibido/computado

| Persona | Computada | Percibida | Δ | Diagnóstico |
|---|---:|---:|---:|---|
| Rodrigo | 36 | 65 | 29 | Agente complaciente: no refleja el corte del flujo ni tres daños externos |
| Milagros | 52 | 78 | 26 | Agente complaciente: subestima disponibilidad ambigua y fricción externa |
| Carmen | 48 | 68 | 20 | No supera el umbral de reporte |
| Aníbal | 32 | 82 | 50 | Agente claramente complaciente frente a contexto, delegación y revisión incompletos |

## D2 — Problemas críticos: 83,3

| Problema | RF asociados | Evaluación | Puntos |
|---|---|---|---:|
| P1 Rotación | TUR-01–16, DIA-01–11, REG-06, IAM-01/02/03/06, SUP-01/02 | Parcial: no se garantiza que la entrega sea la del turno inmediatamente anterior y falta la sustitución urgente sobre la programación vigente | 50 |
| P2 Medianoche | ESC-01–12/14, REG-07/08, IAM-02/04/05, SUP-03/04 | Resuelto funcionalmente: emisión, responsable vigente, falta de acuse, delegación, agotamiento, acuse y toma. Los tiempos quedan fuera del alcance funcional | 100 |
| P3 Tiempo real | ESC-08/13 y REG-01–05 | Resuelto funcionalmente: difusión múltiple y persistencia de registros, incluida desconexión | 100 |

`D2 = (50 + 100 + 100) / 3 = 83,3`

## D3 — Verificabilidad y forma: 66,1

**39 conformes de 59.**

`D3 = 39 / 59 × 100 = 66,1`

Los 20 no conformes son:

| RF | Condición incumplida |
|---|---|
| TUR-01 | C8: CA-2 agrega el registro de una asignación válida |
| TUR-04 | C8: CA-2 agrega consulta y obtención de la programación |
| TUR-08 | C6/C8: CA-2 describe una acción de Carmen y no demuestra el contrato del sistema |
| TUR-10 | C8: CA-2 agrega el rechazo de publicación incompleta |
| TUR-13 | C2: combina aceptación y rechazo con dos respuestas distintas |
| TUR-14 | C8: el CA agrega recuperación/consulta del historial |
| DIA-01 | C2 y C8: bloqueo y señalamiento son respuestas separadas; CA-2 agrega cierre exitoso |
| DIA-07 | C8: CA-2 agrega que la nueva versión pasa a ser vigente |
| ESC-01 | C2: alcanzar al responsable y registrar la emisión son dos respuestas |
| ESC-03 | C1/C3/C8: omite `el sistema` como sujeto explícito del DEBE y CA-3 agrega declaración de ausencia |
| ESC-09 | C2: alcanzar a jefatura y registrar agotamiento son dos respuestas |
| ESC-10 | C1/C3: omite `el sistema` como sujeto explícito del DEBE |
| ESC-11 | C2: encamina y además asigna una marca de severidad |
| REG-01 | C8: CA-2 agrega consulta posterior y ausencia de transcripción |
| REG-06 | C8: CA-2 agrega el instante del resultado |
| REG-07 | C8: CA-2 agrega presentación posterior a enfermería |
| IAM-01 | C8: CA-2 agrega consulta de auditoría |
| IAM-02 | C8: CA-2 agrega aceptación e incorporación del registro autorizado |
| IAM-03 | C8: CA-2 agrega recuperación de los accesos auditados |
| IAM-05 | C8: CA-2 agrega la entrega positiva del contexto después de autenticarse |

Los controles mecánicos M1–M4 no sustituyen estos hallazgos manuales.

## D4 — Trazabilidad: 100,0

- RF con persona y problema válidos: `59/59 × 70 = 70`.
- Tareas con al menos un punto: `24/24 × 30 = 30`.
- Filas de matrices desfasadas: `0 × 10 = 0`.

`D4 = 70 + 30 − 0 = 100`

No hay RF huérfanos.

## D5 — Consistencia y tensiones: 100,0

Las cinco tensiones están decididas explícitamente:

| Tensión | RF | Puntos |
|---|---|---:|
| Velocidad/completitud | DIA-01 | 12 |
| Sensibilidad del escalamiento | ESC-06, ESC-11 | 12 |
| Autonomía/control de intercambios | TUR-06, TUR-13 | 12 |
| Adopción/fuente oficial | TUR-08, TUR-16 | 12 |
| Movilidad/control de datos | IAM-04, IAM-05 | 12 |

Tramo de tensiones: `5 × 12 = 60`.  
Tramo de consistencia: `40 − 0 = 40`.

`D5 = 60 + 40 = 100`

El glosario existe, por lo que no aplica el techo de 80. Que una decisión perjudique a una persona baja D1; no convierte por sí sola la decisión en una contradicción de D5.

## D6 — Priorización: 95,0

Distribución: 43 MUST, 14 SHOULD y 2 COULD; no es uniforme.

Se descuenta 5 por **TUR-06**: sin la aprobación automática, los intercambios todavía pueden resolverse mediante TUR-13, por lo que su ausencia no deja P1 sin resolver ni descubre una tarea crítica. La autonomía pactada es una decisión de tensión, pero no justifica MUST bajo la fórmula literal de D6.

`D6 = 100 − 5 = 95`

## Cálculo global

| Dimensión | Puntaje | Peso | Aporte |
|---|---:|---:|---:|
| D1 | 42,0 | 30 % | 12,6 |
| D2 | 83,3 | 25 % | 20,8 |
| D3 | 66,1 | 20 % | 13,2 |
| D4 | 100,0 | 10 % | 10,0 |
| D5 | 100,0 | 10 % | 10,0 |
| D6 | 95,0 | 5 % | 4,8 |

`42×0,30 + 83,333…×0,25 + (39/59×100)×0,20 + 100×0,10 + 100×0,10 + 95×0,05 = 71,4`

## Condiciones de PASSED

| Condición | Obtenido | Cumple |
|---|---:|:---:|
| Global ≥ 80 | 71,4 | No |
| D1 ≥ 80 | 42,0 | No |
| Ninguna persona < 7 | mínima 3,2 | No |
| D2 ≥ 80 | 83,3 | Sí |
| Nueve controles vacíos | `verificar.sh --sin-agentes`: 9/9, código 0 | Sí* |

**Veredicto: FAILED.**

\* C1 pasó contra las corridas ya registradas. Debe repetirse después de materializar el `corrida.json` de esta corrida; el directorio actual todavía solo contiene los cuatro veredictos.

## Brechas abiertas

1. No existe productor funcional para decisiones clínicas y fundamento, día terapéutico y estado de información familiar.
2. DIA-10 puede presentar una entrega confirmada antigua sin advertir que el turno inmediato no cerró.
3. Faltan el plan clínico y una firma explícita de la entrega médica.
4. ESC-08 no diferencia disponibilidad declarada de disponibilidad real.
5. REG-05 no garantiza registro de eventos y medicamentos junto a la cama.
6. DIA-08/11 no garantizan reutilización de lo registrado sin nueva transcripción.
7. Falta registrar una ausencia, retirar al ausente y sustituirlo directamente en la programación vigente.
8. Un permiso resuelto y un alta/retiro de rotante no tienen efecto explícito y completo sobre elegibilidad y programación.
9. No se garantiza confirmación de lectura del cambio urgente ni se muestran acuses pendientes.
10. SUP-01 no identifica intentos bloqueados específicamente por falta de diagnóstico.
11. ESC-03 no garantiza paciente inequívoco después de autenticar ni el laboratorio clínicamente relevante.
12. No se garantiza el registro de una indicación remota desde el celular personal.
13. La indisponibilidad/delegación carece de expiración, revocación y retorno del titular.
14. SUP-03 omite eventos, acuses, tomas, avances de cadena y desenlaces de la revisión matutina.
15. ESC-11 y ESC-13 pueden aumentar fatiga de alertas y competir con el escalamiento crítico.
16. Veinte RF incumplen al menos una condición binaria de D3.
17. TUR-06 conserva una prioridad MUST no justificada por la regla literal de D6.

Las necesidades listadas como cubiertas por los agentes no se convierten en brechas: Carmen T1, T2 y T6, y Aníbal T2 y T3, tienen cobertura funcional. Los límites temporales y de cantidad de pasos de Milagros pertenecen al alcance no funcional.

## Acciones priorizadas

1. Cerrar P1: declarar productores del contenido clínico, detectar entrega inmediata ausente y completar el flujo de sustitución urgente.
2. Resolver las brechas de seguridad operativa: disponibilidad real, ciclo de delegación y escritura móvil.
3. Separar los 20 contratos/criterios no conformes hasta que cada RF tenga una respuesta y ningún CA amplíe el enunciado.
4. Eliminar transcripción en enfermería y permitir registro de todos los eventos junto a cama.
5. Reducir fatiga de avisos y reclasificar TUR-06 como SHOULD.

## Datos para `corrida.json`

```json
{
  "corrida": "2026-08-14-iteracion-2",
  "fecha": "2026-08-14",
  "rama": "eval/iteracion-2",
  "modelo": "<modelo>",
  "commits": {
    "requerimientos": "34877c7cc8316f7222914b8f03b0b548fb5d2806",
    "rubrica": "b492237b254baa5c538b9d68803e1b0bd456112a",
    "personas": "6340172da2d8c0b4ccabfc93880446cce9025732",
    "agentes": "34877c7cc8316f7222914b8f03b0b548fb5d2806"
  },
  "instrumento_modificado": false,
  "glosario": true,
  "iteraciones": [{
    "n": 1,
    "personas": {
      "rodrigo":  {"tareas": 24, "estorba_fuera": 3, "flujo": 0, "puntaje": 3.6, "percibida": 65, "tareas_en_cero": 0},
      "milagros": {"tareas": 20, "estorba_fuera": 2, "flujo": 2, "puntaje": 5.2, "percibida": 78, "tareas_en_cero": 0},
      "carmen":   {"tareas": 24, "estorba_fuera": 0, "flujo": 0, "puntaje": 4.8, "percibida": 68, "tareas_en_cero": 0},
      "anibal":   {"tareas": 20, "estorba_fuera": 2, "flujo": 0, "puntaje": 3.2, "percibida": 82, "tareas_en_cero": 0}
    },
    "dimensiones": {
      "D1": 42.0,
      "D2": 83.3,
      "D3": 66.1,
      "D4": 100.0,
      "D5": 100.0,
      "D6": 95.0
    },
    "d2_problemas": {"P1": 50, "P2": 100, "P3": 100},
    "d3_rf": {"conformes": 39, "total": 59},
    "tensiones_sin_decidir": 0,
    "prioridad_uniforme": false,
    "controles_pasan": true,
    "global": 71.4,
    "veredicto": "FAILED"
  }],
  "resultado": {
    "global": 71.4,
    "veredicto": "FAILED",
    "promedio_personas": 4.2,
    "brechas_abiertas": 17
  }
}
```
