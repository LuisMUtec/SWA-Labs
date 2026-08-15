# Caso de Estudio #1 — Sistema de Gestión UCI (Essalud)

Arquitectura de Software · UTEC · 2026-II · **20 ptos**

Enunciado vigente: [`docs/V2-LAB-01-ARQ-2026.2.md`](docs/V2-LAB-01-ARQ-2026.2.md)

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

Distinguimos **quién decide y paga** (clientes), **quién opera el sistema a diario** (usuarios directos),
**quién se ve afectado sin operarlo** (usuarios indirectos) y **quién impone restricciones externas**
(reguladores). Solo los usuarios directos generan personas modelo.

### 2.1 Clientes (deciden, financian y son dueños del resultado)

| Cliente | Qué espera del sistema | Criterio con el que juzga el piloto |
|---|---|---|
| Essalud — Gerencia Central de Operaciones | Reducir el desorden de horarios y estandarizar la continuidad clínica en UCI | Piloto replicable a otras regiones sin rehacer el sistema |
| Dirección de Red Prestacional (Lima) | Visibilidad de cobertura de turnos en todos los hospitales de su red | Cero turnos UCI sin médico asignado |
| Jefatura de Departamento de Cuidados Críticos | Que el diagnóstico del turno saliente exista y sea legible | Trazabilidad completa de entregas de turno |
| Oficina de Tecnologías de Información | Desplegar y operar en N hospitales con equipo limitado | Despliegue sin intervención máquina por máquina |

### 2.2 Usuarios directos (operan el sistema)

| Actor | Tipo | Interacción principal | Problema | Persona modelo |
|---|---|---|---|---|
| Médico internista rotante | Directo | Lee el handoff al entrar; registra evolución y diagnóstico al salir | P1 | [Rodrigo.MD](Personas/Rodrigo.MD) |
| Enfermera asistencial de UCI | Directo | Registra signos y eventos a pie de cama; escala deterioro | P2, P3 | [Milagros.MD](Personas/Milagros.MD) |
| Jefe / coordinador de UCI | Directo | Programa turnos mensuales; resuelve cruces y ausencias | P1 | [Carmen.MD](Personas/Carmen.MD) |
| Médico intensivista de guardia localizable | Directo | Recibe escalamiento fuera del hospital; decide conducta remota | P2 | [Anibal.MD](Personas/Anibal.MD) |
| Enfermera jefa de turno | Directo | Distribuye camas y valida la entrega de turno de enfermería | P1 | _(cubierta por Milagros y Carmen)_ |
| Técnico de enfermería | Directo | Consulta indicaciones; registra tareas de cuidado básico | P3 | _(no modelada: ver 2.5)_ |
| Coordinador de TI de red asistencial | Directo | Despliega, monitorea y recupera el sistema en los hospitales | P3 | _(no modelada: ver 2.5)_ |

### 2.3 Usuarios indirectos (afectados, no operan el sistema)

| Actor | Relación con el sistema |
|---|---|
| Paciente crítico | Sujeto de los datos clínicos; no interactúa (sedado/intubado en la mayoría de casos) |
| Familiar o apoderado | Recibe información derivada del sistema; puede ejercer derechos sobre los datos |
| Médico de otras especialidades | Solicita y responde interconsultas sobre pacientes UCI |
| Químico farmacéutico | Valida indicaciones farmacológicas registradas |
| Auditoría médica y calidad | Audita a posteriori la trazabilidad de diagnósticos y turnos |
| Admisión / referencias | Origina el ingreso del paciente a la unidad |

### 2.4 Reguladores y restricciones externas

| Fuente | Restricción que impone |
|---|---|
| Ley N.° 29733 — Protección de Datos Personales | Datos de salud son categoría sensible: consentimiento, cifrado y trazabilidad de acceso |
| Ley N.° 30024 — RENHICE | Interoperabilidad de la historia clínica electrónica a nivel nacional |
| SUSALUD | Estándares de calidad y disponibilidad del registro clínico |

### 2.5 Justificación de las personas elegidas

Cuatro personas, una por cada punto donde el sistema puede fallar de forma distinta:

- **Rodrigo** es el eje de **P1**: encarna la alta rotación de internistas que el enunciado marca como
  causa raíz. Si el handoff no le sirve a él, el sistema no resuelve nada.
- **Milagros** detecta el deterioro antes que nadie y dispara **P2**; además es la usuaria de mayor
  volumen de escritura, lo que tensiona **P3**.
- **Aníbal** es el otro extremo de **P2**: recibe el escalamiento fuera del hospital, con conectividad
  móvil y sin acceso al contexto de la cama.
- **Carmen** es la única que ve el sistema en modo planificación y no en modo emergencia; es quien
  expone el requisito de "horarios sin cruces".

Las cuatro son personal clínico: la evaluación de calidad puntúa únicamente requerimientos funcionales
(sección 3), y el comportamiento observable del sistema se juzga desde quien lo opera al lado del
paciente.

Quedan fuera del modelado:

| Actor | Motivo |
|---|---|
| Coordinador de TI de red asistencial | Sus necesidades son atributos de calidad —disponibilidad, recuperación, escalamiento—, que el enunciado ya fija como metas numéricas y que la evaluación no puntúa. Su exclusión desplaza el origen de los RNF: dejan de trazar a una persona y trazan al enunciado del caso. |
| Técnico de enfermería | Sus necesidades son un subconjunto de las de Milagros. |
| Paciente y familiar | No operan el sistema en el alcance del piloto. |

