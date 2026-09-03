#!/usr/bin/env bash
# Convierte docs/RESUMEN.md en un PDF de una lamina por hoja, con los diagramas
# renderizados.  uso: scripts/resumen-a-pdf.sh
# Requiere: pandoc y Google Chrome. Comparte la cache de mermaid con
# scripts/entrega-a-pdf.sh, asi que la segunda corrida no necesita red.
set -euo pipefail
cd "$(dirname "$0")/.."
MD=docs/RESUMEN.md
HTML=docs/RESUMEN.html
PDF=docs/RESUMEN.pdf
MERMAID=scripts/mermaid.min.js
MERMAID_URL=https://cdn.jsdelivr.net/npm/mermaid@11/dist/mermaid.min.js
CHROME="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

[ -f "$MD" ] || { echo "falta $MD"; exit 1; }

if [ ! -f "$MERMAID" ]; then
  echo "bajando mermaid a $MERMAID (una sola vez)..."
  curl -fsSL "$MERMAID_URL" -o "$MERMAID" || {
    echo "no se pudo bajar mermaid. Con red: curl -fsSL $MERMAID_URL -o $MERMAID"; exit 1; }
fi

# 1 · cuerpo desde markdown, con los bloques mermaid marcados para el renderer
pandoc "$MD" -f gfm -t html --no-highlight \
  | perl -0pe 's{<pre class="mermaid"><code>(.*?)</code></pre>}{<pre class="mermaid">$1</pre>}gs' \
  | perl -0pe 's{<pre><code class="language-mermaid">(.*?)</code></pre>}{<pre class="mermaid">$1</pre>}gs' \
  | perl -pe 's/&quot;/"/g if /<pre class="mermaid">/ .. /<\/pre>/' > /tmp/_resumen_cuerpo.html

