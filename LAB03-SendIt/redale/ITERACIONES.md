# Iteraciones del diseño

El enunciado exige mostrar claramente las iteraciones. Una fila por pasada; el detalle de
cada una queda en el paso que tocó.

| # | Fecha | Pasos tocados | Qué la forzó | Qué cambió | EVAL |
|---|---|---|---|---|---|
| 01 | — | — | — | — | — |

## Cómo se registra una iteración

Una iteración es una pasada por R.E.D.A.L.E. que **cambia una decisión**, no una corrección
de redacción. Se abre cuando algo obliga a volver atrás: el EVAL quedó bajo el gate, una
estimación no cierra contra los requerimientos, el modelo de datos no soporta un flujo, o
una persona modelo no puede completar su día.

Para cada iteración, registrar:

1. **Qué la forzó** — el hallazgo concreto, con su origen (iteración del EVAL, veredicto de
   una persona, contradicción entre dos pasos).
2. **Qué paso se corrigió** y qué decisión reemplazó a cuál.
3. **La propagación** — qué pasos aguas abajo quedaron afirmando lo viejo. Este es el punto:
   corregir `R` sin volver a mirar `E`, `D`, `A` y `L` deja el diseño incoherente, y el
   defecto aparece dos iteraciones después disfrazado de otra cosa.
4. **El puntaje del EVAL** de esa ronda, si se corrió.
