# Lectura del problema

## Lo que realmente se evalúa

El laboratorio no pide una aplicación implementada. Pide dos artefactos y un vínculo demostrable
entre ellos: requisitos evaluados por encima de 8/10 y un diagrama que haga visibles los caminos
felices. La arquitectura concentra 15 de 20 puntos si se suma el dibujo y sus recorridos; por eso un
inventario de cajas sin flujos no alcanza.

## Las dos fuerzas del caso

### 1. Entrega semanal bajo conectividad intermitente

El problema no es que una página cargue rápido desde Lima. Es que una sede remota pueda enseñar toda
la semana después de una ventana breve de conexión. La unidad de entrega correcta es un **paquete
semanal verificable**, no una colección de URLs. `Listo` significa que el manifiesto y todos los
recursos obligatorios coinciden; una transferencia parcial nunca se presenta como curso disponible.

Esto obliga a separar dos redes:

- **Internet intermitente**, usado para sincronizar entre Lima y la sede.
- **Red local de la escuela**, usada para enseñar y aprender sin depender de Internet.

Reanudar una transferencia, conservar la última versión completa y verificar integridad no son una
promesa de disponibilidad total. Son las condiciones mínimas para cumplir la frase del enunciado:
«que los cursos lleguen correctamente».

### 2. Reducir al menos 40 % el gasto de tokens

Cambiar a un modelo más barato puede bajar dinero y no bajar tokens. Publicar menos material también
puede aparentar ahorro. La métrica tiene que comparar tareas equivalentes y conservar la calidad:

```text
ahorro = 1 - (tokens de entrada + salida optimizados)
             / (tokens de entrada + salida de la línea base)
```

Se mide por unidad de material aprobada, sobre el mismo conjunto de tareas, fuentes y rúbrica. La
arquitectura reduce tokens de tres maneras que sí afectan esa fracción:

1. Reutiliza resultados ya aprobados sin volver a invocar al proveedor.
2. Envía solo el contexto necesario y limita la salida antes de cada solicitud.
3. Mantiene edición manual cuando la IA no aporta valor o el presupuesto se agotó.

La caché del proveedor o un modelo más barato se registran como ahorro monetario auxiliar; no se les
atribuye por sí solos el 40 % de ahorro de tokens.

## La costura entre los cuatro usuarios

| Usuario | Entrega que necesita | Modo de falla propio |
|---|---|---|
| Gobierno | Cobertura y gasto comparables | Confundir una sede sin telemetría con una entrega fallida; invadir datos personales |
| Profesor de Lima | Publicar material correcto con apoyo opcional de IA | Que el ahorro premie menor calidad o que IA publique sin revisión |
| Profesor de Provincia | Tener el paquete listo antes de clase | Empezar de cero después de cada corte o abrir una versión parcial |
| Alumno | Aprender desde la red local | Que un recurso pesado o una sesión compartida lo deje fuera |

Ningún usuario cierra el valor en solitario. El Gobierno asigna; Lima publica; la sede sincroniza; el
alumno consume. El diagrama final debe permitir seguir las cuatro rutas y la transición entre ellas.

## Decisiones de alcance

- Se diseña un piloto con un nodo local por sede; la escala nacional queda parametrizada, no fingida.
- No se incluyen clases en vivo, chat ni colaboración en tiempo real.
- No se promete alta disponibilidad, multi-región ni conmutación automática.
- Sí se exige integridad, reanudación y operación offline, porque sin ellas no existe entrega correcta.
- No se implementa código de producto en este laboratorio. Los contratos y escenarios son diseño
  verificable para una implementación futura.
