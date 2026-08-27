# A — Armar el modelo de datos

> Paso 4 de [R.E.D.A.L.E.](../README.md) · anterior:
> [**D** — Diseñar el servicio](../D-disenar-servicio/README.md) · siguiente:
> [**L** — Listar los componentes](../L-listar-componentes/README.md) · bitácora:
> [`ITERACIONES.md`](../ITERACIONES.md)

**Estado: entregado.** Veintiocho entidades con campos concretos, motor elegido por entidad contra
el requisito que lo obliga, otros almacenamientos decididos y las cuatro tensiones propias del caso
—el desafío, la frontera de la inmutabilidad, el trato de los datos personales y la retención por
jurisdicción— resueltas y con su precio escrito. Lo que sigue abierto lleva `[CLARIFY: …]` y dice
qué lo destraba; no hay ninguna celda vacía.

El material pide cuatro cosas: **tablas**, **campos**, **opciones de base de datos** y **otros tipos
de almacenamiento** (archivos, caché, almacenamiento de objetos, sistemas de archivos distribuidos).

**Las diez `BD` que [`L`](../L-listar-componentes/README.md) dibuja se deciden acá, y no hay una
undécima.** Cada entidad de este documento declara en qué `BD` del diagrama vive, y ninguna entidad
inventa un almacén que el diagrama no tenga: `BD identidad`, `BD giros`, `BD cumplimiento`,
`BD cotizaciones`, `BD contable`, `BD intentos`, `BD corredores y reguladores`,
`BD puntos de atención y efectivo`, `BD auditoría` y `BD desafíos`. Esa correspondencia es el
contrato con `L`, y se lee en las dos direcciones: una `BD` sin entidad es una elipse decorativa, y
una entidad sin `BD` es una tabla que nadie escribe.

**Una convención que atraviesa todo el modelo y conviene enunciar antes que las tablas: nadie se
identifica por su documento.** Toda persona —emisor, receptor, operario, rol de cumplimiento— entra
en el modelo por un **seudónimo estable** `persona_ref`, opaco y sin significado, y es ese seudónimo
el que viaja al asiento contable, a la traza y a los acumulados. El nombre y el documento viven en
una sola tabla, cifrados, detrás de otro control de acceso. Esa decisión es la que hace ejecutables
a la vez a `RNF-03` —que no se borra nada del registro de actos— y a `RF-81` —que se borran los
datos personales de quien los entregó—, y está justificada entera en la sección 6.

---

## Contrato con los pasos vecinos

| | |
|---|---|
| **Consume de D** | El tipo de persistencia por familia de dato, y —sobre todo— las seis decisiones abiertas de `D`. Cuatro de ellas *son* decisiones de modelo de datos disfrazadas de arquitectura: dónde vive la verdad del dinero decide si hay tabla de movimientos; la idempotencia decide si hay entidad de clave de intento; el momento del tamizaje decide qué estados existen; y dónde vive la respuesta del desafío decide si hay entidad para un secreto que nadie puede leer |
| **Consume de E** | El volumen por tipo de dato y los años de retención, que deciden qué entidad puede vivir en una fila y cuál necesita almacenamiento de objetos |
| **Entrega a L** | Las bases de datos del diagrama. En el ejemplo de clase hay **varias `BD`, no una sola**: cada grupo de servicios tiene la suya, y cuál es cuál se decide acá |
| **Queda inválido si D cambia** | La entidad cuyo mecanismo se reeligió. Reabrir (a) borra o crea la tabla de movimientos; reabrir (c) cambia los estados del giro y lo que el punto de atención sostiene sin conexión; reabrir (e) cambia qué se guarda y en qué momento |
| **Queda inválido si E cambia** | La elección de motor que se justificó por volumen, y la política de retención por entidad |

---

## 1. Entidades candidatas

Nombradas, no definidas. Cada una existe porque alguien del conjunto de personas la necesita; una
entidad sin persona que la exija es un huérfano y se borra o se le busca el requerimiento que faltó
en `R`.

| Entidad candidata | Por qué es candidata |
|---|---|
| **Emisor** | Rosa. Entrega el efectivo y tiene que ser identificable contra un documento oficial vigente antes de que el dinero se mueva (`RF-01`, `RF-02`) |
| **Receptor** | Elena. No es un campo del giro: es una persona con identidad propia, que se verifica y que cobra contra código y documento (`RF-34`, `RF-85`). Modelarla como texto dentro del giro hace imposible reconocer que dos giros van a la misma persona, que es justo lo que el tamizaje necesita ver (`RF-26`, `RF-27`) y lo que `RF-58` obliga a contar |
| **Giro** | La operación completa, de extremo a extremo. Su cierre no es «despachado» ni «disponible»: es el momento en que el receptor recibe el dinero (`RF-64`, tensión T6) |
| **Código de seguimiento** | El objeto que este modelo introduce y el anterior no tenía. `RF-11` lo entrega **únicamente al emisor**, y `RNF-15` exige que quede ilegible incluso para quien administra la infraestructura: no es un identificador público del giro, es el secreto que vuelve ejecutable la cancelación (`BR-08`) |
| **Desafío** | La pregunta y la respuesta que `RF-68` obliga al emisor a registrar al crear el giro, y contra las que el receptor cobra cuando su documento no está vigente (`RF-69`, `RF-86`). No es un campo del giro y no puede serlo: `RF-12` prohíbe mostrárselo a quien atiende y `RNF-17` a quien administra el almacenamiento, `RF-82` acota los intentos —que son un dato aparte y sobre el mismo secreto— y `RF-83` lo caduca con el giro |
| **Devolución** | El camino de vuelta del dinero, con estado y plazo propios: nace de la cancelación (`RF-47`), de la retención vencida (`RF-32`) o de la prescripción (`RF-50`); es siempre en efectivo (`RF-71`) y en la moneda que el emisor entregó (`RF-88`); se retira en el punto que el emisor elija (`RF-72`), se le avisa dónde (`RF-14`), incluye la comisión cuando el giro no llegó a pagarse (`RF-74`) y queda disponible hasta la prescripción si nadie la retira (`RF-89`). Un estado más del giro no sostiene un plazo propio ni un punto de retiro distinto del de cobro |
| **Caja del punto de atención** | El efectivo que cada punto declara al abrir y al cerrar (`RF-76`), y que `RF-92` obliga a poner delante del operario antes de habilitarle un pago. Es un saldo por punto y por jornada, no el efectivo del corredor que `RF-20` exige antes de dar un giro por fondeado: dos cifras distintas que hoy nada distingue |
| **Declaración de diferencia del receptor** | La voz de Elena en el mostrador: `RF-90` la deja declarar que el dinero recibido no coincide con el informado. Es un hecho asentado por quien no es usuaria del sistema, contra un monto que `RF-38` declara intocable y una diferencia que `RF-59` atribuye al punto donde se entregó el dinero. Sin entidad, esa declaración solo existe si el operario la escribe — y es sobre él que se declara |
| **Acumulado de cobros del receptor** | `RF-58` cuenta cuántos giros cobró un mismo receptor en la ventana vigente y `RF-93` retiene el giro de quien la superó. Es el espejo del acumulado del emisor, pero sobre una persona que **no es clienta de SendIt** y de la que solo existe lo que el mostrador capturó: el contador decide una retención, así que su identidad tiene que resolverse igual entre giros |
| **Supresión** | La solicitud de `RF-81`: borrar los datos personales de quien los entregó, de nadie más, y salvo los que el registro de actos debe conservar (`RF-55`, `RNF-03`). Es un acto con solicitante, alcance, momento y resultado — y es él mismo un acto que la traza registra. Sin entidad no hay forma de demostrar qué se borró ni de defender por qué algo no |
| **Acumulado del emisor** | `RF-08` rechaza el giro que supere el límite por operación y `RF-09` el que supere el acumulado de la ventana vigente; `RF-10` obliga a contarlos **sobre la identidad del emisor y no sobre el punto de atención**. Un contador que vive dentro de la fila del punto no puede cumplir eso |
| **Segunda autorización** | El acto de un segundo rol, con su identidad y su momento: `RF-13` la exige **antes** de crear un giro sobre el umbral reforzado —y `RF-79` da el giro por creado al registrar la recepción del efectivo, así que la autorización tiene que existir antes de ese instante— y `RF-61` la exige para corregir un giro pagado. `RNF-02` obliga a poder compararla con las demás identidades del mismo giro |
| **Prescripción** | El plazo del giro no cobrado y su terminador: `RF-49` lo deja no pagable, `RF-50` pone el monto a disposición del emisor y `RF-51` avisa antes de que ocurra. Un plazo que nadie hace vencer no vence |
| **Jurisdicción** | Los dos reguladores que tocan un mismo giro: `RF-15` aplica las reglas de los dos, `RF-31` toma el plazo de retención del más estricto y `RF-18` el de conservación del más largo. Sin entidad, esos plazos quedan como constantes globales — que es exactamente lo que `RNF-03` prohíbe al exigir que se calculen por giro |
| **Movimiento contable** | El asiento. Existe si `D`(a) decide que la verdad del dinero es una suma de movimientos y no un campo |
| **Tasa aplicada / cotización** | La promesa de cuánto cobra el receptor en moneda destino. `RF-07` obliga a producirla y fecharla y `RF-06` a no recalcularla nunca: tiene momento de emisión, vencimiento y valor propios, no es un número dentro del giro |
| **Verificación de identidad** | El acto de haber comprobado quién es alguien, con su evidencia, su momento y su resultado. Distinto de la persona verificada |
| **Caso de cumplimiento** | El expediente de cumplimiento: la coincidencia, la evidencia, la decisión, el plazo y su vencimiento |
| **Traza de auditoría** | Quién vio qué, quién decidió qué, cuándo. Crece con las lecturas, no solo con las escrituras |

### Las cinco que faltaban por decidir, decididas

Cada una se decide contra el ítem que la obliga, no por gusto. Las cinco dan entidad: ninguna
sobrevive como campo.

| Candidata | Decisión | Contra qué ítem |
|---|---|---|
| **Punto de atención** | **Entidad propia**, en `BD puntos de atención y efectivo`. `RF-63` deja que el emisor lo elija entre los del país destino, así que tiene que ser **listable antes de que el giro exista** —un campo de texto dentro del giro no se puede listar— y `RF-91` deja cobrar en otro punto cuando el elegido no puede pagar, así que el giro lleva **dos** referencias distintas: `punto_eleccion_id`, que `RF-105` congela salvo que el emisor conteste, y `punto_pago_id`, que se resuelve al pagar | `RF-63`, `RF-91`, `RF-105`, `RF-76`, `RF-92` |
| **Agente** | **Entidad distinta del punto**, en la misma `BD`. Un agente opera uno o varios puntos, y `RF-24` obliga a liquidarle **el efectivo que puso de su caja**: el saldo a liquidar se agrega por agente y no por punto, y la `Caja del agente` que `L` dibuja con borde grueso es una cuenta del libro con `agente_id`, no una columna del punto | `RF-24`, `RF-20`, `RF-102` |
| **Operario** | **Identidad propia** en `BD identidad`, no un texto en la traza. `RNF-02` exige que **ninguna identidad aparezca dos veces** en la cadena crear → autorizar → pagar → liberar → corregir de un mismo giro, y eso es una restricción de unicidad sobre un conjunto de claves foráneas: no se puede comprobar contra cadenas de texto. `RF-30` y `RF-33` piden lo mismo del rol | `RF-54`, `RF-30`, `RF-33`, `RNF-02` |
| **Clave de idempotencia** | **Entidad propia**, en `BD intentos`, con vida acotada y motor distinto del resto. `RF-43` y `RF-44` obligan a tratar el reintento como la misma operación, y para eso la clave tiene que persistirse **antes** de mover un centavo y devolver el resultado original —no un error— al segundo intento. Es la única entidad del modelo que **caduca sola y no deja registro contable** | `RF-42`, `RF-43`, `RF-44` |
| **Aviso enviado** | **Entidad propia**, y ya no por conveniencia: `RF-98` obliga a conservar **constancia de cada aviso que se envió por el canal del receptor**. Con nueve tipos de aviso colgando de ítems distintos —`RF-25`, `RF-41`, `RF-75`, `RF-37`, `RF-60`, `RF-14`, `RF-51`, `RF-65`, `RF-67`— un campo `avisado` no distingue cuál se envió ni prueba nada | `RF-98`, `RF-25`, `RF-41`, `RF-60` |

