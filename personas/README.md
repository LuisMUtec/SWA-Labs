# Personas de RemoteSchooly

Las cuatro personas vienen de los cuatro usuarios fijados por el encargo. Están en `status: proto`:
el enunciado nombra roles, no individuos, por lo que cada detalle operativo inventado permanece
marcado como supuesto.

| Persona | Rol | Qué ancla |
|---|---|---|
| [Valeria Rojas](Gobierno.md) | Gobierno | Cobertura real y control del presupuesto sin invadir datos personales |
| [Lucía Salazar](Profesora-Lima.md) | Profesora de Lima | Material aprobado y reducción medible de tokens |
| [Julio Quispe](Profesor-Provincia.md) | Profesor de Provincia | Paquete completo y utilizable antes de la clase |
| [Diego Huamán](Alumno.md) | Alumno | Aprendizaje desde la red local aun sin Internet |

## El recorrido completo

No existe una persona que pueda cerrar el valor sola:

```text
Gobierno asigna -> Lima aprueba -> Provincia sincroniza -> Alumno aprende
       ^                                                      |
       +---------- cobertura y participación agregada --------+
```

Los agentes de persona puntúan cada tramo por separado, pero el agregador comprueba que la costura
entre los cuatro no tenga saltos.

## Tensiones que los requisitos deben decidir

| ID | Tensión | Decisión en la spec |
|---|---|---|
| T1 | Material rico vs. ancho de banda y almacenamiento | Todo audiovisual obligatorio tiene alternativa de bajo consumo (`FR-031`). |
| T2 | Versión nueva vs. continuidad de la clase | La versión anterior completa sigue disponible mientras la nueva es parcial (`FR-025`). |
| T3 | Control desde Lima vs. autonomía offline | Lima publica y asigna; la sede sincroniza y sirve localmente (`FR-016`–`FR-030`). |
| T4 | Velocidad de IA vs. calidad y autoridad docente | IA es opcional, nunca publica y toda salida requiere aprobación (`FR-006`–`FR-007`). |
| T5 | Medición de ahorro vs. privacidad | Se miden tokens y resultados de autoría; datos de alumnos quedan fuera de IA y Gobierno (`FR-008`, `FR-012`, `FR-039`). |
| T6 | Cobertura nacional vs. telemetría intermitente | El tablero distingue silencio de error y muestra la fecha del último reporte (`FR-041`, `BR-13`). |
| T7 | Dispositivo compartido vs. privacidad del alumno | Permisos y avance se aplican por identidad activa, no por equipo (`FR-001`, `FR-005`). |

## Cómo se usan en el EVAL

Cada evaluador de `evals/agents/` lee solo su persona y la spec. Puede restar hasta un punto de D1 si
encuentra un paso sin cubrir, pero no puede sumar ni negociar con las otras personas. El agregador
lee las cuatro respuestas y comprueba problema, medida y coherencia.
