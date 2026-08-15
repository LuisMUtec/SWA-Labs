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

Los plazos que [`ReqFunc.MD`](ReqFunc.MD) invoca sin fijar —el plazo de acuse de cada severidad de
escalamiento— se fijan aquí, en `RNF-PER-03`.

---

## RNF-PER — Rendimiento

### RNF-PER-01 — Tiempo de inicio de la aplicación

| Parte | Contenido |
|---|---|
| Fuente | Profesional clínico que inicia turno |
| Estímulo | Abre la aplicación en el equipo de la estación o en el dispositivo a pie de cama |
| Artefacto | Aplicación cliente |
| Entorno | Operación normal, 10 M unidades UCI federadas registradas y hasta 200 000 activas durante la ventana de cambio de turno |
| Respuesta | Se presenta la unidad del profesional con sus camas asignadas, en estado operable |
| Medida | p95 inferior a 1 s |

**Origen:** enunciado del caso, metas de rendimiento.

### RNF-PER-02 — Tiempo de configuración de la aplicación

| Parte | Contenido |
|---|---|
| Fuente | Coordinador de tecnología de la red asistencial |
| Estímulo | Habilita la aplicación en una sede nueva y la asocia a su unidad |
| Artefacto | Aplicación cliente y servicio de configuración de sedes |
| Entorno | Operación normal, sede sin configuración previa, enlace de datos de la sede en su ancho de banda nominal |
| Respuesta | La aplicación queda operable con la unidad, las camas y el rol de la sede cargados |
| Medida | p95 inferior a 5 s |

**Origen:** enunciado del caso, metas de rendimiento.

### RNF-PER-03 — Latencia y plazo de acuse del escalamiento

| Parte | Contenido |
|---|---|
| Fuente | Profesional de enfermería a pie de cama |
| Estímulo | Emite un escalamiento clasificado como deterioro que exige respuesta inmediata |
| Artefacto | Servicio de escalamiento y aplicación cliente del destinatario |
| Entorno | Turno noche, destinatario fuera de la sede sobre enlace móvil de calidad variable, 10 M unidades UCI federadas registradas |
| Respuesta | El escalamiento queda disponible en el dispositivo del destinatario con su contexto clínico adjunto |
| Medida | p95 inferior a 15 s desde la emisión. El plazo de acuse antes de avanzar en la cadena es de 90 s para el deterioro inmediato y de 15 min para la consulta diferible |

**Origen:** enunciado del caso, problema crítico de medianoche. `[SUPUESTO: los plazos de 90 s y 15 min no constan en el enunciado; se fijan para que la cadena completa de tres integrantes se agote antes de los 5 min que el enunciado admite como indisponibilidad tolerable del sistema.]`

### RNF-PER-04 — Disponibilidad del diagnóstico para el turno entrante

| Parte | Contenido |
|---|---|
| Fuente | Médico del turno entrante |
| Estímulo | Solicita la entrega de turno de las camas que recibe |
| Artefacto | Aplicación cliente y servicio de diagnósticos |
| Entorno | Ventana de cambio de turno, 10 M unidades UCI federadas registradas y hasta 200 000 activas en esa ventana |
| Respuesta | Se entrega el diagnóstico vigente de cada cama con las decisiones del turno anterior |
| Medida | p95 inferior a 1 s por cama, para unidades de hasta 20 camas |

**Origen:** enunciado del caso, meta de disponibilidad del diagnóstico para el turno siguiente.

---

## RNF-DIS — Disponibilidad

### RNF-DIS-01 — Disponibilidad del sistema

| Parte | Contenido |
|---|---|
| Fuente | Conjunto de los profesionales clínicos de la red |
| Estímulo | Solicitan cualquier operación de consulta o registro clínico |
| Artefacto | Sistema completo |
| Entorno | Operación mensual acumulada, incluidas las ventanas de mantenimiento |
| Respuesta | La operación se atiende sin rechazo por indisponibilidad |
| Medida | 99,9 % del tiempo de un mes calendario, equivalente a un máximo acumulado de 43 min 12 s de indisponibilidad mensual |

**Origen:** enunciado del caso, metas de rendimiento.

### RNF-DIS-02 — Recuperación ante caída