El punto corre el software de SendIt, así que lo que no esté modelado no lo tiene nadie más; pero el
efectivo y el local son del agente, y esa frontera es de `RF-24` y está modelada como dos entidades y
una cuenta del libro, no como un comentario.

### Campos

Una fila por entidad, con la `BD` de [`L`](../L-listar-componentes/README.md) en la que vive. El
formato es el del material —*«Tabla: Video · Campos: Titulo, FechaCreacion, Autor, Categoría,
Puntaje, Comentarios(FK)»*— con dos columnas más que este caso obliga: la clave, porque de ella
depende que `RNF-05` y `RNF-13` sean restricciones y no buenas intenciones, y las relaciones, porque
de ellas depende que `RF-81` pueda borrar sin arrastrar el asiento.

Convenciones de los nombres de campo: `*_ref` es un seudónimo opaco de persona, `*_cif` es una
columna cifrada con llave por corredor, `*_hmac` es un verificador que se compara y no se lee, y
`*_id` es una clave foránea corriente.

| Entidad · `BD` | Campos | Clave | Relaciones |
|---|---|---|---|
| **Emisor** · `BD identidad` | `persona_ref`, `token_documento` (HMAC determinista, llave en el módulo de claves), `tipo_documento`, `pais_documento`, `documento_cif`, `nombre_cif`, `fecha_nacimiento_cif`, `telefono_cif`, `jurisdiccion_origen_id`(FK), `declarante`=`emisor`, `giro_captura_id`(FK), `estado_supresion`, `creado_en` | `persona_ref` | 1→N `Giro` por `emisor_ref` · 1→N `Verificación de identidad` · 1→1 `Acumulado del emisor` · 1→N `Supresión` |
| **Receptor** · `BD identidad` | `persona_ref`, `token_documento`, `nombre_designado_cif` (lo escribe el emisor al crear), `nombre_verificado_cif` (lo captura el mostrador de destino), `telefono_cif`, `pais_destino`, `declarante`=`receptor`, `punto_captura_id`(FK), `es_cliente`=`false`, `estado_supresion` | `persona_ref` | 1→N `Giro` por `receptor_ref` · 1→1 `Acumulado de cobros del receptor` · 1→N `Verificación de identidad` |
| **Identidad de actor** (operario, segundo rol, cumplimiento) · `BD identidad` | `identidad_id`, `persona_ref`, `rol`, `agente_id`(FK), `punto_id`(FK), `alta_en`, `baja_en`, `activa` | `identidad_id` | N→1 `Punto de atención` · 1→N `Traza de auditoría` · 1→N `Segunda autorización` |
| **Giro** · `BD giros` | `giro_id`, `emisor_ref`(FK), `receptor_ref`(FK), `jurisdiccion_origen_id`(FK), `jurisdiccion_destino_id`(FK), `version_regla_jurisdiccion` (congelada al crear), `monto_origen`, `moneda_origen`, `monto_destino`, `moneda_destino`, `comision`, `cotizacion_id`(FK), `punto_eleccion_id`(FK), `punto_pago_id`(FK), `estado` (proyección), `version_estado`, `disponible_desde`, `prescribe_en`, `conservar_hasta`, `clave_idempotencia`(FK), `creado_en`, `creada_por_identidad_id`(FK) | `giro_id` | 1→1 `Código de seguimiento`, `Desafío`, `Prescripción` · 1→0..1 `Pago`, `Devolución` · 1→N `Movimiento contable`, `Traza de auditoría`, `Aviso enviado`, `Resultado de tamizaje` |
| **Código de seguimiento** · `BD giros` | `giro_id`(PK,FK), `codigo_hmac`, `llave_id` (referencia al módulo de claves; la llave nunca sale de él), `prefijo_busqueda` (4 caracteres, para no barrer la tabla entera), `emitido_en`, `emitido_a`=`emisor`, `reemitible`=`false`, `estado` | `giro_id` | 1→1 `Giro`. **Ninguna columna guarda el código en claro, en ninguna base** |
| **Desafío** · `BD desafíos` | `giro_id`(PK), `pregunta_cif` (se le entrega al receptor por `RF-69`, nunca al operario), `verificador` = HMAC de la respuesta normalizada con llave del módulo, `llave_id`, `normalizacion_version` (`RF-84`, congelada al crear), `intentos_fallidos`, `intentos_max`, `caduca_en`, `estado` ∈ {`vigente`,`agotado`,`caducado`,`consumido`} | `giro_id` | 1→1 `Giro`, **por referencia y sin clave foránea comprobable desde `BD giros`**: quien administra la base del giro no alcanza esta |
| **Pago** · `BD giros` | `pago_id`, `giro_id`(FK, **ÚNICO**), `punto_id`(FK), `identidad_operario_id`(FK), `monto_entregado`, `moneda`, `entregado_en`, `verificacion_receptor_id`(FK), `desafio_usado` (bool, nunca el valor), `asiento_id`(FK), `clave_idempotencia`(FK) | `pago_id`; `UNIQUE(giro_id)` | 1→1 `Giro` · 1→0..N `Declaración de diferencia`. **El `UNIQUE` es `RNF-05`**: no hay forma de escribir dos entregas del mismo giro, en ningún punto y en ningún momento |
| **Devolución** · `BD giros` | `devolucion_id`, `giro_id`(FK, **ÚNICO**), `causa` ∈ {`cancelacion`,`retencion_vencida`,`prescripcion`,`intentos_agotados`}, `monto`, `moneda` (= `giro.moneda_origen`), `incluye_comision`, `punto_retiro_id`(FK), `disponible_desde`, `disponible_hasta` (= `giro.prescribe_en`), `estado`, `retirada_en`, `asiento_id`(FK) | `devolucion_id`; `UNIQUE(giro_id)` | 1→1 `Giro`. `UNIQUE(giro_id)` sobre `Pago` **y** sobre `Devolución`, más la exclusión mutua entre las dos, es `RNF-13` |
| **Movimiento contable** · `BD contable` | `movimiento_id`, `asiento_id`, `secuencia`, `giro_id`(FK), `cuenta` ∈ {`efectivo_origen`,`obligacion_receptor`,`caja_agente`,`comision`,`diferencia_cambio`}, `debe`, `haber`, `moneda`, `tipo_hecho`, `identidad_autor_id`(FK), `ocurrido_en`, `registrado_en`, `compensa_movimiento_id`(FK, `RF-56`), `hash_anterior` | `movimiento_id`; `UNIQUE(asiento_id, cuenta)` | N→1 `Giro` · N→1 `Liquidación con el agente`. **Restricción de asiento:** `SUM(debe) − SUM(haber) = 0` por `asiento_id` — es `RNF-07` escrito como constraint, no como intención |
| **Cotización** · `BD cotizaciones` | `cotizacion_id`, `par_monedas`, `tasa`, `proveedor`, `emitida_en`, `vence_en`, `margen_aplicado`, `giro_id`(FK, nulo hasta congelarse), `congelada_en` | `cotizacion_id` | 1→0..1 `Giro`. Una cotización con `giro_id` no nulo es la que `RF-06` prohíbe recalcular; una con `giro_id` nulo caduca sola por `vence_en` |
| **Verificación de identidad** · `BD identidad` | `verificacion_id`, `persona_ref`(FK), `giro_id`(FK), `rol` ∈ {`emisor`,`receptor`}, `momento`, `resultado`, `fuente` ∈ {`RENIEC`,`verificación documental del corredor`}, `documento_vigente` (bool), `evidencia_uri` (almacenamiento de objetos), `evidencia_hash`, `llave_objeto_id`, `regla_coincidencia_version`, `identidad_operario_id`(FK) | `verificacion_id` | N→1 `Emisor` o `Receptor` · N→1 `Giro`. `evidencia_uri` **no es un binario en la fila**: es la referencia que la sección 3 justifica |
| **Resultado de tamizaje** · `BD cumplimiento` | `tamizaje_id`, `giro_id`(FK), `sujeto_ref`(FK), `rol`, `momento` ∈ {`creacion`,`autorizacion_pago`,`retamizaje`}, `lista`, `version_lista`, `consultada_en`, `veredicto`, `grado` ∈ {`exacta`,`homonimia`,`sin_coincidencia`}, `nombre_contrastado_cif` (el valor tal como se vio, no un puntero), `payload_proveedor` (documento), `hash` | `tamizaje_id` | N→1 `Giro` · 1→0..1 `Caso de cumplimiento`. Son **dos filas por giro como mínimo** —`RF-26` y `RF-27`— y una más por cada `RF-97` |
| **Caso de cumplimiento** · `BD cumplimiento` | `caso_id`, `giro_id`(FK), `tamizaje_id`(FK), `tipo` ∈ {`exacta`,`homonimia`}, `abierto_en`, `plazo_vence_en`, `derivado_a_rol`, `identidad_excluida_id`(FK, la del operario que atendió), `estado`, `motivo_liberacion_cif`, `liberado_por_identidad_id`(FK), `liberado_en` | `caso_id` | 1→1 `Retención` · N→1 `Giro`. `motivo_liberacion_cif` vive **en esta tabla y no en la retención**: es el dato cuyo lector es distinto |
| **Retención** · `BD cumplimiento` | `retencion_id`, `giro_id`(FK), `caso_id`(FK, nulo cuando la origina `RF-93`), `origen` ∈ {`sancion`,`acumulado_receptor`}, `regulador_id`(FK, **el más estricto de los dos**), `vence_en`, `estado`, `liberada_en` | `retencion_id` | 1→1 `Caso de cumplimiento` · N→1 `Giro`. **La existencia y la fecha se sirven al emisor (`RF-66`); el motivo no está en esta tabla y por eso no se puede filtrar por descuido** |
| **Punto de atención** · `BD puntos de atención y efectivo` | `punto_id`, `agente_id`(FK), `pais`, `jurisdiccion_id`(FK), `geo`, `horario`, `monedas_que_paga`, `estado_operativo`, `estado_conexion`, `ultima_sincronizacion`, `tope_pago_sin_conexion` | `punto_id` | 1→N `Caja del punto` · N→1 `Agente` · 1→N `Giro` por `punto_eleccion_id` y `punto_pago_id` |
| **Agente** · `BD puntos de atención y efectivo` | `agente_id`, `razon_social`, `pais`, `jurisdiccion_id`(FK), `plazo_liquidacion`, `moneda_liquidacion`, `cuenta_libro` | `agente_id` | 1→N `Punto de atención` · 1→N `Liquidación con el agente` |
| **Caja del punto** · `BD puntos de atención y efectivo` | `caja_id`, `punto_id`(FK), `jornada`, `turno`, `moneda`, `declarado_apertura`, `declarado_cierre`, `saldo_corriente` (`RF-95` lo descuenta en cada pago, sin esperar al cierre), `declarada_por_identidad_id`(FK), `abierta_en`, `cerrada_en`, `diferencia_cierre` | `caja_id`; `UNIQUE(punto_id, jornada, turno)` | N→1 `Punto de atención`. **No es el efectivo del corredor** que `RF-20` exige: ese se agrega sobre esta tabla por `jurisdiccion_id`, y son dos cifras distintas |
| **Liquidación con el agente** · `BD puntos de atención y efectivo` + asiento en `BD contable` | `liquidacion_id`, `agente_id`(FK), `periodo_desde`, `periodo_hasta`, `total_efectivo_puesto`, `total_liquidado`, `moneda`, `estado`, `asiento_id`(FK), `archivo_export_uri`, `corrida_en` | `liquidacion_id` | N→1 `Agente` · 1→N `Movimiento contable`. Lo que la puebla es cada `Pago` con el `punto_id` de un punto de ese agente |
| **Acumulado del emisor** · `BD giros` | `emisor_ref`(FK), `jurisdiccion_origen_id`(FK), `ventana_desde`, `ventana_hasta`, `monto_acumulado`, `giros_contados`, `limite_operacion`, `limite_ventana`, `actualizado_en` | `(emisor_ref, jurisdiccion_origen_id, ventana_desde)` | N→1 `Emisor`. La clave **no lleva `punto_id`**, y esa ausencia es literalmente `RF-10` |
| **Acumulado de cobros del receptor** · `BD cumplimiento` | `receptor_ref`(FK), `pais_destino`, `ventana_desde`, `ventana_hasta`, `cobros_contados`, `limite_ventana`, `actualizado_en` | `(receptor_ref, pais_destino, ventana_desde)` | N→1 `Receptor` · 1→N `Retención` por `RF-93`. Sobrevive a una supresión porque no tiene ningún atributo personal: solo el seudónimo y un número |
| **Segunda autorización** · `BD auditoría`, con la compuerta en `BD giros` | `autorizacion_id`, `secuencia`, `giro_id`(FK), `motivo` ∈ {`umbral_reforzado`,`correccion_monto`}, `identidad_solicitante_id`(FK), `identidad_autorizante_id`(FK), `rol_autorizante`, `otorgada_en`, `resultado`, `hash_anterior` | `autorizacion_id` | N→1 `Giro`. **Restricción `RNF-02`:** `identidad_autorizante_id` no puede aparecer en ninguna otra fila de la cadena crear → autorizar → pagar → liberar → corregir del mismo `giro_id` |
| **Prescripción** · `BD giros` | `giro_id`(PK,FK), `prescribe_en`, `jurisdiccion_origen_id`(FK), `version_regla`, `aviso_previo_enviado_en`, `ejecutada_en`, `devolucion_id`(FK) | `giro_id` | 1→1 `Giro` · 1→0..1 `Devolución`. `prescribe_en` es **fecha absoluta congelada al crear**, no un plazo que se recalcula |
| **Jurisdicción** · `BD corredores y reguladores` | `jurisdiccion_id`, `version`, `pais`, `regulador`, `plazo_conservacion_anios`, `plazo_retencion_horas`, `plazo_prescripcion_meses`, `umbral_reporte`, `limite_operacion`, `limite_acumulado_ventana`, `umbral_reforzado`, `motivo_revelable` (bool, `RF-40`), `vigente_desde`, `vigente_hasta` | `(jurisdiccion_id, version)` | 1→N `Corredor` · 1→N `Giro`. **Versionada**: el giro congela la versión que obedeció, porque `RNF-03` exige calcular por giro y no por política global |
| **Corredor** · `BD corredores y reguladores` | `corredor_id`, `jurisdiccion_origen_id`(FK), `jurisdiccion_destino_id`(FK), `habilitado`, `incompatibilidad` (`RF-16`), `monedas_destino`, `motivo_no_atendible` (`RF-19`) | `corredor_id` | N→2 `Jurisdicción`. Es la entidad que hace que `RF-15` aplique **las dos** y `RF-16` rechace en vez de elegir |
| **Aviso enviado** · `BD auditoría` | `aviso_id`, `secuencia`, `giro_id`(FK), `destinatario_ref`(FK), `rol` ∈ {`emisor`,`receptor`}, `tipo` (uno de los nueve: `RF-25`, `RF-41`, `RF-75`, `RF-37`, `RF-60`, `RF-14`, `RF-51`, `RF-65`, `RF-67`), `canal` ∈ {`llamada`,`sms`}, `telefono_token`, `enviado_en`, `acuse`, `intentos`, `resumen_contenido`, `hash_anterior` | `aviso_id` | N→1 `Giro`. `telefono_token` y no el número: la constancia de `RF-98` tiene que sobrevivir a la supresión del contacto, y sobrevive porque no lo contiene |
| **Declaración de diferencia del receptor** · `BD giros` | `declaracion_id`, `giro_id`(FK), `pago_id`(FK), `monto_informado`, `monto_declarado_recibido`, `moneda`, `declarada_en`, `canal`=`mostrador`, `punto_atribuido_id`(FK, `RF-59`), `identidad_operario_id`(FK), `estado`, `correccion_movimiento_id`(FK) | `declaracion_id` | N→1 `Pago` · N→1 `Punto de atención`. El punto atribuido es el del pago, y el operario registrado es aquel **sobre el que** se declara |
| **Reporte a la autoridad** · `BD auditoría` + archivo plano | `reporte_id`, `giro_id`(FK), `autoridad`, `jurisdiccion_id`(FK), `umbral_aplicado`, `base_del_umbral`=`giro_completo` (`RF-22`), `enviado_en`, `acuse`, `archivo_uri`, `hash_anterior` | `reporte_id` | N→1 `Giro`. **No tiene ninguna relación hacia `Retención` ni hacia el estado que ve el emisor**, y esa ausencia es la garantía de que su existencia no se deduce |
| **Traza de auditoría** · `BD auditoría` | `traza_id`, `secuencia`, `giro_id`(FK), `tipo_acto` (incluidas las **lecturas** de identidad, `RNF-04`), `identidad_autor_id`(FK), `rol`, `punto_id`(FK), `entidad_objetivo`, `id_objetivo`, `valores_relevantes` (documento con el valor que se vio, no un puntero), `ocurrido_en`, `registrado_en`, `conservar_hasta`, `hash_anterior` | `traza_id` | N→1 `Giro`. Crece con las lecturas: cada consulta de Kevin sobre un expediente es una fila |
| **Supresión** · `BD auditoría`, ejecuta sobre `BD identidad` y el almacenamiento de objetos | `supresion_id`, `solicitante_ref`(FK), `rol_declarante`, `solicitada_en`, `alcance` (lista de campos y objetos), `ejecutada_en`, `campos_borrados`, `objetos_criptoborrados`, `conservado_por_regla` (qué **no** se borró y qué ítem lo obliga), `identidad_ejecutor_id`(FK), `resultado`, `hash_anterior` | `supresion_id` | N→1 `Emisor` o `Receptor`. Es el acto que **demuestra** el borrado, y por eso no puede vivir en la base que borra |
| **Clave de idempotencia** · `BD intentos` | `clave`, `operacion` ∈ {`crear`,`pagar`,`cancelar`,`devolver`,`liberar`}, `punto_id`(FK), `giro_id`(FK, nulo hasta que existe), `huella_contenido`, `estado`, `resultado_serializado`, `creada_en`, `expira_en` (TTL) | `clave` | 1→0..1 `Giro`. **Un reintento con la misma clave y distinta `huella_contenido` es un conflicto y no una operación nueva** — es lo único que impide que un corte convierta un giro en dos |

