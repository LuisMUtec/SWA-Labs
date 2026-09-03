---
name: remoteschooly-alumno
allowed_inputs:
  - personas/Alumno.md
  - specs/001-remoteschooly/spec.md
---

# Evaluador — Alumno

Juzga solo el flujo de Diego. Debe comprobar con citas `FR-nnn`:

1. Abre los recursos obligatorios desde la red local sin Internet.
2. Tiene alternativa de bajo consumo para recursos audiovisuales obligatorios.
3. Guarda avance local y recibe sincronización posterior.
4. Un reintento no duplica su entrega.
5. Un equipo compartido no mezcla identidad o avance.
6. Solo ve sus cursos y su propio avance.

Emite el veredicto de D1 según `evals/README.md`. Un edge case listado sin requisito que lo decida
cuenta como reserva o falla, según corte o no el recorrido.
