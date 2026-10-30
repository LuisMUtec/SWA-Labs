# Lab #12 – Save Chernobyl – Entregable 2: Criterios hipotéticos de escalabilidad

**Arquitectura de Software 2026-II · Prof. Carlos Balbuena · TEAM: Maquera - Barzola · INTEGRANTES: Luis Maquera, Johar Barzola**

Son hipotéticos porque aún no hay data: se confirman con logs, monitoring, dashboards y performance testing (S10). Regla: "Scale your architecture only when needed, not before" (S11 p8).

## 1. Nuestra load (lo que estresa al sistema)

La load no son los operadores, son las mediciones (S5: "define cuál es tu LOAD").

| Cálculo | Valor |
|---|---|
| 1 sensor: 1 envío cada 0.05 s | 20 mediciones/s |
| 1 reactor: hasta 100 sensores | 2 000 mediciones/s |
| 3 reactores | **6 000 mediciones/s** |
| Por día (× 86 400 s) | ≈ 518 millones de mediciones |
| Supuesto: ~100 bytes por registro | ≈ 52 GB/día de trazabilidad |

Por eso la trazabilidad viaja por una cola asíncrona y se guarda en tablas con columna de latencia, sin impactar al control: "si el logging se cae, la aplicación debe continuar" (S10 p25-p28).

## 2. Qué medimos en el dashboard

Las cuatro métricas de escalabilidad del curso (S10 p41): tráfico (mediciones/s y comandos/s), availability = 2xx/(2xx+5xx), reliability = 2xx/(2xx+4xx+5xx) (S10 p26) y latencia P95/P99 (nunca el promedio, S5).

## 3. CUÁNDO escalar: umbrales Good / OK / Bad (formato fitness function, S7)

| FF | Dimensión e indicador | Good | OK | Bad | Cómo se mide |
|---|---|---|---|---|---|
| FF1 | Latencia P99 medición → decisión local → comando a refrigeración (critical path) | ≤ 50 ms | ≤ 100 ms | > 100 ms | monitoring por reactor; test de latencia en cada PR, Bad bloquea el merge |
| FF2 | Latencia P99 Controller → Main Controller (decisión global) | ≤ 200 ms | ≤ 500 ms | > 1 s | monitoring + load testing |
| FF3 | Availability del control por reactor | ≥ 99.9 % | ≥ 99.5 % | < 99.5 % | tabla de transacciones (2xx/5xx) |
| FF4 | Reliability de comandos (ON/OFF con ack correcto) | ≥ 99.9 % | ≥ 99 % | < 99 % | tabla de transacciones (2xx/4xx/5xx) |
| FF5 | Tráfico sostenido vs capacidad medida con load testing | < 50 % | 50-70 % | > 70 % por 10 min | dashboard de tráfico |
| FF6 | Atraso (lag) de la cola de eventos de trazabilidad | < 1 s | < 5 s | > 30 s | monitoring de la cola |

Regla de decisión (S10 p55-p56 y escenarios p80-p83):
- Tráfico sube → availability baja → latencia sube ⇒ **es hora de escalar** (escenario 2: crecimiento sostenido).
- Pico transitorio que ya bajó (escenario 3) ⇒ no se escala; lo absorbe la cola.
- Caída súbita con availability crítica (escenario 4) ⇒ no es escalabilidad, es un incidente: RCA.

## 4. QUÉ escalar: el bottleneck, "no con intuición, con métricas" (S11 p61)

Se busca el P95/P99 más alto, el recurso saturado (CPU, memoria, I/O, red) y las colas de espera, usando performance testing (S10 p62-p69): load (fijar umbrales), stress (validar el LB), spike (picos de alarmas), volume (hasta dónde aguanta la Log DB), endurance (memory leaks de un controller 24/7).

Candidatos hipotéticos: Main Controller (recibe las 6 000 mediciones/s), Log DB (escrituras), panel de operadores (lecturas), red Controller ↔ Main.

## 5. CÓMO escalar: patrón mínimo necesario (S11 p62)

| Tipo de bottleneck | Patrón (en orden) | En Save Chernobyl |
|---|---|---|
| Cómputo (CPU alta en Main Controller) | Escala horizontal → más instancias + LB | Main Controller stateless replicado detrás del LB con /health |
| Datos (lecturas del panel lentas) | Cache-aside → Read Replicas → Sharding | últimas lecturas en cache con TTL corto; reportes en Read Replica; sharding natural por reactor |
| I/O (escrituras de logs lentas) | Queue asíncrona → Write Replica | la cola de eventos ya está; Write Replica si las escrituras superan el 30 % |
| Red (latencia Controller ↔ Main) | Sidecar (mismo host) | logging y monitoring como side-car del controller |
| Concurrencia (locks en Log DB) | Read Replicas → revisar índices | lecturas del panel fuera de la Master; índices por reactor y fecha |

- Scale out (horizontal) para lo stateless; scale up (vertical) solo en la BD primaria, que tiene límite físico (S3).
- **Nuevo reactor = nuevo shard**: se agrega un controller local y su partición de trazabilidad sin tocar los demás reactores.
- Trade-off: "más instancias = más costo, mismo P99" si el bottleneck no es cómputo (S11 p63). Primero medir, después escalar.
