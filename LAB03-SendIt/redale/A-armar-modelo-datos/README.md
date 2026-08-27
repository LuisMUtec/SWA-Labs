# A — Armar el modelo de datos

> Paso 4 de [R.E.D.A.L.E.](../README.md) · anterior:
> [**D** — Diseñar el servicio](../D-disenar-servicio/README.md) · siguiente:
> [**L** — Listar los componentes](../L-listar-componentes/README.md) · bitácora:
> [`ITERACIONES.md`](../ITERACIONES.md)

**Estado: andamiaje.** No hay campos definidos ni motores elegidos. Las entidades están **nombradas
y sin campos** a propósito: nombrarlas es reconocer que el dominio las tiene; darles campos es
decidir, y eso se hace contra el backlog ya evaluado.

El material pide cuatro cosas: **tablas**, **campos**, **opciones de base de datos** y **otros tipos
de almacenamiento** (archivos, caché, almacenamiento de objetos, sistemas de archivos distribuidos).

---

## Contrato con los pasos vecinos

| | |
|---|---|
| **Consume de D** | El tipo de persistencia por familia de dato, y —sobre todo— las cinco decisiones abiertas de `D`. Tres de ellas *son* decisiones de modelo de datos disfrazadas de arquitectura: dónde vive la verdad del dinero decide si hay tabla de movimientos; la idempotencia decide si hay entidad de clave de intento; el momento del tamizaje decide qué estados existen |
| **Consume de E** | El volumen por tipo de dato y los años de retención, que deciden qué entidad puede vivir en una fila y cuál necesita almacenamiento de objetos |
| **Entrega a L** | Las bases de datos del diagrama. En el ejemplo de clase hay **varias `BD`, no una sola**: cada grupo de servicios tiene la suya, y cuál es cuál se decide acá |
| **Queda inválido si D cambia** | La entidad cuyo mecanismo se reeligió. Reabrir (a) borra o crea la tabla de movimientos; reabrir (c) cambia los estados del envío; reabrir (e) cambia qué se guarda y en qué momento |
| **Queda inválido si E cambia** | La elección de motor que se justificó por volumen, y la política de retención por entidad |

---

## 1. Entidades candidatas

Nombradas, no definidas. Cada una existe porque alguien del conjunto de personas la necesita; una
entidad sin persona que la exija es un huérfano y se borra o se le busca el requerimiento que faltó
en `R`.

| Entidad candidata | Por qué es candidata |
|---|---|
| **Remitente** | Rosa. Es quien paga y quien tiene que ser identificable antes de que el dinero se mueva |
| **Destinatario** | Elena. No es un campo del envío: es una persona con identidad propia, que se verifica y que cobra. Modelarla como texto dentro del envío hace imposible reconocer que dos envíos van a la misma persona, que es justo lo que Marco necesita ver |
| **Envío** | La operación completa, de extremo a extremo. Su cierre no es «despachado» sino «Elena contó los billetes» (tensión T6) |
| **Movimiento contable** | El asiento. Existe si `D`(a) decide que la verdad del dinero es una suma de movimientos y no un campo |
| **Tasa aplicada / cotización** | La promesa de cuántos soles. Tiene momento de emisión, vencimiento y valor; no es un número dentro del envío |
| **Verificación de identidad** | El acto de haber comprobado quién es alguien, con su evidencia, su momento y su resultado. Distinto de la persona verificada |
| **Caso de cumplimiento** | El expediente de Marco: la coincidencia, la evidencia, la decisión, el plazo y su vencimiento |
| **Traza de auditoría** | Quién vio qué, quién decidió qué, cuándo. Crece con las lecturas, no solo con las escrituras |

Faltan por decidir, y hay que decidirlas: si el **agente pagador** y la **red pagadora** son
entidades del modelo o referencias a un sistema externo; si la **clave de idempotencia** es entidad
propia; si el **aviso enviado a Elena** se guarda como prueba de haber avisado.

### Campos

Una sección por entidad. Vacías.

| Entidad | Campos | Clave | Relaciones |
|---|---|---|---|
| Remitente | — | — | — |
| Destinatario | — | — | — |
| Envío | — | — | — |
| Movimiento contable | — | — | — |
| Tasa aplicada | — | — | — |
| Verificación de identidad | — | — | — |
| Caso de cumplimiento | — | — | — |
| Traza de auditoría | — | — | — |

