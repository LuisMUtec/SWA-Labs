#!/usr/bin/env bash
# Convierte docs/ENTREGA.md en un PDF con los diagramas renderizados.
#   uso: scripts/entrega-a-pdf.sh
# Requiere: pandoc y Google Chrome. Mermaid se baja una vez y queda cacheado,
# de modo que la segunda corrida y las siguientes no necesitan red.
set -euo pipefail
cd "$(dirname "$0")/.."
MD=docs/ENTREGA.md
HTML=docs/ENTREGA.html
PDF=docs/ENTREGA.pdf
MERMAID=scripts/mermaid.min.js
MERMAID_URL=https://cdn.jsdelivr.net/npm/mermaid@11/dist/mermaid.min.js
CHROME="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

[ -f "$MD" ] || { echo "falta $MD"; exit 1; }

# 0 · mermaid: 3,2 MB de dependencia. No se versiona (ver .gitignore); se cachea.
if [ ! -f "$MERMAID" ]; then
  echo "bajando mermaid a $MERMAID (una sola vez)..."
  curl -fsSL "$MERMAID_URL" -o "$MERMAID" || {
    echo "no se pudo bajar mermaid. Con red: curl -fsSL $MERMAID_URL -o $MERMAID"; exit 1; }
fi

# 1 · cuerpo desde markdown, con los bloques mermaid marcados para el renderer
pandoc "$MD" -f gfm -t html --no-highlight \
  | perl -0pe 's{<pre class="mermaid"><code>(.*?)</code></pre>}{<pre class="mermaid">$1</pre>}gs' \
  | perl -0pe 's{<pre><code class="language-mermaid">(.*?)</code></pre>}{<pre class="mermaid">$1</pre>}gs' \
  | perl -pe 's/&quot;/"/g if /<pre class="mermaid">/ .. /<\/pre>/' > /tmp/_cuerpo.html

# 2 · documento completo, con estilo de impresión y mermaid embebido
{
cat <<'CSS'
<!doctype html><html lang="es"><head><meta charset="utf-8">
<title>SendIt — Caso de Estudio #3</title>
<style>
@page { size: A4; margin: 18mm 16mm 20mm 16mm; }
* { box-sizing: border-box; }
body { font: 10.5pt/1.55 "Helvetica Neue", Helvetica, Arial, sans-serif; color:#1a1a1a; margin:0; }
h1 { font-size:21pt; margin:1.6em 0 .5em; padding-bottom:.25em; border-bottom:2px solid #1a1a1a; page-break-after:avoid; }
h1:first-child { margin-top:0; }
h2 { font-size:14pt; margin:1.5em 0 .5em; page-break-after:avoid; }
h3 { font-size:11.5pt; margin:1.2em 0 .4em; color:#333; page-break-after:avoid; }
h4 { font-size:10.5pt; margin:1em 0 .3em; color:#444; page-break-after:avoid; }
p, li { orphans:3; widows:3; }
table { border-collapse:collapse; width:100%; margin:.8em 0; font-size:8.8pt; page-break-inside:avoid; }
th, td { border:1px solid #ccc; padding:4px 7px; text-align:left; vertical-align:top; }
th { background:#f0f0f0; font-weight:600; }
tr:nth-child(even) td { background:#fafafa; }
code { font-family:"SF Mono",Menlo,Consolas,monospace; font-size:.86em; background:#f2f2f2; padding:1px 4px; border-radius:3px; }
pre { background:#f7f7f7; border:1px solid #e0e0e0; border-radius:4px; padding:9px 11px; overflow-x:auto; font-size:8.5pt; page-break-inside:avoid; }
pre code { background:none; padding:0; }
blockquote { margin:.9em 0; padding:.5em 0 .5em 1em; border-left:3px solid #999; color:#333; background:#fafafa; page-break-inside:avoid; }
blockquote p { margin:.35em 0; }
hr { border:none; border-top:1px solid #ddd; margin:2em 0; }
.mermaid { background:#fff; border:1px solid #e0e0e0; border-radius:4px; padding:10px; text-align:center; page-break-inside:avoid; margin:1em 0; }
.mermaid svg { max-width:100%; height:auto; }
a { color:#0b5; text-decoration:none; }
strong { font-weight:600; }
</style></head><body>
CSS
cat /tmp/_cuerpo.html
echo '<script>'; cat "$MERMAID"; echo '</script>'
cat <<'JS'
<script>
mermaid.initialize({ startOnLoad:false, theme:'neutral', securityLevel:'loose',
                     flowchart:{ useMaxWidth:true, htmlLabels:true } });
mermaid.run({ querySelector:'.mermaid' })
  .then(()=>{ document.title = document.title + ' '; })
  .catch(e=>console.error(e));
</script></body></html>
JS
} > "$HTML"

# 3 · PDF
"$CHROME" --headless --disable-gpu --no-sandbox --no-pdf-header-footer \
  --virtual-time-budget=20000 --run-all-compositor-stages-before-draw \
  --print-to-pdf="$PDF" "file://$PWD/$HTML" 2>/dev/null

printf '  %-22s %s\n' "$HTML" "$(du -h "$HTML" | cut -f1)"
printf '  %-22s %s\n' "$PDF"  "$(du -h "$PDF"  | cut -f1)"
printf '  %-22s %s\n' "diagramas" "$(grep -c 'class=\"mermaid\"' "$HTML") bloques"