| Parte | Contenido |
|---|---|
| Fuente | Falla de infraestructura en una zona de la red |
| Estímulo | Un componente del que depende la operación clínica deja de responder |
| Artefacto | Sistema completo |
| Entorno | Turno noche, sin personal de tecnología presente en la sede |
| Respuesta | El sistema restablece la operación clínica sin intervención local |
| Medida | Inferior a 5 min desde la detección, sin acción del personal de la sede |

**Origen:** enunciado del caso, metas de rendimiento.

### RNF-DIS-03 — Persistencia del diagnóstico confirmado

| Parte | Contenido |
|---|---|
| Fuente | Falla de infraestructura |
| Estímulo | Un nodo que recibió una confirmación de entrega de turno deja de responder inmediatamente después |
| Artefacto | Servicio de diagnósticos |
| Entorno | Cualquier estado de carga, incluida la ventana de cambio de turno |
| Respuesta | El diagnóstico confirmado permanece recuperable y legible para el turno entrante |
| Medida | Ningún diagnóstico confirmado se pierde ante la caída de un nodo |

**Origen:** enunciado del caso, meta de disponibilidad permanente del diagnóstico.

### RNF-DIS-04 — Operación a pie de cama sin conectividad

| Parte | Contenido |
|---|---|
| Fuente | Profesional de enfermería a pie de cama |
| Estímulo | Registra signos vitales, eventos o medicación mientras el enlace de la unidad está interrumpido |
| Artefacto | Aplicación cliente en el dispositivo de captura |
| Entorno | Interrupción del enlace dentro de la unidad, con el resto del sistema operativo |
| Respuesta | El registro se conserva localmente y se incorpora al episodio al restablecerse el enlace |
| Medida | Ningún registro se pierde ni se duplica ante interrupciones de hasta 4 h; la incorporación concluye en menos de 60 s desde el restablecimiento |

**Origen:** enunciado del caso, meta de disponibilidad permanente del diagnóstico. `[SUPUESTO: la ventana de 4 h acota el peor caso de un turno noche sin soporte de tecnología presente; el enunciado no fija una duración de interrupción tolerable.]`

---

## RNF-ESC — Escalabilidad

Las cifras de escalamiento del enunciado son **entorno**, no requerimientos por sí solas. Conforme a
`docs/DECISIONES-ITERACION-2.md`, una unidad UCI federada es una unidad lógica con identidad, camas y
programación propias; no equivale a un hospital físico.

### RNF-ESC-01 — Carga al lanzamiento

| Parte | Contenido |
|---|---|
| Fuente | Conjunto de las sedes incorporadas al piloto |
| Estímulo | Operan de forma concurrente en la ventana de cambio de turno |
| Artefacto | Sistema completo |
| Entorno | 1 K unidades UCI federadas registradas, región de Lima y sus distritos |
| Respuesta | El sistema atiende la operación sin degradar los umbrales de `RNF-PER-01`, `RNF-PER-03` ni `RNF-PER-04` |
| Medida | Los umbrales de rendimiento se mantienen en p95 con 1 K unidades UCI federadas registradas |

**Origen:** enunciado del caso, requerimientos de escalamiento.

### RNF-ESC-02 — Carga a seis meses

| Parte | Contenido |
|---|---|
| Fuente | Conjunto de las sedes incorporadas tras la expansión a seis meses |
| Estímulo | Operan de forma concurrente en la ventana de cambio de turno |
| Artefacto | Sistema completo |
| Entorno | 100 K unidades UCI federadas registradas, incorporación de regiones adicionales |
| Respuesta | El sistema atiende la operación sin degradar los umbrales de rendimiento y sin reescritura de sus componentes |
| Medida | Los umbrales de rendimiento se mantienen en p95 con 100 K unidades UCI federadas registradas; la incorporación de una región adicional no exige detener la operación de las regiones ya activas |

**Origen:** enunciado del caso, requerimientos de escalamiento.

### RNF-ESC-03 — Carga a dos años