# 2 · documento completo, con estilo de lamina y mermaid embebido
{
cat <<'CSS'
<!doctype html><html lang="es"><head><meta charset="utf-8">
<title>SendIt — Resumen</title>
<style>
@page { size: A4 portrait; margin: 13mm 14mm; }
@page apaisada { size: A4 landscape; margin: 11mm 12mm; }
* { box-sizing: border-box; }
html, body { margin:0; padding:0; }
body {
  font: 8.9pt/1.42 system-ui, -apple-system, "Segoe UI", Helvetica, Arial, sans-serif;
  color:#0b0b0b; -webkit-print-color-adjust: exact; print-color-adjust: exact;
}
body { counter-reset: hoja; }

/* --- la lamina --------------------------------------------------------- */
.hoja { position:relative; min-height:268mm; padding-bottom:9mm; page-break-after:always; break-after:page; counter-increment: hoja; }
.hoja.ultima { page-break-after:auto; break-after:auto; }
.hoja::after { content: counter(hoja); position:absolute; bottom:1mm; right:0; font-size:8pt; color:#898781; font-variant-numeric:tabular-nums; }
.hoja.portada { counter-increment: none; }
.hoja.portada::after { content:none; }
.hoja.apaisada { page: apaisada; min-height:184mm; }

/* --- titulos ----------------------------------------------------------- */
h1 { font-size:19pt; font-weight:650; letter-spacing:-.01em; margin:0 0 .55em; padding-bottom:.28em; border-bottom:2px solid #0b0b0b; }
h2 { font-size:11.6pt; font-weight:650; margin:1.05em 0 .35em; color:#0b0b0b; page-break-after:avoid; }
h3 { font-size:9.2pt; font-weight:650; margin:.9em 0 .3em; color:#52514e; text-transform:uppercase; letter-spacing:.055em; page-break-after:avoid; }
p { margin:.42em 0; }
strong { font-weight:650; }
em { color:#52514e; }
a { color:#0b0b0b; text-decoration:none; }
code { font-family:"SF Mono",Menlo,Consolas,monospace; font-size:.87em; background:#f4f4f1; padding:.5px 3px; border-radius:2px; }

/* --- tablas ------------------------------------------------------------ */
table { border-collapse:collapse; width:100%; margin:.5em 0; font-size:7.9pt; page-break-inside:avoid; }
th, td { border:none; border-bottom:1px solid #e1e0d9; padding:3.6px 8px 3.6px 0; text-align:left; vertical-align:top; }
th { font-weight:650; font-size:7.6pt; text-transform:uppercase; letter-spacing:.05em; color:#52514e; border-bottom:1px solid #c3c2b7; }
tbody tr:last-child td { border-bottom:1px solid #c3c2b7; }
td code { font-size:.9em; white-space:nowrap; }
.tabla-mini table { font-size:6.8pt; }
.tabla-mini td, .tabla-mini th { padding:3px 3px 3px 0; font-variant-numeric:tabular-nums; }

/* --- portada ----------------------------------------------------------- */
.portada { padding-top:26mm; }
.portada h1 { font-size:52pt; font-weight:700; letter-spacing:-.03em; border:none; margin:0; padding:0; }
.portada h2 { font-size:15pt; font-weight:400; color:#52514e; margin:.15em 0 0; letter-spacing:-.01em; }
.marca { font-size:8.4pt; color:#898781; line-height:1.5; margin-bottom:14mm; }
.autores { font-size:10.5pt; color:#0b0b0b; margin:9mm 0 0; font-weight:550; }
.lede { font-size:10.4pt; line-height:1.55; color:#0b0b0b; margin:9mm 0 0; padding-left:11px; border-left:3px solid #2a78d6; }
.indice { margin-top:12mm; }
.indice table { font-size:8.6pt; }
.indice td:first-child { width:18px; color:#898781; font-variant-numeric:tabular-nums; }
.indice td:last-child { color:#898781; text-align:right; }
.indice thead { display:none; }
.pie { position:absolute; bottom:0; left:0; right:0; font-size:7.8pt; color:#898781; border-top:1px solid #e1e0d9; padding-top:5px; }

/* --- cifras (stat tiles) ----------------------------------------------- */
.cifras { display:flex; flex-wrap:wrap; gap:0; margin:11mm 0 0; }
.cifras .cifra { flex:1 1 33%; min-width:33%; padding:9px 12px 9px 0; }
.cifras.tres .cifra { flex:1 1 33%; }
.cifra b { display:block; font-size:24pt; font-weight:650; letter-spacing:-.025em; line-height:1.05; }
.cifra span { display:block; font-size:7.8pt; color:#52514e; line-height:1.35; margin-top:3px; }

/* --- hero -------------------------------------------------------------- */
.hero { display:flex; gap:16px; align-items:flex-start; margin:.5em 0 1em; }
.hero-num { font-size:40pt; font-weight:680; letter-spacing:-.035em; line-height:1; color:#2a78d6; white-space:nowrap; }
.hero-num span { font-size:14pt; font-weight:500; color:#898781; letter-spacing:0; margin-left:4px; }
.hero-txt { font-size:9.4pt; }
.hero-txt p { margin:0; }

/* --- bloques auxiliares ------------------------------------------------ */
.nota { margin:.75em 0; padding:6px 0 6px 11px; border-left:3px solid #c3c2b7; font-size:8.4pt; page-break-inside:avoid; }
.nota.destacada { border-left-color:#2a78d6; }
.nota p:first-child { margin-top:0; } .nota p:last-child { margin-bottom:0; }
.nota h2 { margin-top:.1em; }
.dos-col { display:flex; gap:22px; margin:.4em 0; }
.dos-col > div { flex:1 1 50%; min-width:0; }
.dos-col table { font-size:7.4pt; }
blockquote { margin:.7em 0; padding:6px 0 6px 11px; border-left:3px solid #eb6834; background:none; font-size:8.4pt; page-break-inside:avoid; }
blockquote p { margin:.2em 0; }
pre { background:#f7f7f5; border:none; border-left:3px solid #e1e0d9; border-radius:0; padding:8px 10px; font-size:7.5pt; line-height:1.42; page-break-inside:avoid; overflow:hidden; }
pre code { background:none; padding:0; }
ol, ul { margin:.45em 0; padding-left:1.15em; }
li { margin:.22em 0; }

/* --- figuras y diagramas ----------------------------------------------- */
.fig { margin:.25em 0 .85em; page-break-inside:avoid; }
.fig svg { display:block; width:100%; height:auto; }
.mermaid { text-align:center; page-break-inside:avoid; margin:.6em 0; }
.mermaid svg { max-width:100%; height:auto; }

/* --- tramos de escalamiento -------------------------------------------- */
.tramos { display:flex; gap:6px; margin:.7em 0 1em; }
.tramo { flex:1 1 20%; border-top:3px solid #e1e0d9; padding:6px 6px 0 0; }
.tramo.activo { border-top-color:#2a78d6; }
.tramo b { display:block; font-size:10pt; font-weight:650; letter-spacing:-.01em; }
.tramo span { display:block; font-size:7.4pt; color:#52514e; margin-top:2px; line-height:1.3; }
.tramo em { display:block; font-size:7.4pt; color:#898781; margin-top:4px; line-height:1.3; }
.tramo.activo em { color:#2a78d6; font-style:normal; font-weight:600; }
.inventario { margin-top:.8em; padding-top:7px; border-top:1px solid #c3c2b7; font-size:8.6pt; color:#52514e; }
</style></head><body>
CSS
cat /tmp/_resumen_cuerpo.html
echo '<script>'; cat "$MERMAID"; echo '</script>'
cat <<'JS'
<script>
mermaid.initialize({ startOnLoad:false, theme:'neutral', securityLevel:'loose',
                     flowchart:{ useMaxWidth:true, htmlLabels:true } });
mermaid.run({ querySelector:'.mermaid' })
  .then(()=>{ ajustarDiagramas(); document.title = document.title + ' '; })
  .catch(e=>console.error(e));

// Los diagramas se escalan para caber en su lamina: mermaid no tiene tope de alto.
function ajustarDiagramas() {
  var MM = 96 / 25.4;
  document.querySelectorAll('.mermaid svg').forEach(function (svg) {
    var caja = svg.parentElement;
    var apaisada = !!caja.closest('.apaisada');
    // El ancho no se mide: se toma de la caja de impresion, porque el layout de
    // pantalla es mas angosto y dejaria los diagramas mas chicos de lo que caben.
    var anchoMax = (apaisada ? 273 : 182) * MM;
    var altoMax  = (apaisada ? 136 : 78) * MM;
    var vb = svg.viewBox.baseVal;
    if (!vb || !vb.width) return;
    var escala = Math.min(anchoMax / vb.width, altoMax / vb.height);
    svg.removeAttribute('width'); svg.removeAttribute('height');
    svg.style.maxWidth = 'none';
    svg.style.width  = (vb.width  * escala) + 'px';
    svg.style.height = (vb.height * escala) + 'px';
  });
}
</script></body></html>
JS
} > "$HTML"

# 3 · PDF
"$CHROME" --headless --disable-gpu --no-sandbox --no-pdf-header-footer \
  --generate-pdf-document-outline \
  --virtual-time-budget=20000 --run-all-compositor-stages-before-draw \
  --print-to-pdf="$PDF" "file://$PWD/$HTML" 2>/dev/null

printf '  %-22s %s\n' "$HTML" "$(du -h "$HTML" | cut -f1)"
printf '  %-22s %s\n' "$PDF"  "$(du -h "$PDF"  | cut -f1)"
