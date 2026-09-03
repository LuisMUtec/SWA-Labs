# Trazabilidad de requisitos a arquitectura

`Iteración` indica la primera vista que hace visible el comportamiento completo, no solo al actor.
`HP` identifica el happy path donde se demuestra; `Cross` es una regla compartida.

| Requisito | Componente(s) responsable(s) | Iteración | HP |
|---|---|---:|---|
| FR-001 | Identity & Access; Sesión Local | 3 | Cross |
| FR-002 | Portal Central; Course & Assignment | 3 | H4 |
| FR-003 | Portal Central; Authoring & Approval | 3 | H1 |
| FR-004 | Identity & Access; Sync Catalog; Sesión Local | 3 | H2 |
| FR-005 | Identity & Access; Sesión Local; Portal Local | 3 | H3 |
| FR-006 | Authoring & Approval; AI Gateway & Policy | 3 | H1 |
| FR-007 | Authoring & Approval | 3 | H1 |
| FR-008 | AI Gateway & Policy; Tokens/baseline/reuse | 3 | H1 |
| FR-009 | Portal Central; AI Gateway & Policy | 3 | H1 |
| FR-010 | AI Gateway & Policy; reuse index | 3 | H1 |
| FR-011 | Authoring & Approval | 3 | H1 |
| FR-012 | AI Gateway & Policy; Identity & Access | 3 | H1 |
| FR-013 | AI Gateway & Policy; Token baseline | 3 | H1/H4 |
| FR-014 | Token baseline; Reporting & Audit | 3 | H1/H4 |
| FR-015 | AI Gateway & Policy; Reporting & Audit | 3 | H1/H4 |
| FR-016 | Authoring & Approval; Package Builder | 3 | H1 |
| FR-017 | Package Builder; Sync Catalog | 3 | H1/H2 |
| FR-018 | Package Builder; Objetos por huella | 3 | H1/H2 |
| FR-019 | Course & Assignment; Sync Catalog | 3 | H4/H2 |
| FR-020 | Nodo Escolar / Sync Agent | 2 | H2 |
| FR-021 | Sync Agent; Objetos por huella | 3 | H2 |
| FR-022 | Sync Agent; Objetos por huella; almacén local | 3 | H2 |
| FR-023 | Sync Agent; paquetes/fragmentos locales | 3 | H2 |
| FR-024 | Sync Agent; Portal Local | 3 | H2 |
| FR-025 | paquetes/fragmentos locales; Sync Agent | 3 | H2 |
| FR-026 | Portal Local; Sync Agent | 3 | H2 |
| FR-027 | Sync Catalog; Sync Agent | 3 | H2 |
| FR-028 | paquetes/fragmentos locales; Outbox local | 3 | H2/H3 |
| FR-029 | Nodo Escolar / Portal Local | 2 | H2 |
| FR-030 | Nodo Escolar / Portal Local | 2 | H3 |
| FR-031 | Package Builder; Portal Local | 3 | H1/H3 |
| FR-032 | Portal Local; Outbox local | 3 | H3 |
| FR-033 | Outbox local; Progress Ingest | 3 | H3 |
| FR-034 | Outbox local; Progress Ingest | 3 | H3 |
| FR-035 | Portal Local; Outbox local | 3 | H2 |
| FR-036 | Sync Catalog; Reporting & Audit; Portal Central | 3 | H4 |
| FR-037 | Tokens/baseline/reuse; Reporting & Audit | 3 | H4 |
| FR-038 | Course & Assignment; AI Gateway & Policy; Audit | 3 | H4 |
| FR-039 | Progress Ingest; Reporting & Audit | 3 | H4 |
| FR-040 | Reporting & Audit; Audit store | 3 | H4/Cross |
| FR-041 | Sync Agent; Sync Catalog; Reporting & Audit | 3 | H4 |

## Cobertura

- Requisitos en la spec: **41**.
- Requisitos con fila: **41**.
- Requisitos sin componente: **0**.
- Requisitos sin iteración: **0**.
- Requisitos sin happy path o marca `Cross`: **0**.

La validación mecánica de estos conteos vive en `scripts/validate_repo.py`.
