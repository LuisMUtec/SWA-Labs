# Caso de Estudio #3 — SendIt

**Universidad de Ingeniería y Tecnología** · Departamento de Ciencias de la Computación
**Curso:** Arquitectura de Software (CS5382) — Teo. 1 · Lab. 11 · **Ciclo:** 2026-II
**Background:** Top Down Design · R.E.D.A.L.E. · **Puntaje:** 20 ptos · **Vence:** 2026-08-28 23:59

| | |
|---|---|
| **Integrantes** | _______________________________ |
| | _______________________________ |
| | _______________________________ |
| | _______________________________ |
| **Repositorio** | https://github.com/LuisMUtec/SWA-LAB03-SendIt |

> **Enunciado.** *Diseñe un sistema que permita mandar remesas a personas en diferentes países. El
> tema de seguridad es muy importante y también la consistencia de datos ya que estamos hablando de
> dinero.*
>
> **Entregables pedidos:** un **EVAL** con resultado de requerimientos —*8/10 aceptable*— y **todos
> los entregables del framework R.E.D.A.L.E.**, mostrando **claramente las iteraciones del diseño**.
> **Restricción:** los requerimientos van en **formato backlog**, solo el título.

---

## Resumen

SendIt es una red de remesas con **efectivo en las dos puntas**, modelo Western Union: quien envía
entrega billetes en la ventanilla de un agente afiliado y sale con un código; quien recibe cobra
billetes en otro mostrador, en otro país, contra ese código y su documento. Ninguna de las dos
puntas necesita cuenta bancaria. Entre la entrega y el cobro el dinero no es de ninguna de las dos:
está con SendIt, que lo **debe**. Ese intervalo es todo el problema.

**El usuario modelo es Rosa Quispe**, la remitente. Es quien decide usar SendIt o abandonarlo, quien
paga, y la única de las tres personas que elige libremente. La acompañan Elena —la destinataria en
Huanta, sin datos móviles y con el DNI vencido— y Kevin —el operario del mostrador, que no es el
guardián de la seguridad sino **el vector por donde se rompe**.

El entregable cubre los seis pasos de R.E.D.A.L.E.: un **backlog de 118 ítems** (101 funcionales, 17
no funcionales), una estimación con su aritmética a la vista (**13 servidores**, **3,2 TB
retenidos**, **1,6 Mbit/s en pico**), una arquitectura mixta con **32 endpoints** y **seis
decisiones cerradas**, un modelo de **30 entidades** repartidas en **10 bases**, **tres iteraciones
del diagrama de componentes** con trazabilidad **118/118**, y los tramos de escalamiento con sus
cinco cuellos de botella.

### El resultado del EVAL, dicho de una

**El EVAL dio 6,0 / 10 en la séptima ronda. El gate del enunciado es 8. No se alcanzó.**

```
Ronda      01     02     03     04     05     06     07
Puntaje   3,5 →  4,0 →  5,0 →  6,0 →  6,5 →  5,5 →  6,0
```

Siete rondas de evaluación con tres agentes de persona y un agregador movieron el backlog de 41 a
118 ítems y el puntaje de 3,5 a 6,0, con una regresión real en la sexta que la séptima revirtió
entera. **La séptima ronda además produjo el hallazgo más valioso de todo el trabajo:** el agregador
dictaminó, con evidencia de siete puntos de datos, que la dimensión `D4 = 2 − 0,25n` **no está
calibrada para un artefacto de 118 ítems** —varianza cero en las siete rondas— y que, en
consecuencia, **el techo real de este EVAL es exactamente 8,0 y coincide con el gate**. La rúbrica
**no se cambió**. La sección 11 desarrolla el dictamen completo, porque es el resultado que este
trabajo entrega y no el puntaje.

---

## 1. El caso y las personas

### El problema

Una persona necesita entregar dinero en un país y que otra lo reciba en otro, **sin que ninguna de
las dos tenga cuenta bancaria**. El enunciado nombra dos limitaciones y solo dos: **seguridad**,
porque el efectivo se entrega a un desconocido en una ventanilla que no es de SendIt, y
**consistencia de datos**, porque un giro pagado dos veces no es un registro sucio sino dinero
perdido que no se recupera. A eso se suma una tercera que el enunciado implica al decir *«diferentes
países»*: el negocio es transfronterizo y por tanto **multirregulador**, y un giro obedece a la vez
al regulador de origen y al de destino.

Lo que hace difícil el caso no es mover el dinero: es el intervalo. Mientras el giro viaja, SendIt no
es dueño del dinero —lo debe—, el tipo de cambio se mueve, las listas de sanciones cambian, el
mostrador de destino puede quedarse sin conexión con los billetes en la caja, y quien tiene que
decidir si paga es la persona con menos autoridad y más exposición de toda la cadena. **El diseño
entero consiste en decidir qué pasa dentro de ese intervalo.**

### Las tres personas

| Persona | Rol | Qué ancla | Modo de falla que solo ella ve |
|---|---|---|---|
| **Rosa Quispe** — *usuario modelo* | Remitente en Paterson, Nueva Jersey. Manda a Huanta USD 200–400 cada quincena | Que el envío llegue **por el monto y en la fecha prometidos** | La promesa de monto y fecha que nadie más está en posición de exigir |
| **Elena Quispe** | Destinataria en Huanta, 68 años. Cobra en efectivo en una bodega-agente. Sin datos, sin correo, sin cuenta. DNI vencido hace catorce meses | Que el último tramo, **el que no tiene pantalla**, también cierre | El envío que el sistema da por cerrado antes de que ella cuente los billetes |
| **Kevin Ramos** | Cajero del mostrador de un negocio afiliado. Paga con el efectivo **de su patrón**, no de SendIt | La **seguridad** del enunciado — es el vector, no el guardián | La operación cortada a la mitad: la única que rompe la **consistencia** con dinero ya en la mano |

### Por qué Rosa es el usuario modelo

El enunciado pide, como hint, *identificar correctamente quién es el usuario modelo*, en singular.
Una remesa tiene al menos cinco actores con un problema propio y legítimo. La decisión está
registrada como **D-01** y se argumenta por descarte:

| Candidato | Su problema | Por qué no es el usuario modelo |
|---|---|---|
| **Remitente (Rosa)** | Comprar una llegada: tantos soles, tal día | — |
| Destinataria (Elena) | Cobrar sin viajar en vano y sin que le falte | No elige el servicio: recibe por donde el remitente mandó |
| Operario (Kevin) | Cerrar la operación sin equivocarse, con cola detrás y con el efectivo de su patrón | Atiende el mostrador de un tercero afiliado. No elige SendIt: SendIt llegó a su negocio |
| Tesorería | Prefinanciar el corredor, cerrar la posición de cambio | Su problema es de la empresa, no del envío |
| Oficial de cumplimiento | Detener lo que hay que detener, con evidencia | Trabaja dentro de la empresa. Su día se resuelve sin que exista un cliente |

**Rosa.** Es quien decide usar SendIt o abandonarlo, quien paga, y la única de las cinco que elige
libremente. Un backlog que resuelve el día de Kevin y no el de Rosa **describe una red de agentes muy
bien controlada y sin clientes** — y el enunciado invita a ese error, porque nombra la seguridad y no
nombra al cliente.

**Elegirla no la vuelve la única, y esa es la otra mitad de la decisión:** el problema de Rosa **no se
resuelve dentro de la pantalla de Rosa**. La promesa que ella necesita la cumple o la rompe Elena en
la bodega de Huanta, y la sostiene o la pierde Kevin en el mostrador. Un diseño que solo mira su lado
declara el envío terminado cuando el dinero salió, que es exactamente el momento en que nada se
resolvió. Por eso hay tres personas y no una, y por eso **el usuario modelo no compra peso en la
rúbrica**: D1 reparte un punto por persona, igual para las tres.

### Las seis tensiones que el backlog tuvo que decidir

Estos conflictos son deliberados. Un conjunto de requerimientos que deja conformes a las tres
personas a la vez probablemente **evitó decidir** alguno — y eso lo cobra la rúbrica en D4 como
*tensión esquivada*.

| # | Tensión | Entre | En qué consiste |
|---|---|---|---|
| **T1** | Control ↔ rapidez | Rosa ↔ Kevin | Cada verificación que Kevin hace es tiempo que Rosa espera con la cola detrás. El control tiene que ocurrir **antes** de que Kevin toque el efectivo; Rosa quiere salir con su código y una promesa firme |
| **T2** | Explicación ↔ reserva | Rosa ↔ Kevin | Rosa exige saber por qué se detuvo su dinero. Kevin es la cara de SendIt y tiene **prohibido** decírselo cuando hay un reporte de por medio — y ni siquiera fue él quien decidió. No se resuelve redactando mejor un mensaje |
| **T3** | Verificación de identidad ↔ lo que Elena tiene | Elena ↔ Kevin | Kevin necesita saber quién cobra y responde con el efectivo de su patrón si se equivoca. Elena tiene un DNI vencido y una foto de hace veinte años, del lado donde no hay a quién reclamar |
| **T4** | Certeza del monto ↔ exposición cambiaria | Rosa ↔ la empresa | Rosa necesita que el monto en soles se fije al pagar. Fijarlo deja a SendIt cargando el movimiento del tipo de cambio hasta que Elena cobre — que puede ser nunca |
| **T5** | El canal de Rosa ↔ el canal de Elena | Rosa ↔ Elena | Rosa consulta desde su teléfono; Elena solo tiene llamada y mensaje de texto, y el código se lo pasa Rosa, no SendIt. Todo aviso que dependa de una pantalla deja a Elena afuera — y Elena es quien decide si viaja |
| **T6** | Cerrar el envío ↔ cerrarlo de verdad | Rosa ↔ Elena | Para el sistema es cómodo dar por terminado el envío cuando el dinero llegó al agente. Para Rosa y Elena termina cuando Elena contó los billetes. Entre esos dos momentos vive el defecto que nadie ve |

### Las decisiones que gobiernan el resto del documento

| # | Decisión | Qué gobierna |
|---|---|---|
| **D-01** | El usuario modelo es Rosa | Contra quién se mide si el backlog resolvió algo |
| **D-02** | Tres personas, no más | El reparto de D1: 3 = 1 + 1 + 1 |
| **D-03** | Se incluye el segundo paso `E` (Escalar), acotado | Cuántos entregables tiene R.E.D.A.L.E. en este caso |
| **D-04** | La rúbrica del EVAL se recorta respecto del Caso #2 | D3 pasa a medir **seguridad y consistencia**, que es lo que este enunciado nombra |
| **D-05** | «Las iteraciones del diseño» son iteraciones del **diagrama de componentes** | Qué se entrega como iteración y en qué orden se construye |
| **D-06** | El backlog adopta el formato literal del profesor | La forma exacta de cada ítem del único artefacto puntuado |
| **D-07** | SendIt opera el modelo **Western Union** | El canal de origen, quién es la tercera persona y la mitad de las reglas de seguridad |

**D-04** merece una línea, porque cambia qué mide el EVAL. La rúbrica llegó heredada del Caso #2,
donde D3 medía *«criterios de aceptación demostrables»*. Aquí el artefacto puntuado es un backlog de
**solo títulos** —el enunciado prohíbe describirlos—, así que la dimensión heredada mediría algo que
el enunciado prohíbe escribir y todo backlog sacaría 0. D3 pasa a ser **cobertura de seguridad y
consistencia**, dos puntos, uno por cada una: las dos únicas exigencias que el enunciado nombra por
su nombre dejan de depender de que alguien se acuerde de mirarlas.

**D-05** decide el entregable entero y no es una preferencia: es lo que el profesor mostró en clase.
El ejemplo de Leasing es **el mismo diagrama dibujado tres veces, cada vez más abierto** —#1 los
actores contra una sola caja; #2 esa caja abierta en servicios, bases y APIs externas; #3 el resto
del backlog—, con el backlog escrito en el mismo lienzo y los ítems ya cubiertos terminando en
`DONE`. La consecuencia operativa, que hay que sostener aunque incomode: **la iteración 1 es un
cuadrado**, y lo que fuerza la 2 es un ítem del backlog que el cuadrado no explica.