## 2. Elección de motor por entidad

La elección es **por entidad**, no global — el material lo hace así en su ejemplo, con NoSQL para
imágenes y SQL para metadata. El criterio no es la preferencia sino qué garantía necesita cada dato:
integridad transaccional, capacidad de agregar sin bloquear, o volumen barato de solo escritura.
**El dinero y la traza no toleran lo mismo que un historial de avisos, y por eso no comparten
motor.**

| Entidad | Necesidad dominante | Motor | Por qué | Decisión |
|---|---|---|---|---|
| `Giro`, `Pago`, `Devolución`, `Prescripción`, `Código de seguimiento`, `Declaración de diferencia`, `Acumulado del emisor` | Restricciones de unicidad y transacción sobre varias filas | **Relacional** — `BD giros` | `RNF-05` y `RNF-13` son `UNIQUE(giro_id)` sobre `Pago` y sobre `Devolución` más su exclusión mutua. Ningún motor que resuelva conflictos «el último gana» puede sostener un invariante que dice *ninguno, en ningún punto y en ningún momento*: la unicidad tiene que ser del motor, no de la aplicación | **Relacional, con las tres restricciones declaradas en el esquema** |
| `Movimiento contable`, `Liquidación con el agente` | Suma que cuadra y valor anterior que no desaparece | **Relacional en modo append-only** (`INSERT` únicamente; sin `UPDATE` ni `DELETE` concedidos al servicio) — `BD contable` | `RNF-07` es una restricción aritmética por asiento —`SUM(debe) − SUM(haber) = 0`— y eso pide transacción. `BR-13` y `RF-56` prohíben corregir borrando: la corrección es un movimiento **nuevo** con `compensa_movimiento_id`. Un motor documental daría el `INSERT` barato y no daría el asiento que cuadra | **Relacional append-only, con encadenamiento `hash_anterior` por partición de giro** |
| `Traza de auditoría`, `Segunda autorización`, `Reporte a la autoridad` | Escritura masiva que nunca se modifica y casi nunca se lee | **Append-only encadenado, particionado por fecha** — `BD auditoría` | `RNF-03` dice *«ningún acto registrado se modifica ni se borra, cualquiera sea quien lo pida»* y `RF-54` le exige autor. `RNF-04` la hace crecer con las **lecturas**, así que el volumen es de escritura pura y el patrón de consulta es por giro y por rango de fechas. Un relacional mutable no da la garantía; un almacén de solo-agregar con encadenamiento la da y además la vuelve comprobable | **Append-only, sin `UPDATE` posible ni para el administrador; conservación por partición, con `conservar_hasta` por fila** |
| `Aviso enviado` | Volumen alto, valor probatorio bajo, retención corta | **Append-only barato, en la misma `BD auditoría` pero en su propia partición con retención propia** | `RF-98` exige constancia, no exige inalterabilidad de asiento: el aviso prueba que se avisó, no mueve dinero. Ponerlo en la partición del asiento le pagaría a un SMS el precio de conservación de `RF-18` durante cinco años. **Este es el caso que muestra por qué la elección es por entidad: mismo motor, distinta retención, distinta partición** | **Append-only, partición separada, purga al cerrar el giro y sus plazos** |
| `Cotización` | Serie temporal fechada, escritura durable, lectura por giro y análisis por rango | **Append-only fechado, con lectura columnar para el análisis** — `BD cotizaciones` | `RF-07` obliga a producirla y fecharla y `RF-06` a no recalcularla: es un hecho con momento, no un valor que se actualiza. La lectura del camino crítico es puntual por `giro_id`; la que dimensiona el margen y la diferencia de cambio es un barrido por par de monedas y rango, que es exactamente donde un formato columnar paga | **Append-only fechado; las no congeladas caducan por `vence_en` y no se conservan** |
| `Emisor`, `Receptor`, `Identidad de actor`, `Verificación de identidad` | Cifrado por columna, control de acceso propio y **borrado selectivo de fila** | **Relacional con cifrado por columna y llave por corredor** — `BD identidad` | `RNF-01` exige que queden ilegibles para quien administra la infraestructura, `RNF-04` que todo acceso deje traza, y `RF-81` que se pueda **borrar** — que es la única entidad del modelo de la que eso se dice. Un motor append-only aquí sería un defecto: haría inejecutable el derecho de supresión | **Relacional, borrable, con la llave fuera del motor** |
| `Resultado de tamizaje`, `Caso de cumplimiento` | Payload heterogéneo de un tercero, guardado tal como llegó | **Documental**, dentro de `BD cumplimiento` | `RF-27` decide contra las listas **vigentes al momento de autorizar el pago** y `RF-28` separa coincidencia exacta de homonimia: hay que guardar el valor que se vio, con su lista y su versión, y el formato lo fija OFAC, ONU o la UE, no nosotros. Un esquema fijo obliga a normalizar la respuesta de un tercero, y normalizar es perder justo lo que la auditoría vendría a mirar | **Documental para la evidencia; relacional para el estado del caso y su plazo, en la misma base** |
| `Retención`, `Acumulado de cobros del receptor` | Plazo que vence y contador por identidad | **Relacional** — `BD cumplimiento` | `RF-31` le pone plazo a la retención y `RF-32` la termina; `RF-58` cuenta por identidad de receptor y `RF-93` retiene al superarla. Las dos son consultas por clave con una fecha o un número, y las dos deciden si el dinero sale: no toleran una lectura desactualizada | **Relacional, sin caché** |
| `Desafío` | Comparar sin poder leer, con contador de intentos y caducidad | **Clave-valor con llave propia y TTL, en base separada** — `BD desafíos` | `RNF-17` exige ilegibilidad frente a quien administra la infraestructura y `RF-12` frente a quien atiende. Vivir como columna de `BD giros` lo pondría bajo el mismo administrador que el giro; `L` ya lo dibuja como base aparte por esta razón. El acceso es siempre por `giro_id`, nunca por barrido, así que no hace falta un relacional | **Clave-valor, base separada, llave en el módulo de claves, TTL igual a `giro.prescribe_en` (`RF-83`)** |
| `Clave de idempotencia` | Escritura antes de mover dinero, lectura por clave, muerte por TTL | **Clave-valor durable con TTL** — `BD intentos` | `RF-43` y `RF-44` obligan a que el reintento sea la misma operación, y para eso la clave tiene que persistirse **antes** del primer efecto. Es la única entidad que puede desaparecer sola sin romper nada: no la reclama ningún regulador. Durable y no en memoria, porque una caché perdida convierte un reintento en un giro nuevo | **Clave-valor durable, TTL corto, conflicto explícito ante misma clave y distinto contenido** |
| `Punto de atención`, `Agente`, `Caja del punto` | Lectura muy frecuente del catálogo, escritura transaccional del saldo | **Relacional** — `BD puntos de atención y efectivo` | `RF-95` descuenta el efectivo del punto **en cada pago y sin esperar al cierre**: es un saldo que se decrementa bajo concurrencia y decide si Elena cobra. `RF-92` lo lee antes de habilitar cada pago. El catálogo (`RF-63`, `RF-91`) sí se cachea; el saldo no, y por eso están en tablas distintas de la misma base | **Relacional; catálogo cacheable, saldo transaccional** |
| `Jurisdicción`, `Corredor` | Volumen mínimo, lectura en cada operación, **historial de versiones** | **Relacional versionado** — `BD corredores y reguladores` | `RF-15` aplica las dos, `RF-18` toma el plazo más largo y `RF-31` el más estricto: son constantes que cambian por acto del regulador y de las que el giro tiene que recordar **qué versión obedeció**. Sin `version` en la clave, una norma nueva reescribiría retroactivamente el plazo de giros ya conservados — que es lo que `RNF-03` prohíbe al pedir el cálculo por giro | **Relacional versionado, `(jurisdiccion_id, version)` como clave, cacheable por versión** |
| `Supresión` | Prueba de un borrado, que no puede vivir donde se borra | **Append-only** — `BD auditoría` | `RF-81` tiene que ser demostrable ante quien lo pidió y defendible ante el regulador, y una constancia de borrado guardada en la base borrada no prueba nada | **Append-only, con el alcance y lo conservado escritos en la propia fila** |

