Después de cada merge en GitHub:

```bash
git checkout main
git pull --ff-only
git branch -d nombre-de-la-rama          # borra la rama local ya fusionada
git push origin --delete nombre-de-la-rama   # borra la rama remota ya fusionada
```

- `git checkout main` — te regresa a la rama principal.
- `git pull --ff-only` — trae el merge commit que se generó en GitHub. El `--ff-only` es solo una precaución para que falle limpiamente si por algo tu `main` local se desvió, en vez de crear un merge commit inesperado.
- `git branch -d` — borra la rama local; `-d` (minúscula) se niega a borrar si la rama tuviera commits no fusionados, así que es seguro.
- `git push origin --delete` — borra la rama remota; opcional si ya la borraste desde el botón de GitHub al mergear el PR (en ese caso este comando falla porque ya no existe, sin problema).

Si el PR se mergeó con "squash" o "rebase" en vez de merge commit normal, `git pull --ff-only` puede fallar porque el historial local y remoto divergen — en ese caso el equivalente es simplemente `git fetch origin && git reset --hard origin/main` (perdiendo los commits locales de esa rama, que ya están integrados igual en el squash).