### Las reglas de negocio

Diecisiete reglas gobiernan el negocio y sobreviven a cualquier lista de requerimientos. Cada ítem
del backlog cita la que ejerce.

| # | Regla |
|---|---|
| **BR-01** | SendIt nunca es dueño del dinero, solo lo debe |
| **BR-02** | Un giro tiene exactamente un emisor, un receptor designado y un país destino |
| **BR-03** | El emisor se identifica **antes** de que SendIt acepte el efectivo |
| **BR-04** | Todo giro tiene un límite por operación, un acumulado por emisor y un acumulado por receptor |
| **BR-05** | Por encima de cierto monto, un giro exige una **segunda autorización** |
| **BR-06** | Emisor y receptor se tamizan contra listas de sanciones antes de mover dinero. Una coincidencia **detiene** el giro; no lo cancela |
| **BR-07** | El tipo de cambio se fija al crear el giro y **no se recalcula** |
| **BR-08** | El giro se identifica por un código que **solo el emisor** puede transmitir |
| **BR-09** | El receptor cobra contra código **y** documento; cuando el documento no está vigente, el tercer factor es el **desafío** que el emisor registró |
| **BR-10** | Un giro se paga **una sola vez** |
| **BR-11** | Ningún giro se paga sin que los fondos estén confirmados en el origen |
| **BR-12** | El emisor puede cancelar mientras el dinero no esté a disposición del receptor, y solo él |
| **BR-13** | Un giro pagado se corrige con un movimiento **nuevo**, nunca borrando el anterior |
| **BR-14** | Un giro no cobrado prescribe y el dinero vuelve al emisor |
| **BR-15** | Toda operación queda registrada con quién la hizo, y ese registro **no se altera** |
| **BR-16** | El operario ve lo que necesita para atender, **no el giro completo** |
| **BR-17** | Un giro transfronterizo obedece a los **dos** reguladores, y cuando chocan **no se elige uno**: no se crea |

---

## 2. R — Requerimientos (backlog)

**Este es el único artefacto que el EVAL puntúa.** Formato exigido por el enunciado: backlog, solo el
título, claro y entendible, sin descripción. Cada ítem sigue el formato literal del ejemplo de clase
fijado en **D-06**: *el sistema **[verbo en futuro] [capacidad]** - `<Persona>`*, con el sufijo de
persona cuando el ítem pertenece a alguien concreto — tal como *«el sistema me permitira ver mis
deudores y montos adeudados **- Leaser**»*. Eso da la trazabilidad que D4 exige —ningún huérfano— sin
agregar una sola línea de descripción.

### Preguntas de encuadre

| Pregunta | Respuesta |
|---|---|
| **¿Cuál es el problema?** | Una persona necesita entregar dinero en un país y que otra lo reciba en otro, **sin que ninguna de las dos tenga cuenta bancaria**. Entre la entrega y el cobro el dinero no está con ninguna: está con SendIt, que lo debe (BR-01). Ese intervalo es todo el problema |
| **¿Para quién lo resolvemos?** | Para **Rosa**, que paga y elige el servicio. Elena y Kevin existen porque sin ellos su operación no cierra |
| **¿Cuáles son las limitaciones?** | Las dos del enunciado: **seguridad**, porque el efectivo se entrega a un desconocido en una ventanilla ajena, y **consistencia de datos**, porque un giro pagado dos veces es dinero perdido, no un registro sucio. A eso se suma que el negocio es transfronterizo y por tanto **multirregulador** |

### El backlog — 118 ítems

**101 requerimientos funcionales y 17 no funcionales.** Los identificadores llegan hasta `RF-105` y
`RNF-17`; los huecos son **identificadores retirados**, y un identificador retirado no se reutiliza:
su número queda muerto (la tabla final de esta sección dice cuáles y por qué).

#### Funcionales · Creación del giro

| ID | Título | Persona | Regla | Prioridad |
|---|---|---|---|---|
| RF-01 | el sistema identificará al emisor contra un documento oficial vigente antes de crear un giro - Rosa | Rosa | BR-03 | P0 |
| RF-02 | el sistema entregará al receptor su dinero en efectivo, sin exigirle cuenta bancaria - Elena | Elena | BR-09 | P0 |
| RF-79 | el sistema dará el giro por creado en el momento en que registra la recepción del efectivo - Kevin | Kevin | BR-03 | P0 |
| RF-03 | el sistema exigirá un único receptor designado por giro - Rosa | Rosa | BR-02 | P0 |
| RF-04 | el sistema exigirá un único país destino por giro - Rosa | Rosa | BR-02 | P0 |
| RF-63 | el sistema permitirá al emisor elegir el punto de atención donde cobrará el receptor, entre los disponibles en el país destino - Rosa | Rosa | BR-02 | P0 |
| RF-05 | el sistema informará al emisor el monto exacto en moneda destino antes de que entregue el efectivo - Rosa | Rosa | BR-07 | P0 |
| RF-06 | el sistema conservará ese monto sin recalcularlo durante toda la vida del giro - Rosa | Rosa | BR-07 | P0 |
| RF-07 | el sistema producirá y fechará la cotización de la que sale ese monto - Rosa | Rosa | BR-07 | P0 |
| RF-08 | el sistema rechazará, antes de registrar la recepción del efectivo, el giro que haga al emisor superar su límite por operación - Rosa | Rosa | BR-04 | P0 |
| RF-09 | el sistema rechazará, antes de registrar la recepción del efectivo, el giro que haga al emisor superar su acumulado en la ventana vigente - Rosa | Rosa | BR-04 | P0 |
| RF-10 | el sistema contará esos límites sobre la identidad del emisor y no sobre el punto de atención - Kevin | Kevin | BR-04 | P0 |
| RF-11 | el sistema entregará el código de seguimiento del giro únicamente al emisor - Rosa | Rosa | BR-08 | P0 |
| RF-94 | el sistema no volverá a entregar un código ya emitido, ni siquiera al emisor que lo perdió - Rosa | Rosa | BR-08 | P0 |
| RF-12 | el sistema comprobará la respuesta del desafío sin mostrarla a quien atiende el mostrador - Kevin | Kevin | BR-09 | P0 |
| RF-13 | el sistema exigirá, antes de registrar la recepción del efectivo, la autorización de un segundo rol para un giro sobre el umbral reforzado - Kevin | Kevin | BR-05 | P0 |
| RF-14 | el sistema avisará al emisor por llamada o mensaje de texto que su devolución está disponible y en qué punto retirarla - Rosa | Rosa | BR-12 | P0 |

#### Funcionales · La frontera

Este bloque existe por una sola razón: **el giro cruza un país.** Si dejara de cruzarlo, **ninguno de
sus ítems tendría sentido** — y esa prueba se corre cada ronda del EVAL, no se declara. La iteración
01 mostró que un backlog sin este bloque describe un transmisor de dinero doméstico con un campo de
moneda.

| ID | Título | Persona | Regla | Prioridad |
|---|---|---|---|---|
| RF-15 | el sistema aplicará a un mismo giro las reglas del regulador de origen y las del regulador de destino - Kevin | Kevin | BR-17 | P0 |
| RF-16 | el sistema rechazará el giro cuando los dos reguladores impongan condiciones incompatibles, en vez de elegir una - Kevin | Kevin | BR-17 | P0 |
| RF-17 | el sistema reportará a la autoridad de origen el giro que supere su umbral de reporte transfronterizo - Kevin | Kevin | BR-17 | P0 |
| RF-18 | el sistema conservará el registro de un giro por el plazo más largo de los dos países que lo tocaron - Kevin | Kevin | BR-17 | P1 |
| RF-19 | el sistema informará al emisor que un país destino no puede atenderse antes de que entregue el efectivo - Rosa | Rosa | BR-02 | P0 |
| RF-20 | el sistema exigirá efectivo disponible en el corredor de destino antes de dar un giro por fondeado - Kevin | Kevin | BR-11 | P0 |
| RF-21 | el sistema informará al emisor en qué moneda cobrará el receptor, con su nombre y no solo su cifra - Rosa | Rosa | BR-07 | P1 |
| RF-22 | el sistema aplicará el umbral de reporte de cada país sobre el giro completo y no sobre su tramo local - Kevin | Kevin | BR-17 | P0 |
| RF-23 | el sistema impedirá que un giro rechazado por el regulador de destino se cree en el de origen - Kevin | Kevin | BR-17 | P2 |

#### Funcionales · Cumplimiento

| ID | Título | Persona | Regla | Prioridad |
|---|---|---|---|---|
| RF-26 | el sistema contrastará a emisor y receptor contra las listas de sanciones antes de aceptar el efectivo - Kevin | Kevin | BR-06 | P0 |
| RF-27 | el sistema contrastará al receptor contra las listas vigentes al momento de autorizar el pago - Kevin | Kevin | BR-06 | P0 |
| RF-97 | el sistema volverá a tamizar los giros aún no pagados cuando cambia una lista, y avisará por su canal a quien deje de poder cobrar - Kevin | Kevin | BR-06 | P1 |
| RF-28 | el sistema separará una coincidencia exacta de sanciones de una coincidencia por homonimia - Kevin | Kevin | BR-06 | P0 |
| RF-78 | el sistema resolverá la coincidencia por homonimia en un plazo más corto que la coincidencia exacta - Kevin | Kevin | BR-06 | P1 |
| RF-29 | el sistema dejará retenido el giro con coincidencia de sanciones, ni pagable ni cancelable - Kevin | Kevin | BR-06 | P0 |
| RF-30 | el sistema derivará el giro retenido a un rol distinto del operario que lo atendió - Kevin | Kevin | BR-06 | P0 |
| RF-31 | el sistema exigirá que toda retención lleve el plazo del regulador más estricto de los dos países del giro - Kevin | Kevin | BR-06 | P0 |
| RF-32 | el sistema devolverá al emisor el monto del giro cuya retención venció sin liberarse, y avisará al receptor por su canal - Kevin | Kevin | BR-06 | P0 |
| RF-71 | el sistema devolverá siempre en efectivo - Rosa | Rosa | BR-12 | P0 |
| RF-88 | el sistema devolverá siempre en la moneda que el emisor entregó - Rosa | Rosa | BR-12 | P0 |
| RF-72 | el sistema devolverá en el punto de atención que el emisor elija - Rosa | Rosa | BR-12 | P0 |
| RF-73 | el sistema informará al emisor el plazo de una eventual devolución antes de que entregue el efectivo - Rosa | Rosa | BR-12 | P0 |
| RF-96 | el sistema informará al emisor cuánto puede durar como máximo una revisión, antes de que entregue el efectivo - Rosa | Rosa | BR-06 | P0 |
| RF-89 | el sistema mantendrá disponible la devolución no retirada hasta el plazo de prescripción del giro - Rosa | Rosa | BR-12 | P2 |
| RF-74 | el sistema devolverá también la comisión cobrada cuando el giro no llegó a pagarse - Rosa | Rosa | BR-12 | P0 |
| RF-33 | el sistema permitirá liberar un giro retenido únicamente al rol de cumplimiento - Kevin | Kevin | BR-06 | P0 |
| RF-87 | el sistema registrará el motivo de cada liberación de un giro retenido - Kevin | Kevin | BR-06 | P1 |
| RF-58 | el sistema contará cuántos giros cobró un mismo receptor en la ventana vigente - Kevin | Kevin | BR-04 | P1 |
| RF-93 | el sistema retendrá el giro cuyo receptor superó su acumulado de cobros de la ventana - Kevin | Kevin | BR-04 | P0 |

#### Funcionales · Pago