**Lo que este reparto deja dicho de una vez:** ninguna base guarda a la vez el secreto y el dato que
el secreto protege. El código vive en `BD giros` como verificador y su llave no; la respuesta del
desafío vive en `BD desafíos` y ni siquiera comparte administrador; el documento vive en
`BD identidad` cifrado y su llave está fuera del motor. Un administrador con acceso total a una
cualquiera de las diez bases no reconstruye ninguno de los tres, y eso es `RNF-01`, `RNF-15` y
`RNF-17` cumplidos por la forma de las tablas.

## 3. Otros almacenamientos

| Necesidad | Qué guarda | Opción | Por qué | Decisión |
|---|---|---|---|---|
| Almacenamiento de objetos | Binarios de identidad —la evidencia que `RF-80` obliga a conservar de emisor y receptor—, evidencia adjunta de un caso | **Almacenamiento de objetos, un objeto por verificación, cifrado con una llave por giro**; en la fila queda `evidencia_uri`, `evidencia_hash` y `llave_objeto_id`, nunca el binario | Es la partida que domina el volumen —`RF-80` la captura **dos veces por giro**, en dos países— y la que casi nunca se lee: cientos de kilobytes escritos una vez y consultados solo por auditoría o por un caso. Meterla en la fila haría lento todo lo que sí se consulta. Y una llave por giro es lo que hace ejecutable a `RF-81`: destruirla vuelve el objeto irrecuperable sin tocar el asiento que lo referencia | **Objetos, cifrado por objeto con llave por giro; el hash queda en la fila para poder demostrar que el binario no cambió incluso después de destruirlo** |
| Caché | El catálogo de puntos de atención que `RF-63` le ofrece al emisor y que `RF-91` usa para proponer otro; las jurisdicciones y corredores de `BD corredores y reguladores`, **cacheados por `version`** | **Caché en memoria, con clave que incluye la versión del dato** | Son los dos únicos datos del sistema que se leen en cada operación, cambian por acto administrativo y **no deciden si el dinero sale**. Cachear por versión hace que una norma nueva invalide la entrada por cambio de clave, en vez de por expiración | **Se cachea el catálogo y la norma. Nada más** |
| Caché — lo que **no** se cachea, y es la decisión que importa | Estado del giro (`RF-52`, `RF-53`, `RF-66`), saldo de la caja del punto (`RF-92`, `RF-95`), resultado de tamizaje (`RF-27`), efectivo del corredor (`RF-20`), retención y su plazo (`RF-31`), verificador del código y del desafío | **Ninguna. Lectura directa del motor** | Cachear es servir un dato que puede estar viejo, y `RNF-06` declara imposible que dos lugares del sistema afirmen a la vez que un giro está retenido y disponible para cobro. Una caché **es** un segundo lugar que afirma. `RF-27` es todavía más explícito: contrasta contra las listas **vigentes al momento de autorizar el pago**, no contra las que estaban vigentes cuando se llenó la caché | **Prohibido por diseño, no por configuración: estos datos no tienen ruta de lectura cacheada** |
| Sistema de archivos distribuido | Archivo frío: binarios de identidad y particiones de traza cuyo giro ya cerró pero cuyo `conservar_hasta` sigue corriendo; los lotes de re-tamizaje de `RF-97`, que barren todos los giros no pagados cuando cambia una lista | **Sistema de archivos distribuido, escritura por lote, lectura por barrido** | El plazo de `RF-18` —el más largo de los dos reguladores, con piso de cinco años— produce un cuerpo de datos que hay que conservar y casi nunca leer, y que si se deja en el motor caliente paga precio de disponibilidad por nada. `RF-97`, en cambio, necesita justo lo contrario: leer **todo** de una vez, que es donde un barrido secuencial gana | **Archivo frío al vencer el plazo de prescripción del giro, no al pagarse — `RF-89` mantiene viva la devolución no retirada hasta ahí** |
| Archivos planos / exportación | Reportes a la autoridad de origen (`RF-17`), liquidación con cada agente (`RF-24`) | **Archivo plano firmado por corrida, con su `acuse` y su `hash` guardados en `BD auditoría`** | Los dos salen del sistema hacia alguien que no es SendIt y que responde con un acuse: el formato lo fija el receptor —FinCEN, SEPBLAC, UIF-Perú, o el contrato con el agente— y no nosotros. Lo que se modela acá no es el archivo sino **la prueba de haberlo entregado**: `reporte_id`, `enviado_en`, `acuse`, `archivo_uri`. Un reporte no entregado es incumplimiento regulatorio, no un mensaje perdido | **El archivo vive en el almacenamiento de objetos; la constancia y el acuse en `BD auditoría`** |
| Almacén local del punto de atención | Lo que el mostrador tiene que sostener sin conexión: las autorizaciones ya bajadas, las prohibiciones que `RF-45` le obliga a respetar, los pagos hechos y no informados, el efectivo declarado al abrir y al cerrar (`RF-76`, `RF-92`) y —si la comparación del desafío corre ahí— algo derivado de una respuesta que `RNF-17` prohíbe que sea legible en el local de un tercero | **Base embebida en el equipo del punto, cifrada en reposo con llave del dispositivo, con dos tablas y nada más: `autorizacion_bajada` (con `caduca_en` y `tope_monto`) y `hecho_local_pendiente` (append-only, se vacía al sincronizar)** | La lista de prohibiciones de `RF-45` no se puede bajar completa —una retención nace en el centro mientras el punto está caído— así que el modelo local no guarda «lo prohibido» sino **lo autorizado, con caducidad**: lo que no se puede sostener con lo local se rechaza. Y `RF-100` cierra el caso del desafío sin dejar margen: *«el sistema impedirá que un punto sin conexión autorice un pago que no puede comprobar contra el centro»*. **Del desafío no baja nada al local — ni el verificador, ni la pregunta, ni el contador** | **El punto sin conexión paga contra autorización caducable y con tope, y no ejerce `RF-69`. Los hechos locales suben como filas nuevas, nunca como estados que pisan** |

**Un aviso sobre la caché en este dominio.** Cachear es servir un dato que puede estar viejo. El
monto que Rosa vio, el estado de un giro retenido que `RF-66` le muestra y el resultado de un
tamizaje son exactamente los datos que no toleran estar viejos, y son los que más se consultan. Por
eso la tabla de arriba lleva **dos filas de caché y no una**: la que dice qué se cachea y la que dice
qué no, con su ítem cada una. Justificar la caché por capa —«las lecturas van por caché»— habría
metido el estado del giro adentro sin que nadie lo decidiera, y `RNF-06` no admite ese segundo lugar
que afirma.

---

## 4. Datos personales y su trato

