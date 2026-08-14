#!/usr/bin/env bash
#
# verificar-puntaje.sh — recomputa los puntajes declarados por una corrida.
#
#   scripts/verificar-puntaje.sh [--silencioso] [ruta/a/corrida.json ...]
#
# Sin rutas, verifica todas las corridas de Spec/corridas/. Los archivos cuyo
# nombre empieza por «_» son plantillas y se ignoran.
#
# La rúbrica de Spec/Eval-Spec.MD define fórmulas, techos duros y cinco
# condiciones de veredicto, y hasta ahora las aplicaba el mismo agente que quería
# aprobar. Este control las vuelve mecánicas: lee los números que la corrida
# declaró en corrida.json, los recomputa y reporta cada discrepancia.
#
# No juzga la evaluación. Que una tarea crítica valga 5 y no 3 lo decide la
# evidencia del diagnóstico, y ningún script la lee. Un control en verde dice que
# las cuentas cierran, no que la evaluación sea correcta.
#
# No hay límite de corridas: se verifican todas las que existan.
#
# Con --silencioso imprime solo las líneas infractoras, sin adornos: ese es el
# modo que consume verificar.sh.
#
# Códigos de salida
#   0  todo lo declarado es consistente, o no hay corridas que verificar
#   1  al menos una discrepancia
#   2  falta jq, o un archivo no es JSON válido

set -uo pipefail
export LC_ALL="${LC_ALL:-en_US.UTF-8}"

cd "$(dirname "$0")/.." || exit 2

SILENCIOSO=0
ARCHIVOS=""
for arg in "$@"; do
  case "$arg" in
    --silencioso) SILENCIOSO=1 ;;
    -*) printf '⛔ Opción desconocida: %s\n' "$arg" >&2; exit 2 ;;
    *) ARCHIVOS="${ARCHIVOS}${arg}
" ;;
  esac
done

command -v jq >/dev/null 2>&1 || {
  [ "$SILENCIOSO" -eq 1 ] && echo 'falta jq: no se puede verificar la aritmética del puntaje'
  [ "$SILENCIOSO" -eq 0 ] && printf '⛔ Falta jq. Instálalo para verificar la aritmética del puntaje.\n' >&2
  exit 2
}

# Sin rutas explícitas, todas las corridas registradas. No hay tope: se verifican
# cuantas haya.
if [ -z "$ARCHIVOS" ]; then
  ARCHIVOS="$(find Spec/corridas -mindepth 2 -maxdepth 2 -name 'corrida.json' \
                -not -name '_*' 2>/dev/null | sort)"
fi
ARCHIVOS="$(printf '%s' "$ARCHIVOS" | grep -v '^$')"
N_ARCHIVOS="$([ -z "$ARCHIVOS" ] && echo 0 || printf '%s\n' "$ARCHIVOS" | grep -c '')"

HALLAZGOS=""

