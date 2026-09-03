# Quickstart de validación

Guía para comprobar la arquitectura cuando exista una implementación. Hoy funciona como contrato de
demostración: no afirma que los comandos o servicios estén construidos.

## Prerrequisitos de una futura prueba

- Una instancia central con un curso, una semana y dos versiones.
- Una sede con nodo local y capacidad suficiente para un paquete.
- Cuatro identidades, una por rol.
- Un paquete fixture con manifiesto, recurso audiovisual y alternativa liviana.
- Un proveedor de IA simulado que reporte tokens y pueda fallar de forma controlada.

## Escenario A — autoría y 40 %

1. Ejecutar el corpus base de al menos 30 unidades y congelar tokens y calidad.
2. Ejecutar las mismas tareas con reutilización, contexto acotado y límites de salida.
3. Rechazar cualquier par que no alcance el umbral común de calidad.
4. Calcular `1 - optimizados/base` sobre entrada + salida de pares válidos.
5. Esperar ahorro ≥ 0,40 y el 100 % de solicitudes medidas o rechazadas antes del proveedor.
6. Deshabilitar el proveedor y confirmar que Lucía termina y publica manualmente.

## Escenario B — sincronización 10/50/90

Para cada punto de corte:

1. Asignar el paquete a la sede e iniciar sincronización.
2. Cortar Internet cuando los bytes verificados alcancen 10 %, 50 % o 90 %.
3. Confirmar que el paquete no aparece `Listo` y que la versión completa previa sigue activa.
4. Reconectar y comprobar que solo se solicitan rangos faltantes.
5. Comparar todas las huellas con el manifiesto y esperar `Listo`.

## Escenario C — corrupción

1. Alterar un recurso después de descargarlo.
2. Ejecutar verificación local.
3. Esperar `Incompleto`, recurso identificado y acción de recuperación.
4. Recuperarlo y esperar activación atómica de la misma versión.

## Escenario D — clase offline

1. Con un paquete listo, desconectar el enlace externo de la sede.
2. Julio abre y presenta la semana desde la LAN.
3. Diego abre todos los recursos y usa la alternativa de bajo consumo.
4. Diego completa una actividad; el nodo la muestra pendiente.
5. Reconectar, reenviar dos veces el mismo `progress_id` y esperar un solo avance central.

## Escenario E — gobierno y privacidad

1. Preparar sedes en estados distintos y una sede sin telemetría reciente.
2. Confirmar los cinco estados, versiones y fecha de último reporte.
3. Confirmar que la sede silenciosa aparece `sin reporte reciente`, no como fracaso confirmado.
4. Buscar prompts, respuestas individuales y entregas en la respuesta del tablero; esperar cero.

## Evidencia esperada

- Resultado del corpus y fórmula de ahorro.
- Registro de tokens por intento.
- Manifiesto y huellas del paquete final.
- Bytes transferidos antes/después de cada corte.
- Estados central/local y confirmaciones de progreso.
- Captura o exportación del tablero sin datos personales.
