# Requerimientos No Funcionales

Sistema de Gestión de UCI — Essalud

Forma: [`docs/CONVENCIONES.md`](../docs/CONVENCIONES.md), sección 7.

> **Alcance.** Este documento es entregable exigido por el enunciado, pero queda **fuera de la
> evaluación** de [`Spec/Eval-Spec.MD`](../Spec/Eval-Spec.MD): ninguna de sus afirmaciones suma ni
> resta en el porcentaje de calidad. Se verifica contra las metas numéricas del caso, no contra la
> satisfacción de una persona.

## Convenciones

- **ID:** `RNF-‹atributo›-‹n›`
- **Origen:** el enunciado del caso. Ninguna persona modelada motiva un RNF — las cuatro son
  clínicas y los atributos de calidad no se juzgan desde su satisfacción.
- **Forma:** escenario de atributo de calidad en seis partes.

| Parte | Qué fija |
|---|---|
| Fuente | Quién o qué origina el estímulo |
| Estímulo | El evento que llega al sistema |
| Artefacto | La parte del sistema estimulada |
| Entorno | El estado del sistema cuando llega el estímulo, incluida la carga |
| Respuesta | Lo que el sistema hace en consecuencia |
| Medida | El umbral con el que se declara cumplida la respuesta |

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

### RNF-PER-01 — Tiempo de inicio de la aplicación

| Parte | Contenido |
|---|---|
| Fuente | |
| Estímulo | |
| Artefacto | |
| Entorno | |
| Respuesta | |
| Medida | Inferior a 1 s |

**Origen:** enunciado del caso, metas de rendimiento.

### RNF-PER-02 — Tiempo de configuración de la aplicación

| Parte | Contenido |
|---|---|
| Fuente | |
| Estímulo | |
| Artefacto | |
| Entorno | |
| Respuesta | |
| Medida | Inferior a 5 s |

**Origen:** enunciado del caso, metas de rendimiento.

---

## RNF-DIS — Disponibilidad

### RNF-DIS-01 — Disponibilidad del sistema

| Parte | Contenido |
|---|---|
| Fuente | |
| Estímulo | |
| Artefacto | |
| Entorno | |
| Respuesta | |
| Medida | 99,9 % de disponibilidad mensual |

**Origen:** enunciado del caso, metas de rendimiento.

### RNF-DIS-02 — Recuperación ante caída

| Parte | Contenido |
|---|---|
| Fuente | |
| Estímulo | |
| Artefacto | |
| Entorno | |
| Respuesta | |
| Medida | Inferior a 5 min |

**Origen:** enunciado del caso, metas de rendimiento.

---

## RNF-ESC — Escalabilidad

Las cifras de escalamiento del enunciado son **entorno**, no requerimientos por sí solas: cada una se
enuncia dentro de un escenario con su respuesta y su medida.

`[ACLARAR: qué cuenta como «hospital» en la meta de 10 M a dos años. Perú registra del orden de miles
de establecimientos de salud, de modo que la cifra no admite lectura literal como sedes hospitalarias.
Las lecturas posibles —camas, pacientes atendidos, dispositivos conectados— conducen a entornos de
carga distintos.]`

### RNF-ESC-01 — Carga al lanzamiento

| Parte | Contenido |
|---|---|
| Fuente | |
| Estímulo | |
| Artefacto | |
| Entorno | 1 K sedes registradas |
| Respuesta | |
| Medida | |

**Origen:** enunciado del caso, requerimientos de escalamiento.

### RNF-ESC-02 — Carga a seis meses

| Parte | Contenido |
|---|---|
| Fuente | |
| Estímulo | |
| Artefacto | |
| Entorno | 100 K sedes registradas |
| Respuesta | |
| Medida | |

**Origen:** enunciado del caso, requerimientos de escalamiento.

### RNF-ESC-03 — Carga a dos años

| Parte | Contenido |
|---|---|
| Fuente | |
| Estímulo | |
| Artefacto | |
| Entorno | 10 M sedes registradas |
| Respuesta | |
| Medida | |

**Origen:** enunciado del caso, requerimientos de escalamiento.

---

## RNF-SEG — Seguridad y privacidad

### RNF-SEG-01 — ‹título›

| Parte | Contenido |
|---|---|
| Fuente | |
| Estímulo | |
| Artefacto | |
| Entorno | |
| Respuesta | |
| Medida | |

**Origen:** Ley N.° 29733, datos personales de salud como categoría sensible.

---

## RNF-USA / RNF-MAN / RNF-INT / RNF-OBS

Pendientes de enunciar bajo la misma forma de seis partes.