| Dato | ¿Se guarda? | En claro / cifrado / tokenizado / hash / no se guarda | Quién puede leerlo | Bajo qué condición | Por qué así |
|---|---|---|---|---|---|
| Documento de identidad del emisor | Sí, **partido en dos columnas** | `token_documento` tokenizado (HMAC determinista, llave en el módulo) **y** `documento_cif` cifrado con llave por corredor | El token: `Limits Service` y `Cobros del Receptor Service`, sin descifrar nada. El número: solo `Identity Service`, y solo al verificar | Con `giro_id` de la operación que se está atendiendo, y dejando fila en `Traza de auditoría` | Contar límites *sobre la identidad del emisor* (`RF-10`) exige reconocer que dos giros son de la misma persona; **no exige leer su documento**. Partirlo en token y cifrado es lo que permite lo primero sin conceder lo segundo, y es lo que hace que `RNF-01` se cumpla contra quien administra la infraestructura y no solo contra quien roba el disco |
| Imagen del documento (`RF-80`) | Sí | En almacenamiento de objetos, **cifrada con llave por giro**; en la fila solo `evidencia_uri`, `evidencia_hash` y `llave_objeto_id` | `Identity Service` al verificar; el rol de cumplimiento sobre un caso abierto | Con caso o verificación en curso, y con traza obligatoria (`RNF-04`) | Es el dato voluminoso, el que domina el cálculo 2 de `E` y el que `RF-81` puede tener que borrar. Llave por giro convierte el borrado en **destrucción de llave**: instantáneo, demostrable, y sin tocar la fila que lo referencia |
| Documento de identidad del receptor (`RF-85`, `RF-86`) | Sí, igual que el del emisor | Tokenizado + cifrado, con `declarante`=`receptor` y `punto_captura_id` | Igual que arriba, más `Payout Service` para comparar titularidad | Al pagar, y solo sobre el giro que se paga (`RF-57`) | `RF-84` obliga a que **el sistema** decida qué diferencia de escritura cuenta como coincidencia: eso es una comparación entre `nombre_designado_cif` y `nombre_verificado_cif` con `regla_coincidencia_version` guardada, no un juicio del operario. Y `declarante` es lo que hace que `RF-81` sepa que este dato lo entregó Elena y no Rosa |
| Código de seguimiento del giro (`RNF-15`) | **No en claro, en ninguna base** | `codigo_hmac` con llave en el módulo, más `prefijo_busqueda` de cuatro caracteres | Nadie. **Ningún servicio tiene ruta de lectura**: `Payout Service` compara y recibe un booleano | El mostrador teclea lo que el receptor trae y el centro responde coincide / no coincide | `RF-11` lo entrega solo al emisor, `RF-94` prohíbe reemitirlo aun al emisor que lo perdió y `RF-34` obliga a exigirlo para pagar. Las tres juntas describen **comparación sin lectura**, que no es una regla de pantalla: es una columna que guarda un verificador y ninguna que guarde el valor. El prefijo existe porque sin él la comparación barre la tabla, y cuatro caracteres no reconstruyen nada |
| Pregunta del desafío (`RF-68`) | Sí | `pregunta_cif`, cifrada, en `BD desafíos` | `Desafío Service`, para entregársela al receptor por su canal (`RF-69`) | Solo cuando `Identity Service` reporta documento no vigente sobre ese giro | La pregunta **sí** se muestra —a Elena, por el canal de `RF-69`— y **no** al operario: `RF-12` y `RF-57` lo excluyen de los dos lados del desafío. Que pregunta y respuesta tengan trato distinto es la razón de que sean dos columnas y no un blob |
| Respuesta del desafío (`RF-12`, `RF-101`, `RNF-17`) | **No.** Se guarda un verificador, no el valor | `verificador` = HMAC con llave que **nunca sale del módulo de claves**, sobre la respuesta normalizada; `normalizacion_version` al lado | Nadie, en ninguna forma. El módulo compara y devuelve veredicto | El punto manda lo que Elena dijo, el centro responde correcta / incorrecta / intentos agotados | `RF-101` dice que el sistema **no la transmite a nadie, ni siquiera a quien registró la pregunta**: eso descarta cifrado reversible, porque una llave que descifra es una ruta de lectura. El detalle entero, con su precio, está abajo |
| Intentos fallidos del desafío (`RF-82`) | Sí | `intentos_fallidos` en claro, pero **dentro de `BD desafíos`** y no de `BD giros` | El operario ve *«quedan N intentos»*, nunca la fila | Sobre la operación que atiende (`RF-57`) | Un contador es un dato **sobre** el secreto: puesto en la fila del giro, delata que hubo desafío y cuántas veces falló a cualquiera que consulte el giro. Puesto donde vive el secreto, hereda su control de acceso. `RF-103` lee ese contador para devolver el giro al agotarse |
| Domicilio | **No se guarda** | Ninguna forma: no existe la columna | Nadie, porque no hay dato | Ninguna condición lo habilita | Ningún ítem del backlog lo pide: ni `RF-01`, ni `RF-80`, ni `RF-17`. Un dato personal que no tiene requerimiento que lo exija es superficie de ataque sin dueño y una fila más que `RF-81` tendría que borrar. Si un regulador de `RF-15` llegara a exigirlo, entra como **evidencia de identidad en el almacenamiento de objetos bajo su jurisdicción**, con el plazo de esa jurisdicción — no como columna del emisor, que lo volvería global |
| Teléfono de Elena (`RF-25`, `RF-41`, `RF-60`) | Sí, **mientras haya avisos pendientes** | `telefono_cif` en `BD identidad`; en la constancia de `RF-98` solo `telefono_token` | `Notification Service` al despachar; nadie más | Con un aviso pendiente sobre un giro vivo | Es el caso claro de `RF-81` y el que prueba si el modelo sabe borrar sin romper nada: borrar `telefono_cif` deja intacta la constancia del aviso, porque la constancia guarda el token y no el número. Si el aviso guardara el número, o `RF-98` o `RF-81` tendría que ceder |
| Resultado de tamizaje y su coincidencia | Sí, **con el valor que se vio** | `nombre_contrastado_cif` cifrado + `payload_proveedor` como documento, con `lista` y `version_lista` | Rol de cumplimiento sobre un caso; nunca el operario | Caso abierto, con traza | `RF-27` decide contra las listas **vigentes al momento de autorizar el pago**: guardar un puntero a la persona no reconstruye la decisión, porque el nombre pudo cambiar y la lista seguro cambió. Hay que guardar el valor congelado — y eso significa que el tamizaje **conserva un dato personal que `RF-81` no alcanza**, por la excepción de `RNF-03` |
| Existencia de un reporte a la autoridad | Sí | Fila propia en `BD auditoría`, **sin relación alguna hacia `Retención` ni hacia el estado que ve el emisor** | Rol de cumplimiento y `Reporte Service` | Nunca por la ruta de `Consulta Service` ni la de `Punto de Atención Service` | La existencia no está declarada secreta por ningún ítem; lo que se oculta es el **motivo** (`RF-40`), y a Rosa se le sirve el hecho y la fecha (`RF-66`) sin el porqué. Que sean dos tablas con lectores distintos —`Retención` sin motivo, `Caso de cumplimiento` con él— es lo que impide deducir uno del otro. Ocultarlo en la interfaz no bastaba (tensión T2) |
| Motivo de una retención y de su liberación (`RF-40`, `RF-87`) | Sí | `motivo_liberacion_cif` en `Caso de cumplimiento`, **no en `Retención`** | Solo el rol de cumplimiento | Sobre el caso que tiene asignado, con traza | `RF-33` reserva la liberación a ese rol y `RF-87` obliga a que deje motivo escrito; `RF-40` se lo omite al operario y `RF-30` prohíbe que lo toque quien atendió. Un motivo en la misma fila que el estado se filtra por cualquier consulta que traiga la fila entera |
| Identidad de quien ejecutó cada acto (`RF-54`, `RNF-02`) | Sí, siempre | `identidad_autor_id` como clave foránea, nunca como texto | Auditoría y rol de cumplimiento | Sin condición: no hay acto anónimo | `RNF-02` exige comprobar que ninguna identidad aparece dos veces en la cadena del mismo giro. Eso es una comparación entre claves, y una traza que guarde *«Kevin R.»* no la puede hacer |

**Por qué esto es decisión de modelo de datos y no de infraestructura.** Cifrar el disco protege
contra el robo del disco. No protege contra la consulta legítima que no debía ocurrir — y `RF-57`
limita al operario **a los datos de la operación que está atendiendo**, mientras `RNF-01` exige que
los datos de identidad queden ilegibles para quien administra la infraestructura, `RNF-15` lo mismo
del código de seguimiento, `RNF-17` lo mismo de la respuesta del desafío —y además frente a quien
atiende el mostrador (`RF-12`)— y `RNF-04` que todo
acceso a datos de identidad deje autor, momento y giro. Esas garantías se cumplen decidiendo
dónde vive el dato, detrás de qué referencia, con qué llave y con qué registro de acceso: es la
forma de las tablas, no la configuración del servidor.

Cuatro consecuencias concretas que la tabla tiene que resolver:

- **Sacar el documento y el código de la fila cambia la forma de la entidad.** `RNF-01` exige que
  los datos de identidad queden ilegibles para quien administra la infraestructura, y `RNF-15` lo
  mismo del código de seguimiento. Si cualquiera de los dos se guarda detrás de una referencia —con
  otra llave y otro control de acceso— deja de ser un campo del emisor o del giro y pasa a ser una
  relación con otro almacén: una tabla más y una frontera más. Y el código tiene una exigencia que
  el documento no tiene: `RF-11` lo entrega solo al emisor y `RF-34` obliga a exigirlo para
  autorizar el pago, así que el modelo tiene que permitir **comprobarlo en el mostrador sin poder
  mostrarlo** (`RNF-15`) — comparación sin lectura, que es una forma de tabla y no una regla de
  pantalla.
- **La respuesta del desafío es un secreto compartido, y ahí está el problema de modelado más duro
  de este paso.** `RF-68` obliga al emisor a registrarla al crear el giro y `RF-69` deja cobrar con
  un documento no vigente a quien la responde, que es la única excepción a la vigencia que `RF-86`
  admite: hay que guardarla, no es opcional. Y a la vez `RF-12` prohíbe mostrarla a quien atiende,
  `RNF-17` a quien administra la infraestructura y `RF-101` prohíbe transmitirla a nadie **ni
  siquiera a quien registró la pregunta**. Está resuelto abajo, con lo que se pierde escrito al
  lado.
- **Del reporte a la autoridad, lo que se oculta es el motivo, no el hecho.** Ningún ítem declara
  secreta la existencia del reporte; lo que el backlog decide es más fino y hay que modelarlo así.
  Al operario: `RF-39` le entrega **la acción** que corresponde ofrecer ante un rechazo y `RF-40` le
  **omite el motivo** cuando revelarlo está prohibido. Al emisor: `RF-66` le muestra **que** su giro
  está retenido y **hasta qué fecha**, y `RF-67` le avisa cuando pasa a estarlo. Motivo y hecho son
  entonces dos datos con lectores distintos —no una fila que se muestra u oculta entera—, y el
  modelo tiene que permitir servir el segundo sin que el primero se deduzca. `RF-57` acota quién
  llega al motivo y `RNF-04` obliga a que ese acceso quede trazado. Ocultarlo en la interfaz no
  basta (tensión T2).
- **El dato del receptor lo captura el mostrador de un agente, y ahí hay una frontera contable.**
  Elena se identifica ante un punto de atención que corre el software de SendIt, pero el efectivo
  que se le entrega sale de la caja del agente y SendIt se lo liquida después (`RF-24`): sí hay un
  tercero, y la custodia del dato y la del dinero no caen del mismo lado. Eso cierra una cosa y abre
  tres. Cierra: el registro es de SendIt, porque el software lo es. Abre: **qué se le exige a Elena
  lo decide la regla de este lado** —código (`RF-34`), documento del titular designado (`RF-85`) y
  vigencia salvo desafío respondido (`RF-86`, `RF-69`)—, y quien la atiende no puede saltarla aunque
  sepa que es ella, ni decidir por su cuenta si el nombre coincide (`RF-84`)
  —eso es T3, y con `RF-57` limitando lo que ve, tiene todavía menos margen—; **qué queda
  escrito en el equipo del local del agente** mientras el punto opera sin conexión, dónde vive
  mientras tanto y quién puede leerlo después; y **qué parte del asiento es del agente y cuál de
  SendIt**, cuando la liquidación de `RF-24` y la conservación de `RF-18` piden cosas distintas del
  mismo hecho. Qué de ese dato puede ver el emisor no lo decide ningún ítem todavía: ni se lo
  concede ni se lo niega, y eso es un hueco para `R`, no una licencia para este paso.

