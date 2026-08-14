#!/usr/bin/env bash
#
# verificar.sh — controles de forma y estructura sobre los entregables.
#
#   scripts/verificar.sh [--sin-agentes]
#
# Con --sin-agentes, el control E4 deja de admitir cambios en Agents/*: así debe
# ejecutarse desde la primera iteración en adelante, cuando los agentes ya son
# instrumento de medición y no material editable.
#
# Ocho controles. Los cuatro primeros son los mecánicos de docs/CONVENCIONES.md,
# sección 11: buscan texto que no debería existir, y aciertan cuando no encuentran
# nada. Los cuatro siguientes verifican que el documento de requerimientos sea
# internamente consistente y que la corrida no haya tocado archivos ajenos.
#
# Ninguno emite juicio. Un control en verde no dice que el requerimiento sea
# bueno: dice que no incurre en el defecto que ese control sabe detectar.
#
# Códigos de salida
#   0  los ocho controles pasan
#   1  al menos un control falla; el detalle va después de la tabla
#   2  falta un archivo obligatorio

set -uo pipefail
export LC_ALL="${LC_ALL:-en_US.UTF-8}"

cd "$(dirname "$0")/.." || exit 2

SIN_AGENTES=""
for arg in "$@"; do
  case "$arg" in
    --sin-agentes) SIN_AGENTES="--sin-agentes" ;;
    *) printf '⛔ Opción desconocida: %s\n' "$arg" >&2; exit 2 ;;
  esac
done

REQ="Requirements/ReqFunc.MD"
[ -f "$REQ" ] || { printf '⛔ No existe %s\n' "$REQ" >&2; exit 2; }

ANCHO=42
FALLAS=0
DETALLE=""

# reportar <etiqueta> <n_hallazgos> <cuerpo>
reportar() {
  local etiqueta="$1" n="$2" cuerpo="${3:-}" puntos=""
  local relleno=$((ANCHO - ${#etiqueta}))
  [ "$relleno" -lt 1 ] && relleno=1
  puntos="$(printf '%*s' "$relleno" '' | tr ' ' '.')"

  if [ "$n" -eq 0 ]; then
    printf '%s %s PASA\n' "$etiqueta" "$puntos"
  else
    printf '%s %s FALLA (%s)\n' "$etiqueta" "$puntos" "$n"
    FALLAS=$((FALLAS + 1))
    DETALLE="${DETALLE}
── ${etiqueta}
${cuerpo}
"
  fi
}

contar() { [ -z "$1" ] && echo 0 || printf '%s\n' "$1" | grep -c '' ; }

printf '\nVerificación de requerimientos — %s\n\n' "$(git rev-parse --abbrev-ref HEAD 2>/dev/null || echo 'sin git')"
printf 'Controles mecánicos (CONVENCIONES §11)\n'

# ── M1 ── Todo enunciado lleva el auxiliar DEBE.
H="$(grep -nE '^\*\*Enunciado:\*\*' "$REQ" | grep -v 'DEBE')"
reportar '[M1] Enunciado sin DEBE' "$(contar "$H")" "$H"

# ── M2 ── El sujeto del DEBE es el sistema, nunca una persona.
H="$(grep -nEi 'el médico DEBE|la enfermera DEBE|el coordinador DEBE|el hospital DEBE|el equipo DEBE' Requirements/*.MD)"
reportar '[M2] Sujeto distinto del sistema' "$(contar "$H")" "$H"

# ── M3 ── Un requerimiento enuncia la garantía, no el mecanismo que la cumple.
H="$(grep -nEi 'kafka|redis|websocket|microservicio|kubernetes|base de datos|caché|endpoint|push' Requirements/*.MD)"
reportar '[M3] Mecanismo o producto nombrado' "$(contar "$H")" "$H"

# ── M4 ── El cuerpo registra el estado vigente; el historial vive en git.
H="$(grep -nE '~~|\(Decidido|\(Refinado|\(Corregido|versión anterior|por ahora' README.md Requirements/*.MD Personas/*.MD)"
reportar '[M4] Lápidas o rastro de historial' "$(contar "$H")" "$H"

printf '\nControles estructurales\n'

# ── E1 ── Ningún identificador de RF se repite.
DEFINIDOS="$(grep -oE '^### RF-[A-Z]+-[0-9]+' "$REQ" | awk '{print $2}')"
H="$(printf '%s\n' "$DEFINIDOS" | sort | uniq -d)"
reportar '[E1] Identificadores duplicados' "$(contar "$H")" "$H"

# ── E2 ── Cada RF declara enunciado, prioridad, persona, problema y un criterio.
H="$(awk '
  /^### RF-[A-Z]+-[0-9]+/ { n++; ids[n] = $2; next }
  /^## Matriz de trazabilidad/ { fin = 1 }
  !fin && n > 0 && /^\*\*Enunciado:\*\*/ { enun[ids[n]] = 1 }
  !fin && n > 0 && /^\| *Prioridad *\|/  { prio[ids[n]] = 1 }
  !fin && n > 0 && /^\| *Persona *\|/    { pers[ids[n]] = 1 }
  !fin && n > 0 && /^\| *Problema *\|/   { prob[ids[n]] = 1 }
  !fin && n > 0 && /^- \*\*CA-/          { crit[ids[n]] = 1 }
  END {
    for (i = 1; i <= n; i++) {
      id = ids[i]; falta = ""
      if (!(id in enun)) falta = falta " enunciado"
      if (!(id in prio)) falta = falta " prioridad"
      if (!(id in pers)) falta = falta " persona"
      if (!(id in prob)) falta = falta " problema"
      if (!(id in crit)) falta = falta " criterios-de-aceptación"
      if (falta != "") printf "%s: falta%s\n", id, falta
    }
  }' "$REQ")"
reportar '[E2] Campos obligatorios del RF' "$(contar "$H")" "$H"

# ── E3 ── Las matrices de cierre no citan identificadores inexistentes.
REFERIDOS="$(awk '/^## Matriz de trazabilidad/ { p = 1 } p' "$REQ" |
             grep -oE 'RF-[A-Z]+-[0-9]+' | sort -u)"
H="$(comm -23 <(printf '%s\n' "$REFERIDOS") <(printf '%s\n' "$DEFINIDOS" | sort -u))"
reportar '[E3] Matrices citan IDs inexistentes' "$(contar "$H")" "$H"

# ── E4 ── La corrida solo tocó archivos declarados editables.
if [ -x scripts/guardia-diff.sh ]; then
  H="$(scripts/guardia-diff.sh --silencioso $SIN_AGENTES)"
  ETIQUETA='[E4] Archivos de solo lectura intactos'
  [ -n "$SIN_AGENTES" ] && ETIQUETA='[E4] Solo lectura intactos (sin agentes)'
  reportar "$ETIQUETA" "$(contar "$H")" "$H"
else
  reportar '[E4] Archivos de solo lectura intactos' 1 'falta scripts/guardia-diff.sh'
fi

# ── Cierre ──
TOTAL="$(printf '%s\n' "$DEFINIDOS" | sort -u | grep -c '')"
printf '\n%s requerimientos funcionales inventariados.\n' "$TOTAL"

if [ "$FALLAS" -eq 0 ]; then
  printf '\n✅ Los ocho controles devuelven vacío.\n\n'
  exit 0
fi

printf '\nDetalle de los %s control(es) en falla:\n%s\n' "$FALLAS" "$DETALLE"
printf '⛔ La verificación no pasa. No se declara PASSED con un control en rojo.\n\n'
exit 1
