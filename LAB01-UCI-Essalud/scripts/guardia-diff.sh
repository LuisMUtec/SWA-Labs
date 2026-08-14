#!/usr/bin/env bash
#
# guardia-diff.sh — comprueba que la corrida solo tocó archivos editables.
#
#   scripts/guardia-diff.sh [--silencioso] [--sin-agentes]
#
# La lista de editables la fija el protocolo de evaluación: los cuatro agentes de
# persona, el índice de agentes, los requerimientos funcionales, el reporte y el
# marcador de resultado del README. Todo lo demás —personas, convenciones, la
# definición del evaluador y los requerimientos no funcionales— es de solo lectura
# durante una corrida: son la vara con la que se mide, y una vara que se ajusta
# para alcanzar el número deja de medir.
#
# Los agentes de persona solo son editables durante el Paso 0. Terminado ese paso,
# pasan a ser instrumento de medición: si cambian entre una iteración y la
# siguiente, la mejora del reporte deja de ser atribuible a las correcciones de los
# requerimientos. Con --sin-agentes se los retira de la lista, que es como debe
# ejecutarse el control desde la primera iteración en adelante.
#
# Con --silencioso imprime solo las rutas infractoras, una por línea, sin adornos:
# ese es el modo que consume verificar.sh.
#
# Códigos de salida
#   0  no se tocó ningún archivo de solo lectura
#   1  se tocó al menos uno
#   2  no es un repositorio git

set -uo pipefail
export LC_ALL="${LC_ALL:-en_US.UTF-8}"

cd "$(dirname "$0")/.." || exit 2

SILENCIOSO=0
SIN_AGENTES=0
for arg in "$@"; do
  case "$arg" in
    --silencioso)  SILENCIOSO=1 ;;
    --sin-agentes) SIN_AGENTES=1 ;;
    *) printf '⛔ Opción desconocida: %s\n' "$arg" >&2; exit 2 ;;
  esac
done

git rev-parse --git-dir >/dev/null 2>&1 || {
  [ "$SILENCIOSO" -eq 1 ] && echo 'no es un repositorio git'
  exit 2
}

EDITABLES="
Requirements/ReqFunc.MD
Spec/Eval-Report.MD
README.md
"

# Los agentes solo entran en la lista durante el Paso 0.
if [ "$SIN_AGENTES" -eq 0 ]; then
  EDITABLES="${EDITABLES}Agents/agent-rodrigo.MD
Agents/agent-milagros.MD
Agents/agent-carmen.MD
Agents/agent-anibal.MD
Agents/README.md
"
fi

# Todo lo que cambió respecto a HEAD, confirmado o no, con seguimiento o sin él.
TOCADOS="$( { git diff --name-only HEAD
              git diff --name-only --cached
              git ls-files --others --exclude-standard; } | sort -u | grep -v '^$')"

INFRACTORES=""
for ruta in $TOCADOS; do
  if ! printf '%s\n' "$EDITABLES" | grep -qxF "$ruta"; then
    INFRACTORES="${INFRACTORES}${ruta}
"
  fi
done
INFRACTORES="$(printf '%s' "$INFRACTORES" | grep -v '^$')"

if [ "$SILENCIOSO" -eq 1 ]; then
  [ -n "$INFRACTORES" ] && printf '%s\n' "$INFRACTORES"
  [ -z "$INFRACTORES" ] && exit 0 || exit 1
fi

printf '\nGuardia de archivos editables\n\n'

if [ -z "$TOCADOS" ]; then
  printf '   Sin cambios respecto a HEAD.\n\n'
  exit 0
fi

printf '   Archivos tocados:\n'
printf '%s\n' "$TOCADOS" | sed 's/^/     /'

if [ -z "$INFRACTORES" ]; then
  printf '\n✅ Todos son editables.\n\n'
  exit 0
fi

printf '\n⛔ Fuera de la lista de editables:\n'
printf '%s\n' "$INFRACTORES" | sed 's/^/     /'
printf '\n   Revierte esos archivos antes de continuar. Si la corrección que\n'
printf '   necesitas vive en uno de ellos, repórtala como bloqueada: no la\n'
printf '   sustituyas por una solución inventada.\n\n'
exit 1
