#!/usr/bin/env bash
#
# preparar-git.sh — deja el repositorio listo para una corrida de evaluación.
#
#   scripts/preparar-git.sh [rama] [base]
#
#   rama   Rama de trabajo a crear.   Por defecto: eval/additional-v2
#   base   Rama de la que se parte.   Por defecto: main
#
# Aborta —sin tocar nada— ante cualquier condición que obligaría a descartar,
# sobrescribir o esconder trabajo. Nunca ejecuta stash, reset ni checkout -f.
#
# Códigos de salida
#   0  rama creada y lista
#   1  condición de aborto: el mensaje dice cuál y qué hacer
#   2  uso incorrecto

set -uo pipefail
export LC_ALL="${LC_ALL:-en_US.UTF-8}"

RAMA="${1:-eval/additional-v2}"
BASE="${2:-main}"

abortar() {
  printf '\n⛔ %s\n' "$1" >&2
  [ $# -gt 1 ] && printf '   %s\n' "$2" >&2
  exit 1
}

paso() { printf '   %s\n' "$1"; }

cd "$(dirname "$0")/.." || exit 2
printf '\nPreparación Git — rama «%s» sobre «%s»\n\n' "$RAMA" "$BASE"

# 1. Estamos dentro de un repositorio.
git rev-parse --git-dir >/dev/null 2>&1 ||
  abortar "Esto no es un repositorio git." "Ejecuta el script desde el repositorio del proyecto."

# 2. No hay cambios locales sobre archivos versionados.
SUCIO="$(git status --porcelain --untracked-files=no)"
if [ -n "$SUCIO" ]; then
  printf '%s\n' "$SUCIO" >&2
  abortar "Hay cambios locales sin confirmar." \
          "Confírmalos o guárdalos tú mismo. El script no descarta trabajo ajeno."
fi

# Los archivos sin seguimiento no bloquean, pero se anuncian: pueden ser
# archivos que una corrida anterior creó fuera de la lista de editables.
NUEVOS="$(git ls-files --others --exclude-standard)"
if [ -n "$NUEVOS" ]; then
  printf '⚠️  Archivos sin seguimiento presentes:\n'
  printf '%s\n' "$NUEVOS" | sed 's/^/     /'
  printf '\n'
fi

# 3. La rama de trabajo no existe todavía, ni aquí ni en origin.
if git show-ref --verify --quiet "refs/heads/$RAMA"; then
  abortar "La rama «${RAMA}» ya existe localmente." \
          "Renómbrala, bórrala tú mismo o pasa otro nombre como primer argumento."
fi
if git show-ref --verify --quiet "refs/remotes/origin/$RAMA"; then
  abortar "La rama «${RAMA}» ya existe en origin." \
          "Una corrida anterior la publicó. Elige otro nombre."
fi
paso "✓ Rama «${RAMA}» libre"

# 4. Traer origin.
git fetch origin --prune --quiet ||
  abortar "No se pudo contactar origin." "Revisa la conexión o las credenciales."
paso "✓ origin actualizado"

# 5. La base existe en ambos lados.
git show-ref --verify --quiet "refs/heads/$BASE" ||
  abortar "La rama base «${BASE}» no existe localmente."
git show-ref --verify --quiet "refs/remotes/origin/$BASE" ||
  abortar "La rama base «origin/${BASE}» no existe."

# 6. Situarse en la base y adelantarla solo por fast-forward.
ACTUAL="$(git rev-parse --abbrev-ref HEAD)"
if [ "$ACTUAL" != "$BASE" ]; then
  git checkout --quiet "$BASE" ||
    abortar "No se pudo cambiar a «${BASE}»."
fi

if ! git merge --ff-only "origin/$BASE" --quiet 2>/dev/null; then
  ADELANTE="$(git rev-list --count "origin/$BASE..$BASE")"
  abortar "«${BASE}» no puede adelantarse por fast-forward: tiene $ADELANTE commit(s) que origin no conoce." \
          "Resuélvelo tú mismo (rebase o push). El script no reescribe historia."
fi

# 7. La base quedó idéntica a origin.
if [ "$(git rev-parse "$BASE")" != "$(git rev-parse "origin/$BASE")" ]; then
  abortar "«${BASE}» no coincide con «origin/${BASE}» después del fast-forward."
fi
paso "✓ «${BASE}» limpio y sincronizado con origin"

# 8. Crear la rama de trabajo.
git checkout --quiet -b "$RAMA" ||
  abortar "No se pudo crear la rama «${RAMA}»."

printf '\n✅ Preparación Git completada\n'
printf '   Rama activa: %s (desde %s @ %s)\n\n' \
  "$RAMA" "$BASE" "$(git rev-parse --short "$BASE")"