| ID | Título | Persona | Regla | Prioridad |
|---|---|---|---|---|
| RF-34 | el sistema exigirá el código del giro para autorizar un pago - Elena | Elena | BR-09 | P0 |
| RF-85 | el sistema exigirá un documento de identidad cuyo titular coincida con el receptor designado - Elena | Elena | BR-09 | P0 |
| RF-86 | el sistema exigirá que el documento del receptor esté vigente - Elena | Elena | BR-09 | P0 |
| RF-68 | el sistema exigirá al emisor registrar al crear el giro una pregunta y su respuesta - Rosa | Rosa | BR-09 | P0 |
| RF-101 | el sistema no transmitirá a nadie la respuesta del desafío, ni siquiera a quien registró la pregunta - Rosa | Rosa | BR-09 | P0 |
| RF-102 | el sistema impedirá que el punto de atención cobre al receptor por recibir su dinero - Elena | Elena | BR-01 | P0 |
| RF-69 | el sistema entregará al receptor por su canal la pregunta del desafío cuando no tiene documento vigente - Elena | Elena | BR-09 | P0 |
| RF-82 | el sistema limitará a un número acotado los intentos de responder el desafío de un giro - Kevin | Kevin | BR-09 | P0 |
| RF-103 | el sistema devolverá al emisor el giro cuyos intentos de desafío se agotaron - Kevin | Kevin | BR-09 | P0 |
| RF-83 | el sistema caducará la respuesta del desafío junto con el giro que la lleva - Kevin | Kevin | BR-09 | P0 |
| RF-84 | el sistema decidirá qué diferencias de escritura cuentan como coincidencia de titular, y no el operario - Kevin | Kevin | BR-09 | P0 |
| RF-36 | el sistema no habilitará el pago de un giro cuyos fondos de origen no estén confirmados - Kevin | Kevin | BR-11 | P0 |
| RF-24 | el sistema liquidará con el agente el efectivo que puso de su caja, en el plazo acordado con él - Kevin | Kevin | BR-01 | P1 |
| RF-37 | el sistema avisará al receptor por llamada o mensaje de texto si su giro quedó retenido - Elena | Elena | BR-06 | P0 |
| RF-59 | el sistema responderá ante el emisor y el receptor por toda diferencia entre el monto fijado y el entregado - Elena | Elena | BR-13 | P0 |
| RF-104 | el sistema resolverá con el agente, por separado, la diferencia de la que respondió - Elena | Elena | BR-13 | P1 |
| RF-60 | el sistema informará al emisor y al receptor, cada uno por llamada o mensaje de texto, toda diferencia registrada sobre el giro - Elena | Elena | BR-13 | P1 |
| RF-90 | el sistema permitirá al receptor declarar por llamada o mensaje de texto que el dinero recibido no coincide con el informado - Elena | Elena | BR-13 | P0 |
| RF-91 | el sistema ofrecerá al emisor otro punto de atención cercano al elegido cuando ese no puede pagar - Rosa | Rosa | BR-02 | P0 |
| RF-105 | el sistema no cambiará el punto de atención elegido sin la respuesta del emisor - Rosa | Rosa | BR-02 | P0 |
| RF-39 | el sistema no dejará ningún giro rechazado, retenido ni en espera de autorización sin una salida que el operario pueda ofrecer - Kevin | Kevin | BR-16 | P0 |
| RF-40 | el sistema omitirá al operario el motivo de un rechazo cuando revelarlo esté prohibido - Kevin | Kevin | BR-16 | P0 |
| RF-25 | el sistema avisará al receptor que hay un giro a su nombre por llamada o mensaje de texto - Elena | Elena | BR-09 | P0 |
| RF-41 | el sistema informará al receptor por llamada o mensaje de texto, antes de que viaje, el monto que cobrará - Elena | Elena | BR-09 | P0 |
| RF-75 | el sistema informará al receptor por llamada o mensaje de texto si el punto elegido puede pagarle, y volverá a avisarle si deja de poder - Elena | Elena | BR-11 | P0 |
| RF-76 | el sistema registrará el efectivo que cada punto de atención declara al abrir y al cerrar su caja - Kevin | Kevin | BR-01 | P0 |
| RF-92 | el sistema informará al operario el efectivo disponible en su punto antes de habilitarle un pago - Kevin | Kevin | BR-01 | P0 |
| RF-95 | el sistema descontará del efectivo del punto cada pago que autoriza, sin esperar al cierre de caja - Kevin | Kevin | BR-01 | P0 |
| RF-77 | el sistema informará al emisor la fecha desde la cual el giro estará disponible para cobro, antes de que entregue el efectivo - Rosa | Rosa | BR-07 | P0 |

#### Funcionales · Interrupción y consistencia

| ID | Título | Persona | Regla | Prioridad |
|---|---|---|---|---|
| RF-42 | el sistema dejará el giro, o el efectivo ya recibido sin giro creado, en un estado único que el operario puede leer y retomar - Kevin | Kevin | BR-10 | P0 |
| RF-43 | el sistema tratará todo reintento de una creación interrumpida como la misma operación - Kevin | Kevin | BR-10 | P0 |
| RF-44 | el sistema tratará todo reintento de un pago interrumpido como la misma operación - Kevin | Kevin | BR-10 | P0 |
| RF-45 | el sistema impedirá que un punto sin conexión pague un giro que el centro ya retuvo, canceló o dio por pagado en otro punto - Kevin | Kevin | BR-10 | P0 |
| RF-100 | el sistema impedirá que un punto sin conexión autorice un pago que no puede comprobar contra el centro - Kevin | Kevin | BR-10 | P0 |

#### Funcionales · Cancelación y prescripción

| ID | Título | Persona | Regla | Prioridad |
|---|---|---|---|---|
| RF-46 | el sistema permitirá al emisor cancelar su giro mientras el dinero no esté a disposición del receptor - Rosa | Rosa | BR-12 | P0 |
| RF-47 | el sistema devolverá al emisor el monto entregado al cancelar, y avisará al receptor por su canal que ya no podrá cobrarlo - Rosa | Rosa | BR-12 | P0 |
| RF-48 | el sistema admitirá la cancelación de un giro únicamente del emisor que lo creó - Rosa | Rosa | BR-12 | P0 |
| RF-49 | el sistema dejará no pagable el giro cuyo plazo de prescripción venció - Rosa | Rosa | BR-14 | P0 |
| RF-50 | el sistema devolverá al emisor el monto del giro prescrito - Rosa | Rosa | BR-14 | P0 |
| RF-51 | el sistema avisará al emisor y al receptor, cada uno por llamada o mensaje de texto, antes de que el giro prescriba - Rosa | Rosa | BR-14 | P1 |

#### Funcionales · Consulta

| ID | Título | Persona | Regla | Prioridad |
|---|---|---|---|---|
| RF-52 | el sistema permitirá al emisor consultar el estado de sus giros sin depender del receptor - Rosa | Rosa | BR-01 | P0 |
| RF-53 | el sistema distinguirá al emisor el giro disponible para cobro del que todavía no lo está - Rosa | Rosa | BR-01 | P0 |
| RF-64 | el sistema dará el giro por cerrado en el momento en que el receptor recibe el dinero - Elena | Elena | BR-10 | P0 |
| RF-65 | el sistema avisará al emisor por llamada o mensaje de texto que su giro fue cobrado - Rosa | Rosa | BR-01 | P0 |
| RF-66 | el sistema mostrará al emisor que su giro está retenido y hasta qué fecha - Rosa | Rosa | BR-06 | P0 |
| RF-67 | el sistema avisará al emisor por llamada o mensaje de texto cuando su giro pase a estar retenido - Rosa | Rosa | BR-06 | P0 |

#### Funcionales · Registro y privilegio

| ID | Título | Persona | Regla | Prioridad |
|---|---|---|---|---|
| RF-54 | el sistema asociará cada acto sobre un giro a la identidad de quien lo ejecutó - Kevin | Kevin | BR-15 | P0 |
| RF-56 | el sistema registrará la corrección del **monto** de un giro pagado como un movimiento nuevo - Kevin | Kevin | BR-13 | P1 |
| RF-70 | el sistema impedirá alterar el receptor designado de un giro después de creado - Rosa | Rosa | BR-09 | P0 |
| RF-61 | el sistema exigirá la autorización de un segundo rol para corregir el monto de un giro pagado - Kevin | Kevin | BR-13 | P0 |
| RF-57 | el sistema limitará lo que el operario ve a los datos de la operación que está atendiendo, excluida la respuesta del desafío - Kevin | Kevin | BR-16 | P0 |
| RF-80 | el sistema conservará la evidencia de la identificación del emisor y del receptor de cada giro - Kevin | Kevin | BR-15 | P1 |
| RF-98 | el sistema conservará constancia de cada aviso que envió por el canal del receptor - Elena | Elena | BR-15 | P1 |
| RF-99 | el sistema descartará la evidencia de identificación de un emisor que no llegó a crear un giro - Kevin | Kevin | BR-15 | P1 |
| RF-81 | el sistema suprimirá a pedido los datos personales de quien los entregó, y de nadie más - Rosa | Rosa | BR-15 | P2 |

### No funcionales

El enunciado nombra dos como críticos —**seguridad** y **consistencia de datos**— y no da ninguna
cifra. Para la consistencia la medida correcta no es un número sino un **invariante**: algo que nunca
puede ser falso, y que por lo tanto se comprueba en cualquier momento. Un invariante es más fuerte
que un porcentaje porque no depende del conjunto de casos que alguien haya armado.

#### Seguridad

| ID | Título | Medida | Regla | Prioridad |
|---|---|---|---|---|
| RNF-01 | el sistema mantendrá ilegibles los datos de identidad para quien administre la infraestructura | Nadie que tenga acceso al almacenamiento reconstruye un documento de identidad | BR-08, BR-16 | P0 |
| RNF-15 | el sistema mantendrá ilegible el código de seguimiento para quien administre la infraestructura | El sistema puede comprobar un código sin poder mostrarlo | BR-08 | P0 |
| RNF-17 | el sistema mantendrá ilegible la respuesta del desafío para quien administre la infraestructura | El sistema puede comprobar una respuesta sin poder mostrarla | BR-08 | P0 |
| RNF-02 | el sistema impedirá que una misma identidad ejerza dos roles de un mismo giro | Ninguna identidad aparece dos veces en la cadena crear → autorizar → pagar → liberar → corregir de un mismo giro | BR-05 | P0 |
| RNF-03 | el sistema conservará inalterable el registro de actos | Ningún acto registrado se modifica ni se borra, cualquiera sea quien lo pida — y esa conservación prevalece sobre toda supresión | BR-15 | P0 |
| RNF-04 | el sistema dejará traza de todo acceso a datos de identidad | Todo acceso tiene autor, momento y giro; ninguno es anónimo | BR-16 | P1 |

#### Consistencia de datos

| ID | Título | Invariante | Regla | Prioridad |
|---|---|---|---|---|
| RNF-05 | el sistema impedirá que un giro quede pagado dos veces | Ningún giro registra dos entregas al receptor, en ningún punto y en ningún momento | BR-10, BR-11 | P0 |
| RNF-16 | el sistema impedirá que un giro quede pagado con un monto distinto del que se le informó al emisor | Ninguna entrega registrada difiere de la cifra que el emisor vio antes de entregar su efectivo | BR-07, BR-13 | P0 |
| RNF-06 | el sistema mantendrá un solo estado del giro entre el centro y el punto de atención | Dos lugares del sistema nunca afirman a la vez que un giro está retenido y disponible para cobro | BR-10 | P0 |
| RNF-13 | el sistema impedirá que un giro quede devuelto y cobrado a la vez | Ningún giro figura simultáneamente devuelto al emisor y entregado al receptor, en ningún punto y en ningún momento | BR-12 | P0 |
| RNF-07 | el sistema conservará la suma del dinero en toda operación | Lo que sale de una cuenta entra en otra; ningún movimiento deja el total distinto | BR-01 | P0 |
| RNF-08 | el sistema recuperará el estado de los giros de un punto caído sin intervención del operario | Un punto que vuelve no necesita que nadie le diga qué pasó mientras no estaba | BR-10 | P1 |

#### Servicio

| ID | Título | Medida | Prioridad |
|---|---|---|---|
| RNF-09 | el sistema resolverá en un tiempo acotado todo lo que no dependa de una persona ni de un sistema ajenos | `[ASSUMPTION: menos de 3 minutos]` desde que alguien llega al mostrador, incluida la verificación del documento. Una espera por un segundo rol o por una lista externa se mide aparte, y su suma no se descuenta de este techo | P1 |
| RNF-10 | el sistema dejará un giro fondeado disponible para cobro en el destino en un tiempo acotado | `[ASSUMPTION: menos de 15 minutos]` desde su creación | P0 |
| RNF-11 | el sistema sostendrá la capacidad de crear y de pagar giros | `[ASSUMPTION: 99,9 % mensual]`, medida sobre crear y pagar, no sobre consultar | P1 |
| RNF-12 | el sistema operará con más de un país de origen desde el primer día | Ninguna cifra ni regla del sistema supone un solo país de origen | P0 |
| RNF-14 | el sistema operará con más de una moneda destino desde el primer día | Ninguna cifra del sistema supone una sola moneda de destino | P0 |