| Parte | Contenido |
|---|---|
| Fuente | Conjunto de las unidades UCI federadas incorporadas al cabo de dos años |
| Estímulo | Operan de forma concurrente en la ventana de cambio de turno |
| Artefacto | Sistema completo |
| Entorno | 10 M unidades UCI federadas registradas y hasta 200 000 activas en la ventana de cambio de turno |
| Respuesta | El sistema atiende la operación sin degradar los umbrales de rendimiento |
| Medida | Los umbrales de rendimiento se mantienen en p95 con 10 M unidades UCI federadas registradas |

**Origen:** enunciado del caso, requerimientos de escalamiento.

---

## RNF-SEG — Seguridad y privacidad

### RNF-SEG-01 — Trazabilidad del acceso a datos de salud

| Parte | Contenido |
|---|---|
| Fuente | Auditoría médica o autoridad de protección de datos |
| Estímulo | Solicita el registro de accesos a un episodio en un periodo |
| Artefacto | Servicio de trazabilidad de accesos |
| Entorno | Operación normal, episodio con accesos de múltiples profesionales y sedes |
| Respuesta | Se entrega el conjunto completo de consultas y modificaciones con su autor, el dato alcanzado y su instante |
| Medida | El 100 % de los accesos a datos clínicos queda registrado; ningún acceso registrado puede eliminarse ni alterarse |

**Origen:** Ley N.° 29733, datos personales de salud como categoría sensible.

### RNF-SEG-02 — Exposición de datos fuera del entorno institucional

| Parte | Contenido |
|---|---|
| Fuente | Médico de guardia localizable con dispositivo personal |
| Estímulo | Recibe un escalamiento fuera de la sede |
| Artefacto | Aplicación cliente en dispositivo no institucional y canal de escalamiento |
| Entorno | Enlace móvil, dispositivo sin gestión institucional, profesional aún no autenticado |
| Respuesta | El aviso llega sin dato identificatorio del paciente y el contexto clínico se presenta solo tras autenticación |
| Medida | Ningún dato identificatorio del paciente se presenta antes de la autenticación; los datos clínicos no permanecen legibles en el dispositivo tras el cierre de sesión |

**Origen:** Ley N.° 29733, y tensión de movilidad frente a control de datos.

### RNF-SEG-03 — Integridad del registro clínico

| Parte | Contenido |
|---|---|
| Fuente | Profesional clínico o proceso interno |
| Estímulo | Intenta modificar un diagnóstico, una indicación o un acuse ya registrados |
| Artefacto | Servicio de registro clínico |
| Entorno | Operación normal, en cualquier sede de la red |
| Respuesta | La versión previa se conserva y la modificación queda como versión nueva con su autoría |
| Medida | Ninguna versión registrada se sustituye ni se elimina |

**Origen:** Ley N.° 29733 y estándares de trazabilidad del registro clínico exigidos por SUSALUD.

### RNF-SEG-04 — Derechos del titular sobre sus datos

| Parte | Contenido |
|---|---|
| Fuente | Paciente o su apoderado |
| Estímulo | Solicita conocer qué datos suyos existen y quién accedió a ellos |
| Artefacto | Servicio de trazabilidad de accesos y registro clínico |
| Entorno | Operación normal, episodio cerrado o en curso |
| Respuesta | La solicitud se registra, se deriva al responsable institucional de datos personales y se entrega la relación de datos del episodio y de sus accesos por un canal autenticado |
| Medida | Respuesta en un máximo de 20 días contados desde el día siguiente de la presentación; una sola ampliación de hasta 20 días adicionales requiere justificación comunicada dentro del plazo inicial |

**Origen:** Ley N.° 29733, derechos del titular de datos personales.

---

## RNF-USA — Usabilidad

### RNF-USA-01 — Esfuerzo de registro de la nota de evolución

| Parte | Contenido |
|---|---|
| Fuente | Médico que cierra su turno |
| Estímulo | Registra la nota de evolución y el diagnóstico de una cama |
| Artefacto | Aplicación cliente |
| Entorno | Estación de enfermería con equipo compartido, profesional con guantes y bajo presión de tiempo, sin capacitación formal previa |
| Respuesta | La nota queda registrada y el diagnóstico pasa a ser el vigente de la cama |
| Medida | Mediana inferior a 3 min por cama en el primer turno de uso del profesional, sin asistencia de un tercero |

