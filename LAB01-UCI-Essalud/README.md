# Caso de Estudio #1 — Sistema de Gestión UCI (Essalud)

Arquitectura de Software · UTEC · 2026-II · **20 ptos**

Enunciado completo: [`docs/LAB-01-ARQ-2026.2.md`](docs/LAB-01-ARQ-2026.2.md)

## Equipo

| Nombre | GitHub | Rol |
|---|---|---|
| Luis Maquera | [@LuisMUtec](https://github.com/LuisMUtec) | |
| Johar Barzola | [@Joharjbe](https://github.com/Joharjbe) | |
| Fernando Aguilar | [@LordFernan](https://github.com/LordFernan) | |

---

## 1. Definición del Problema

Essalud lanza un piloto para gestionar sus Unidades de Cuidados Intensivos (UCI). El problema central es
el **desorden en los horarios de médicos y enfermeras** en un entorno de **alta rotación de médicos
internistas**, donde es crítico que el diagnóstico del turno saliente esté siempre disponible para el
turno entrante.

El piloto arranca en **Lima y sus distritos**, con proyección a escalar a nivel nacional.

### Problemáticas críticas

| # | Problema | Descripción |
|---|---|---|
| P1 | Rotación de doctor | El diagnóstico del médico previo debe estar disponible antes del cambio de turno. |
| P2 | Medianoche | Un paciente se agrava en turno noche: contactar rápido al médico encargado y manejar su indisponibilidad. |
| P3 | Actualizaciones en tiempo real | Notificaciones push a múltiples médicos/enfermeras y persistencia del diagnóstico con disponibilidad permanente. |

### Escalamiento esperado

| Hito | Hospitales |
|---|---|
| Lanzamiento | 1 K |
| 6 meses | 100 K |
| 2 años | 10 M |

### Metas de rendimiento

- Inicio de aplicación: **< 1 s**
- Configuración de aplicación: **< 5 s**
- Disponibilidad: **99.9 %**
- Recuperación ante caída: **< 5 min**

---

## 2. Usuarios / Clientes del Sistema

> Identificación de los actores que interactúan con el sistema. Completar en grupo.

| Actor | Tipo | Interacción principal | Persona modelo asociada |
|---|---|---|---|
| _(pendiente)_ | Directo / Indirecto | | |

---

## 3. Prompt de Evaluación

> Prompt usado para contrastar los requerimientos contra las definiciones de personas (usuarios modelo).

```text
(pendiente)
```

Resultado del agente [`Spec/Eval-Spec.MD`](Spec/Eval-Spec.MD): **__ %**

---

## Estructura del repositorio

```
README.md              # Este archivo: problema, usuarios/clientes y prompt de evaluación
/docs                  # Enunciado del caso de estudio
/Personas              # Un MD por persona / usuario modelo
/Requirements          # ReqFunc.MD y ReqNoFunc.MD
/Agents                # Definición de agente por cada persona
/Spec                  # Eval-Spec.MD — agente evaluador de calidad de requerimientos
```

## Cómo trabajamos

1. Cada quien toma una persona y escribe su MD en `/Personas` + su agente en `/Agents`.
2. Los requerimientos F y NF se consensúan en grupo antes de commitear.
3. Ramas por tema (`persona/pablo`, `reqs/funcionales`), PR a `main`.
4. La corrida de `Eval-Spec` se documenta al final en este README.