### El desafío: un secreto que se comprueba y no se lee

Es el problema de modelado más interesante del paso porque las tres salidas obvias están cerradas por
un ítem cada una, y hay que verlas cerradas antes de aceptar la cuarta.

| Salida obvia | Qué la cierra |
|---|---|
| Guardar la respuesta en claro | `RNF-17` — la vuelve legible para quien administra `BD desafíos`, que es exactamente el lector que el invariante nombra |
| Guardarla cifrada con llave del sistema | `RF-101` — *no transmitirá a nadie la respuesta*. Una llave que descifra **es** una ruta de lectura: quien la tiene reconstruye el valor, y el invariante de `RNF-17` no dice «difícil de leer», dice que el sistema puede comprobarla **sin poder mostrarla** |
| No guardar nada | `RF-69` — sin nada guardado no hay contra qué comparar, y la única excepción a la vigencia del documento que `RF-86` admite deja de existir. Elena vuelve a quedarse sin cobrar, que es la tensión T3 sin resolver |

**Lo que se guarda, entonces.** Un **verificador** y ninguna forma del valor:

```
Tabla: Desafío  ·  BD desafíos  ·  clave: giro_id
Campos: giro_id, pregunta_cif, verificador, llave_id, normalizacion_version,
        intentos_fallidos, intentos_max, caduca_en, estado
```

`verificador = HMAC(llave_del_módulo, normalizar(respuesta, normalizacion_version))`

Cuatro decisiones de modelo, cada una contra su ítem, y ninguna es de infraestructura porque todas
cambian qué columnas existen:

1. **La llave nunca sale del módulo de claves, y la derivación corre dentro de él.** No es lo mismo
   que un hash con sal guardado en la fila. El espacio de respuestas de este dominio es
   diminuto —el nombre de un perro, el pueblo de la abuela, un apodo— así que un hash con sal
   robado se rompe con un diccionario en una tarde. Con la llave adentro del módulo, quien copia
   `BD desafíos` entera se lleva verificadores que no puede atacar sin el módulo, y el módulo no
   responde «cuál es» sino «coincide». Eso es lo que hace verdadero el invariante de `RNF-17`
   frente a **quien administra la infraestructura**, y no solo frente a quien roba el disco.
2. **`normalizacion_version` es una columna, no una constante del código.** `RF-84` ya le quitó al
   operario la decisión de qué diferencias de escritura cuentan como coincidencia sobre el nombre
   del titular; acá vale igual, y la regla —minúsculas, sin tildes, sin puntuación, sin espacios en
   los extremos— se congela **al crear el giro** y viaja en la fila. Sin esa columna, cambiar la
   regla mañana invalidaría en silencio todos los verificadores vigentes y nadie podría saber
   cuáles: no hay forma de recalcularlos, porque no hay dónde leer el valor original.
3. **El contador vive en esta tabla y no en la del giro.** `RF-82` acota los intentos y `RF-103`
   devuelve el giro al agotarlos, así que el contador decide sobre dinero; pero es un dato **sobre**
   el secreto, y en la fila del giro delataría a cualquier lector que hubo desafío y cuántas veces
   falló. Al mostrador le llega *«quedan N intentos»*, que es lo que `RF-57` le concede.
4. **La comparación corre en el centro y devuelve un veredicto.** `RF-100` lo cierra sin margen:
   un punto sin conexión no autoriza un pago que no puede comprobar contra el centro. Del desafío
   **no baja nada al almacén local del punto** — ni verificador, ni pregunta, ni contador—, y por lo
   tanto la salida de `RF-69` no existe mientras el punto está incomunicado. Es la respuesta de este
   paso a `D`(f), y se apoya en un ítem P0, no en una preferencia.
5. **Caducar es destruir, no marcar.** `RF-83` la caduca junto con el giro: al vencer, se borran
   `verificador` y `pregunta_cif` y la fila queda con `estado = caducado` y su traza en
   `BD auditoría`. Dejarla marcada e inservible mantendría el material atacable durante los cinco
   años de `RF-18` para nada — el asiento no la necesita, y la sección 6 lo dice: la respuesta es el
   único dato de este modelo cuyo plazo es **más corto** que todo lo demás.

**Qué se pierde, que es la mitad de la respuesta.** Cinco cosas, y ninguna es recuperable después:

- **No se puede corregir un error de tipeo.** Si Rosa escribió mal la respuesta en el mostrador,
  nadie —ni ella, ni Kevin, ni SendIt— puede leerla para verificar qué pasó. La única salida es
  agotar los intentos y devolver el giro (`RF-103`), que es una devolución causada por un error de
  tipeo.
- **La regla de normalización no se puede revisar sobre datos vivos.** Descubrir que `«Ancash»` y
  `«Áncash»` deberían coincidir solo arregla los giros creados después: los vigentes conservan su
  `normalizacion_version` y no hay forma de migrarlos.
- **No hay analítica, ni detección de respuestas débiles, ni aviso al emisor de que eligió mal.**
  El sistema no puede saber que la respuesta es `«1234»`, y por tanto no puede desaconsejarla.
- **El módulo de claves se vuelve dependencia dura del camino de pago.** Si no responde, `RF-69` no
  se puede ejercer y Elena con documento vencido no cobra. Es un tercer punto de falla junto a la
  verificación documental y las listas, y `E`(escalar) tiene que contarlo como tal.
- **La ilegibilidad es de ida.** Ningún requerimiento futuro que necesite leer una respuesta
  —una disputa, una investigación, un pedido judicial— se va a poder cumplir sobre giros ya
  creados. Eso es un costo aceptado, no un descuido: `RF-101` no admite excepción de lector.

---

## 5. Qué es inmutable y qué no

No hace falta invocar a nadie: lo exige el backlog y con ítems que se pueden contar. `RF-55` impide
modificar o eliminar el registro de un acto ya ejecutado; `RF-54` ata cada acto a la identidad de
quien lo ejecutó; `RF-33` obliga a que toda liberación de una retención deje registrado su motivo;
`RF-56` obliga a que la corrección de un giro pagado sea un movimiento **nuevo** y `RF-61` a que
lleve la autorización de un segundo rol; y `RNF-03` conserva todo eso inalterable por el plazo más
largo de los dos reguladores del giro, calculado **por giro y no por política global** (`BR-15`,
`RF-18`).

**Un modelo donde todo se actualiza en el sitio no puede darle eso.** Un `UPDATE` no deja rastro del
valor anterior; una fila de estado que pasa de `retenido` a `liberado` no dice quién, cuándo, ni con
qué a la vista — y `RF-54` pide exactamente esas tres cosas. El problema es más agudo de lo que
parece: se decide mirando un dato que **después cambia**, y el backlog lo asume explícitamente al
obligar a contrastar al receptor contra las listas **vigentes al momento de autorizar el pago**
(`RF-27`) y no contra las de la creación (`RF-26`). Guardar un puntero al dato no basta: hay que
guardar el valor que tenía en el momento de decidir.

**La frontera, en una frase:** *se agrega lo que describe un **acto**; se actualiza lo que describe
un **estado derivado de esos actos**; y cuando los dos difieren, manda el acto.* Eso cierra `D`(a)
desde este lado: existe libro de movimientos, y `giro.estado` es una **proyección** con
`version_estado`, no la verdad.

| Dato | ¿Se actualiza en el sitio o solo se agrega? | Quién lo exige | Decisión |
|---|---|---|---|
| Estado del giro | **Se actualiza** — es proyección | `RF-52`, `RF-53`, `RF-66`, `RNF-06` | Fila mutable en `BD giros` con `version_estado`, derivada de los hechos. Se puede reconstruir entera desde `BD contable` y `BD auditoría`, y **eso es lo que la hace segura de actualizar**: si se pierde o se corrompe, no se perdió nada |
| Código de seguimiento | **Se agrega una vez y no se toca nunca más** | `RF-11`, `RF-94`, `RNF-15` | `INSERT` al crear el giro, sin `UPDATE` concedido. `RF-94` prohíbe reemitirlo aun al emisor que lo perdió, así que **no hay ninguna operación legítima que reescriba esa fila** |
| Respuesta del desafío y su cuenta de intentos (`RF-82`, `RF-83`) | **Mixto, y es deliberado**: el verificador se agrega una vez; el contador se actualiza; la caducidad **destruye** | `RF-68`, `RF-82`, `RF-83`, `RF-103`, `RNF-17` | El verificador es un hecho (`INSERT` único); el contador es estado (`UPDATE`); la caducidad borra verificador y pregunta y deja `estado = caducado`. Es la única entidad del modelo donde borrar es lo correcto, y lo es porque `RF-83` le da plazo propio y ningún regulador la reclama |
| Punto de atención donde se cobra (`RF-63`, `RF-91`) | **Dos campos, uno de cada clase** | `RF-63`, `RF-91`, `RF-105` | `punto_eleccion_id` se agrega al crear y solo cambia con respuesta del emisor —`RF-105` lo exige y cada cambio deja acto en `BD auditoría`—; `punto_pago_id` se escribe una vez, al pagar, y nunca se corrige. Un solo campo mutable habría borrado en silencio la elección de Rosa |
| Estado de la devolución y su plazo (`RF-14`, `RF-89`) | **El estado se actualiza; el asiento que la origina se agrega** | `RF-47`, `RF-32`, `RF-50`, `RF-89`, `RNF-13` | `disponible_hasta` se fija una vez —igual a `giro.prescribe_en`— y no se prorroga; `estado` recorre disponible → retirada. El movimiento contable de la devolución es `INSERT` en `BD contable`, nunca un `UPDATE` que revierta el original |
| Efectivo declarado por el punto al abrir y al cerrar (`RF-76`) | **Se agrega**: dos declaraciones por punto, jornada y turno | `RF-76`, `RF-92`, `RF-95` | `declarado_apertura` y `declarado_cierre` son hechos con autor y momento, y `UNIQUE(punto_id, jornada, turno)` impide redeclarar. `saldo_corriente` **sí** se actualiza —`RF-95` lo descuenta en cada pago— y su cuadre contra los pagos del turno es lo que el `Cierre de Caja Job <EOD>` compara: si `declarado_cierre ≠ declarado_apertura − pagos`, ahí aparece `diferencia_cierre` |
| Declaración de diferencia del receptor (`RF-90`) | **Se agrega. Nunca se corrige ni se retira** | `RF-90`, `RF-59`, `RF-60` | Es la única versión de los hechos que no escribió el punto al que `RF-59` le atribuye la diferencia. Si se pudiera editar, la editaría quien la sufre o quien la causó. Su resolución es otra fila —`correccion_movimiento_id`—, no un cambio de esta |
| Movimiento contable | **Solo se agrega** | `RF-56`, `RF-61`, `RNF-07`, `RNF-03`, `BR-13` | Corregir el monto de un giro pagado es un movimiento **nuevo** con `compensa_movimiento_id` y con la autorización de un segundo rol. `hash_anterior` encadena la partición del giro, de modo que quitar una fila del medio se detecta sin comparar contra una copia |
| Decisión de cumplimiento | **Se agrega** — cada transición es una fila | `RF-29`, `RF-33`, `RF-87`, `RF-30` | Un `UPDATE` de `retenido` a `liberado` no dice quién, ni cuándo, ni con qué a la vista, y `RF-87` obliga a las tres. La liberación lleva `liberado_por_identidad_id`, `liberado_en` y `motivo_liberacion_cif`, y `RF-30` obliga a que esa identidad sea distinta de la que atendió |
| Evidencia sobre la que se decidió | **Se agrega, con el valor y no con el puntero** | `RF-26`, `RF-27`, `RF-28`, `RNF-03` | `nombre_contrastado_cif` y `payload_proveedor` guardan lo que se vio. Un puntero a `Receptor` no reconstruye la decisión: el nombre pudo cambiar y la persona pudo pedir supresión. **Este es el caso donde guardar el valor es la única forma de auditar** |
| Versión de la lista consultada | **Se agrega** | `RF-27`, `RF-97` | `lista`, `version_lista` y `consultada_en` en cada fila de tamizaje. Sin ellos, `RF-97` no sabe qué giros re-tamizar cuando cambia una lista, y ninguna auditoría puede decir contra qué se aprobó lo que se aprobó |
| Cotización emitida | **Se agrega. `RF-06` prohíbe el `UPDATE` por definición** | `RF-05`, `RF-06`, `RF-07`, `RNF-16` | Congelarla es ponerle `giro_id` y `congelada_en`, no reescribir la tasa. `RNF-16` —ninguna entrega difiere de la cifra que el emisor vio— solo es comprobable si esa cifra sigue existiendo tal cual al momento del pago |
| Datos de contacto del emisor | **Se actualiza, y además se borra** | `RF-25`, `RF-75`, `RF-81` | Es el único dato de esta tabla del que `RF-81` dice *sí*. Se actualiza porque un teléfono cambia y los avisos pendientes tienen que llegar; se borra a pedido, y no rompe nada porque la constancia de `RF-98` guarda `telefono_token` y no el número |
| Constancia de aviso enviado (`RF-98`) | **Se agrega** | `RF-98`, `RF-25`, `RF-60` | Prueba que se avisó. Un campo `avisado` en el giro se sobrescribiría con el aviso siguiente y no probaría ninguno de los nueve |
| Segunda autorización (`RF-13`, `RF-61`) | **Se agrega** | `RF-13`, `RF-61`, `RNF-02` | `BR-15` es explícita: *la segunda autorización solo es un control si después se puede probar quién autorizó qué*. Un booleano `autorizado` en el giro no prueba nada y no permite comprobar `RNF-02` |
| Traza de auditoría | **Solo se agrega, y ni el administrador tiene `UPDATE`** | `RF-54`, `RNF-03`, `RNF-04` | `RNF-03` dice *cualquiera sea quien lo pida*: eso es un privilegio que no se concede, no una política que se escribe. Y `RNF-04` la hace crecer con las **lecturas** |
| Solicitud de supresión y su ejecución (`RF-81`) | **Se agrega** | `RF-81`, `RF-54`, `RNF-03` | El acto que demuestra el borrado no puede vivir en lo que se borra, ni poder editarse después. Guarda `alcance`, `campos_borrados`, `objetos_criptoborrados` y `conservado_por_regla` |
| Acumulados del emisor y del receptor | **Se actualizan** — son proyecciones | `RF-09`, `RF-10`, `RF-58`, `RF-93` | Contadores derivados de giros y pagos. Reconstruibles desde `BD giros` y `BD contable`, y por eso seguros de actualizar. El del receptor sobrevive a su supresión porque no contiene ningún atributo personal |

