# Reporte de Evaluación de Requerimientos Funcionales
## Sistema de Gestión UCI — EsSalud

| | |
|---|---|
| Corrida | 2026-08-14-iteracion-2 |
| Rama | `eval/iteracion-2` |
| Modelo | `gpt-5` |
| Evaluado | `Requirements/ReqFunc.MD` @ `34877c7` |
| Rúbrica | `Spec/Eval-Spec.MD` @ `b492237` |
| Personas | `Personas/` @ `6340172` |
| Agentes | `Agents/` @ `34877c7` |
| Instrumento modificado | no |

## Puntaje global: 71,4 %

| Dimensión | Puntaje | Peso | Aporte |
|---|---:|---:|---:|
| D1 Satisfacción de las personas | 42,0 | 30 % | 12,60 |
| D2 Cobertura de problemas críticos | 83,3 | 25 % | 20,83 |
| D3 Verificabilidad y forma | 66,1 | 20 % | 13,22 |
| D4 Trazabilidad | 100,0 | 10 % | 10,00 |
| D5 Consistencia y tensiones | 100,0 | 10 % | 10,00 |
| D6 Priorización | 95,0 | 5 % | 4,75 |

Suma de aportes: 12,60 + 20,83 + 13,22 + 10,00 + 10,00 + 4,75 = **71,4**.

## Veredicto: FAILED

| # | Condición | Umbral | Obtenido | Cumple |
|---|---|---:|---:|:---:|
| 1 | Puntaje global | ≥ 80,0 % | 71,4 % | ✗ |
| 2 | D1 | ≥ 80,0 | 42,0 | ✗ |
| 3 | Persona más baja | ≥ 7,0/10 | 3,2 | ✗ |
| 4 | D2 | ≥ 80,0 | 83,3 | ✓ |
| 5 | Controles de `verificar.sh` | 9/9 | 9/9 | ✓ |

Los nueve controles pasan. El resultado falla por satisfacción de personas y por el puntaje global.

## Puntajes por persona

| Persona | Tareas | Estorba fuera | Flujo | Puntaje /10 | Percibida |
|---|---:|---:|---:|---:|---:|
| Rodrigo | 24 | 3 | 0 | 3,6 | 65 % |
| Milagros | 20 | 2 | 2 | 5,2 | 78 % |
| Carmen | 24 | 0 | 0 | 4,8 | 68 % |
| Aníbal | 20 | 2 | 0 | 3,2 | 82 % |
| **PROMEDIO** | **22** | **1,75** | **0,5** | **4,2** | **73,25 %** |

## Brechas abiertas

1. Faltan productores explícitos para decisión y razonamiento clínico, día de tratamiento e información familiar.
2. La entrega de turno puede mostrar información desactualizada.
3. El plan clínico y la firma deben declararse explícitamente.
4. La disponibilidad de guardia no distingue el estado declarado del real.
5. El registro de enfermería no declara su ejecución a pie de cama.
6. La entrega de enfermería no reutiliza los datos ya registrados sin transcripción.
7. Faltan ausencia imprevista y reemplazo inmediato.
8. Permisos y rotaciones no actualizan elegibilidad ni programación.
9. Los cambios urgentes no muestran confirmaciones pendientes.
10. La supervisión no conserva la causa de los intentos bloqueados.
11. El escalamiento no garantiza identificación inequívoca ni el laboratorio relevante.
12. No se permite explícitamente registrar una indicación remota desde un equipo personal verificado.
13. La delegación no define vencimiento, revocación ni retorno de responsabilidad.
14. El resumen de guardia omite eventos, acuses, casos, cadena y desenlaces.
15. Dos alertas pueden producir fatiga por falta de priorización y agrupación.
16. Veinte RF incumplen la forma cerrada evaluada por D3.
17. `RF-TUR-06` usa una prioridad MUST no justificada por los tres problemas críticos.

## Acciones priorizadas

1. Corregir los veinte RF no conformes sin alterar su intención.
2. Completar los productores clínicos, la entrega vigente y el circuito de enfermería a pie de cama.
3. Completar ausencia, reemplazo, permisos, rotaciones y confirmaciones de programación.
4. Fortalecer escalamiento, delegación, registro remoto y supervisión nocturna.
5. Reducir la fricción y la fatiga señaladas por las cuatro personas.
6. Ejecutar una corrida nueva; esta medición no se recalcula después de corregir.

## Evidencia

- `Spec/corridas/2026-08-14-iteracion-2/diagnostico.MD`: cálculo, inventario y acciones.
- `Spec/corridas/2026-08-14-iteracion-2/veredicto-*.MD`: 59 veredictos aislados por persona.
- `Spec/corridas/2026-08-14-iteracion-2/controles.txt`: salida de los nueve controles.
- `Spec/corridas/2026-08-14-iteracion-2/corrida.json`: resultado computable.

## Resultado final: 71,4 %

Esta corrida mide una vez y no corrige. Las 17 brechas se atienden en una rama posterior.

- Veredicto final: FAILED
- Promedio final de personas: 4,2/10
- Puntaje global final: 71,4 %
- Brechas abiertas: 17