**Origen:** tensión de velocidad frente a completitud documentada en `Personas/README.md`; contrapeso de `RF-DIA-01`. `[SUPUESTO: el enunciado no fija un umbral de esfuerzo de registro; los 3 min se derivan de que el bloqueo de cierre de turno solo es sostenible si registrar cuesta menos que eludir el sistema.]`

### RNF-USA-02 — Esfuerzo de emisión de un escalamiento

| Parte | Contenido |
|---|---|
| Fuente | Profesional de enfermería a pie de cama |
| Estímulo | Decide escalar un deterioro clínico |
| Artefacto | Aplicación cliente en el dispositivo a pie de cama |
| Entorno | Turno noche, profesional con doble guante y una sola mano libre, ruido de alarmas constante |
| Respuesta | El escalamiento queda emitido con su severidad y su contexto adjunto |
| Medida | Mediana inferior a 30 s desde la decisión, con un máximo de dos acciones del profesional |

**Origen:** enunciado del caso, problema crítico de medianoche. `[SUPUESTO: el umbral de 30 s y el máximo de dos acciones no constan en el enunciado; se fijan porque un escalamiento más costoso que una llamada telefónica no se adopta.]`

### RNF-USA-03 — Uniformidad de la aplicación en la red

| Parte | Contenido |
|---|---|
| Fuente | Profesional rotante que llega a una sede en la que no operó antes |
| Estímulo | Ejecuta la recepción de entrega de turno en esa sede |
| Artefacto | Aplicación cliente |
| Entorno | Sede distinta de aquella en la que el profesional usó el sistema por última vez |
| Respuesta | La recepción se completa sin instrucción específica de esa sede |
| Medida | El 100 % de las operaciones clínicas se ejecuta con la misma secuencia en todas las sedes de la red |

**Origen:** enunciado del caso, alta rotación de médicos internistas en la red.

---

## RNF-MAN — Mantenibilidad

### RNF-MAN-01 — Despliegue de una versión en la red

| Parte | Contenido |
|---|---|
| Fuente | Coordinador de tecnología de la red asistencial |
| Estímulo | Publica una versión nueva de la aplicación |
| Artefacto | Aplicación cliente en todas las sedes |
| Entorno | Red con sedes distribuidas, sin personal de tecnología en cada sede |
| Respuesta | Las sedes quedan operando la versión publicada |
| Medida | Ninguna sede requiere intervención presencial equipo por equipo; la operación clínica no se interrumpe durante la publicación |

**Origen:** cliente Oficina de Tecnologías de Información, criterio de despliegue sin intervención máquina por máquina.

### RNF-MAN-02 — Incorporación de una sede

| Parte | Contenido |
|---|---|
| Fuente | Coordinador de tecnología de la red asistencial |
| Estímulo | Incorpora una sede nueva con sus unidades y camas |
| Artefacto | Servicio de configuración de sedes |
| Entorno | Sistema en operación con las sedes existentes activas |
| Respuesta | La sede queda operativa sin modificar el código desplegado ni detener las sedes activas |
| Medida | La incorporación se resuelve por configuración; ninguna sede activa interrumpe su operación |

**Origen:** cliente Essalud Gerencia Central de Operaciones, criterio de piloto replicable a otras regiones sin rehacer el sistema.

---

## RNF-INT — Interoperabilidad

### RNF-INT-01 — Intercambio de la historia clínica electrónica

| Parte | Contenido |
|---|---|
| Fuente | Sistema nacional de historia clínica electrónica |
| Estímulo | Solicita o remite información clínica de un episodio de cuidados intensivos |
| Artefacto | Servicio de intercambio clínico |
| Entorno | Operación normal, episodio con diagnóstico vigente registrado |
| Respuesta | La información se intercambia conforme al perfil CorePE v0.1 de MINSA basado en HL7 FHIR R4 e IPS Perú, registrando la versión del perfil y los catálogos aplicados |
| Medida | El 100 % de los episodios cerrados valida contra la versión registrada del perfil y sus catálogos sin transformación manual |

**Origen:** Ley N.° 30024, interoperabilidad de la historia clínica electrónica a nivel nacional.

### RNF-INT-02 — Entrega de indicadores a la Dirección de Red