anotar() { HALLAZGOS="${HALLAZGOS}${1}
"; }

# ── Un reporte sin su gemelo en JSON ──────────────────────────────────────────
# Si la corrida produjo reporte, produjo también los números que lo sostienen.
# Sin esta comprobación, omitir corrida.json bastaría para esquivar el control.
if [ "$N_ARCHIVOS" -eq 0 ] && [ -f Spec/Eval-Report.MD ]; then
  anotar 'Spec/Eval-Report.MD existe pero ninguna corrida declaró su corrida.json'
fi

# ── Programa de verificación ──────────────────────────────────────────────────
# Devuelve una línea por discrepancia. Cada comprobación cita el valor declarado
# y el recomputado, para que el hallazgo se corrija donde está.
FILTRO=$(cat <<'JQ'
def abs: if . < 0 then - . else . end;
def cerca($a; $b): (($a - $b) | abs) <= 0.051;
def n1: (. * 10 | round) / 10;

[
  # ── Cabecera ────────────────────────────────────────────────────────────────
  ( ["corrida","fecha","rama","modelo","commits","instrumento_modificado",
     "glosario","iteraciones","resultado"][] as $k
    | select(.[$k] == null) | "cabecera: falta el campo \($k)" ),

  ( ["requerimientos","rubrica","personas","agentes"][] as $k
    | select((.commits // {})[$k] == null) | "cabecera: falta commits.\($k)" ),

  ( select((.iteraciones // []) | length == 0) | "cabecera: la corrida no declara ninguna iteración" ),

  # ── Por iteración ───────────────────────────────────────────────────────────
  ( (.iteraciones // [])[] as $it
    | "iteración \($it.n // "?")" as $p
    | ([ "dimensiones","d2_problemas","d3_rf","tensiones_sin_decidir",
         "prioridad_uniforme","controles_pasan","global","veredicto","personas" ]
       | map(select($it[.] == null))) as $faltan_it
    | ([ "rodrigo","milagros","carmen","anibal" ]
       | map(select(($it.personas // {})[.] == null))) as $faltan_pers
    | ([ "D1","D2","D3","D4","D5","D6" ]
       | map(select(($it.dimensiones // {})[.] == null))) as $faltan_dim
    | ([ ($it.personas // {}) | to_entries[] as $e
         | ["tareas","estorba_fuera","flujo","puntaje","percibida","tareas_en_cero"][] as $k
         | select($e.value[$k] == null)
         | "personas.\($e.key).\($k)" ]) as $faltan_campos
    | ([ ["P1","P2","P3"][] as $q
         | select(($it.d2_problemas // {})[$q] == null) | "d2_problemas.\($q)" ]
       + [ ["conformes","total"][] as $q
           | select(($it.d3_rf // {})[$q] == null) | "d3_rf.\($q)" ]) as $faltan_sub
    | (($faltan_it + $faltan_pers + $faltan_dim + $faltan_campos + $faltan_sub) | length) as $huecos
    | if $huecos > 0 then
        ( ($faltan_it[]     | "\($p): falta el campo \(.)"),
          ($faltan_pers[]   | "\($p): falta la persona \(.)"),
          ($faltan_dim[]    | "\($p): falta la dimensión \(.)"),
          ($faltan_campos[] | "\($p): falta \(.)"),
          ($faltan_sub[]    | "\($p): falta \(.)") )
      else
        $it.dimensiones as $D
        | ($it.personas | [ .rodrigo, .milagros, .carmen, .anibal ]) as $ps
        | (
          # Rangos de las dimensiones.
          ( ["D1","D2","D3","D4","D5","D6"][] as $d
            | select($D[$d] < 0 or $D[$d] > 100)
            | "\($p): \($d) = \($D[$d]), fuera de 0–100" ),

          # Rangos y aritmética de cada persona.
          ( $it.personas | to_entries[] as $e
            | $e.key as $nom | $e.value as $x
            | ( ( select($x.tareas < 0 or $x.tareas > 30)
                  | "\($p)/\($nom): tareas = \($x.tareas), fuera de 0–30" ),
                ( select(([0,2,4] | index($x.flujo)) == null)
                  | "\($p)/\($nom): flujo = \($x.flujo); solo admite 0, 2 o 4" ),
                ( select($x.percibida < 0 or $x.percibida > 100)
                  | "\($p)/\($nom): percibida = \($x.percibida), fuera de 0–100" ),
                ( select($x.tareas_en_cero < 0 or $x.tareas_en_cero > 6)
                  | "\($p)/\($nom): tareas_en_cero = \($x.tareas_en_cero), fuera de 0–6" ),
                ( select($x.estorba_fuera < 0)
                  | "\($p)/\($nom): estorba_fuera = \($x.estorba_fuera), no puede ser negativo" ),
                ( select($x.puntaje < 0 or $x.puntaje > 10)
                  | "\($p)/\($nom): puntaje = \($x.puntaje), fuera de 0–10" ),
                ( ((([0, ($x.tareas - 2 * $x.estorba_fuera)] | max) / 5) + $x.flujo) as $esp
                  | select(cerca($x.puntaje; $esp) | not)
                  | "\($p)/\($nom): puntaje declarado \($x.puntaje); máx(0, \($x.tareas) − 2×\($x.estorba_fuera))/5 + \($x.flujo) = \($esp | n1)" ) ) ),

          # D1 y el promedio de personas son el mismo número en dos unidades.
          ( (($ps | map(.puntaje) | add) / 4 * 10) as $esp
            | select(cerca($D.D1; $esp) | not)
            | "\($p): D1 declarada \($D.D1); el promedio de personas × 10 da \($esp | n1)" ),

          # D2 = (P1 + P2 + P3) / 3.
          ( ["P1","P2","P3"][] as $q
            | select(([0,50,100] | index($it.d2_problemas[$q])) == null)
            | "\($p): \($q) = \($it.d2_problemas[$q]); solo admite 0, 50 o 100" ),
          ( (([$it.d2_problemas.P1, $it.d2_problemas.P2, $it.d2_problemas.P3] | add) / 3) as $esp
            | select(cerca($D.D2; $esp) | not)
            | "\($p): D2 declarada \($D.D2); (P1+P2+P3)/3 = \($esp | n1)" ),

          # D3 = RF conformes / total × 100.
          ( select($it.d3_rf.total <= 0)
            | "\($p): d3_rf.total = \($it.d3_rf.total); debe ser mayor que 0" ),
          ( select($it.d3_rf.total > 0 and $it.d3_rf.conformes > $it.d3_rf.total)
            | "\($p): d3_rf.conformes (\($it.d3_rf.conformes)) supera el total (\($it.d3_rf.total))" ),
          ( select($it.d3_rf.total > 0)
            | ($it.d3_rf.conformes / $it.d3_rf.total * 100) as $esp
            | select(cerca($D.D3; $esp) | not)
            | "\($p): D3 declarada \($D.D3); \($it.d3_rf.conformes)/\($it.d3_rf.total) × 100 = \($esp | n1)" ),

          # Global ponderado.
          ( ($D.D1*0.30 + $D.D2*0.25 + $D.D3*0.20
             + $D.D4*0.10 + $D.D5*0.10 + $D.D6*0.05) as $esp
            | select(cerca($it.global; $esp) | not)
            | "\($p): global declarado \($it.global); la suma ponderada da \($esp | n1)" ),

          # ── Techos duros de Eval-Spec ──
          ( select(.glosario == false and $D.D5 > 80)
            | "\($p): D5 = \($D.D5); mientras falte el glosario no puede superar 80" ),
          ( select(($ps | map(.percibida >= 90) | all)
                   and $it.tensiones_sin_decidir > 0 and $D.D5 > 40)
            | "\($p): D5 = \($D.D5); con las cuatro percibidas ≥ 90 y \($it.tensiones_sin_decidir) tensión(es) sin decidir no puede superar 40" ),
          ( select(([$it.d2_problemas.P1, $it.d2_problemas.P2, $it.d2_problemas.P3]
                    | map(. == 0) | any) and $D.D2 > 60)
            | "\($p): D2 = \($D.D2); con un problema crítico sin resolver no puede superar 60" ),
          ( select(($ps | map(.tareas_en_cero == 6) | any) and $D.D1 > 50)
            | "\($p): D1 = \($D.D1); con una persona sin ninguna tarea cubierta no puede superar 50" ),
          ( select($it.prioridad_uniforme == true and $D.D6 > 60)
            | "\($p): D6 = \($D.D6); con todos los RF en la misma prioridad no puede superar 60" ),

          # ── Las cinco condiciones del veredicto ──
          ( select(["PASSED","FAILED"] | index($it.veredicto) | not)
            | "\($p): veredicto = \($it.veredicto); solo admite PASSED o FAILED" ),
          ( [ $it.global >= 80.0,
              $D.D1 >= 80.0,
              ($ps | map(.puntaje) | min) >= 7.0,
              $D.D2 >= 80.0,
              $it.controles_pasan == true ] as $cond
            | (if ($cond | all) then "PASSED" else "FAILED" end) as $esp
            | select($it.veredicto != $esp)
            | "\($p): veredicto declarado \($it.veredicto); las cinco condiciones dan \($esp) (cumple \($cond | map(select(.)) | length) de 5)" )
        )
      end ),

  # ── Cierre ──────────────────────────────────────────────────────────────────
  ( select((.iteraciones // []) | length > 0)
    | .resultado as $r
    | (.iteraciones[-1]) as $u
    | ( ( select($r == null) | "cierre: la corrida no declara resultado" ),
        ( select($r != null and $r.global != null and $u.global != null
                 and (cerca($r.global; $u.global) | not))
          | "cierre: resultado.global \($r.global) no coincide con la última iteración (\($u.global))" ),
        ( select($r != null and $r.veredicto != $u.veredicto)
          | "cierre: resultado.veredicto \($r.veredicto) no coincide con la última iteración (\($u.veredicto))" ),
        ( select($r != null and $r.promedio_personas != null and $u.personas != null)
          | (($u.personas | [ .rodrigo, .milagros, .carmen, .anibal ]
              | map(.puntaje // 0) | add) / 4) as $esp
          | select(cerca($r.promedio_personas; $esp) | not)
          | "cierre: promedio_personas \($r.promedio_personas) no coincide con el de la última iteración (\($esp | n1))" ) ) )
]
| .[]
JQ
)

if [ "$N_ARCHIVOS" -gt 0 ]; then
  while IFS= read -r f; do
    [ -z "$f" ] && continue
    if [ ! -f "$f" ]; then
      anotar "$f: no existe"
      continue
    fi
    if ! ERR="$(jq empty "$f" 2>&1)"; then
      anotar "$f: no es JSON válido — $(printf '%s' "$ERR" | head -1)"
      continue
    fi
    # Un error de jq no puede pasar por silencio: dejaría el control en verde
    # justamente cuando no llegó a verificar nada.
    if ! SALIDA="$(jq -r "$FILTRO" "$f" 2>&1)"; then
      anotar "$f: el control no pudo evaluarse — $(printf '%s' "$SALIDA" | head -1)"
      continue
    fi
    while IFS= read -r linea; do
      [ -n "$linea" ] && anotar "${f#Spec/corridas/}: $linea"
    done <<< "$SALIDA"
  done <<< "$ARCHIVOS"
fi

# ── El README publica el resultado de la última corrida ───────────────────────
# El porcentaje del README es la cara pública del trabajo. Si se queda en el de
# una corrida anterior, publica un número que ya nadie sostiene.
if [ "$N_ARCHIVOS" -gt 0 ] && [ -f README.md ]; then
  ULTIMA="$(printf '%s\n' "$ARCHIVOS" | tail -1)"
  DECLARADO="$(jq -r '.resultado.global // empty' "$ULTIMA" 2>/dev/null)"
  PUBLICADO="$(grep -m1 'Resultado del agente' README.md |
               grep -oE '\*\*[0-9]+([.,][0-9]+)? ?%\*\*' |
               tr -d '*% ' | tr ',' '.')"
  if [ -n "$DECLARADO" ] && [ -n "$PUBLICADO" ]; then
    if ! awk -v a="$DECLARADO" -v b="$PUBLICADO" \
         'BEGIN { d = a - b; if (d < 0) d = -d; exit !(d <= 0.051) }'; then
      anotar "README.md: publica $PUBLICADO % y la última corrida cerró en $DECLARADO %"
    fi
  fi
fi

HALLAZGOS="$(printf '%s' "$HALLAZGOS" | grep -v '^$')"

if [ "$SILENCIOSO" -eq 1 ]; then
  [ -n "$HALLAZGOS" ] && printf '%s\n' "$HALLAZGOS"
  [ -z "$HALLAZGOS" ] && exit 0 || exit 1
fi

printf '\nAritmética del puntaje\n\n'

if [ "$N_ARCHIVOS" -eq 0 ] && [ -z "$HALLAZGOS" ]; then
  printf '   Sin corridas registradas en Spec/corridas/.\n\n'
  exit 0
fi

if [ "$N_ARCHIVOS" -gt 0 ]; then
  printf '   %s corrida(s) verificada(s):\n' "$N_ARCHIVOS"
  printf '%s\n' "$ARCHIVOS" | sed 's/^/     /'
  printf '\n'
fi

if [ -z "$HALLAZGOS" ]; then
  printf '✅ Los puntajes declarados coinciden con los recomputados.\n\n'
  exit 0
fi

printf '⛔ Discrepancias entre lo declarado y lo recomputado:\n'
printf '%s\n' "$HALLAZGOS" | sed 's/^/     /'
printf '\n   Corrige el número, nunca la fórmula. Si la discrepancia nace de un\n'
printf '   insumo mal juzgado, vuelve a la evidencia del diagnóstico: este control\n'
printf '   comprueba que las cuentas cierren, no que la evaluación sea correcta.\n\n'
exit 1
