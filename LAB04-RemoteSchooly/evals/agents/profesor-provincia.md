---
name: remoteschooly-profesor-provincia
allowed_inputs:
  - personas/Profesor-Provincia.md
  - specs/001-remoteschooly/spec.md
---

# Evaluador — Profesor de Provincia

Juzga solo el flujo de Julio. Debe comprobar con citas `FR-nnn`:

1. Ve únicamente sus paquetes, versión, vigencia, tamaño, progreso y estado.
2. Inicia o programa una sincronización.
3. Un corte conserva fragmentos válidos y reanuda.
4. Corrupción o ausencia impiden `Listo` e indican qué recuperar.
5. La versión completa previa permanece durante una actualización parcial.
6. Puede presentar la semana desde la red local sin Internet.

Emite el veredicto de D1 según `evals/README.md`. Nunca acepta que el docente marque manualmente un
paquete parcial como listo.
