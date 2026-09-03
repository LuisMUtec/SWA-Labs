# Correcciones pendientes — ronda 13

Derivadas de la [iteración 12](iterations/2026-08-27-12.md), que cerró en **7,34 / 10**. El backlog
vigente es `redale/R-requerimientos/backlog.md` con **157 RF + 18 RNF = 175 ítems**, congelado en
`ed909ed`.

## Aritmética del gate

| Escenario | D1 | D2 | D3 | D4 | Total |
|---|---|---|---|---|---|
| Hoy (ronda 12) | 1,5 | 3,0 | 1,5 | 1,34 | **7,34** |
| Con los bloques 1–3 | 2,5 | 3,0 | 2,0 | ≈1,4 | **≈ 8,9** |
| Con los bloques 1–4 | 3,0 | 3,0 | 2,0 | ≈1,4 | **≈ 9,4** |
| Con los ocho | 3,0 | 3,0 | 2,0 | ≈1,7 | **≈ 9,7** |

**Lo que separa del gate son cuatro títulos.** Los bloques 1 a 4 no tocan la forma del backlog: son
cuatro decisiones que faltan, una por cada reserva de persona más el medio punto de D3 — y el bloque
1 paga en las dos dimensiones a la vez.

---

## Bloque 1 — el motivo de la retención · +0,5 D3 y −0,5 D1

El hallazgo que ordena a los demás, y **el único que cuesta en dos dimensiones**.

`RF-29` crea la retención. `RF-40` omite al operario **el motivo de un rechazo**. `RF-152` obliga a
que la acción ofrecible **de un rechazo** no permita deducirlo. `RF-150` crea la acción ofrecible del
giro **retenido** y ningún título le pone la misma restricción.

- **Escribir la omisión que falta:** quién no puede leer el motivo de una retención, con la forma con
  que `RF-40` lo decidió para el rechazo.
- **Escribir la restricción que falta:** que la acción ofrecible de un giro retenido tampoco permita
  deducir el motivo, con la forma de `RF-152`.
- **Corregir `L:855-859`**, que apoya en `RF-40` una afirmación sobre reportes a la autoridad que
  `RF-40` no sostiene.

> **La lección de esta ronda.** El defecto **no lo introdujo** partir `RF-39` en tres: estaba tapado
> dentro de un título no atómico desde que `RF-40` se escribió, y el partido lo hizo visible. Es la
> primera vez en la serie que una corrección de forma **descubre** una falla de fondo en vez de
> producirla, y vale anotarlo porque contradice el patrón de las cuatro rondas anteriores.

## Bloque 2 — el estado *no pagable* de Rosa · −0,5 D1 y dos hallazgos de D4

La reserva de Rosa, y el único *estado sin terminador* que la ronda 12 abrió.

`RF-149` deja no pagable el giro sin constancia de que el código llegó. `RF-67` avisa el paso a
*retenido*, y no pagable no es retenido. `RF-53` solo distingue disponible de todavía-no-disponible.
`RF-130` le muestra la acción **al operario**.

- **Un título que se lo diga a Rosa por su canal**, como `RF-67` hace con la retención.
- **Un terminador:** qué pasa cuando la constancia llega tarde, y cuánto dura el estado si no llega
  nunca. Hoy el único reloj es la prescripción de `RF-49`/`RF-50`, a doce meses.
- **Y el gemelo que le falta a `RF-89`:** `RF-155` paga la reposición en el punto donde cobró y nada
  la prescribe — es la devolución sin su `RF-137`.

## Bloque 3 — el techo de la espera por lista externa · −0,5 D1

La reserva (b) de Kevin, y **el precio que T1 prometió acotar**.

`RNF-09` fija 3 minutos para lo que depende del sistema y 10 para el segundo rol, y remite la espera
por lista externa a `RNF-11` — que es `99,9 % mensual`, una disponibilidad, no un plazo. Como
`RF-26`, `RF-119` y `RF-167` corren el contraste **antes** de aceptar el efectivo, es la única espera
que ocurre con la persona delante y la cola detrás.

- **Darle a esa espera un techo de tiempo propio**, dentro de `RNF-09` y sin remitir a `RNF-11`.
- **Y decir qué pasa al vencerlo**, que es lo que lo vuelve negable.