### Las seis tensiones, y dónde quedan decididas

| Tensión | Entre | Cómo se decide | Ítems |
|---|---|---|---|
| **T1** Control ↔ rapidez | Rosa ↔ Kevin | **A favor del control, con precio acotado.** El tamizaje corre *antes* de aceptar el efectivo, de modo que se **detiene** en vez de revertir; a cambio, toda retención nace con plazo y se resuelve sola al vencerlo | RF-26 · RF-31 · RF-32 |
| **T2** Explicación ↔ reserva | Rosa ↔ Kevin | **Se decide en la altitud correcta, y en los dos mostradores.** Cuando revelar el motivo está prohibido, el operario recibe **la acción y no el motivo** — atiende sin saber y sin poder deducir. Y del lado de Rosa: ve **que** está retenido y **hasta cuándo**, nunca por qué | RF-39 · RF-40 · RF-66 · RF-67 |
| **T3** Identidad del receptor | Elena ↔ Kevin | **Se parte.** La regla dura queda: el documento tiene que estar **vigente** (RF-86) y **qué cuenta como coincidencia lo decide el sistema, no el operario** (RF-84). La salida al documento vencido es el **desafío**: el emisor lo registra (RF-68), el sistema le entrega la pregunta al receptor por su canal (RF-69), **no transmite la respuesta a nadie** (RF-101), la comprueba sin mostrarla (RF-12, RF-57, RNF-17), acota intentos (RF-82) y devuelve al agotarlos (RF-103) | RF-86 · RF-84 · RF-68 · RF-69 · RF-101 · RF-12 · RF-82 · RF-103 |
| **T4** Certeza del monto ↔ exposición cambiaria | Rosa ↔ la empresa | **A favor de Rosa.** El monto de destino se fija al crear el giro y no se recalcula nunca, con una cotización que el sistema produce y fecha. **La empresa carga el movimiento** | RF-05 · RF-06 · RF-07 |
| **T5** El canal de Rosa ↔ el de Elena | Rosa ↔ Elena | **Se parte en dos, y los dos canales están nombrados.** El **código** y la **respuesta** del desafío son secretos que el sistema no transmite a nadie (RF-11, RF-94, RF-101): solo Rosa los pasa. Todo lo demás —aviso, monto, disponibilidad, pregunta del desafío, mala noticia— viaja **por llamada o mensaje de texto a los dos**, porque ninguno origina desde una aplicación | RF-11 · RF-94 · RF-101 · RF-25 · RF-41 · RF-69 · RF-14 · RF-65 · RF-67 |
| **T6** Cerrar ↔ cerrar de verdad | Rosa ↔ Elena | **A favor de Elena, con ítem que lo diga.** El giro cierra en el momento en que el receptor recibe el dinero, no al fondearse ni al quedar disponible. Y el límite de la cancelación se corre para que Rosa no pueda anular con Elena en la ventanilla: no es «mientras no esté pagado» sino **mientras el dinero no esté a disposición del receptor** | RF-64 · RF-65 · RF-46 |

### Reparto de prioridad

| | P0 | P1 | P2 | Total |
|---|---:|---:|---:|---:|
| Funcionales | 84 | 14 | 3 | **101** |
| No funcionales | 13 | 4 | 0 | **17** |
| **Total** | **97** | **18** | **3** | **118** |

La rúbrica tiene un techo duro para esto: si **todos** los ítems comparten la misma prioridad, D4 no
supera 1,5. Una lista sin gradiente no está priorizada.

### Supuestos y ambigüedades

| Marca | Dónde | Estado |
|---|---|---|
| `[ASSUMPTION: modelo Western Union — red de agentes, efectivo contra efectivo, sin cuenta bancaria en ninguna punta]` | Todo el backlog | **Vigente** — indicación del profesor |
| `[ASSUMPTION: umbral de límites (BR-04) y umbral reforzado (BR-05)]` | RF-08 · RF-09 · RF-13 | Vigente |
| `[ASSUMPTION: umbrales de servicio de RNF-09 a RNF-11]` | RNF-09 · RNF-10 · RNF-11 | Vigente — **los consume el paso `E`** |
| `[ASSUMPTION: el plazo de prescripción lo fija el regulador de origen; a falta de norma expresa, 12 meses desde la creación]` | RF-49 · RF-50 · RF-51 · BR-14 | **Cerrada** |
| `[ASSUMPTION: la conservación es el plazo más largo de los dos reguladores del giro, con un piso de 5 años]` | RNF-03 · RF-18 | **Cerrada** en la iteración 03 — el paso `E` ya puede dimensionar |
| `[ASSUMPTION: dos corredores al lanzamiento — Estados Unidos → Perú y Estados Unidos → México]` | RNF-12 · RNF-14 | **Cerrada** — dos monedas destino, para no romper RNF-14 |
| `[ASSUMPTION: la retención dura lo que fije el regulador más estricto de los dos países; a falta de norma expresa, 72 horas]` | RF-31 · RF-32 | **Cerrada** — sin techo global, para no contradecir a RF-31 |

### Identificadores retirados

Un identificador retirado **no se reutiliza**: su número queda muerto. La iteración 05 aprendió por
qué —reusar `RF-02`, `RF-12`, `RF-14`, `RF-37` y `RF-58` produjo una **deriva semántica que ningún
`grep` delata**, porque el puntero sigue resolviendo a un ítem que dice otra cosa.

| ID | Por qué se retira | Qué lo cubre ahora |
|---|---|---|
| `RF-35` | Duplicado encubierto: decía como comportamiento lo que un invariante ya decía | **RNF-05** — «ningún giro registra dos entregas al receptor, en ningún punto y en ningún momento» |
| `RF-62` | Ídem | **RNF-13** — «ningún giro figura simultáneamente devuelto al emisor y entregado al receptor» |
| `RF-55` | Ídem | **RNF-03** — «ningún acto registrado se modifica ni se borra» |
| `RF-38` | Ídem | **RNF-16** — «ninguna entrega difiere de la cifra que el emisor vio antes de entregar su efectivo» |

---

## 3. E — Estimar

**Las tres cifras, con su aritmética a la vista.** Ninguna sale del enunciado —**el enunciado no da
ni un número**— y por eso cada entrada lleva su `[ASSUMPTION]` con la calibración contra la que se
defiende. Las divisiones se muestran enteras: esto se audita dividiendo, no creyendo.

> ### 🖥 13 servidores  ·  💾 3,2 TB retenidos  ·  📡 1,6 Mbit/s en pico
>
> `1,01 GB/día` de almacenamiento nuevo · `196 KB/s` en la hora pico · `2 800 giros/día` de carga

### El hallazgo, antes que las cifras

**La carga de SendIt pide `0,09` servidores. Lo que pide once es RNF-11 y la geografía de los dos
corredores.** Este sistema no se rompe por CPU: se rompe por la cuota del canal de voz y SMS y por el
efectivo de la caja del punto, y ninguna de las dos se arregla comprando máquinas.

### Las entradas, y por qué no son las del material

El material pide cinco entradas: usuarios registrados, usuarios activos, RPS, **logins por segundo**
y almacenamiento. Tres de ellas suponen un modelo que este backlog no tiene. **SendIt no tiene cuenta
ni sesión:** RF-01 identifica al emisor presencialmente contra un documento vigente **cada vez** que
se crea un giro, y RF-11 le entrega un código de seguimiento —no una credencial— que solo él
transmite. No hay padrón que contar ni login que medir. Dimensionar sobre «usuarios registrados»
mediría un sistema que no es este.

Las unidades de carga de SendIt son tres, y la tercera no deriva de las otras dos:

| Entrada | Qué cuenta | Valor | De dónde sale |
|---|---|---:|---|
| **Giros por día** | Giros creados sobre los dos corredores de RNF-12 | **2 800** | `0,5 % de USD 61 300 M/año ÷ USD 300 de ticket ÷ 365` — derivación abajo |
| **Operaciones de ventanilla por día** | Atenciones presenciales: crear, pagar, autorizar, corregir, devolver, declarar diferencia, rederivar | **5 900** | `2 800 crear + 2 690 pagar + 84 autorizar (RF-13) + 8 corregir + 95 entregar devolución + 13 declarar diferencia + 54 rederivar + 179 identificar sin giro = 5 921`. Son **2,11 ventanillas por giro**, no 2 |
| **Aperturas y cierres de caja por día** | `puntos × turnos × 2` (RF-76). **No depende de los giros** | **9 000** | `3 000 puntos × 1,5 turnos × 2`. Es **3,2 veces** el número de giros del día: la carga con piso es mayor que la carga de negocio |
| **Avisos al receptor por día** | Unidades de voz o SMS entregadas a un tercero. Se pagan **por unidad**, no por byte | **13 720** | `4,9 unidades por giro × 2 800`. A USD 0,05: `USD 686/día` = **USD 250 k/año** = **USD 0,24 por giro** |
| Giros por día en pico | `giros × 3,0` (componente **diario** de `P`) | **8 400** | `2 800 × 3,0` |
| RPS | Derivada del desglose por operación | **0,89 promedio · 9,8 en pico** | `76 785 requests/día ÷ 86 400 s = 0,889` · `× 11 = 9,78` |
| **Factor de pico `P`** | Ventana de **una hora** | **11** | `3,0 (día señalado) × 3,6 (hora del día) = 10,8` |

#### De dónde salen los 2 800 giros por día

Un supuesto de volumen que no se calibra contra nada es un número inventado con formato de
estimación. Se calibra contra el tamaño real de los dos corredores:

1. **Tamaño de los corredores.** México recibe del orden de **USD 62 000 M/año** en remesas, ≈ 96 %
   desde Estados Unidos → `62 000 × 0,96 ≈ USD 59 700 M`. Perú recibe ≈ **USD 4 600 M/año**, ≈ 35 %
   desde Estados Unidos → `4 600 × 0,35 ≈ USD 1 600 M`. Suma: `59 700 + 1 600 = USD 61 300 M/año`.
2. **Cuota de SendIt al lanzamiento: 0,5 %** → `61 300 × 0,005 = USD 306,5 M/año`. Medio punto de un
   mercado con incumbentes de treinta años es agresivo sin ser fantasioso para un año 1 apoyado en
   red afiliada. **Es la cifra de la que más depende todo el documento.**
3. **Ticket promedio USD 300** (punto medio del rango de Rosa) → `306 500 000 / 300 = 1 021 667`
   giros/año.
4. **A giros por día** → `1 021 667 / 365 = 2 799` → **2 800 giros/día**.

**Contraste *bottom-up*, que es la única forma de saber si el número de arriba miente.** `2 800 ×
30,4 = 85 120 giros/mes`; a 2 giros por emisor y mes (la quincena de Rosa) son `85 120 / 2 = 42 560`
emisores distintos al mes. Repartidos en 3 000 puntos: `42 560 / 3 000 ≈ 14` emisores por punto y
mes, es decir **menos de un giro por punto y por día**. Una red ancha y flojamente cargada es
exactamente la forma del modelo Western Union. Si el *bottom-up* hubiera dado cien giros por punto y
día, uno de los dos supuestos estaría roto.

**El reparto entre corredores no es uniforme,** y decide el multiplicador de retención:
`1 600 × 5,0 % = USD 80 M` (Perú) y `59 700 × 0,38 % = USD 226,5 M` (México). A ticket igual, el
reparto por giros es `80 / 306,5 = 26 %` **Perú** y `226,5 / 306,5 = 74 %` **México**.

#### El factor de pico

Las remesas no son planas: el volumen se concentra en la quincena y se dispara en fechas señaladas.
El sistema pasa la mayor parte del año por debajo de su capacidad y falla los pocos días que a Rosa
le importan. De ahí la regla: **se dimensiona contra el pico, no contra el promedio.**