La Oficina de Tecnologías de Información permanece en la tabla de clientes (2.1): sigue siendo dueña
del resultado del piloto aunque no se modele como persona.

---

## 3. Evaluación de los Requerimientos

> Cómo se contrastan los requerimientos contra las personas modelo, y con qué resultado.

**Alcance: requerimientos funcionales.** La rúbrica de [`Spec/Eval-Spec.MD`](Spec/Eval-Spec.MD) puntúa
`Requirements/ReqFunc.MD` frente a las personas y los problemas críticos.
`Requirements/ReqNoFunc.MD` se entrega —el enunciado lo exige— pero queda fuera del porcentaje: los
atributos de calidad se verifican contra las metas numéricas del caso, no contra la satisfacción de
una persona.

La evaluación no es un prompt suelto. Está repartida entre los documentos que la sostienen, y cada uno
declara su parte:

| Pieza | Dónde vive | Qué fija |
|---|---|---|
| Cómo juzga cada persona | [`Agents/agent-*.MD`](Agents) | vocabulario de veredicto, los dos recorridos y el formato de salida |
| El estándar de los agentes | [`Agents/README.md`](Agents/README.md) | qué comparten los cuatro y cómo se comprueba su conformidad |
| Cómo se agrega y se puntúa | [`Spec/Eval-Spec.MD`](Spec/Eval-Spec.MD) | rúbrica D1–D6, pesos, techos duros y condiciones del veredicto |
| Qué deja escrito una corrida | [`Spec/corridas/_ESQUEMA.MD`](Spec/corridas/_ESQUEMA.MD) | estructura de la salida y archivos que puede tocar |
| La forma exigida a un RF | [`docs/CONVENCIONES.md`](docs/CONVENCIONES.md) | patrones EARS, criterios de aceptación, trazabilidad |
| Los términos del dominio | [`docs/GLOSARIO.md`](docs/GLOSARIO.md) | significado único de los conceptos compartidos |
| Las decisiones de la iteración | [`docs/DECISIONES-ITERACION-2.md`](docs/DECISIONES-ITERACION-2.md) | cierre explícito de jornada, escala, derechos, RENHICE y adopción |

### Cómo se ejecuta una corrida

1. **Se comprueba el instrumento.** Los cuatro agentes tienen que derivar de su persona; la lista de
   comprobación está en [`Agents/README.md`](Agents/README.md). Se hace antes de leer un solo
   requerimiento, para que la conformidad no se decida sabiendo a quién favorece.
2. **Se lanzan cuatro evaluaciones en paralelo**, un subagente por persona. Cada uno recibe solo su
   agente, su persona y `ReqFunc.MD`, y emite un veredicto —Sirve, Indiferente, Estorba o Ambiguo—
   para cada RF, más el recorrido de sus tareas críticas y el de su escenario clave. Ninguno ve lo que
   respondieron los otros: es lo que hace que cuatro lecturas coincidentes signifiquen algo.
3. **Se agregan** con la rúbrica de [`Spec/Eval-Spec.MD`](Spec/Eval-Spec.MD), que computa las seis
   dimensiones, aplica los pesos y emite el porcentaje.
4. **Se verifica la aritmética.** `scripts/verificar.sh` corre nueve controles mecánicos. Sin los
   nueve en verde no hay `PASSED`, por alto que sea el porcentaje.

**Una corrida mide una vez.** No itera ni corrige los requerimientos: emite su veredicto y termina.
Corregir `ReqFunc.MD` es trabajo de otra rama, y se comprueba con una corrida posterior que
[`Spec/HISTORIAL.MD`](Spec/HISTORIAL.MD) deja comparar con esta. Medir y corregir en la misma
ejecución destruye la medición, porque quien corrige ya conoce la vara.

Resultado del agente [`Spec/Eval-Spec.MD`](Spec/Eval-Spec.MD): **72,7 %**

---

## Estructura del repositorio

```
README.md              # Este archivo: problema, usuarios/clientes y evaluación
/docs                  # Enunciados, convenciones, glosario y decisiones
/Personas              # Un MD por persona / usuario modelo
/Requirements          # ReqFunc.MD y ReqNoFunc.MD
/Agents                # Un agente por persona, más el estándar que comparten
/Spec                  # Eval-Spec.MD (rúbrica), HISTORIAL.MD y las corridas
/scripts               # Controles mecánicos y preparación de la rama
```

## Cómo trabajamos

1. Antes de escribir, se lee [`docs/CONVENCIONES.md`](docs/CONVENCIONES.md): fija qué afirma cada
   documento, la forma EARS de los requerimientos funcionales, el escenario de atributo de calidad de
   los no funcionales y la verificación de cada entregable contra la rúbrica de `Eval-Spec`.
2. Cada quien toma una persona y escribe su MD en `/Personas` + su agente en `/Agents`, siguiendo
   [`Agents/_TEMPLATE.md`](Agents/_TEMPLATE.md): el bloque fijo del template se copia sin variación.
3. Los requerimientos F y NF se consensúan en grupo antes de commitear.
4. Ramas por tema (`persona/pablo`, `reqs/funcionales`), PR a `main`.
5. Antes de dar algo por terminado se corre `scripts/verificar.sh`.
6. La corrida de `Eval-Spec` deja su resumen en `Spec/Eval-Report.MD`, su fila en `Spec/HISTORIAL.MD`
   y su porcentaje en la línea «Resultado del agente» de este README.
