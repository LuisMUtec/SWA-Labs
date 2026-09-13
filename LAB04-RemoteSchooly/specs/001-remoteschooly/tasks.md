---
description: "Future implementation tasks for RemoteSchooly"
---

# Tasks: RemoteSchooly

**Input**: `spec.md`, `plan.md`, `research.md`, `data-model.md`, `contracts/` and `quickstart.md`.

**Scope note**: El laboratorio actual termina en diseño. Estas tareas permanecen sin marcar porque
describen una implementación futura; no son evidencia de código existente.

## Format

`[ID] [P?] [Story?] Description with exact path`

## Phase 1: Setup

- [ ] T001 Create future workspace folders in `central/`, `school-edge/`, `web-clients/` and `tests/`
- [ ] T002 Define shared identifiers and event envelopes in `contracts/shared/identifiers.schema.json`
- [ ] T003 [P] Configure formatting and static checks in `tooling/quality/`
- [ ] T004 [P] Add environment examples without secrets in `central/.env.example` and `school-edge/.env.example`
- [ ] T005 [P] Add central and edge build jobs in `.github/workflows/ci.yml`
- [ ] T006 Add fixture manifests and token corpus metadata in `tests/fixtures/`

## Phase 2: Foundational

- [ ] T007 Define Actor, Site, Course and CourseWeek persistence in `central/src/domain/program/`
- [ ] T008 Define Package, Manifest and Assignment persistence in `central/src/domain/content/`
- [ ] T009 Define AIUsage, TokenBaseline and TokenBudget persistence in `central/src/domain/ai/`
- [ ] T010 Define local package, chunk and outbox persistence in `school-edge/src/storage/`
- [ ] T011 [P] Implement role and scope authorization in `central/src/auth/authorization.ts`
- [ ] T012 [P] Implement local cached-session boundaries in `school-edge/src/auth/local-session.ts`
- [ ] T013 Implement append-only audit events in `central/src/audit/audit-log.ts`
- [ ] T014 Add shared idempotency middleware in `central/src/http/idempotency.ts`

## Phase 3: User Story 1 — Publicar con gasto controlado (P1)

**Independent Test**: el mismo corpus mantiene calidad y reduce ≥ 40 % entrada + salida por unidad.

- [ ] T015 [P] [US1] Add AI estimate contract tests in `tests/contracts/ai-estimate.test.ts`
- [ ] T016 [P] [US1] Add authoring-without-AI integration test in `tests/integration/manual-authoring.test.ts`
- [ ] T017 [P] [US1] Add paired token corpus test in `tests/integration/token-comparison.test.ts`
- [ ] T018 [US1] Implement manual authoring and approval in `central/src/authoring/authoring-service.ts`
- [ ] T019 [US1] Implement token budgets and preflight estimate in `central/src/ai/policy-service.ts`
- [ ] T020 [US1] Implement approved-unit reuse lookup in `central/src/ai/reuse-index.ts`
- [ ] T021 [US1] Implement provider-neutral metering adapter in `central/src/ai/ai-gateway.ts`
- [ ] T022 [US1] Implement paired baseline calculation in `central/src/ai/token-comparison.ts`
- [ ] T023 [US1] Build Lima authoring screens in `web-clients/central/src/pages/authoring/`
- [ ] T024 [US1] Block AI output publication without approval in `central/src/content/publication-policy.ts`

## Phase 4: User Story 2 — Sincronizar una sede intermitente (P1)

**Independent Test**: cortes al 10/50/90 reanudan y activan bytes idénticos al paquete publicado.