| Ventana | Multiplicador | Qué la produce |
|---|---:|---|
| Quincena / fin de mes | **2,0×** | `40 % del volumen del mes en 6 días` → `(0,40/6) / (1/30,4) = 2,03` |
| Fecha señalada | **3,0×** | Día de la Madre, Navidad, inicio del año escolar. Se **apilan** sobre la quincena → `2,0 × 1,5 = 3,0`. **Es el que dimensiona** |
| Hora del día | **3,6×** | Huso del emisor. `15 % del día en 1 h → 0,15 × 24 = 3,6` |

**El compuesto no es la suma de los tres.** La quincena ya está dentro de la fecha señalada:
`P = 3,0 (diario) × 3,6 (intradía) = 10,8` → **`P` = 11**, ventana de **una hora**. Un pico de una
hora se enfrenta con capacidad ya encendida; uno de una semana, con otra arquitectura.

**Ningún RNF del backlog fija este factor**, y se declara así en vez de heredarlo de un RNF que no lo
dice. Es el supuesto más frágil de los grandes.

#### Los umbrales de servicio, consumidos aquí

| RNF | Umbral | Qué restringe | Valor derivado |
|---|---|---|---|
| **RNF-09** | Ventanilla en < 3 min, incluida la verificación del documento | Servidores (latencia por operación) | `180 s − 150 s de tiempo humano = 30 s de máquina`. Una creación encadena ≈ 9 requests → `30/9 = ` **3,3 s por request en p99**. Cabe la llamada a las listas; **no** cabe la espera por el segundo rol, y RNF-09 la mide aparte por eso |
| **RNF-10** | Disponible para cobro en destino en < 15 min | Servidores y ancho de banda | `900 s` de ventana. Una réplica asíncrona propaga en ≈ 1 s → **900× de margen**. Conclusión: **RNF-10 no obliga a escritura síncrona multirregión** |
| **RNF-11** | 99,9 % mensual sobre **crear y pagar**, no sobre consultar | Servidores | `43 200 min × 0,001 = ` **43,2 min/mes** de presupuesto de error. Un nodo solo no lo cumple → **3 nodos con quórum** en escritura; la consulta queda excluida y se sostiene con **2** sin quórum. **Es el término que manda** |

### Cálculo 1 — Servidores requeridos

El método del material: capacidad de un core → capacidad de un servidor → `carga / capacidad`.

> **Ejemplo del material, para la forma.** Un core a 5 req/s · servidor de 32 cores → `32 × 5 = 160`
> req/s · carga de 100 k req/s → `100 000 / 160 = ` **625 servidores**.

Se calcula **en dos columnas y no en una**: promediar una escritura contable con una consulta de
estado promedia dos cosas que no se promedian.

| Paso | Fórmula | Escritura contable | Lectura |
|---|---|---|---|
| 1. Capacidad de un core | req/s por tipo de operación | **5 req/s** | **50 req/s** |
| 2. Capacidad de un servidor | `#cores × core`, servidor de 16 vCPU | `16 × 5 = ` **80 req/s** | `16 × 50 = ` **800 req/s** |
| 3. Carga objetivo | `RPS × P` | `50 729 / 86 400 = 0,587`, `× 11 = ` **6,45 req/s** | `26 056 / 86 400 = 0,302`, `× 11 = ` **3,32 req/s** |
| 4. Servidores | `carga / capacidad` | `6,45 / 80 = ` **0,081** | `3,32 / 800 = ` **0,004** |
| | | **Suma: 0,085 → 0,09 servidores** | |

Donde el material obtiene `100 000 / 160 = 625 servidores`, SendIt obtiene `6,45 / 80 = 0,081`. **No
es un error de método: es el resultado, y dice algo.** Un sistema de remesas en efectivo mueve
**dinero**, no bytes: 2 800 giros diarios son `USD 840 000` al día atravesando la frontera con dos
reguladores encima, y **caben en una máquina**. La dificultad de SendIt nunca fue el cómputo.

Tres advertencias que este caso obliga y el ejemplo del material no necesita:

- **Un `request` no cuesta lo mismo que otro.** Consultar el estado de un giro es una lectura;
  ejecutar un pago es una escritura contable que toca varias filas, cruza la frontera del corredor y
  **no puede servirse desde caché**.
- **Cotizar no es una lectura.** RF-07 hace que el sistema *produzca y feche* la cotización, y RF-06
  la conserva sin recalcular: es una **escritura durable**, una por giro, en el camino crítico de
  RNF-09. Contarla como lectura cacheable subestimaría el eje que más caro escala.
- **El aviso al receptor no se mide en requests.** Es una llamada o un SMS que entrega un operador de
  telefonía, con cuota diaria y precio por unidad. Cinco requerimientos se apoyan en él —RF-25,
  RF-37, RF-41 y RF-75, los cuatro P0, y RF-60— y **ninguno tiene alternativa**: Elena no tiene
  aplicación ni datos, así que un aviso no entregado no degrada, **desaparece**.

#### Desglose por operación

| Operación | Tipo | Ítems | Peso | Volumen diario |
|---|---|---|---:|---:|
| Identificar al emisor contra documento | escritura + verificación externa | RF-01, RF-02 | 6 | **2 980** |
| Conservar la evidencia de identidad de las dos puntas | escritura de binario | RF-80, RNF-01 | **40** | **1 734** |
| Registrar pregunta y respuesta al crear | escritura ilegible, 1 por giro | RF-68, RNF-17 | 2 | **2 800** |
| Cotizar y fechar la cotización | **escritura durable** | RF-05, RF-06, RF-07 | 10 | **3 640** |
| Contar límites sobre la identidad del emisor | lectura agregada | RF-08, RF-09, RF-10 | 3 | **2 980** |
| Contar los cobros del receptor en la ventana | lectura agregada por identidad | RF-58, RF-93 | 3 | **2 690** |
| Tamizar contra listas | lectura externa + escritura de evidencia | RF-26, RF-27, RF-28 | 12 | **8 400** |
| Crear el giro y emitir su código | escritura contable | RF-11, RF-13, RF-20 | 10 | **2 800** |
| Declarar el efectivo al abrir y cerrar caja | escritura, `puntos × turnos × 2` | RF-76 | 4 | **9 000** |
| Informar al operario el efectivo del punto | lectura previa a cada pago | RF-92 | 1 | **2 690** |
| Comprobar la respuesta del desafío sin mostrarla | lectura ilegible | RF-12, RF-69, RF-82 | 2 | **896** |
| **Ejecutar el pago en destino** | escritura contable + frontera | RF-34, RF-36, RF-85, RNF-05 | **15** | **2 690** |
| Rederivar el cobro a otro punto | escritura de estado + 2ª ventanilla | RF-91, RF-105 | 6 | **54** |
| Declarar una diferencia de monto | escritura + atribución | RF-90, RF-59 | 8 | **13** |
| Cerrar el giro y avisar al emisor | escritura + notificación | RF-64, RF-65 | 10 | **2 690** |
| **Consultar estado** | lectura | RF-52, RF-53, RF-66 | 1 | **16 800** — el **22 %** de todos los requests |
| Avisar al receptor por llamada o mensaje | **unidad de tercero** | RF-25, RF-37, RF-41, RF-60, RF-75 | *no se mide en requests* | **13 720 unidades** + 13 720 constancias (RF-98) |
| Devolver al emisor | escritura contable | RF-32, RF-47, RF-50 | 15 | **112** |
| Entregar la devolución en ventanilla | escritura + notificación + ventanilla | RF-14, RF-71, RF-72, RF-74 | 12 | **95** |
| **Suprimir a pedido los datos de una persona** | **búsqueda transversal + borrado parcial** | RF-81 | **400** | **1,3** — *«1,3 requests al día que dictan una decisión de particionado en `A`»* |

**Suma:** `76 785 requests/día` = **50 729 escrituras + 26 056 lecturas**.
`76 785 / 86 400 = 0,89 req/s` de promedio; `× 11 = ` **9,8 req/s en pico**.

**La comprobación que este cálculo se exigió a sí mismo.** Normalizando por peso: las escrituras dan
`392 498 / 10 = 39 250` equivalentes —**menos** que el recuento plano, porque la mayoría son
ligeras— y las lecturas `38 292`, `1,47×` el plano, arrastradas por las 16 800 consultas. Ninguno
mueve la cifra medio orden de magnitud: `39 250 / 86 400 × 11 / 80 = 0,062` servidores. **El sistema
sigue pidiendo menos de un décimo de máquina.**

#### Lo que sí dimensiona: RNF-11, RNF-10 y la geografía

`0,09` no es un número de servidores: es **la prueba de que la carga no es la restricción activa.**
El número real sale del **máximo** entre lo que pide la carga y lo que piden los umbrales.

| Plano | Por qué existe | Nodos |
|---|---|---:|
| Escritura del giro | RNF-11 pide 99,9 % sobre crear y pagar; RNF-06 exige un solo estado. Quórum que tolera una caída sin gastar los 43,2 min/mes | **3** |
| Réplica de lectura en destino | Dos países (RNF-12, RNF-14) y RNF-10 con 900 s de margen: alcanza réplica asíncrona. Dos nodos por país | **4** = `2 × 2` |
| Consulta del emisor | RF-52, RF-53, RF-66. RNF-11 **la excluye** de su medida, así que no lleva quórum — pero es el 22 % de los requests y no puede compartir suerte con la escritura | **2** |
| Cumplimiento y tamizaje | RF-26, RF-27, RF-97 llaman a listas cuya latencia SendIt no fija. Aislarlo evita que una lista lenta consuma el techo de 3,3 s de RNF-09 | **2** |
| | | **11** |

```
servidores = max(carga / capacidad ; piso de disponibilidad y geografía)
           = max(0,09 ; 11)
           = 11
```

**Y la consecuencia que este paso entrega a `E`-escalar:** para que el término de carga alcance al de
disponibilidad, el volumen tendría que multiplicarse por `11 / 0,09 ≈ 122` — **341 000 giros
diarios**, `USD 102 M` al día, el 61 % de los dos corredores. **Antes de eso se rompen otras tres
cosas, y ninguna se arregla con servidores:** la cuota diaria del operador de telefonía, el efectivo
de la caja del punto y el caudal de la cola de cumplimiento. Ese es el orden en que este sistema se
rompe.

### Cálculo 2 — Almacenamiento requerido

El método: **tipos de dato → espacio de cada tipo → agregar y multiplicar por el volumen diario** —
y aquí, obligatoriamente, **por los años de retención**, que es el paso que el método del material no
tiene porque su ejemplo no está regulado.

**La intuición engaña.** El instinto dice que lo que ocupa es la transacción, y una transacción es
una fila de unos pocos cientos de bytes. **Lo que ocupa es la evidencia**, en tres familias: la
prueba de quién es cada quien (binarios de identidad, que **RF-80 pide de las dos puntas**); la
prueba de que se tamizó (RF-26 al aceptar y RF-27 al autorizar: **dos evidencias por giro, haya o no
coincidencia** — la ausencia de coincidencia también hay que poder demostrarla); y el registro
inalterable, que **crece con las lecturas** porque RNF-04 exige traza de todo acceso a identidad.

**Y una cuarta familia con signo menos, con dos miembros.** RF-81 suprime a pedido; **RF-99 es el
mayor de los dos por un factor de treinta**: descarta la evidencia del emisor que se identificó y no
llegó a crear un giro —porque RF-01 corre antes de RF-02, y entre los dos caben el rechazo por
límite, el país no atendible y el emisor que simplemente se fue.

