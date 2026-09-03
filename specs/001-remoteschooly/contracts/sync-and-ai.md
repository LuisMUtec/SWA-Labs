# Logical Contracts: Sync, Progress and AI

Contratos de diseño para una implementación futura. Los nombres HTTP son ilustrativos; los campos y
los invariantes son la parte vinculante.

## 1. Descubrir asignaciones

```http
GET /v1/sites/{siteId}/assignments?after={cursor}
Authorization: site credential
```

Devuelve asignación, versión, vigencia, estado central y URL del manifiesto. Solo incluye sedes
autorizadas (`FR-004`, `BR-11`). Una revocación viaja en el mismo flujo (`FR-027`).

## 2. Obtener manifiesto

```http
GET /v1/packages/{packageId}/manifest
If-None-Match: "manifest-version"
```

La respuesta es inmutable y contiene identidad del paquete más `resource_hash`, tamaño, obligatoriedad
y variante de cada recurso (`FR-017`, `FR-018`).

## 3. Descargar o reanudar recurso

```http
GET /v1/resources/{resourceHash}
Range: bytes={start}-{end}
If-Match: "resource-validator"
```

Un rango válido devuelve contenido parcial; un validador distinto obliga a descartar solo los
fragmentos que no resuelvan a la huella solicitada. El nodo nunca activa el recurso antes de verificar
tamaño y huella (`FR-021`–`FR-024`).

## 4. Reportar estado de sede

```http
POST /v1/sites/{siteId}/package-status
Idempotency-Key: {siteId}:{packageId}:{stateVersion}
```

Incluye paquete, estado local, bytes, recurso fallido, error accionable y momento observado. El centro
guarda además el momento recibido para distinguir estado antiguo de silencio (`FR-036`, `FR-041`).

## 5. Sincronizar avances

```http
POST /v1/progress/batches
Idempotency-Key: {batchId}
```

Cada entrada lleva un `progress_id` estable. La respuesta confirma identificadores individuales; los
no confirmados permanecen en la bandeja local (`FR-032`–`FR-034`).

## 6. Estimar una solicitud de IA

```http
POST /v1/ai/estimate
```

Entrada: docente, curso, tarea, fuentes aprobadas, unidad y límite de salida. Salida: presupuesto
restante, contexto estimado, límite, contenido reutilizable y si una llamada sería permitida. No
acepta campos de alumno (`FR-009`, `FR-010`, `FR-012`).

## 7. Ejecutar ayuda de IA

```http
POST /v1/ai/assist
Idempotency-Key: {authoringAttemptId}
```

La política puede devolver una propuesta reutilizada sin proveedor, una propuesta generada con su
medición, o un rechazo antes de llamar. Ninguna respuesta cambia el estado editorial a `Approved` o
`Published` (`FR-006`–`FR-011`).

## 8. Consultar cobertura gubernamental

```http
GET /v1/government/coverage?week={week}&region={region}
GET /v1/government/token-savings?period={period}
```

La cobertura devuelve estados por sede y última telemetría. El ahorro devuelve corpus, unidades,
tokens base/optimizados, porcentaje y calidad. Ninguna respuesta incluye prompts o entregas de
alumnos (`FR-036`–`FR-041`).

## Error envelope

Todo error incluye código estable, objeto afectado, acción sugerida y si el reintento conserva
progreso. Un error no puede cambiar `Incomplete` a `Ready` ni confirmar un avance que no persistió.
