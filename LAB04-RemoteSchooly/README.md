# SWA — Caso de Estudio #4: RemoteSchooly

Arquitectura de Software — UTEC 2026-II. Diseño de una plataforma que distribuye material semanal
desde Lima hacia escuelas remotas y reduce al menos 40 % el consumo comparable de tokens de IA.

| Campo | Estado |
|---|---|
| Requisitos | 41 funcionales, cuatro recorridos y nueve criterios medibles |
| EVAL | **9.5/10 — PASSED** |
| Diagrama | Tres iteraciones top-down, fuentes y SVG/PNG |
| Trazabilidad | **41/41** requisitos con componente, iteración y happy path |
| Implementación | Fuera del alcance de este laboratorio; tareas futuras documentadas |

Enunciado vigente: [`docs/LAB-04-ARQ-2026.2.md`](docs/LAB-04-ARQ-2026.2.md) ·
[DOCX original](docs/Lab-04-ARQ-2026.2.docx) ·
[análisis](docs/ENUNCIADO-ANALISIS.md)

## Equipo del repositorio

| GitHub |
|---|
| [@LuisMUtec](https://github.com/LuisMUtec) |
| [@Joharjbe](https://github.com/Joharjbe) |

## El problema

Los materiales nacen en una central de Lima, pero la clase ocurre donde el enlace externo es
limitado. Un LMS alojado solo en Internet puede tener una interfaz correcta y fracasar en el único
momento importante: cuando profesor y alumnos intentan usar la semana.

RemoteSchooly cambia la unidad de entrega. No publica un conjunto de URLs, sino un **paquete semanal
versionado** con manifiesto y recursos verificables. Una sede lo sincroniza durante cualquier ventana
de conexión, conserva lo ya validado y lo sirve después por su propia Wi-Fi/LAN. `Listo` significa
que todos los recursos obligatorios coinciden; una descarga parcial nunca se presenta como curso.

En paralelo, la ayuda de IA de los Profesores de Lima atraviesa una sola frontera de presupuesto y
medición. El ahorro no se compra usando un modelo más barato o publicando menos: se compara el mismo
trabajo, con la misma calidad, por unidad aprobada.

## Los cuatro usuarios

| Usuario | Recorrido | Falla que el diseño contiene |
|---|---|---|
| [Gobierno](personas/Gobierno.md) | Asigna, presupuesta y supervisa | Una sede silenciosa no se convierte en error; solo ve agregados |
| [Profesora de Lima](personas/Profesora-Lima.md) | Crea, revisa y publica | IA no publica ni bloquea la autoría manual |
| [Profesor de Provincia](personas/Profesor-Provincia.md) | Sincroniza y enseña | Un corte no reinicia ni activa un paquete parcial |
| [Alumno](personas/Alumno.md) | Aprende y guarda avance offline | Un recurso pesado tiene alternativa y un reintento no duplica |

Las siete tensiones entre ellos y su decisión explícita están en
[`personas/README.md`](personas/README.md).

## Requirements EVAL

La única fuente de comportamiento es
[`specs/001-remoteschooly/spec.md`](specs/001-remoteschooly/spec.md). El EVAL fija cuatro puntos de
personas, dos de ajuste al caso, dos de verificabilidad y dos de coherencia.

| Iteración | D1 | D2 | D3 | D4 | Total | Estado |
|---|---:|---:|---:|---:|---:|---|
| [01](evals/iterations/2026-09-02-01.md) | 4.0 | 2.0 | 2.0 | 1.5 | **9.5** | **PASSED** |

La pérdida de 0,5 no se esconde: las historias tienen P1/P2/P3, pero los 41 requisitos no declaran
prioridad individual; la rúbrica limita D4 a 1,5. El hallazgo no corta ningún recorrido y el gate se
supera con margen. Rúbrica y protocolo: [`evals/README.md`](evals/README.md).

## Arquitectura final

![Arquitectura final de RemoteSchooly](architecture/diagrams/iteration-3-components.svg)

El diagrama se construyó en tres pasadas reales:

1. [Actores frente a una caja](architecture/diagrams/iteration-1-context.svg).
2. [Centro de Lima y sede remota](architecture/diagrams/iteration-2-center-edge.svg).
3. [Componentes, datos y cuatro happy paths](architecture/diagrams/iteration-3-components.svg).

El razonamiento, la responsabilidad de cada caja y los cuatro recorridos paso a paso están en
[`architecture/README.md`](architecture/README.md). La cobertura `FR → componente → iteración → HP`
está en [`architecture/TRACEABILITY.md`](architecture/TRACEABILITY.md).

## Los cuatro happy paths

| ID | Inicio | Cierre observable |
|---|---|---|
| H1 | Lucía crea material | Paquete aprobado publicado y tokens comparables registrados |
| H2 | Julio sincroniza | Paquete completo activado y utilizable sin Internet externo |
| H3 | Diego aprende | Avance local confirmado exactamente una vez al reconectar |
| H4 | Valeria gobierna | Cobertura y 40 % visibles sin prompts ni entregas personales |

## El 40 % de tokens

```text
ahorro = 1 - tokens_optimizados / tokens_base
```

`tokens` significa entrada + salida por unidad aprobada sobre las mismas tareas, fuentes y rúbrica.
El numerador baja por reutilización sin llamada, contexto acotado, límites de salida y edición manual.
Precio, modelo, caché del proveedor y menor volumen se reportan aparte; no cuentan por sí solos hacia
la meta. Decisión y alternativas: [`research.md`](specs/001-remoteschooly/research.md#5-reducción-de-tokens).

## Spec Kit

El repositorio fue inicializado con [Spec Kit](https://github.com/github/spec-kit) estable `v1.0.4`,
siguiendo el flujo que resume [speckit.org](https://speckit.org): constitución → specify → evaluación
de calidad → plan → tasks → análisis. A diferencia del LAB03, aquí existe una única spec viva porque
el enunciado no exige un backlog limitado a títulos.

| Artefacto | Función |
|---|---|
| [Constitución](.specify/memory/constitution.md) | Gates no negociables |
| [Spec](specs/001-remoteschooly/spec.md) | Qué debe ocurrir y cómo se reconoce éxito |
| [Plan](specs/001-remoteschooly/plan.md) | Forma técnica y límites |
| [Research](specs/001-remoteschooly/research.md) | Decisiones y alternativas |
| [Modelo](specs/001-remoteschooly/data-model.md) | Entidades, invariantes y estados |
| [Contratos](specs/001-remoteschooly/contracts/sync-and-ai.md) | Sincronización, progreso, IA y reportes |
| [Quickstart](specs/001-remoteschooly/quickstart.md) | Cómo demostrar los recorridos en una futura implementación |
| [Tasks](specs/001-remoteschooly/tasks.md) | 53 tareas futuras; ninguna se presenta como implementada |

## Estructura

```text
.
├── .agents/skills/           # Skills de Spec Kit para Codex
├── .specify/                 # Constitución, plantillas y scripts oficiales
├── architecture/             # Iteraciones, fuentes DOT, SVG/PNG y trazabilidad
├── docs/                     # Enunciado original, transcripción, análisis y decisiones
├── evals/                    # Rúbrica, cuatro evaluadores, agregador e historial
├── personas/                 # Gobierno, Alumno, Profesora Lima, Profesor Provincia
├── scripts/                  # Render y validación mecánica
├── specs/001-remoteschooly/  # Spec Kit: spec, plan, research, modelo, contratos y tareas
└── business-rules.md         # Invariantes BR-01..BR-15
```

## Verificación local

```bash
./scripts/render-diagrams.sh
./scripts/validate_repo.py
git diff --check
```

La validación comprueba enlaces, 41 IDs secuenciales, trazabilidad 41/41, huella vigente del EVAL,
render de Graphviz, 53 tareas en formato Spec Kit y artefactos obligatorios.

## Proyectos hermanos

| Caso | Repositorio | Patrón heredado |
|---|---|---|
| #1 | [SWA-LAB01-UCI-Essalud](https://github.com/LuisMUtec/SWA-LAB01-UCI-Essalud) | Personas y evaluadores por perspectiva |
| #2 | [SWA-LAB02-Lease](https://github.com/LuisMUtec/SWA-LAB02-Lease) | Spec Kit, rúbrica con gate en 8 y artefactos por altitud |
| #3 | [SWA-LAB03-SendIt](https://github.com/LuisMUtec/SWA-LAB03-SendIt) | Top-down, iteraciones visibles, decisiones y trazabilidad al diagrama |
