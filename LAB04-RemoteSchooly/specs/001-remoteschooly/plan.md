# Implementation Plan: RemoteSchooly

**Branch**: `main` | **Date**: 2026-09-02 | **Spec**: [`spec.md`](spec.md)

**Input**: Feature specification from `specs/001-remoteschooly/spec.md`.

## Summary

RemoteSchooly distribuye paquetes semanales desde Lima hacia sedes con conectividad intermitente. Un
nodo local por escuela descarga recursos reanudables, verifica un manifiesto inmutable y sirve el
contenido por la red local. La autoría usa una frontera única de IA que limita contexto y salida,
reutiliza material aprobado y registra tokens contra una línea base comparable. El Gobierno recibe
cobertura y gasto agregados; el contenido personal de alumnos no cruza hacia IA ni hacia su tablero.

Este plan es un diseño de arquitectura. El laboratorio no autoriza afirmar que el sistema esté
implementado o desplegado.

## Technical Context

**Language/Version**: N/A para el entregable; las tareas futuras proponen TypeScript sobre una
versión LTS mantenida de Node.js, sin fijar una versión antes de iniciar la implementación.

**Primary Dependencies**: estándares HTTP para descargas parciales y validadores; cliente web
offline; proveedor de IA detrás de un contrato propio. Las bibliotecas concretas quedan diferidas.

**Storage**: base relacional central para metadatos y auditoría; almacenamiento de objetos
direccionado por contenido; índice de reutilización; base liviana y almacén de archivos en cada sede.

**Testing**: escenarios de aceptación del quickstart, validación mecánica de trazabilidad, prueba de
interrupción 10/50/90, corrupción, duplicado y corpus pareado de tokens.

**Target Platform**: centro en Lima; nodo Linux o portátil administrado en cada sede; navegadores de
profesores y alumnos sobre Internet o LAN según el rol.

**Project Type**: sistema web distribuido offline-first con centro y edge escolar.

**Performance Goals**: ninguna transferencia válida vuelve a cero tras un corte; `Listo` implica
100 % de integridad; todos los recursos obligatorios funcionan localmente; ahorro ≥ 40 % por unidad
aprobada con calidad constante.

**Constraints**: Internet limitado; recursos de sede acotados; cuatro roles; privacidad de alumnos;
sin clases en vivo; sin 100 % de disponibilidad ni alta disponibilidad avanzada en esta versión.

**Scale/Scope**: piloto de múltiples sedes y cursos; el enunciado no entrega cifras nacionales, por
lo que capacidad y costo se parametrizan y no se inventan.

## Constitution Check

### Pre-design gate

| Principio | Evidencia | Estado |
|---|---|---|
| Requisitos antes que arquitectura | EVAL 01 puntúa la spec inmutable `2c3a372` con 9.5/10 | PASS |
| Aprendizaje sin Internet continuo | `FR-017`–`FR-034`, `SC-001`–`SC-003` | PASS |
| Reducción de tokens medida | `FR-008`–`FR-015`, `SC-004`, `SC-005` | PASS |
| Todo comportamiento tiene dueño | Cuatro personas, permisos y tensiones trazados | PASS |
| Evaluación y trazabilidad | EVAL superado; matriz prevista en `architecture/TRACEABILITY.md` | PASS |

### Post-design gate

| Comprobación | Resultado |
|---|---|
| Cada componente de la iteración 3 tiene requisitos | PASS; tabla en `architecture/README.md` |
| Cada `FR-001`–`FR-041` llega a un componente | PASS; matriz en `architecture/TRACEABILITY.md` |
| Los cuatro happy paths se pueden recorrer | PASS; rutas HP-1 a HP-4 en el diagrama final |
| El diseño evita HA no solicitada | PASS; no hay réplica activa-activa, quorum ni failover multi-región |
| La IA no bloquea autoría ni publicación manual | PASS; AI Gateway queda fuera del camino manual |

## Architecture Shape

### Centro de Lima

- **Portal central** para Gobierno y Profesores de Lima.
- **Identity & Access** para roles, sedes y cursos autorizados.
- **Course & Assignment** para catálogo, semanas, sedes y asignaciones.
- **Authoring & Approval** para creación manual, revisión y publicación humana.
- **AI Gateway & Policy** para presupuesto, límites, reutilización, medición y delegación externa.
- **Package Builder** para manifiesto, versión y recursos direccionados por huella.
- **Sync Catalog** para asignaciones, versiones, revocaciones y sesiones.
- **Progress Ingest** para eventos idempotentes de la bandeja local.
- **Reporting & Audit** para cobertura, ahorro, participación agregada y trazas.
- Almacenamientos separados lógicamente: metadatos, objetos, tokens/reutilización y auditoría.

### Sede provincial

- **Sync Agent** descarga por fragmentos, reanuda, verifica y activa una versión completa.
- **Local Content Store** conserva paquetes listos y fragmentos parciales por separado.
- **Local Learning Portal** sirve contenido a profesor y alumnos sobre Wi-Fi/LAN.
- **Local Outbox** conserva avances y telemetría hasta la confirmación central.

### Fronteras externas

- **Proveedor de IA**: puede fallar o cambiar sin bloquear autoría manual.
- **Enlace de Internet**: es intermitente por definición; la LAN escolar no depende de él.

## Project Structure

### Documentation

```text
.
├── .agents/skills/                  # Skills oficiales de Spec Kit para Codex
├── .specify/                        # Constitución, plantillas y scripts de Spec Kit
├── architecture/
│   ├── README.md                    # Tres iteraciones y happy paths
│   ├── TRACEABILITY.md              # FR -> componentes -> iteración
│   └── diagrams/                    # Fuentes DOT y SVG renderizados
├── docs/                            # Enunciado, análisis, glosario y decisiones
├── evals/                           # Rúbrica, evaluadores y corridas inmutables
├── personas/                        # Cuatro usuarios modelo
├── scripts/                         # Validación mecánica del entregable
├── specs/001-remoteschooly/
│   ├── spec.md
│   ├── plan.md
│   ├── research.md
│   ├── data-model.md
│   ├── quickstart.md
│   ├── contracts/
│   ├── checklists/
│   └── tasks.md
└── business-rules.md
```

### Future source code

No se crea `src/` en este laboratorio. Una implementación futura debería separar `central/`,
`school-edge/` y `web-clients/`, pero crear esas carpetas ahora sugeriría código que no existe.

**Structure Decision**: repositorio de arquitectura dirigido por una única spec viva; los diagramas
y contratos son entregables, no sustitutos de implementación.

## Complexity Tracking

| Choice | Why Needed | Simpler Alternative Rejected Because |
|---|---|---|
| Nodo local por sede | La clase debe operar sin Internet externo | Un portal solo en Lima falla precisamente durante la clase |
| Almacén de objetos más metadatos relacionales | Recursos grandes e inmutables tienen un ciclo distinto a asignaciones y auditoría | Una sola base obliga a tratar video y metadatos como si fueran iguales |
| AI Gateway propio | La meta del 40 % necesita política y medición completas | Llamadas directas desde el portal dejan consumo sin dueño y sin línea base |

No se introducen microservicios por defecto. Los nombres del diagrama son componentes lógicos y
pueden empezar dentro de un despliegue central modular más un proceso de sincronización por sede.
