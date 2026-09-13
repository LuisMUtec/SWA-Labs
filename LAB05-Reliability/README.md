# Lab 5

Hola profe, este será el readme más manual que hemos realizado en nuestras vidas y lamentablemente (para nosotros) hicimos todas las task usando nuestro cerebro. Eso dolió

Solo usamos IA para corregir ortografía y subir los archivos.

![Prueba de que lo hicimos a mano](IMG_2849.jpg)

Identificamos 6 tareas según lo que pide el lab.

1. Halla el SPOF
2. Buscar los componentes de mayor riesgo.
3. Tipos de incidentes y sus variables individuales
4. Ciclo de vida de un issue
5. Diseño del nuevo harness
6. Diagrama de arquitectura

## 1. SPOF

Según la teoría, el SPOF viene a ser la pieza que si falla, compromete todo el flujo del sistema. Ademas de no tener un respaldo.

Por eso consideramos que el LLM es el SPOF.

Sin ese componente no hay comunicación mediante la api ni funcionarían los MCPs

## 2. Componentes de mayor riesgo

Aquí la diferencia es que el componente de riesgo puede causar daños graves pese a que siga funcionando. Consideremos 3:

* LLM: Causó el problema más grave cuando borró la BD y también nos cuentan que da respuestas incorrectas o con info desfasada.
* MCP de BD: Porque fue el punto de entrada cuando se borró la BD
* BD: Tiene los issues y en caso se borré, se pierde todo. Además que si no se lee el estado actual, un incidente cerrado puede aparecer como pendiente.

## 3. Issues

De cara al Harness, a cada tipo de issues, le asignamos variables y % de importancia para que por cada valor, obtengamos un valor y nos permita cuantificar la urgencia.

* Customer (prioritario, SLA de 1 día) : tiempo que falta para vencer el SLA, categoría del cliente (VIP, normal) y tipo de mercado (B2B, B2C).
* Support : mismas variables que Customer porque el problema viene de un cliente, más lo que ya hizo soporte (si lo diagnosticó o lo pudo contener). Estamos asumiendo SLA de 2 días para este caso.
* Engineering : tiempo que falta para vencer el SLA, Relevancia según rol (practi, analista, …, senior, lead), Sistema afectado (plataforma, bd, etc)

## 4. Ciclo de vida

Cuando entra un issue pasa por el LLM y se abren 3 caminos según la complejidad:

* Alta: pasa primero por un "embudo", que es unn diccionario con palabras clave potencialmente destructivas y después se crea el plan.md.
* Media: se crea directamente el plan.md.
* Baja: solo se permiten consultas de lectura. Si es una pregunta común, se usa la respuesta ya guardada para que siempre sea la misma. Si no, se lee el estado actual en la BD y se responde.

Alta y Media terminan en un plan.md que pasa por Human in the loop. Mientras más complejo es el issue, más aprobación humana pide el harness: Alta necesita más aprobación del ingeniero y Media menos

```mermaid
flowchart TD
    A["Entra un issue"] --> B{"LLM: ¿qué complejidad tiene?"}
    B -->|Alta| C["Embudo: diccionario de palabras destructivas"]
    C --> D["Crea plan.md"]
    D --> E["Human in the loop: más aprobación del ingeniero"]
    B -->|Media| F["Crea plan.md"]
    F --> G["Human in the loop: menos aprobación del ingeniero"]
    B -->|Baja| H{"¿Es una pregunta común?"}
    H -->|Sí| I["Usa la respuesta guardada"]
    H -->|No| J["Lee el estado actual en la BD"]
    I --> K["Responde (solo lectura)"]
    J --> K
```

## 5. Harness

Nosotros entendemos que el harness es todo lo que ponemos alrededor del LLM para que funcione bien y no dependa solo de él. El LLM sigue siendo el que responde, pero el harness decide qué información le va a llegar, qué hacer y cómo reaccionar cuando falla. El harness actual solo tenía la API y los MCP de base de datos y Slack, por eso nada frenó al LLM cuando borró la BD y cuando falla no hay plan B.

Lo que agregamos:

* Varios LLM con load balancer: como el LLM es nuestro SPOF, ponemos más de una instancia. El load balancer revisa el /health de cada una y si alguna se cae deja de mandarle issues, así las demás siguen respondiendo.
* Cola por urgencia: los issues entran a una cola y se ordenan con el puntaje de la parte 3. En la primera semana del mes, que es cuando llegan más incidentes, se atienden primero los que están por vencer su SLA.
* Circuit breaker: si el LLM empieza a fallar muchas veces seguidas, se cortan los pedidos por un rato para que se recupere y no se sature más. Mientras tanto las preguntas comunes se responden con las respuestas guardadas y lo demás espera en la cola.
* Control de acciones: el MCP de BD por defecto solo deja leer. Si hace falta cambiar algo, va en un plan.md y recién se ejecuta cuando el ingeniero lo aprueba en el human in the loop de la parte 4. Así el LLM ya no puede borrar nada por su cuenta.
* Backups y réplica de la BD: en la parte 2 vimos que si se borra la BD se pierde todo, por eso sacamos backups seguido y tenemos una réplica para recuperarla si pasa algo.
* Estado actualizado: el estado de un incidente siempre se lee de la BD. Si usamos caché le ponemos un TTL corto y se limpia apenas el incidente cambia de estado, así no aparece un incidente cerrado como pendiente.
* Respuestas guardadas: las preguntas comunes tienen una respuesta ya revisada en caché, entonces el LLM responde siempre lo mismo y no algo distinto cada día.
* Base de conocimiento: cada vez que se cierra un incidente guardamos cómo se resolvió y el LLM lo consulta antes de responder. Es su forma de aprender de casos anteriores sin reentrenarlo.
* Cola para Slack: si Slack no responde, los avisos se guardan y se mandan cuando vuelva, para que no frene lo demás.
* Métricas: para saber si cumplimos con disponibilidad, tolerancia a fallos y baja latencia medimos el P95 y P99 del tiempo de respuesta del LLM, la availability con 2xx / (2xx + 5xx) y la reliability con 2xx / (2xx + 4xx + 5xx). También contamos cuántos issues vencen su SLA.