## 2. Elección de motor por entidad

| Entidad | Necesidad dominante | Motor | Por qué | Decisión |
|---|---|---|---|---|
| — | — | — | — | — |

La elección es **por entidad**, no global — el material lo hace así en su ejemplo, con NoSQL para
imágenes y SQL para metadata. El criterio no es la preferencia sino qué garantía necesita cada dato:
integridad transaccional, capacidad de agregar sin bloquear, o volumen barato de solo escritura.

## 3. Otros almacenamientos

| Necesidad | Qué guarda | Opción | Por qué | Decisión |
|---|---|---|---|---|
| Almacenamiento de objetos | Binarios de identidad, evidencia adjunta de un caso | — | — | — |
| Caché | — | — | — | — |
| Sistema de archivos distribuido | — | — | — | — |
| Archivos planos / exportación | Reportes a la autoridad, archivos de conciliación con la red pagadora | — | — | — |

**Un aviso sobre la caché en este dominio.** Cachear es servir un dato que puede estar viejo. El
monto que Rosa vio, el estado de un envío retenido y el resultado de un tamizaje son exactamente los
datos que no toleran estar viejos, y son los que más se consultan. Lo que se cachee y lo que no se
decide aquí y hay que justificarlo por dato, no por capa.

---

## 4. Datos personales y su trato

| Dato | ¿Se guarda? | En claro / cifrado / tokenizado / hash / no se guarda | Quién puede leerlo | Bajo qué condición | Por qué así |
|---|---|---|---|---|---|
| Documento de identidad del remitente | — | — | — | — | — |
| Imagen del documento | — | — | — | — | — |
| Documento de identidad del destinatario | — | — | — | — | — |
| Instrumento de pago de Rosa | — | — | — | — | — |
| Domicilio | — | — | — | — | — |
| Teléfono de Elena | — | — | — | — | — |
| Resultado de tamizaje y su coincidencia | — | — | — | — | — |
| Existencia de un reporte a la autoridad | — | — | — | — | — |

**Por qué esto es decisión de modelo de datos y no de infraestructura.** Cifrar el disco protege
contra el robo del disco. No protege contra la consulta legítima que no debía ocurrir — y el permiso
de Marco dice literalmente que **no debe consultar los datos de un cliente sin un caso abierto que
lo justifique**. Esa garantía se cumple decidiendo dónde vive el dato, detrás de qué referencia, con
qué llave y con qué registro de acceso: es la forma de las tablas, no la configuración del servidor.

Tres consecuencias concretas que la tabla tiene que resolver:

- **Tokenizar cambia la forma de la entidad.** Si el instrumento de pago se guarda como referencia,
  deja de ser un campo del remitente y pasa a ser una relación con otro almacén, con otra llave y
  otro control de acceso. Eso no es un detalle: es una tabla menos y una frontera más.
- **Hay un dato cuya sola existencia es secreta.** La de un reporte a la autoridad. Marco tiene
  prohibido revelarla (tensión T2), y una tabla donde el reporte es una fila más deja que cualquiera
  con acceso de lectura deduzca lo que la ley prohíbe decir. Ocultarlo en la interfaz no basta.
- **El dato del destinatario lo captura un tercero.** Elena se identifica ante el agente pagador, no
  ante SendIt. Qué parte de eso llega a nuestro modelo, en qué forma y con qué garantía de que es
  cierto, es una decisión de modelo con consecuencias de seguridad — y Rosa tiene prohibido verlo.

---

## 5. Qué es inmutable y qué no

Marco necesita que su decisión y la evidencia sobre la que la tomó **no se puedan editar**. Su
permiso lo dice: nunca debe borrar ni editar una decisión suya ya registrada. Su señal de éxito lo
dice: un año después, la decisión, su momento, su evidencia y la versión de la lista contra la que
se tomó siguen siendo recuperables y nadie pudo haberlas alterado.