**La pregunta de fondo, respondida:** el giro es **las dos cosas, y el orden entre ellas está
decidido.** Los hechos —movimientos, autorizaciones, tamizajes, pagos, avisos— se agregan y son la
verdad; `giro.estado` es una proyección que existe porque `RF-52`, `RF-53` y `RF-66` le deben a Rosa
una consulta barata, y porque `RNF-11` mide la disponibilidad sobre crear y pagar y no sobre
consultar. **Cuando difieren manda el hecho**, y la proyección se recalcula: es reconstruible entera
desde `BD contable` y `BD auditoría`, y esa reconstruibilidad es lo único que autoriza a tener una
fila mutable en un sistema que `RNF-03` obliga a conservar inalterable. La regla operativa es
estrecha: **ningún servicio decide contra la proyección.** `Payout Service` no consulta
`giro.estado` para autorizar un pago; consulta la ausencia de fila en `Pago` y en `Devolución` —las
dos con `UNIQUE(giro_id)`— y la ausencia de `Retención` vigente. La proyección se lee para mostrar,
nunca para permitir.

**Y hay un tercer lector que no aparece en el material: el punto de atención que estuvo sin
conexión.** Una fila que cambia de estado no se fusiona con la que el punto trae al reconectar —una
de las dos pisa a la otra y la que pierde desaparece sin dejar rastro, que es lo que `RNF-03`
prohíbe—. Por eso el almacén local **no sostiene estados: sostiene hechos**. `hecho_local_pendiente`
es append-only y sube como filas nuevas al `Sync Service`, que las inserta en `BD contable` y
`BD auditoría` con `ocurrido_en` (el reloj del punto) y `registrado_en` (el del centro) **separados**
— dos columnas y no una, porque un pago hecho a las 10:40 en Huanta y registrado a las 17:05 es un
solo hecho con dos momentos, y confundirlos hace irreconstruible el orden.

El precio se paga y se nombra: **dos hechos contradictorios pueden convivir en el registro** —el
pago que subió tarde y la devolución que el `Vencimiento Job` ya asentó—. `RNF-06` no tolera que esa
convivencia sea **observable como estado**, y no lo es: la proyección no se recalcula hasta que la
contradicción se resuelve, y mientras tanto el giro se muestra en un solo estado. `RNF-08` no tolera
que resolverla dependa del operario, y no depende: `UNIQUE(giro_id)` sobre `Pago` y sobre
`Devolución` hace que el segundo `INSERT` **falle en el motor**, y el hecho rechazado no se descarta
sino que se asienta como movimiento de excepción con su contrapartida, que es lo que el
`Cierre de Caja Job <EOD>` cuadra. Nadie tiene que contar nada. Eso materializa `D`(c) en la forma de
las tablas: **la divergencia se detecta por restricción de unicidad, se acota por la caducidad de la
autorización bajada, y se salda como asiento.**

---

## 6. Retención

Dos obligaciones caen sobre el mismo registro y **ninguna anula a la otra**: el cliente puede exigir
que se borren sus datos, y la regulación obliga a conservar la operación durante años — `RF-18` por
el plazo más largo de los **dos** países que tocaron el giro y `RNF-03` calculado por giro y no por
política global. **Las dos tienen ítem, y la asimetría que esta sección registraba ya no existe:**
`RF-81` suprime a pedido los datos personales de quien los entregó, y le pone dos límites que son
exactamente lo que el modelo tiene que poder ejecutar — **de nadie más**, así que hay que saber cuál
de las dos personas de un giro entregó cada dato, cuando el receptor no es cliente y sus datos los
capturó el mostrador; y **salvo los que el registro de actos debe conservar**, que es la frontera de
`RF-55` y `RNF-03`. Un derecho de supresión con excepción nombrada no se cumple con una política: se
cumple si la fila del dato personal se puede borrar sin arrastrar el asiento, y no se cumple si no.
Lo que sigue abierto no es si la obligación existe, ni **quién ejecuta cada plazo** —el
`Vencimiento Job <diario>` que `L` dibuja, contra fechas absolutas y no contra cálculos— ni qué queda
en pie después: las dos cosas se deciden al cierre de esta sección. Lo que sigue abierto es una sola
cifra, y lleva su marca.

La columna de plazo se apoya en el supuesto ya cerrado del backlog —*conservación = el plazo más
largo de los dos reguladores del giro, con un piso de cinco años*—; si `E` lo reabre, esta tabla se
rehace entera.

| Dato | Plazo de conservación | ¿Se borra a pedido del cliente? | Qué lo obliga | Qué se rompe si se borra |
|---|---|---|---|---|
| Registro del giro | El más largo de los dos reguladores, piso de 5 años | No mientras corra el plazo — es la operación, no el dato personal | `RF-18`, `RNF-03`, `BR-15` | El reporte a la autoridad (`RF-17`) queda sin respaldo y el giro deja de ser demostrable ante cualquiera de los dos reguladores |
| Movimiento contable | El del giro que lo originó | No — `RF-81` lo excluye por vía de `RF-55` | `RF-55`, `RNF-03`, `RNF-07` | La prueba de que la suma cuadra: sin asiento no se demuestra `RNF-07`, y el pasivo de `BR-01` queda sin contrapartida |
| Imagen del documento de identidad (`RF-80`) | El del giro. Es el dato voluminoso y el primer candidato a archivo frío al vencer la prescripción | **Sí, a pedido** —es dato personal de quien lo entregó— y **también al vencer `conservar_hasta`**, por cripto-borrado de la llave por giro. Nunca se anonimiza: anonimizar sería reescribir, y el hash quedaría sin verificar | `RF-80`, `RF-18`, `RNF-01`, `RF-81` | La evidencia de que la identificación de `RF-01` y `RF-85` ocurrió. Queda la afirmación de que se verificó, sin nada detrás |
| Pregunta y respuesta del desafío | Caduca con el giro (`RF-83`) — más corto que todo lo demás de esta tabla | Se extingue sola; borrarla antes deja a `RF-69` sin salida | `RF-83`, `RNF-17` | Nada del asiento. Pero si caduca antes de que el receptor llegue, el documento no vigente deja de poder cobrarse y `RF-86` vuelve a cerrar la puerta que `RF-69` abrió |
| Resultado de tamizaje | El del giro | No — sostiene la decisión, no la identidad | `RF-26`, `RF-27`, `RNF-03` | La defensa de por qué se retuvo o se dejó pasar. `RF-27` decide contra listas **vigentes al momento del pago**: sin el valor guardado, esa decisión no se puede reconstruir |
| Caso de cumplimiento | El del giro, con su plazo de retención propio (`RF-31`) vencido adentro | No | `RF-29`, `RF-33`, `RF-87`, `RNF-03` | El motivo de la liberación que `RF-87` obliga a registrar, y con él la trazabilidad de quién dejó salir el dinero |
| Declaración de diferencia del receptor (`RF-90`) | El del giro | No — es un acto, y los actos no se borran | `RF-90`, `RF-59`, `RF-55` | La única versión de los hechos que no escribió el punto al que `RF-59` le atribuye la diferencia |
| Traza de auditoría | El del giro, inalterable (`RNF-03`) | No — es la excepción que `RF-81` nombra | `RF-54`, `RF-55`, `RNF-03`, `RNF-04` | El no repudio entero, y también la prueba de que la supresión pedida se ejecutó |
| Solicitud de supresión y su alcance (`RF-81`) | El del registro de actos | No — es el acto que demuestra el borrado | `RF-81`, `RF-54`, `RF-55` | La capacidad de demostrarle a quien lo pidió qué se borró, y de defender ante el regulador por qué algo no |
| Datos de contacto | Mientras el giro esté vivo y queden avisos pendientes | **Sí — es el caso claro de `RF-81`**, y el que prueba si el modelo sabe borrar sin romper nada | `RF-25`, `RF-41`, `RF-60`, `RF-75`, `RF-81` | Los avisos pendientes se quedan sin destino: la devolución disponible (`RF-14`), el aviso previo a la prescripción (`RF-51`) y el de giro cobrado (`RF-65`). El asiento no se toca |
| Cotizaciones no ejecutadas | **Hasta `vence_en`, y no más.** Es el plazo más corto del sistema junto con el de la clave de idempotencia | Sí, si quedaron atadas a una persona | `RF-07` | Nada del registro contable — salvo que la cotización sea la que `RF-06` congeló en un giro creado, y entonces ya no es «no ejecutada»: tiene `giro_id` y hereda el plazo del giro |
| Código de seguimiento (`codigo_hmac`) | El del giro. **No se borra a pedido y tampoco hace falta**: no es un dato personal, es un verificador sin sujeto | No | `RF-11`, `RF-94`, `RNF-15` | La capacidad de demostrar que el pago se autorizó contra el código correcto. Y borrarlo antes del cierre haría incobrable el giro, porque `RF-94` prohíbe reemitirlo |
| Constancia de aviso enviado (`RF-98`) | **Hasta que el giro cierra y se saldan sus plazos.** Partición propia, la más corta de `BD auditoría` | No mientras corra; el **contacto** sí se borra, la constancia no | `RF-98`, `RF-25`, `RF-60` | La prueba de haber avisado, que es lo que sostiene a SendIt cuando Elena dice que nadie la llamó. Es el ejemplo de que la retención se decide por dato: un SMS no merece los cinco años del asiento, y ponerlo ahí sería pagar conservación regulatoria por un mensaje |
| Evidencia de identificación de un emisor que no llegó a crear un giro | **Se descarta.** `RF-99` lo ordena expresamente | No aplica: se descarta sola, sin que nadie lo pida | `RF-99`, `RNF-01` | Nada. Es el único borrado del modelo que **no** es a pedido y **no** tiene excepción: sin giro no hay operación que conservar, y guardar el binario sería acumular datos de identidad sin requerimiento que los sostenga |
| Clave de idempotencia | **TTL corto**, medido en horas. La única entidad que muere sola sin dejar rastro | No aplica: caduca antes de que nadie pueda pedirlo | `RF-42`, `RF-43`, `RF-44` | Nada, si el TTL supera la ventana de reintento realista de un mostrador. Si se acorta de más, un reintento tardío crea un segundo giro — y ese es el defecto que `RF-43` nombra |
| Reporte a la autoridad y su acuse (`RF-17`) | El del giro, y por el plazo del **regulador que lo recibió**, que puede ser más largo que el otro | No — no es dato del cliente, es constancia frente a la autoridad | `RF-17`, `RF-22`, `RF-18`, `RNF-03` | La prueba de haber reportado. Un reporte sin acuse conservado equivale a no haber reportado el día que la autoridad pregunte |
| Caja del punto y sus declaraciones (`RF-76`) | El del giro más largo cuyos pagos tocaron esa jornada — en la práctica, el plazo de conservación del corredor | No — es un acto del operario, no un dato personal del cliente | `RF-76`, `RF-95`, `RNF-05` | El cuadre del `Cierre de Caja Job <EOD>`, que es donde aparece el doble pago si apareció. Sin las dos declaraciones no hay contra qué cuadrar los pagos del turno |
| Acumulado de cobros del receptor (`RF-58`) | La ventana vigente, más el plazo del último giro que contó | **No, y no hace falta**: sobrevive a la supresión porque no contiene ningún atributo personal, solo `receptor_ref` y un número | `RF-58`, `RF-93`, `RF-81` | La capacidad de retener a quien superó su acumulado. Es la fila que muestra por qué el seudónimo es una decisión de modelo: con el nombre adentro, `RF-81` habría tenido que elegir entre el derecho de Elena y `RF-93` |
| Versión de jurisdicción que el giro obedeció (`version_regla_jurisdiccion`) | El del giro. **La versión vieja se conserva aunque el regulador ya la haya reemplazado** | No | `RF-15`, `RF-18`, `RF-31`, `RNF-03` | La posibilidad de defender por qué se conservó cinco años y no siete, o por qué la retención duró 72 horas. Sin la versión congelada, el plazo de un giro de 2026 se recalcularía con la norma de 2031 |