### Sesiones por ingeniero

También entendemos que cada ingeniero abre una o más sesiones con el LLM por cada issue. El problema es cuando alguien es irresponsable y abre muchas sesiones para lo mismo. Cada sesión ocupa al LLM, entonces se satura más rápido, sobre todo en la primera semana del mes que es cuando llegan más incidentes. Además, cada sesión puede dar una respuesta distinta para el mismo issue, se pueden crear varios plan.md que se contradicen entre sí y los issues urgentes terminan esperando más en la cola.

Por eso proponemos un máximo de sesiones por ingeniero según la relevancia de su rol, la misma que usamos en la parte 3. Cuando alguien llega a su límite, el harness no le deja abrir más sesiones hasta que cierre alguna.

| Rol | Máximo de sesiones |
|---|---|
| Practicante | 10 |
| Analista junior | 20 |
| Analista semi senior | 35 |
| Senior | 50 |
| Lead AI | 100 |

Son valores de ejemplo y se pueden ajustar según cómo se use la plataforma.

## 6. Diagrama de arquitectura

Aquí juntamos todo lo anterior. Antes el sistema era API → LLM → MCP → BD y Slack, y si algo fallaba se caía todo. Ahora el LLM tiene respaldo, nada se ejecuta sin aprobación y la BD tiene réplica y backups.

Las flechas normales son el camino de un issue y las punteadas son lo que pasa por detrás, como las réplicas, los backups o lo que hace el circuit breaker cuando el LLM falla.

```mermaid
flowchart TD
    U["Ingenieros y soporte"]
    API["API LLM"]
    COLA["Cola por urgencia<br/>puntaje de la parte 3"]
    CB["Circuit breaker"]
    LB["Load balancer<br/>revisa /health"]
    CLS{"¿Qué complejidad tiene?"}
    MON["Métricas<br/>P95 y P99, availability,<br/>reliability y SLA vencidos"]

    subgraph LLMS["LLM con respaldo"]
        direction LR
        LLM1["LLM 1"]
        LLM2["LLM 2"]
        LLM3["LLM 3"]
    end

    subgraph CONTROL["Control de acciones"]
        EMB["Embudo<br/>palabras destructivas"]
        PLAN["plan.md"]
        HITL["Human in the loop<br/>el ingeniero aprueba"]
    end

    subgraph ACCESO["Acceso a la BD"]
        MCPL["MCP BD<br/>solo lectura"]
        MCPW["MCP BD<br/>cambios aprobados"]
    end

    subgraph DATOS["Datos"]
        CACHE["Caché<br/>respuestas guardadas y estados<br/>TTL corto"]
        BDP[("BD principal")]
        REP[("BD réplica")]
        BK[("Backups")]
        KB[("Base de conocimiento<br/>incidentes resueltos")]
    end

    subgraph AVISOS["Avisos"]
        AV["Cola de avisos"]
        MCPS["MCP Slack"]
        SL["Slack"]
    end

    U --> API --> COLA --> CB --> LB --> LLMS
    CB -.->|si el LLM falla| CACHE
    CB -.->|el resto espera| COLA
    LLMS --> CLS
    LLMS -.->|consulta| KB
    LLMS --> AV --> MCPS --> SL

    CLS -->|Baja| CACHE
    CLS -->|Baja| MCPL
    CLS -->|Media| PLAN
    CLS -->|Alta| EMB --> PLAN
    PLAN --> HITL
    HITL -->|aprobado| MCPW

    MCPL --> BDP
    MCPW --> BDP
    BDP -.->|réplica| REP
    BDP -.->|backups| BK
    BDP -.->|al cerrar un incidente| KB
    BDP -.->|limpia al cambiar un estado| CACHE

    API -.-> MON
    LLMS -.-> MON
```

## Carpetas para el evaluador de minions

El profe pidió por Discord que corramos el minions archi evaluator cuando ya tengamos la arquitectura. Ese evaluador lee tres carpetas, así que las agregamos solo para eso:

* `requirements/`: requerimientos funcionales y no funcionales, sacados de lo que explicamos en este README.
* `people/`: los usuarios de Genius-x.
* `diagram/`: el diagrama de la parte 6 como imagen.
