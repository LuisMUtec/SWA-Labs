---
persona: Valeria Rojas
rol: Responsable de seguimiento del programa educativo remoto del Gobierno
status: proto
---

# Valeria Rojas — Gobierno

## Contexto

[ASSUMPTION: Valeria coordina cobertura y presupuesto de un programa público que asigna cursos a
sedes remotas, pero no diseña material pedagógico ni revisa respuestas individuales de alumnos.]

## Flujo principal

**Cuando** empieza una semana académica, **quiero** saber qué paquete corresponde a cada sede, si
llegó correctamente y cuánto consumió la autoría con IA, **para** intervenir donde el programa no
cumple antes de que el problema se esconda en un promedio nacional.

1. Registra sedes, cursos, semanas, asignaciones y presupuesto.
2. Observa cada sede como asignada, sincronizando, lista, incompleta o revocada.
3. Contrasta tokens base, optimizados, unidades comparables y calidad.
4. Autoriza una excepción con motivo y vigencia cuando corresponde.
5. Revisa participación agregada después de la semana.

**Cuando sale mal:** una sede deja de reportar. Valeria necesita ver `sin reporte reciente`, no una
entrega fallida inventada ni un éxito basado en silencio.

## Qué se le interpone

- [ASSUMPTION: La conectividad hace que los reportes lleguen con horas o días de retraso.]
- Un único porcentaje nacional puede ocultar escuelas con semanas incompletas.
- El ahorro de dinero puede confundirse con ahorro de tokens o menor calidad.

## Permisos

- **Puede:** gobernar asignaciones, presupuestos, excepciones y consultar agregados.
- **Nunca debe:** leer prompts, respuestas individuales, entregas de alumnos ni editar contenido.

## Señal de éxito

- Cada estado del tablero tiene versión, sede y fecha de último reporte, y el ahorro del 40 % se
  demuestra sobre tareas comparables.