- [ ] T025 [P] [US2] Add manifest contract test in `tests/contracts/package-manifest.test.ts`
- [ ] T026 [P] [US2] Add range-resume tests in `tests/integration/sync-resume.test.ts`
- [ ] T027 [P] [US2] Add corruption and disk-full tests in `tests/integration/sync-failures.test.ts`
- [ ] T028 [US2] Implement immutable manifest builder in `central/src/packages/manifest-builder.ts`
- [ ] T029 [US2] Implement content-addressed resource publishing in `central/src/packages/resource-store.ts`
- [ ] T030 [US2] Implement assignment and revocation feed in `central/src/sync/sync-catalog.ts`
- [ ] T031 [US2] Implement resumable range downloader in `school-edge/src/sync/range-downloader.ts`
- [ ] T032 [US2] Implement hash verification and atomic activation in `school-edge/src/sync/package-activator.ts`
- [ ] T033 [US2] Implement previous-complete-version retention in `school-edge/src/content/version-manager.ts`
- [ ] T034 [US2] Build province synchronization screens in `web-clients/edge/src/pages/sync/`

## Phase 5: User Story 3 — Aprender offline (P2)

**Independent Test**: con Internet desconectado, alumno y profesor usan la semana y un reintento crea
un solo avance central.

- [ ] T035 [P] [US3] Add offline portal journey test in `tests/e2e/offline-class.test.ts`
- [ ] T036 [P] [US3] Add duplicate-progress test in `tests/integration/progress-idempotency.test.ts`
- [ ] T037 [US3] Implement local learning catalog in `school-edge/src/learning/catalog.ts`
- [ ] T038 [US3] Serve verified resources only in `school-edge/src/learning/content-server.ts`
- [ ] T039 [US3] Implement per-student local progress in `school-edge/src/progress/progress-store.ts`
- [ ] T040 [US3] Implement confirmed local outbox in `school-edge/src/progress/outbox-sync.ts`
- [ ] T041 [US3] Build offline teacher/student portal in `web-clients/edge/src/pages/learning/`

## Phase 6: User Story 4 — Gobernar cobertura y presupuesto (P3)

**Independent Test**: el tablero representa estados, silencio y ahorro sin prompts ni datos personales.

- [ ] T042 [P] [US4] Add coverage aggregation tests in `tests/integration/coverage-report.test.ts`
- [ ] T043 [P] [US4] Add privacy projection tests in `tests/integration/government-privacy.test.ts`
- [ ] T044 [US4] Ingest idempotent site telemetry in `central/src/reporting/site-telemetry.ts`
- [ ] T045 [US4] Aggregate participation without content in `central/src/reporting/participation.ts`
- [ ] T046 [US4] Implement comparable token dashboard query in `central/src/reporting/token-savings.ts`
- [ ] T047 [US4] Implement budget exception workflow in `central/src/ai/budget-exceptions.ts`
- [ ] T048 [US4] Build government coverage screens in `web-clients/central/src/pages/government/`

## Phase 7: Polish and cross-cutting verification

- [ ] T049 Run every scenario in `specs/001-remoteschooly/quickstart.md` and store evidence in `evidence/`
- [ ] T050 [P] Threat-model central, edge and AI boundaries in `docs/THREAT-MODEL.md`
- [ ] T051 [P] Verify low-consumption alternatives in `tests/accessibility/resource-variants.test.ts`
- [ ] T052 Re-run requirement-to-code traceability in `scripts/validate_repo.py`
- [ ] T053 Update implementation status without changing design claims in `README.md`

## Dependencies & Execution Order

```text
Setup -> Foundational -> US1 authoring -> US2 distribution -> US3 learning
                           \-------------------------------> US4 reporting
All selected stories -> Polish
```

- US1 produces the approved package input consumed by US2.
- US2 produces the local package consumed by US3.
- US4 can begin after foundational work and integrate each story's telemetry as it becomes available.
- Tasks marked `[P]` touch independent files and may run concurrently after their phase dependency.

## Implementation Strategy

1. Build US1 + US2 first: a verified package in one sede is the smallest end-to-end value.
2. Add US3 to prove the actual class works offline.
3. Add US4 after real status and token events exist; do not build a dashboard over invented data.
4. Preserve the design gate: no task is complete until its cited independent test passes.