**Un modelo donde todo se actualiza en el sitio no puede darle eso.** Un `UPDATE` no deja rastro del
valor anterior; una fila de estado que pasa de `retenido` a `liberado` no dice quién, cuándo, ni con
qué a la vista. Y el problema es más agudo de lo que parece: Marco decidió mirando un dato que
**después cambió** —una lista se actualizó, un patrón se movió—, así que guardar un puntero al dato
no basta. Hay que guardar el valor que tenía en el momento de decidir.

| Dato | ¿Se actualiza en el sitio o solo se agrega? | Quién lo exige | Decisión |
|---|---|---|---|
| Estado del envío | — | — | — |
| Movimiento contable | — | — | — |
| Decisión de cumplimiento | — | — | — |
| Evidencia sobre la que se decidió | — | — | — |
| Versión de la lista consultada | — | — | — |
| Cotización emitida | — | — | — |
| Datos de contacto del remitente | — | — | — |

**La pregunta de fondo, planteada y sin responder:** ¿el envío es una fila que cambia de estado, o
una secuencia de hechos de la que el estado se deriva? Las dos formas soportan la aplicación de
Rosa. Solo una soporta el día de Marco. Y si conviven —hechos para lo que se audita, fila mutable
para lo que se consulta— hay que decidir cuál manda cuando difieren, que es la misma pregunta que
`D`(a) dejó abierta.

---

## 6. Retención

Dos obligaciones reales caen sobre el mismo registro y **ninguna anula a la otra**: el cliente puede
exigir que se borren sus datos, y la regulación obliga a conservar la operación durante años. Un
modelo que solo sabe hacer una de las dos cosas incumple la otra.

| Dato | Plazo de conservación | ¿Se borra a pedido del cliente? | Qué lo obliga | Qué se rompe si se borra |
|---|---|---|---|---|
| Registro del envío | — | — | — | — |
| Movimiento contable | — | — | — | — |
| Imagen del documento de identidad | — | — | — | — |
| Resultado de tamizaje | — | — | — | — |
| Caso de cumplimiento | — | — | — | — |
| Traza de auditoría | — | — | — | — |
| Datos de contacto | — | — | — | — |
| Cotizaciones no ejecutadas | — | — | — | — |

**Lo que esta tabla decide sin que lo parezca.** Si el nombre y el documento de Rosa viven **dentro**
de la fila del envío, borrar a Rosa destruye el asiento contable y con él la posibilidad de demostrar
que la suma cuadra. Si viven **detrás de una referencia**, se puede borrar la identidad y dejar en
pie la operación. Es decir: **la convivencia entre el derecho de supresión y la obligación de
conservación se resuelve en el diseño de las tablas, y solo ahí.** Ninguna política escrita en un
documento la resuelve si el modelo no la permite.

Falta decidir además qué pasa al vencer el plazo: ¿se borra, se anonimiza, se archiva en frío? Y
quién ejecuta ese vencimiento, porque un plazo que nadie hace vencer no vence — el mismo defecto que
Marco sufre con las retenciones sin plazo.

---

## Qué invalida este modelo

| Si cambia… | Se rehace |
|---|---|
| `D`(a) verdad del dinero | Movimiento contable, estado del envío, y la sección 5 completa |
| `D`(b) idempotencia | La entidad que persiste la clave de intento y su ventana de vida |
| `D`(c) frontera con el pagador | Los estados del envío y qué se guarda de lo que el tercero informa |
| `D`(d) tipo de cambio | Tasa aplicada, su vencimiento, y la cuenta de diferencia de cambio |
| `D`(e) momento del tamizaje | Verificación de identidad, caso de cumplimiento, y el orden de los estados |
| Los años de retención en `E` | La sección 6 y la elección de motor de las entidades voluminosas |

---

## Nota sobre las dos clases de iteración

[`ITERACIONES.md`](../ITERACIONES.md) registra dos cosas distintas y no se fusionan: la **iteración
del diseño** —el mismo diagrama de componentes dibujado otra vez y más abierto, que es la que exige
el enunciado ([ejemplo de clase](../../docs/EJEMPLO-CLASE-TOP-DOWN.md))— y la **iteración del EVAL**,
que cambia una decisión del backlog. Este paso las alimenta a las dos: las bases de datos que aquí
se decidan son las `BD` que el diagrama dibuja, y un ítem nuevo del backlog puede agregar una
entidad que nadie había nombrado.
