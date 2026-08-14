# Historial de corridas

Una fila por corrida ejecutada, en orden cronológico. **Este archivo solo se agrega, nunca se
reescribe**: una fila que se corrige a posteriori deja de ser un registro y pasa a ser una
interpretación.

Responde la pregunta que ningún reporte individual responde, porque cada corrida sobrescribe
`Spec/Eval-Report.MD`: si los requerimientos están mejorando, y a costa de qué dimensión.

| Fecha | Corrida | ReqFunc | Rúbrica | Instr. | D1 | D2 | D3 | D4 | D5 | D6 | Global | Veredicto |
|---|---|---|---|:---:|---:|---:|---:|---:|---:|---:|---:|:---:|

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
