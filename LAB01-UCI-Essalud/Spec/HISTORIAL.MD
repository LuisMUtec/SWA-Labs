# Historial de corridas

Una fila por corrida ejecutada, en orden cronológico. **Este archivo solo se agrega, nunca se
reescribe**: una fila que se corrige a posteriori deja de ser un registro y pasa a ser una
interpretación.

Responde la pregunta que ningún reporte individual responde, porque cada corrida sobrescribe
`Spec/Eval-Report.MD`: si los requerimientos están mejorando, y a costa de qué dimensión.

| Fecha | Corrida | ReqFunc | Rúbrica | Instr. | D1 | D2 | D3 | D4 | D5 | D6 | Global | Veredicto |
|---|---|---|---|:---:|---:|---:|---:|---:|---:|---:|---:|:---:|
| 2026-08-13 | 2026-08-13-additional-v2 | `a1df636` | `8af38e9` | — | 61,0 | 66,7 | 54,8 | 40,0 | 40,0 | 95,0 | 58,7 | FAILED |
| 2026-08-14 | 2026-08-14-iteracion-2 | `34877c7` | `b492237` | — | 42,0 | 83,3 | 66,1 | 100,0 | 100,0 | 95,0 | 71,4 | FAILED |
| 2026-08-14 | 2026-08-14-iteracion-3 | `f50cf90` | `b492237` | — | 29,0 | 50,0 | 93,8 | 90,0 | 60,0 | 80,0 | 59,0 | FAILED |
| 2026-08-14 | 2026-08-14-iteracion-4 | `f4cc4cf` | `b492237` | — | 48,0 | 50,0 | 97,5 | 80,0 | 60,0 | 85,0 | 64,7 | FAILED |

## Cómo se lee

- **ReqFunc** y **Rúbrica** son los SHA cortos de lo evaluado y de la vara con que se midió. Dos filas
  con distinta rúbrica **no son comparables**: cambió la unidad, no solo el resultado. Cuando la
  rúbrica cambia, la fila siguiente se separa con un `---` y una línea que diga qué cambió.
- **Instr.** marca `⚠` cuando la comprobación de conformidad corrigió algún agente de persona. Esa
  corrida midió con un instrumento distinto del de la fila anterior, y su delta no es atribuible solo
  a `ReqFunc.MD`.
- **D1 a D6** son las dimensiones de `Spec/Eval-Spec.MD`, cada una de 0 a 100, antes de aplicar el
  peso. Se registran sin ponderar para que una caída se pueda atribuir a su dimensión.
- **Global** es el porcentaje ponderado, con un decimal.

Una fila se agrega al cerrar la corrida, con los mismos valores que `corrida.json` deja en
`resultado`. La evidencia que los sostiene no llega aquí: vive en `Spec/corridas/<id>/`.

Cada corrida mide una vez, así que una fila es una medición completa. Comparar dos filas es comparar
dos estados de `ReqFunc.MD` —siempre que la columna Rúbrica no haya cambiado entre ellas—.
