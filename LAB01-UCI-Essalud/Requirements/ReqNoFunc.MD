# Requerimientos No Funcionales

Sistema de Gestión de UCI — Essalud

## Convenciones

- **ID:** `RNF-<atributo>-<n>`
- Cada RNF debe ser **medible**: métrica, valor objetivo y forma de verificación.

| Atributo de calidad | Prefijo |
|---|---|
| Rendimiento | `RNF-PER` |
| Disponibilidad | `RNF-DIS` |
| Escalabilidad | `RNF-ESC` |
| Seguridad y privacidad | `RNF-SEG` |
| Usabilidad | `RNF-USA` |
| Mantenibilidad | `RNF-MAN` |
| Interoperabilidad | `RNF-INT` |
| Observabilidad | `RNF-OBS` |

---

## RNF-PER — Rendimiento

| ID | Requerimiento | Métrica | Objetivo | Verificación |
|---|---|---|---|---|
| RNF-PER-01 | Tiempo de inicio de la aplicación | Cold start hasta pantalla usable | < 1 s | |
| RNF-PER-02 | Tiempo de configuración de la aplicación | Setup inicial completo | < 5 s | |

## RNF-DIS — Disponibilidad

| ID | Requerimiento | Métrica | Objetivo | Verificación |
|---|---|---|---|---|
| RNF-DIS-01 | Disponibilidad del sistema | Uptime mensual | 99.9 % | |
| RNF-DIS-02 | Recuperación ante caída | RTO | < 5 min | |

## RNF-ESC — Escalabilidad

| ID | Requerimiento | Métrica | Objetivo | Verificación |
|---|---|---|---|---|
| RNF-ESC-01 | Capacidad al lanzamiento | Hospitales concurrentes | 1 K | |
| RNF-ESC-02 | Capacidad a 6 meses | Hospitales concurrentes | 100 K | |
| RNF-ESC-03 | Capacidad a 2 años | Hospitales concurrentes | 10 M | |

## RNF-SEG — Seguridad y privacidad

| ID | Requerimiento | Métrica | Objetivo | Verificación |
|---|---|---|---|---|
| RNF-SEG-01 | | | | |

## RNF-USA — Usabilidad

| ID | Requerimiento | Métrica | Objetivo | Verificación |
|---|---|---|---|---|
| RNF-USA-01 | | | | |

## RNF-MAN / RNF-INT / RNF-OBS

| ID | Requerimiento | Métrica | Objetivo | Verificación |
|---|---|---|---|---|
| | | | | |

---

## Matriz de trazabilidad

| RNF | Persona(s) | Problema | Origen |
|---|---|---|---|
| RNF-PER-01 | | | Enunciado |
| RNF-DIS-01 | | | Enunciado |