| Tipo de dato | Tamaño unitario | Por giro | Volumen diario |
|---|---|---:|---:|
| **Documento de identidad (binario, RF-80: emisor **y** receptor)** | **500 KB** por captura · 2 KB por referencia | `0,619` capturas + 2 referencias | **878 MB — el 87 % del diario** |
| Comprobante de entrega en destino | 35 KB | `0,96` | **94,1 MB** |
| Traza de auditoría de actos y accesos | 0,35 KB | `25` ≈ 18 actos + 7 accesos | **24,5 MB** |
| Resultado de tamizaje | 2 KB sin coincidencia · 60 KB con | `3` · 2 % con coincidencia | **20,2 MB** |
| Aviso al receptor (constancia, RF-98) | 0,3 KB | `4,9` | **4,1 MB** |
| Asiento contable | 0,4 KB | `3,2` | **3,6 MB** |
| Declaración de caja (RF-76) — **por punto y turno** | 0,4 KB | `3,21` equivalentes | **3,6 MB** |
| Caso de cumplimiento y su liberación | 40 KB | `0,025` → 70 casos/día | **2,8 MB** |
| Registro del giro | 1,0 KB | 1 | **2,8 MB** |
| Cotización producida y fechada | 0,3 KB | `1,3` | **1,1 MB** |
| Pregunta y respuesta del desafío, ilegibles | 0,25 KB | 1 — coste fijo | **0,7 MB** |
| Acumulado de cobros por identidad de receptor | 0,2 KB **por identidad** | `0,45` | **0,25 MB** |
| Devolución y su disponibilidad abierta | 1,5 KB | `0,04` | **0,17 MB** |
| Intentos de respuesta al desafío | 0,15 KB | `0,32` | **0,13 MB** |
| Declaración de diferencia del receptor | 5 KB | `0,005` | **0,07 MB** |
| **Supresión a pedido (RF-81)** — negativo | **−700 KB** por pedido | `−0,00046` | **−0,9 MB** |
| **Descarte sin giro (RF-99)** — negativo, **el mayor** | **−500 KB** por captura | `−0,019` | **−27,0 MB — 30× lo que resta RF-81** |

#### Agregado

| | Fórmula | Valor |
|---|---|---|
| **Espacio por giro** | suma de los tipos por su multiplicidad | `370,0 KB brutos − 9,64 KB (RF-99) − 0,32 KB (RF-81) = ` **360,0 KB**. El binario de identidad son `313,5` de esos `370,0`: **el 85 %** |
| **Almacenamiento diario** | `espacio × giros/día` | `360,0 KB × 2 800 = ` **1,01 GB/día**. Para escala: YouTube, en el ejemplo del material, hace `52 TB` diarios — **52 000 veces esto** |
| **Almacenamiento retenido** | `diario × 365 × años` | Los dos reguladores no piden lo mismo: **5 años** en el corredor peruano, **10** en el mexicano. El multiplicador se pondera por el reparto: `0,26 × 5 + 0,74 × 10 = ` **8,7 años** → `1,008 × 365 × 8,7 = ` **3,2 TB** |
| Piso / techo defendible | si los dos pidieran 5 / 10 años | **1,84 TB** / **3,68 TB** |
| **Almacenamiento caliente** | `diario × 365 × 1` (12 meses de prescripción) | **368 GB ≈ 0,37 TB**, el **11,5 %** del retenido. El otro `88,5 %` es archivo: dato que hay que conservar y casi nunca leer |
| Independiente del giro | caja de RF-76, capturas de RF-99, acumulados | `11,5 GB` — irrelevante en el total y **el único piso que no baja cuando el volumen baja**: un día sin un solo giro sigue escribiendo 9 000 declaraciones de caja |

> **Detenerse en el diario habría dicho `1 GB` en vez de `3 200 GB`.** Son los dos órdenes de
> magnitud que el método del material no tiene por qué contemplar y este caso sí.

**Verificación mínima antes de dar por buena la cifra:** si el binario de identidad no es la partida
más grande, o se contó una identidad por giro en vez de **las dos** que pide RF-80, o el cálculo
omitió la retención, o supuso que solo se guarda evidencia cuando hay coincidencia, o restó la
supresión de RF-81 contra la traza en vez de contra la evidencia. Los primeros cuatro errores
producen un número demasiado pequeño y demasiado creíble; **el último produce un número que además es
ilegal.**

### Cálculo 3 — Ancho de banda requerido

El método: **entrada por día → salida por día → dividir entre 86 400 s.**

| Paso | Detalle | Valor |
|---|---|---|
| **1. Entrada por día** | `identidad 1 734 × 500 KB = 867 MB` **(73 %)** · `listas 8 400 × 15 KB = 126 MB` · `comprobantes 2 690 × 35 KB = 94,2 MB` · `resto de ventanilla 28 905 × 3 KB = 86,7 MB` · `ráfaga de RNF-08: 45 puntos × 400 KB = 18 MB` · `caja 9 000 × 0,4 KB = 3,6 MB` | **1 195,5 MB ≈ 1,20 GB/día** |
| **2. Salida por día** | `consultas 16 800 × 8 KB = 134,4 MB` · `respuestas de ventanilla 20 750 × 6 KB = 124,5 MB` · `descargas de evidencia 70 × 2 × 500 KB = 70 MB` · `cotizaciones 3 640 × 4 KB = 14,6 MB` · `saldos de caja 2 690 × 2 KB = 5,4 MB` · `reportes 3 × 50 KB = 0,15 MB` | **349,1 MB ≈ 0,35 GB/día** |
| **2b. Salida por canal de terceros** | **No se mide en bytes.** `13 720 unidades/día`; en el día señalado `× 3,0 = ` **41 160**. Contra una cuota típica de `10 000/día` por país, los dos dan `20 000` → **el día pico la excede por 2,1×**. Costo `USD 686/día` | **Primer cuello de botella del sistema** |
| 3. Entrada por segundo | `1 195 500 KB / 86 400` | **13,8 KB/s** ≈ 0,11 Mbit/s |
| 4. Salida por segundo | `349 100 KB / 86 400` | **4,0 KB/s** ≈ 0,03 Mbit/s |
| **5. Pico** | `(13,8 + 4,0) × 11` | **196 KB/s ≈ 1,6 Mbit/s** — entrada `152 KB/s`, salida `44 KB/s` |

Y hay una que **no obedece a `P`**: la ráfaga de reconexión de RNF-08, `18 MB en 60 s = 300 KB/s`,
que sola supera el pico entero. Se dimensiona contra ella, no contra los 196 KB/s.

Dos observaciones específicas de este caso:

- **La asimetría se invierte respecto del ejemplo del material.** En YouTube la salida aplasta a la
  entrada: se sube un vídeo y se descarga cien millones de veces. En SendIt el binario pesado —el
  documento de identidad— **entra** y casi nunca sale, y entra **dos veces por giro** desde que RF-80
  lo pide de las dos puntas. Con las cifras: YouTube `40 PB / 52 TB = 769×` a favor de la salida;
  SendIt `1 195,5 / 349,1 = 3,4×` a favor de la **entrada**.
- **Dividir entre 86 400 supone que la carga es uniforme, y no lo es.** El paso 3 es un promedio
  contra el que no se dimensiona nada. **La cifra que se usa es la del paso 5.**

### Qué invalida esta estimación

| Si cambia… | Se recalcula | Y hay que revisar |
|---|---|---|
| La **cuota de mercado (0,5 %)** o el ticket | Los tres cálculos, en proporción directa | Nada mientras no cruce un orden de magnitud: `0,09` aguanta `×122` antes de alcanzar el piso de 11 |
| El reparto entre corredores (26/74) | El multiplicador de retención: `8,7 años` se mueve entre 5 y 10 | `A` — la conservación es **por giro**, no global |
| El **factor de pico** | Servidores y ancho de banda | `E`(escalar) — el tramo en que el sistema se rompe |
| El tamaño de la red afiliada | Servidores y almacenamiento, por el piso de RF-76 | `E`(escalar) — el tramo más bajo, que ya nace con carga aunque no haya giros |
| La cuota o el coste del canal de voz y SMS | El costo por giro, no el cómputo | `E`(escalar) — cuello que **no se resuelve con servidores** |
| **Un requerimiento funcional nuevo** | Los tres | **Todo lo de aguas abajo** |

---

## 4. D — Diseñar el servicio

El material pide tres salidas: **arquitectura high-level**, **tipo de persistencia** y **diseño de la
API**. Las tres están decididas, más las **seis decisiones** que este caso obliga, cada una con su
alternativa descartada, el requisito que la obliga y **lo que se pierde**.

**La frontera con `R`, que ordena todo este paso:** el backlog **enuncia la garantía**; este paso
**elige el mecanismo**. Un requerimiento que nombra un mecanismo se verifica contra la implementación
en vez de contra el efecto, y sobrevive a su propia obsolescencia. Toda decisión técnica desplazada
desde el backlog aterriza aquí, no se suprime.

### 4.1 Arquitectura high-level

| Opción | A favor | En contra | Decisión |
|---|---|---|---|
| **Monolito 3-tier** | Una sola transacción cubre el asiento contable y el estado del giro, que es literalmente lo que piden RNF-07 y RNF-05 | Mete en el mismo proceso cinco terceros que fallan por su cuenta: un proveedor de listas lento consume los hilos del camino del pago. Y no puede satisfacer RNF-17 — dentro de un proceso y una base únicos, quien administra la base lo alcanza todo | **Descartada como forma total.** Su núcleo se conserva |
| Monolito modular | Fronteras de compilación sin fronteras de red; una sola base transaccional | Un módulo comparte proceso y credenciales con los demás: no aísla el fallo de un tercero ni el secreto de RNF-17. Y no dice nada sobre el mostrador, que es un despliegue separado lo quiera el diseño o no | **Descartada sola. Adoptada como forma interna del núcleo** |
| Servicios | Cada frontera que falla distinto se aísla y se despliega sola | **Parte el libro contable en escrituras distribuidas:** RNF-07 dejaría de ser una transacción para volverse un protocolo, y el doble pago que RNF-05 prohíbe pasaría a depender de una compensación en vez de una restricción. Es un problema que el diseño se crea a sí mismo | **Descartada como forma total** |
| MVC | Organiza bien la única superficie con pantalla | No es una arquitectura de sistema: es un patrón de la capa de presentación. Adoptarlo arriba obliga a reimplementar el mismo control en cada mostrador — con RF-84 diciendo explícitamente que decide el sistema y no el operario | **Descartada como arquitectura.** Se usa dentro del cliente de ventanilla y del tablero |
| **Mixta — núcleo monolítico + servicios en la frontera** | Conserva la transacción única donde el dinero la exige y aísla exactamente lo que falla distinto: los cinco terceros, el secreto del desafío y el mostrador que se queda sin línea | Son cuatro clases de unidad de despliegue con cuatro formas de fallar. La frontera núcleo↔mostrador introduce el problema más caro del caso —la decisión **(c)**— y **ninguna otra opción lo evita**, porque el mostrador está lejos por geografía y no por diseño | **✅ Elegida** |

**Arquitectura elegida: mixta — un núcleo monolítico modular, en 3 capas, con servicios adaptadores
en cada frontera externa, un servicio aislado para el secreto del desafío, y el punto de atención
como unidad de despliegue propia y desconectable.**

| Unidad | Qué contiene | Por qué está separada | Ítems |
|---|---|---|---|
| **Núcleo transaccional** (un despliegue, una base) | Libro contable, giro y su estado, límites, acumulados, cotización aplicada, idempotencia, doble control, retención, devolución, cancelación, prescripción, caja por punto | **No se separa**, y esa es la decisión: todo lo que tiene que entrar en la misma transacción que el asiento vive acá. Partirlo convierte una escritura atómica en un protocolo | RNF-07, RNF-05, RNF-13, RNF-16, RF-08, RF-09, RF-58, RF-93 |
| **Adaptadores de frontera** (uno por tercero) | Verificación del documento, listas de sanciones, proveedor de cotización, reporte a la autoridad, canal de voz y SMS | Cada uno falla, tarda o miente por su cuenta y ninguno puede arrastrar el camino del pago. Tienen su propio reintento y su tiempo medido **aparte** del techo de RNF-09 | RF-01, RF-26, RF-07, RF-17, RF-25, RF-98 |
| **Servicio de desafío** (proceso, base y credenciales propias) | Pregunta, respuesta derivada, contador de intentos y comparación | RNF-17 exige que el valor sea inalcanzable **para quien administra la infraestructura**. Un módulo del núcleo comparte credenciales con el núcleo; una base aparte con su propio administrador es el único mecanismo que hace **declarable** el invariante | RF-12, RF-68, RF-101, RF-82, RF-83, RNF-17 |
| **Punto de atención** (una instancia por mostrador, con almacén local) | Cliente de ventanilla, diario local de actos, copia de catálogos de solo lectura | Está en una plaza de Huanta y **pierde la conexión**. RF-45 y RF-100 obligan a que esa condición sea explícita en el diseño en vez de un accidente de red | RF-45, RF-100, RF-42, RF-57, RNF-06, RNF-08 |