| Parte | Contenido |
|---|---|
| Fuente | Dirección de Red Prestacional |
| Estímulo | Solicita los indicadores de cobertura de turnos y cumplimiento de entrega de un periodo |
| Artefacto | Servicio de indicadores |
| Entorno | Red con sus unidades activas y sus registros del periodo consolidados |
| Respuesta | Se entregan los indicadores del periodo en un formato procesable por la Dirección |
| Medida | Ningún indicador requiere transcripción manual desde otra fuente |

**Origen:** cliente Dirección de Red Prestacional, criterio de visibilidad de cobertura de turnos.

---

## RNF-OBS — Observabilidad

### RNF-OBS-01 — Detección de indisponibilidad sin personal presente

| Parte | Contenido |
|---|---|
| Fuente | Componente del sistema que deja de responder |
| Estímulo | La operación clínica de una sede empieza a fallar |
| Artefacto | Servicio de supervisión del sistema |
| Entorno | Turno noche, sin personal de tecnología presente en la sede |
| Respuesta | La falla queda detectada y notificada al responsable de operación de la red |
| Medida | Detección en menos de 60 s desde la primera operación fallida, sin que un profesional clínico deba reportarla |

**Origen:** enunciado del caso, meta de recuperación inferior a 5 min. La detección es condición previa de `RNF-DIS-02`.

### RNF-OBS-02 — Reconstrucción de la cadena de un escalamiento

| Parte | Contenido |
|---|---|
| Fuente | Coordinador de la unidad o auditoría médica |
| Estímulo | Solicita la reconstrucción de un escalamiento ocurrido |
| Artefacto | Servicio de escalamiento y registro de trazabilidad |
| Entorno | Operación normal, escalamiento cerrado o agotado |
| Respuesta | Se entrega la secuencia completa de emisión, integrantes alcanzados, acuses y desenlace |
| Medida | El 100 % de los escalamientos emitidos es reconstruible durante el periodo de retención del episodio |

**Origen:** enunciado del caso, problema crítico de medianoche; sostiene la auditoría exigida por `RF-SUP-04`.

---

## Cobertura de las metas del enunciado

| Meta del enunciado | RNF que la enuncia |
|---|---|
| Inicio de aplicación inferior a 1 s | `RNF-PER-01` |
| Configuración de aplicación inferior a 5 s | `RNF-PER-02` |
| Disponibilidad del sistema de 99,9 % | `RNF-DIS-01` |
| Recuperación ante caída inferior a 5 min | `RNF-DIS-02`, `RNF-OBS-01` |
| Lanzamiento con 1 K sedes | `RNF-ESC-01` |
| Seis meses con 100 K sedes | `RNF-ESC-02` |
| Dos años con 10 M sedes | `RNF-ESC-03` |
| Diagnóstico disponible en todo momento | `RNF-PER-04`, `RNF-DIS-03`, `RNF-DIS-04` |

## Decisiones y supuestos vigentes

Las decisiones cerradas se fundamentan en [`docs/DECISIONES-ITERACION-2.md`](../docs/DECISIONES-ITERACION-2.md).

| Condición | Dónde | Qué fija |
|---|---|---|
| 10 M unidades UCI federadas, 2 % concurrentes | `RNF-PER-01`, `RNF-PER-04`, `RNF-ESC-03` | El entorno máximo de carga y 200 000 unidades activas |
| Respuesta al derecho de acceso en 20 días, ampliable una vez | `RNF-SEG-04` | La medida y el canal institucional del derecho del titular |
| CorePE v0.1, HL7 FHIR R4 e IPS Perú | `RNF-INT-01` | La línea base versionada del intercambio con RENHICE |
| `[SUPUESTO]` plazos de acuse de 90 s y 15 min | `RNF-PER-03` | El umbral que `RF-ESC-02` y `RF-ESC-06` invocan sin fijar |
| `[SUPUESTO]` interrupción tolerable de 4 h a pie de cama | `RNF-DIS-04` | El alcance de la operación sin conectividad |
| `[SUPUESTO]` umbrales de esfuerzo de 3 min y 30 s | `RNF-USA-01`, `RNF-USA-02` | El contrapeso de usabilidad de `RF-DIA-01` y `RF-ESC-01` |
