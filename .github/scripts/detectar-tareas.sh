#!/usr/bin/env bash
# Imprime, como arreglo JSON, las carpetas `semana-NN/tarea` que el
# autograding debe calificar. Una tarea se califica cuando cambió su
# notebook `tarea-NN.ipynb` entre dos commits: así un "Sync fork" que trae
# tareas sin resolver del curso no dispara ❌ falsos.
#
# Uso:
#   detectar-tareas.sh <commit-base> <commit-cabeza>   # por diferencia
#   detectar-tareas.sh --tarea semana-05/tarea         # una tarea explícita
set -euo pipefail

if [[ "${1:-}" == "--tarea" ]]; then
  carpetas="${2:?falta la carpeta de la tarea}"
else
  base="${1:?falta el commit base}"
  cabeza="${2:?falta el commit cabeza}"
  # Un push que crea una rama trae base con ceros: no hay con qué comparar,
  # se compara contra el ancestro común con main.
  if [[ "$base" =~ ^0+$ ]]; then
    base="$(git merge-base "origin/main" "$cabeza" 2>/dev/null || git rev-list --max-parents=0 "$cabeza" | tail -1)"
  fi
  carpetas="$(git diff --name-only "$base" "$cabeza" -- 'semana-*/tarea/tarea-*.ipynb' \
    | xargs -r -n1 dirname | sort -u)"
fi

# Solo carpetas que de verdad tienen tests que correr.
salida=()
while IFS= read -r carpeta; do
  [[ -n "$carpeta" && -f "$carpeta/tests/test_tarea.py" ]] && salida+=("$carpeta")
done <<< "$carpetas"

if ((${#salida[@]} == 0)); then
  echo '[]'
else
  printf '%s\n' "${salida[@]}" | python3 -c 'import json,sys; print(json.dumps([l.strip() for l in sys.stdin if l.strip()]))'
fi