## Bloque 4 — la verificación del código antes del viaje · −0,5 D1

La reserva de Elena. Ella **no** pide que el sistema le mande el código —*«mandármelo lo dejaría de
ser secreto»*—: pide poder saber, antes de gastar el pasaje, si el que le dictaron sirve.

- **Un título que le deje comprobar el código sin que el sistema se lo entregue ni se lo confirme a
  nadie más.** `RF-128` le da estado, no código.
- **Y el otro lado de la misma dependencia:** `RF-105`, `RF-111` y `RF-164` dejan su cobro a merced
  de que Rosa conteste, sin ítem que la deje pedir u objetar el cambio de punto.

## Bloque 5 — las dos reparaciones en la altitud equivocada · ≈ +0,17 D4

- **`D:817`** afirma que el secreto *«entra y sale por un dispositivo orientado al cliente»*, contra
  `RF-11`. La ronda 12 corrigió `L:548`, donde se vio el síntoma, y no `D`, que decide la frontera.
  **Es el tercer punto del bloque 1 de la ronda 12, literalmente sin aplicar.**
- **La deriva de `RF-108` a `RF-156`.** `A:118`, `E-estimar:192` y `E-estimar:510` repusieron el
  aviso y la devolución por cambio de lista apuntándolos al número siguiente que quedó libre, que
  dice otra cosa. Es exactamente lo que la sección «Identificadores retirados» existe para impedir.

## Bloque 6 — las dos cifras sin productor que sostienen componentes ya dibujados · ≈ +0,06 D4

- **El plazo para reportar a una autoridad.** `RF-17` y `RF-139` dicen qué y contra qué umbral;
  ninguno dice dentro de cuánto. `L:877` se niega a dibujar el job, que es la conducta correcta.
- **La vigencia de las listas de `RF-167`.** `D:829` inventa 24 h, y `E-estimar:186` y
  `E-escalar:198` dimensionan la cola de cumplimiento sobre esa invención.

## Bloque 7 — forma: un duplicado, un comodín, tres no atómicos, ocho ambiguos · ≈ +0,37 D4

- **Retirar `RF-165`** (⊂ `RF-93`: dar de baja lo anterior a la ventana está contenido en «en la
  ventana»). Sin reusar el número.
- **Reescribir `RF-162`**, el único comodín vivo: nombra una postura y no un hecho.
- **Partir `RF-29`** (ni pagable ni cancelable), **`RF-86`** (regla y excepción) y **`RF-116`**
  (informar el plazo y ponerle piso).
- **Marcar con `[CLARIFY: …]`** los ocho ambiguos: `RNF-09`, `RF-141`, `RF-149`, `RF-152`, `RF-153`,
  `RF-166`, `RF-167`, `RF-169`.
- **Los dos huérfanos:** `RF-104` y `RF-143` declaran persona **Elena** y su destinatario es el
  **agente**.

## Bloque 8 — frenar la dilución de D2 · preserva 3,0 D2

**De los 24 ítems que la ronda 12 agregó, 11 sobreviven intactos a una transferencia doméstica.** La
fracción específica cayó de 61,3 % a **54,9 %**, segunda ronda consecutiva.

**Con una ronda más al mismo ritmo cae por debajo de la mitad y D2 deja de valer 3 sin que nadie haya
empeorado un ítem.** No es una corrección: es una restricción sobre cómo se escriben las de arriba.
Cada título nuevo tiene que morir en una transferencia doméstica, o tener una razón escrita de por
qué no.

---

## Además, y no es del backlog

- **`docs/ENTREGA.md` sigue en 118 ítems**, 32 endpoints, 30 entidades, trazabilidad 118/118 y la
  serie del EVAL hasta la iteración 07 — y **ejecuta `RF-12` como ítem vivo** en al menos siete
  lugares. Hoy son **175 ítems** y doce corridas.
- **`redale/ITERACIONES.md`** declara «Total: 155 de 155» y no tiene fila para la ronda 12.
- **`L:556-564` afirma 155 ítems mientras `L:576-580` afirma 175**, en el mismo archivo.
- **`docs/DECISIONES.md:409`** cita `RF-110`, retirado.
- **Diecinueve de los veinticuatro ítems nuevos no tienen ruta ni capacidad en `D`.**
