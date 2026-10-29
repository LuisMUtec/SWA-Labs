# R — Requerimientos del caso Save Chernobyl

Extraídos del enunciado del Lab 12 (`00-enunciado.md`). No se agregó nada que no esté en el caso.

## Problema y usuarios

Una planta nuclear con 3 reactores funcionales tiene un sistema legacy que funciona, pero el control es demasiado manual: dificulta el control de la planta y hace perder tiempo a los empleados. Se pide modernizar el sistema de control sin detener ni reemplazar por completo el legacy.

El **operador** usa el panel para ver el estado en tiempo real, recibir alarmas, consultar reportes y comandar la planta. Los **medidores de temperatura** envían mediciones periódicas; cada reactor tiene un **controlador local** y la **refrigeración** que ese controlador comanda. El **Main Controller** toma las decisiones globales.

## Requisitos funcionales

| ID | Requisito |
|---|---|
| RF1 | Cada medidor de temperatura envía datos periódicamente; el envío promedio es cada 0.05 s. |
| RF2 | Cada reactor puede tener un controlador local que gestione la refrigeración y las alertas de ese reactor. |
| RF3 | El Main Controller recibe los datos, toma decisiones globales y envía comandos a los controladores. |
| RF4 | Panel para operadores con visualización en tiempo real, alarmas y reportes. |
| RF5 | Alertas cuando la temperatura supera los umbrales definidos. |
| RF6 | Si un sensor falla o el controlador central se desconecta, el sistema debe seguir controlando el reactor (failure scenarios). |
| RF7 | Registro de todas las acciones y datos para trazabilidad: quién prendió o apagó qué, y cuándo. |
| RF8 | Considerar como variante o piloto la librería nueva de manejo de eventos que mejoraría la latencia, sin reemplazar de golpe el mecanismo actual. |

## Requisitos no funcionales

| ID | Calidad | Criterio del caso |
|---|---|---|
| RNF1 | **Disponibilidad y tolerancia a fallos** | El control de cada reactor no puede depender de un único componente: identificar los SPOF y eliminarlos. |
| RNF2 | **Tiempo real** | Latencia mínima para las decisiones críticas (medición → decisión → comando a refrigeración / alarma). |
| RNF3 | **Escalabilidad hipotética** | Definir criterios de escalabilidad antes de tener datos: cuándo escalar, qué escalar y cómo, para hasta 100 sensores por reactor. |

## Restricciones del caso

| ID | Restricción | Condición del caso |
|---|---|---|
| RC1 | **Decisión errónea = desastre** | Hay interacciones con sensores y controladores; cualquier decisión errónea puede causar un desastre. |
| RC2 | **Coexistencia con el legacy** | El sistema actual controla los reactores y no puede ser reemplazado completamente ni detenido durante la modernización. La nueva arquitectura debe coexistir temporalmente con componentes legacy. |
| RC3 | **Hasta 100 sensores por reactor** | Cada reactor puede incorporar hasta 100 sensores, cada uno generando mediciones periódicamente. |
| RC4 | **Failure scenarios** | Considerar explícitamente qué pasa cuando un sensor deja de responder. |

## Entregables del lab

1. Diagrama de arquitectura con reliability y fault tolerance.
2. Criterios hipotéticos de escalabilidad (aún no hay datos para decidir).

Hint del enunciado: identificar los SPOF.