**Las tres capas** —presentación, lógica, datos— con una sola regla que las hace útiles: **ninguna
regla de negocio vive en presentación.** Lo que Kevin ve o no ve (RF-40, RF-57) es una decisión de la
capa de lógica que la presentación obedece; si viviera en la pantalla, un cliente modificado en un
mostrador afiliado la anularía — y el mostrador afiliado es precisamente el vector que Kevin modela.

**El criterio del material no se cumple aquí, y por eso el argumento es otro.** El ejemplo del
material elige monolito 3-tier con el argumento de que su aplicación **no tiene conexiones hacia
afuera**. SendIt es lo contrario: tiene al menos **cinco**. De modo que el criterio queda descartado,
no invocado. El núcleo sigue siendo monolítico, pero por un argumento distinto: **no por ausencia de
fronteras externas, sino por presencia de una invariante contable.** Y se paga el precio inverso, que
también hay que decir: **el núcleo se despliega entero o no se despliega**, y una regresión en el
módulo de devoluciones detiene también la creación de giros.

### 4.2 Persistencia — por familia de dato, no global

El propio material lo hace así en su ejemplo —NoSQL para las imágenes, SQL para la metadata— y aquí
la diferencia es más marcada: el mismo giro tiene una parte que exige integridad transaccional
estricta y otra que es un binario de megabytes que nunca se consulta salvo por auditoría.

| Familia de dato | Motor | Por qué |
|---|---|---|
| **Registro contable del dinero** | **SQL relacional, solo-adición** | RNF-07 es una restricción sobre un conjunto de filas escritas juntas: sin transacción no es declarable. Tabla de asientos con débito y crédito, **restricción de suma cero por asiento**, sin `UPDATE` ni `DELETE` concedidos. Es el único escritor de dinero del sistema |
| Giro y su estado | **SQL, misma base y misma transacción que el asiento** | RNF-06 y RNF-13 prohíben dos afirmaciones incompatibles a la vez; escribir el estado en otra base o en otro momento **fabrica esa posibilidad**. Proyección materializada del libro, reconstruible desde él. Cuando difieren, **manda el libro** |
| Código de seguimiento | **SQL, y no el valor: su derivado** | RNF-15: «puede comprobar un código sin poder mostrarlo». Se genera con aleatoriedad criptográfica, se muestra **una sola vez** y se persiste solo como derivado con sal. **RF-94 deja de ser una política que alguien puede saltarse: es una consecuencia** — el sistema ya no lo puede reconstruir |
| Respuesta del desafío | **SQL en base propia, credenciales propias, derivado con función lenta** | RNF-17 extiende la prohibición a los dos lados del mostrador. Una columna de la base de giros la incumple por construcción |
| Acumulado del emisor / del receptor | **SQL, agregado en la transacción, sin caché** | RF-08 y RF-09 rechazan **antes** de registrar la recepción del efectivo. Un acumulado en caché de un minuto es una ventana para el fraccionamiento que BR-04 existe para impedir |
| Identidad de personas | **SQL con cifrado por campo, clave fuera del motor** | RNF-01 y RF-81. **Suprimir es destruir la clave**, no recorrer filas: RF-81 se ejecuta sin violar RNF-03 |
| Binarios de identidad (RF-80) | **Almacenamiento de objetos, cifrado por objeto** | Volumen alto, lectura rarísima, retención larga. Un objeto por captura, cifrado con clave **por giro**; la fila guarda puntero y huella, nunca el binario |
| Resultado de tamizaje | **NoSQL documental** | Hace falta la respuesta **completa** del proveedor como evidencia, y su esquema no es nuestro ni es estable. Un documento por tamizaje, con veredicto y **versión de lista** |
| Traza de auditoría | **SQL solo-inserción, encadenada por huella, base propia** | RNF-03 y RNF-04. **El encadenamiento hace que borrar una fila del medio sea detectable**, no solo prohibido |
| Cotizaciones | **SQL, y copiada por valor al giro** | Una clave foránea a una tabla que cambia no es una promesa: **es una promesa que alguien puede editar** |
| Catálogo de puntos / efectivo del corredor | **SQL, catálogo cacheado, saldo sin caché** | RF-63 tolera segundos de atraso; RF-20 exige efectivo disponible **antes** de fondear, y ahí un saldo atrasado promete un pago que no existe |
| Declaraciones de caja (RF-76) | **SQL solo-adición** | RF-76 registra **declaraciones**, no un saldo: una declaración corregida con `UPDATE` borra la única prueba de qué dijo el operario |
| Estado local del punto sin conexión | **Base embebida, solo-adición, firmada** | RF-100 prohíbe autorizar lo que no se puede comprobar contra el centro: **lo local no decide, solo recuerda.** Nunca es fuente de verdad de un pago |

### 4.3 Diseño de la API — 32 endpoints

Los ejemplos del material listan rutas desnudas. Aquí la tabla lleva tres columnas más, y las tres
son obligatorias: **quién la usa** —una ruta sin llamador identificado es una superficie de ataque
sin dueño—, **qué garantiza** —un endpoint que mueve dinero y no declara su comportamiento ante el
reintento **es un defecto**, no una omisión de documentación— y **traza a** —una ruta sin ítem no
existe.

**Convención de idempotencia (`IDEMP`):** el llamador envía `Idempotency-Key`; el servidor la
persiste **antes** de escribir el primer asiento; el reintento con la misma clave devuelve **la misma
respuesta** y no ejecuta nada; con la misma clave y distinto contenido devuelve `409`.

| Método | Ruta | Quién la usa | Qué garantiza | Traza a |
|---|---|---|---|---|
| `POST` | `/cotizaciones` | Ventanilla de origen, por Rosa | Monto en moneda destino con su nombre, tasa e instante de vencimiento. **No reserva dinero.** Segura de repetir | RF-05, RF-07, RF-21 |
| `GET` | `/corredores/{origen}/{destino}` | Ventanilla de origen | Antes del efectivo: si el país se puede atender, desde cuándo se cobra, plazo de una eventual devolución y cuánto dura como máximo una revisión | RF-19, RF-73, RF-77, RF-96 |
| `GET` | `/puntos?pais=&cerca_de=` | Ventanilla de origen | Puntos del país destino con su capacidad declarada de pago | RF-63, RF-20 |
| `POST` | `/identificaciones` | Ventanilla de origen | Registra la verificación y conserva la evidencia. Devuelve una referencia, **nunca el documento**. `IDEMP` | RF-01, RF-80, RF-84, RNF-01 |
| `POST` | `/tamizajes` | Ventanilla, **antes del efectivo** | Veredicto —limpio, homonimia o exacta— y versión de lista. **Nunca devuelve la entrada de la lista** | RF-26, RF-28, RF-78 |
| `POST` | `/giros` | Ventanilla de origen, por Rosa | Crea el giro pendiente de efectivo. Devuelve el código **una sola vez y solo al emisor**; el sistema no puede reemitirlo. `IDEMP` | RF-03, RF-04, RF-11, RF-63, RF-94, RNF-15 |
| `POST` | `/giros/{id}/desafio` | Ventanilla, tecleado por Rosa | Registra pregunta y respuesta. **Responde sin cuerpo: no hay lectura de vuelta, para nadie** | RF-68, RF-101, RNF-17 |
| `POST` | `/giros/{id}/autorizaciones` | Segundo rol, **nunca el mismo operario** | Segunda autorización sobre el umbral reforzado. Rechaza si la identidad ya actuó sobre este giro. `IDEMP` | RF-13, RNF-02 |
| `POST` | `/giros/{id}/recepcion-efectivo` | Ventanilla de origen | **El acto que da el giro por creado.** Comprueba límites y efectivo del corredor; escribe el asiento. `IDEMP` | RF-79, RF-08, RF-09, RF-10, RF-20, RF-36, RNF-07 |
| `GET` | `/giros?emisor={id}` | Rosa, sin depender del receptor | Estado de sus giros, lo retenido con su fecha límite — **nunca su motivo** | RF-52, RF-53, RF-66 |
| `POST` | `/giros/{id}/cancelacion` | Rosa, **nunca el receptor** | Cancela mientras el dinero no esté a disposición del receptor y abre la devolución. `IDEMP` | RF-46, RF-47, RF-48, RNF-13 |
| `POST` | `/giros/{id}/punto-alternativo` | Ventanilla, con respuesta del emisor | Traslada el cobro a otro punto. **No cambia nada sin la respuesta del emisor.** `IDEMP` | RF-91, RF-105, RF-39 |
| `POST` | `/giros/{id}/arrendamiento` | Punto → centro | Emite el **arrendamiento exclusivo** del giro por una ventana corta: re-tamiza, comprueba fondos y efectivo, y **mientras vive el centro no dispone del giro en ningún otro lado**. Solo en línea. `IDEMP` | RF-27, RF-36, RF-100, RNF-06 |
| `GET` | `/puntos/{id}/efectivo` | Punto, antes de cada pago | Efectivo disponible, derivado de la apertura y del libro | RF-92, RF-95 |
| `POST` | `/puntos/{id}/caja` | Punto → centro | Declaración de apertura o cierre. Solo-adición: **no corrige la anterior**. `IDEMP` | RF-76 |
| `POST` | `/giros/{id}/desafio/intentos` | Punto → centro | Comprueba y **devuelve un veredicto, nunca el valor**. Consume un intento. Corre solo en el centro. **No es idempotente y no debe serlo**: cada envío *es* un intento | RF-12, RF-69, RF-82, RF-83, RF-86, RNF-17 |
| `POST` | `/giros/{id}/pago` | Punto → centro | Registra la entrega contra código y documento, por el monto fijado y **sin cobrarle nada al receptor**; descuenta el efectivo y cierra el giro. Exige arrendamiento vigente. `IDEMP` **y con unicidad natural** | RF-02, RF-34, RF-85, RF-86, RF-64, RF-95, RF-102, RNF-05, RNF-16 |
| `POST` | `/giros/{id}/diferencias` | Punto → centro, por el receptor | Registra la declaración de Elena y abre el caso con responsable nombrado. Solo-adición. `IDEMP` | RF-90, RF-59 |
| `POST` | `/puntos/{id}/sincronizacion` | Punto → centro | Sube el diario local y baja el estado autoritativo. **Sin intervención del operario.** Repetible sin efecto | RF-45, RF-100, RF-42, RNF-06, RNF-08 |
| `GET` | `/retenciones` | Rol de cumplimiento | Giros retenidos con su plazo y clase de coincidencia. **Excluye los que el propio solicitante atendió** | RF-29, RF-30, RF-28, RF-78 |
| `POST` | `/retenciones/{id}/liberacion` | Cumplimiento, distinto del que atendió | Libera **exigiendo motivo escrito**; rechaza si la identidad ya ejerció otro rol. `IDEMP` | RF-33, RF-87, RNF-02 |
| `POST` | `/retenciones/{id}/vencimiento` | Proceso interno, tarea diaria | Vence la retención no liberada y dispara la devolución, avisando al receptor. `IDEMP` | RF-31, RF-32 |
| `GET` | `/receptores/{id}/acumulado` | Proceso interno → cumplimiento | Cobros del receptor en la ventana, sobre identidad estable | RF-58, RF-93 |
| `POST` | `/tamizajes/relista` | Proceso interno, al cambiar una lista | Re-tamiza los no pagados y avisa por su canal a quien deja de poder cobrar. `IDEMP` por versión | RF-97, RF-27 |
| `POST` | `/reportes-autoridad` | Proceso interno → autoridad | Reporta el giro sobre el umbral, medido **sobre el giro completo**. `IDEMP` por giro y periodo | RF-17, RF-22 |
| `POST` | `/avisos` | Proceso interno → canal de voz y SMS | Entrega el aviso **sin exigir aplicación ni datos**, y conserva constancia. `IDEMP` por hecho avisado | RF-25, RF-37, RF-41, RF-51, RF-60, RF-65, RF-67, RF-75, RF-98 |
| `GET` | `/devoluciones?emisor={id}` | Rosa | Devoluciones disponibles y dónde retirarlas, con su plazo | RF-14, RF-72, RF-89 |
| `POST` | `/devoluciones/{id}/retiro` | Punto elegido por el emisor → centro | Entrega **en efectivo y en la moneda que el emisor entregó**, con comisión cuando el giro no llegó a pagarse. `IDEMP` | RF-71, RF-74, RF-88, RF-89 |
| `POST` | `/prescripciones` | Proceso interno, tarea diaria | Deja no pagable el giro vencido, pone el monto a disposición y avisa antes. `IDEMP` | RF-49, RF-50, RF-51 |
| `POST` | `/correcciones` | Segundo rol, sobre un giro pagado | Registra la corrección como **movimiento nuevo**, nunca editando el anterior. `IDEMP` | RF-56, RF-61, RF-59, RNF-03 |
| `POST` | `/liquidaciones` | Proceso interno → agente afiliado | Liquida el efectivo que el agente puso de su caja. `IDEMP` por agente y periodo | RF-24 |
| `POST` | `/supresiones` | Rosa → proceso interno | Suprime los datos **de quien los pide y de nadie más**, destruyendo la clave de su evidencia. **No toca la traza** | RF-81, RF-99, RNF-03 |

