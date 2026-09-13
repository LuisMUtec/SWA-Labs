---
name: remoteschooly-agregador
allowed_inputs:
  - docs/LAB-04-ARQ-2026.2.md
  - .specify/memory/constitution.md
  - personas/README.md
  - specs/001-remoteschooly/spec.md
  - business-rules.md
  - cuatro veredictos de persona de la corrida actual
---

# Agregador del EVAL

1. Suma D1 desde los cuatro veredictos; no sustituye ninguno ausente.
2. Aplica los tres contrafácticos de D2 y cita requisitos que se volverían falsos.
3. Puntúa D3 con requisitos, criterios de éxito y casos de falla verificables.
4. Busca los ocho tipos de hallazgo de D4 y aplica sus techos duros.
5. Comprueba las cuatro condiciones de aprobación y vuelve a calcular la suma.
6. Produce una corrida con citas existentes, hallazgos concretos y `PASSED` o `FAILED`.

No modifica la spec durante la medición. Si encuentra un defecto, lo registra para una corrida
posterior.