**Lo que esta tabla decide sin que lo parezca.** Si el nombre y el documento de Rosa viven **dentro**
de la fila del giro, borrar a Rosa destruye el asiento contable y con él la posibilidad de demostrar
que la suma cuadra, que es el invariante de `RNF-07`. Si viven **detrás de una referencia**, se
puede borrar la identidad y dejar en pie la operación. Es decir: **la convivencia entre el derecho
de supresión y la obligación de conservación se resuelve en el diseño de las tablas, y solo ahí.**
Ninguna política escrita en un documento la resuelve si el modelo no la permite — y `RF-81` ya no
deja tratarla como hipótesis: la excepción que nombra («salvo los que el registro de actos debe
conservar») es una frontera entre dos tablas, no una cláusula.

**Y la pregunta que quedaba abierta se cierra acá, porque es de este paso: sí, el receptor entra en
esa referencia.** Sus datos los entregó él en el mostrador, así que `RF-81` lo alcanza igual que al
emisor, y la columna `declarante` de `BD identidad` es lo que permite ejecutar el *«y de nadie
más»*: sobre un mismo giro hay dos filas de persona con dos declarantes distintos, y una supresión
pedida por Rosa no toca la de Elena. El contador de cobros de `RF-58` sobrevive porque **no está en
`BD identidad`**: vive en `BD cumplimiento`, con `receptor_ref` y un número, sin un solo atributo
personal. Borrar a Elena de `BD identidad` deja el contador intacto y `RF-93` sigue pudiendo retener
el giro de quien superó su acumulado — sobre un seudónimo que ya no resuelve a ninguna persona
legible. Esa es toda la diferencia entre un modelo que puede cumplir `RF-81` y uno que tiene que
elegir cuál de los dos ítems incumple.

**El único plazo que este paso no puede fijar solo:**
`[CLARIFY: la ventana de vida de la clave de idempotencia (BD intentos). El backlog no la da —RNF-09
acota la operación de ventanilla y RNF-10 la disponibilidad, ninguno la vida de un intento— y
depende de cuánto tarda un mostrador en reintentar tras un corte. La destraba una cifra de D(b) o
una medición de campo del tiempo entre corte y reintento; mientras tanto el modelo la trata como
columna `expira_en` y no como constante, así que cambiarla no rehace ninguna tabla.]`

### El plazo se calcula por giro: qué campo lo lleva

`RNF-03` exige conservar *«calculado por giro y no por política global»* y `RF-18` fija el criterio:
el plazo más largo de los **dos** países que tocaron el giro. Eso no se cumple con una constante en
un archivo de configuración —una constante es exactamente una política global— y tampoco con una
consulta a la tabla de jurisdicciones al momento de purgar, porque para entonces la norma puede haber
cambiado. Se cumple con **tres fechas absolutas, congeladas al crear el giro**, y con la versión de
la norma que las produjo:

| Campo | Dónde vive | Cómo se calcula | Qué ítem lo fija |
|---|---|---|---|
| `giro.conservar_hasta` | `Giro`, en `BD giros`; se copia a `traza.conservar_hasta` y a la partición del asiento | `creado_en + MAX(origen.plazo_conservacion_anios, destino.plazo_conservacion_anios)`, con piso de 5 años | `RF-18` — **el más largo** de los dos · `RNF-03` |
| `retencion.vence_en` | `Retención`, en `BD cumplimiento` | `abierto_en + MIN_estricto(origen.plazo_retencion_horas, destino.plazo_retencion_horas)`, piso de 72 h, y más corto para la homonimia que para la coincidencia exacta | `RF-31` — **el más estricto** · `RF-78` |
| `giro.prescribe_en` | `Giro` y `Prescripción`, en `BD giros` | `creado_en + origen.plazo_prescripcion_meses`, 12 meses a falta de norma expresa | `RF-49`, `RF-50` · `BR-14` — el del **regulador de origen**, y solo ese |

**Tres reglas distintas sobre los mismos dos reguladores, y ninguna se puede derivar de las otras.**
Guardarlas como plazo relativo —«cinco años», «72 horas»— y resolverlas al vencer haría que una norma
nueva reescribiera retroactivamente el plazo de giros ya creados; guardarlas como fecha absoluta con
`version_regla_jurisdiccion` al lado las vuelve defendibles una por una. Ese es el campo que lleva la
retención por jurisdicción, y es una columna del giro y no una línea de configuración.

### Qué pasa al vencer, y quién lo ejecuta

Un plazo que nadie hace vencer no vence. El ejecutor es uno solo y ya está dibujado en `L`: el
`Vencimiento Job <diario>`, que barre por fecha absoluta y no por cálculo. Los seis plazos y qué hace
cada uno:

| Plazo | Qué ejecuta el vencimiento | Ítem |
|---|---|---|
| Retención sin liberar | Devuelve al emisor y avisa al receptor por su canal | `RF-31`, `RF-32` |
| Giro no cobrado | Lo deja no pagable, pone el monto a disposición del emisor, y avisa antes | `RF-49`, `RF-50`, `RF-51` |
| Respuesta del desafío | **Borra** `verificador` y `pregunta_cif`; deja `estado = caducado` y su traza | `RF-83` |
| Devolución no retirada | Se mantiene disponible hasta `giro.prescribe_en`, no antes | `RF-89` |
| Supresión pedida | Borra los campos del alcance y **destruye las llaves** de los objetos, dejando en pie el asiento y la traza | `RF-81` |
| Conservación del giro (`conservar_hasta`) | **Cripto-borrado, no anonimización.** Se destruye la llave de corredor de las columnas cifradas y la llave por giro de los objetos; el asiento y la traza quedan enteros con `persona_ref` que ya no resuelve | `RF-18`, `RNF-03` |

**Por qué cripto-borrado y no anonimizar.** Anonimizar es reescribir filas —un `UPDATE` sobre
`BD auditoría`, que `RNF-03` prohíbe *cualquiera sea quien lo pida*—. Destruir la llave deja la fila
byte por byte como estaba y la vuelve ilegible, así que el encadenamiento `hash_anterior` sigue
verificando y la traza sigue demostrando que el acto ocurrió. **Es la única forma de borrar que no
rompe lo inmutable**, y es la misma primitiva que ejecuta `RF-81` años antes: la diferencia entre las
dos no es el mecanismo, es el alcance y quién lo pide.

`RF-81` es el único de los seis que tiene que **dejar en pie** una parte del registro mientras borra
la otra, y puede hacerlo por una sola razón: la parte que borra y la parte que conserva están en
tablas distintas, en bases distintas, con llaves distintas. Si vivieran en la misma fila, ninguna
política escrita lo salvaría.

---

## Qué invalida este modelo

| Si cambia… | Se rehace |
|---|---|
| `D`(a) verdad del dinero | Movimiento contable, estado del giro, y la sección 5 completa |
| `D`(b) idempotencia | La entidad que persiste la clave de intento y su ventana de vida |
| `D`(c) frontera entre el centro y el punto de atención | Los estados del giro, el estado que el punto sostiene sin conexión, y qué se guarda de lo que informa al reconectar |
| `D`(d) tipo de cambio | Tasa aplicada, su vencimiento, y la cuenta de diferencia de cambio |
| `D`(e) momento del tamizaje | Verificación de identidad, caso de cumplimiento, y el orden de los estados |
| `D`(f) dónde vive y quién compara la respuesta del desafío | La entidad **Desafío**, su llave, su control de acceso y su fila en la tabla de datos personales; y qué del secreto sostiene el punto de atención sin conexión |
| Los años de retención en `E` | La sección 6 y la elección de motor de las entidades voluminosas |

---

## Nota sobre las dos clases de iteración

[`ITERACIONES.md`](../ITERACIONES.md) registra dos cosas distintas y no se fusionan: la **iteración
del diseño** —el mismo diagrama de componentes dibujado otra vez y más abierto, que es la que exige
el enunciado ([ejemplo de clase](../../docs/EJEMPLO-CLASE-TOP-DOWN.md))— y la **iteración del EVAL**,
que cambia una decisión del backlog. Este paso las alimenta a las dos: las bases de datos que aquí
se decidan son las `BD` que el diagrama dibuja, y un ítem nuevo del backlog puede agregar una
entidad que nadie había nombrado.