**Dos ausencias deliberadas, porque una API se define también por lo que no expone.** No hay
`GET /giros/{id}/desafio` ni `GET /giros/{id}/codigo`: RNF-17 y RNF-15 los prohíben, y **una ruta que
no existe es un control más fuerte que una ruta con permisos**. Y **no hay ningún endpoint dirigido
al receptor**: Elena no es clienta de SendIt, no tiene datos ni aplicación, y todo lo que le llega
viaja por `POST /avisos` hacia su teléfono.

### 4.4 Las seis decisiones que este caso obligaba

Cada una lleva lo mismo: **qué se eligió, contra qué alternativa, qué requisito la obliga y qué se
pierde.** Esta última columna no es cortesía: es la mitad que vuelve auditable la decisión.

| | Decisión | Contra qué alternativa | Qué requisito la obliga | **Qué se pierde** |
|---|---|---|---|---|
| **(a)** | **Dónde vive la verdad del dinero.** Libro de movimientos de **partida doble, solo-adición**, con el estado del giro como **proyección** escrita en la misma transacción y reconstruible. Cuando difieren, **manda el libro**. Cuentas: `Efectivo recibido en origen`, `Obligación con el receptor`, `Obligación retenida`, `Caja del agente por punto`, `Comisión`, `Diferencia de cambio`, `Devoluciones por retirar`. **Todo hecho es un asiento, incluidos los que no parecen contables**: la retención no mueve dinero pero *reclasifica* la obligación, suma cero | Un campo `estado` o `saldo` que se actualiza en el sitio: se lee más rápido y **no tiene historia** | RNF-07 no es una propiedad que un campo mutable pueda tener: es una restricción sobre un conjunto de filas escritas juntas. Y RNF-03 prohíbe modificar el registro de un acto. **Nadie audita un campo que se sobrescribió** | Cada hecho nuevo obliga a inventarle un asiento y una contrapartida con nombre, aunque no mueva un centavo · El estado ya no se lee con un `SELECT` barato, y hay **dos lugares** donde puede estar el error en vez de uno · **No se puede corregir un error de tipeo, solo compensarlo**: la traza conserva los errores para siempre, con nombre y autor — y eso incluye los de Kevin · El volumen crece: el multiplicador de almacenamiento no es uno |
| **(b)** | **Idempotencia. Dos mecanismos, no uno, porque protegen cosas distintas.** ① **Unicidad natural en el libro** —índice único sobre `(giro, acto)`—: un segundo pago **no entra en la base**, venga del punto que venga y llegue cuando llegue. ② **Clave de intento generada por el cliente**, persistida **antes de mover un centavo**: el reintento devuelve el resultado original, no un error. Ventana de vida: **la del giro pagable**, y la restricción de unicidad **no caduca nunca** | Clave generada por el servidor —un corte antes de que llegue la respuesta convierte el reintento en operación nueva— y ventana corta de 24 h, que **rehabilita el doble pago al día siguiente** y contradice el «en ningún momento» de RNF-05 | RF-43 y RF-44 enuncian el efecto; RNF-05 lo vuelve invariante «en ningún punto y en ningún momento», y ese *ningún punto* obliga al mecanismo ①: **dos puntos desconectados no se ven entre sí, pero el índice único del libro los ve a los dos** | La lista de actos deja de ser extensible sin migración · La tabla de claves **nunca se purga** mientras el giro sea pagable · Si al punto se le corta la corriente **antes** de escribir la clave, el reintento sí es un intento nuevo, y lo único que queda entre eso y un doble pago es el índice único — **la red de abajo, no la de arriba** · Un `409` es correcto y antipático: Kevin corrigió un dígito y no sabe cuál de los dos cuerpos quedó |
| **(c)** | **La frontera centro ↔ punto de atención. Arrendamiento exclusivo del giro, emitido solo en línea.** El centro no baja «autorizaciones» abiertas: baja un arrendamiento de un giro concreto a un punto concreto por `[ASSUMPTION: 120 s, renovable solo en línea]`, y **mientras vive el centro se prohíbe a sí mismo disponer del giro**. Al reconectar, el pago ejecutado y no confirmado pasa a **pago en duda**, no arrendable en ningún punto | Pagar contra autorización pre-bajada con caducidad y tope —**prohibida por RF-100**— y empujar las prohibiciones antes de la caída, que **se rompe con la retención que nace mientras el punto está caído** | RF-45 y RF-100 son P0 y entre los dos eliminan pagar-y-arreglar: **las tres opciones son la misma cosa, un punto decidiendo sin poder comprobar.** El mecanismo lleva la ventana de RNF-06 **a cero y no a «poco»**: no sincroniza dos afirmaciones más rápido, **hace que solo uno de los dos tenga derecho a afirmar** | **Una caída de línea cierra el mostrador para pagos, sin excepción.** Elena viajó cuarenta minutos en combi, hizo la cola y vuelve con las manos vacías después de que RF-41 y RF-75 le prometieran que ese punto podía pagarle · El estado *pago en duda* congela un giro que **ni se paga ni se devuelve**, y **no hay mensaje que lo mejore** · Toda la disponibilidad de RNF-11 queda apoyada en el enlace del mostrador, que es lo que menos controla SendIt · El arrendamiento agrega una llamada en línea al camino del pago y consume presupuesto de RNF-09 |
| **(d)** | **Cuándo se fija el tipo de cambio.** Cotización con vencimiento de `[ASSUMPTION: 15 min]`, **copiada por valor** dentro del giro; la exposición **la absorbe SendIt** en una cuenta `Diferencia de cambio`, financiada por un margen incorporado y cubierta **por corredor** al cierre del día, no giro a giro | Fijar al pagar —prohibido por RF-06 y BR-07, y **es exactamente lo que Elena ya vivió**: treinta soles menos «por el cambio», explicados por un mostrador que no produjo esa diferencia— y cotización sin vencimiento, que expone a SendIt sin límite | RF-05 obliga a informar el monto **antes** del efectivo, RF-06 a no recalcularlo y RF-07 a producir y fechar la cotización. Copiada **por valor** y no referenciada, porque una clave foránea a una tabla que cambia es una promesa editable | La cotización vencida obliga a **recotizar con Rosa delante**, y el número que le prometió a su madre por teléfono puede cambiar entre que llegó al local y llegó a la ventanilla · SendIt carga la exposición hasta el cobro, que por RF-89 puede ser **muy** largo — y **el margen lo paga Rosa aunque no lo vea**, que es exactamente la mecánica del «cero comisión» que la enfureció · La cuenta `Diferencia de cambio` puede quedar negativa sin que nadie haya hecho nada mal |
| **(e)** | **Dónde corre el tamizaje. Copia local versionada de las listas**, contra la que corren los dos tamizajes de forma sincrónica: **el camino del dinero nunca llama al proveedor en vivo**. **Falla cerrada**: si la copia supera `[ASSUMPTION: 24 h]` sin actualizarse, el sistema **deja de crear giros**. El **punto de no retorno tiene nombre: la emisión del arrendamiento de (c)** — todo control que quiera *detener* en vez de *deshacer* corre antes de esa llamada | Llamar al proveedor en línea dentro del camino del pago —un tercero lento consume los 3 min de RNF-09 y su caída cierra la red con dinero adentro— y tamizar **después** de aceptar el efectivo, que convierte la herramienta de Kevin de *detener* en *revertir*, que es el movimiento que el lavado busca provocar | RF-26 fija el momento y T1 lo decide a favor del control. **El mecanismo que impide deducir el motivo:** el mensaje y el plazo son los mismos para toda retención — se informa siempre el plazo **máximo** (RF-31), nunca el esperado, porque RF-78 resuelve la homonimia más rápido y **la duración filtraría la causa** | Hay que replicar, versionar y almacenar listas ajenas, y **aceptar que la copia va atrasada**: existe una ventana real en que un giro se aprueba contra lista vieja · **Fallar cerrado es indisponibilidad autoinfligida**: una caída del proveedor de más de 24 h detiene la creación en toda la red. Es la decisión correcta y hay que estar dispuesto a sostenerla el día que pase · Informar siempre el plazo máximo significa **decirle a Rosa un número peor que el probable**, y ella va a esperar angustiada por un plazo que casi nunca se cumple |
| **(f)** | **Dónde vive la respuesta del desafío. No se guarda ni se transmite en claro en ningún punto del sistema.** Vive como derivado irreversible —normalización versionada, función lenta con sal por giro, sellado con clave de servicio **fuera de la base**— en base propia, y **la comparación corre solo en el centro**. Por la línea sube el sobre y baja **un veredicto booleano y los intentos restantes**. Caducar es **destruir la sal y el sellado**: borrado criptográfico, no `DELETE` | Cifrado reversible con clave del sistema —**una llave que descifra *es* una ruta de lectura**, y RNF-17 lo prohíbe— y bajar el derivado al mostrador para comparar ahí, que resolvería el caso sin línea y entrega el material para un ataque de diccionario **dentro de un local que no es de SendIt** | RF-12 (no mostrarla a quien atiende), RNF-17 (ni a quien administra la infraestructura), RF-101 (**no transmitirla a nadie, ni siquiera a quien registró la pregunta**). Y el lado que el código no tiene: **la respuesta es un secreto compartido entre dos personas que el sistema solo arbitra** | **Nadie puede recuperar la respuesta.** Ni SendIt para ayudar a Elena, ni Rosa si se olvidó — **y no hay procedimiento de excepción, porque un procedimiento de excepción es un agujero con formulario** · A los tres intentos el giro se devuelve **aunque quien estaba delante fuera la receptora legítima** · Un error de tipeo de Kevin **gasta un intento real** y él no puede ver qué tecleó mal · **El desafío no funciona sin línea**, que es justo el escenario del documento vencido en una plaza de Ayacucho: la salida de RF-69 es la más frágil del sistema **precisamente donde más falta hace** |

### Supuestos que este paso introduce

Cuatro, y son suyos: ninguno viene del backlog, y cada uno es un número que el enunciado no da.

| Marca | Dónde | Qué pasa si se retira |
|---|---|---|
| `[ASSUMPTION: el arrendamiento dura 120 s, renovable solo en línea]` | (c) | El mecanismo sobrevive; cambia cuánto espera una retención y cuán frecuente es *pago en duda* |
| `[ASSUMPTION: la cotización vive 15 minutos]` | (d) | Sube o baja la exposición cambiaria y la frecuencia con que se recotiza con Rosa delante |
| `[ASSUMPTION: la copia de listas falla cerrada a las 24 h]` | (e) | Mueve el equilibrio entre BR-06 y RNF-11 |
| `[ASSUMPTION: tres intentos de desafío por giro]` | (f) | Cambia cuántos giros legítimos terminan devueltos por RF-103 |
