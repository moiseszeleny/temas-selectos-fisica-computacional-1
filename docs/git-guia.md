# Guía de Git y GitHub para el curso

Cómo usar tu propio **fork** de este repositorio para entregar tareas.
Esta guía se usa **a partir de la semana 3**: las tareas de las semanas 1 y
2 se entregan por **Google Classroom**, porque Git todavía no se ha
enseñado.

## ¿Qué es un fork y por qué lo usamos?

Un *fork* es tu propia copia completa de este repositorio, en tu cuenta de
GitHub. Es tu "repositorio personal" del curso: ahí vives, ahí entregas tus
tareas, y de ahí traes el contenido nuevo que se publique cada semana.

No entregas tareas abriendo un PR contra este repositorio — entregas
abriendo un PR **dentro de tu propio fork**. Este repositorio nunca recibe
PRs de estudiantes directamente.

## 1. Haz fork de este repositorio

En la página de GitHub de este repositorio, da clic en el botón **Fork**
(arriba a la derecha) y confirma. Esto crea una copia completa en tu
cuenta, en `github.com/<tu-usuario>/temas-selectos-fisica-computacional-1`.

**Habilita GitHub Actions en tu fork (una sola vez).** GitHub desactiva los
workflows en los forks por seguridad. Entra a la pestaña **Actions** de tu
fork y da clic en el botón verde que confirma y habilita los workflows
(GitHub lo muestra en inglés: «I understand my workflows, go ahead and enable
them»).
Sin esto, el autograding de tus tareas nunca corre y tu PR no muestra
ningún check (ver [`docs/autograding.md`](autograding.md)).

## 2. Clona tu fork

```bash
git clone https://github.com/<tu-usuario>/temas-selectos-fisica-computacional-1.git
cd temas-selectos-fisica-computacional-1
```

## 3. Configura el repositorio del curso como `upstream`

Esto te permite traer el contenido nuevo que se publique cada semana en el
repositorio original (no en tu fork):

```bash
git remote add upstream https://github.com/moiseszeleny/temas-selectos-fisica-computacional-1.git
git remote -v   # deberías ver "origin" (tu fork) y "upstream" (el curso)
```

## 4. Trae el contenido nuevo cada semana

Antes de cada clase, sincroniza tu fork con lo último del curso:

```bash
git fetch upstream
git merge upstream/main
git push origin main
```

(Equivalente al botón **Sync fork** que aparece en la página de tu fork en
GitHub, si prefieres hacerlo desde la interfaz web.)

## 5. Resuelve tu tarea

Trabaja normalmente en tu fork: edita el notebook de la tarea, corre las
celdas, guarda. Trabaja en una rama por tarea (por ejemplo `tarea-03`): el
PR de entrega compara esa rama contra tu `main`, así que no puede ser `main`.

```bash
git switch -c tarea-03
git add semana-03/tarea/tarea-03.ipynb
git commit -m "Resuelve tarea 03"
git push -u origin tarea-03
```

## 6. Abre tu Pull Request de entrega **dentro de tu propio fork**

Este es el paso donde más se confunde la gente, porque GitHub por defecto
propone comparar contra el repositorio del curso (`upstream`), y **no** es
ahí donde debes abrir tu PR:

1. En la página de tu fork, ve a la pestaña **Pull requests** → **New pull
   request**.
2. Arriba aparecen dos repos ("base" y "compare"). Revisa el que dice
   **base repository**: si dice `moiseszeleny/temas-selectos-...`,
   cámbialo por `<tu-usuario>/temas-selectos-...` — el PR debe ser dentro
   de tu propio fork, no contra el repositorio del curso.
3. Selecciona como `base` tu rama `main` y como `compare` la rama con tu
   tarea resuelta (p. ej. `tarea-03`).
4. Crea el PR con un título breve (p. ej. "Tarea 03").

## Qué pasa después

Al abrir el PR, un workflow de GitHub Actions corre automáticamente los
tests de la tarea (`tarea/tests/`) y muestra un check ✅ o ❌ directo en tu
PR — no necesitas instalar ni correr nada especial para que esto pase, solo
tener tu notebook resuelto y haber habilitado Actions en tu fork (paso 1).
Qué debes ver, y qué hacer si sale ❌ o no aparece nada, está en
[`docs/autograding.md`](autograding.md). El asistente revisa tu PR y deja
comentarios línea por línea ahí mismo.

## Tu primer PR: agrégate al roster

Como práctica de Git de la semana 3, tu primer PR es agregar tu fila a
[`docs/roster.md`](roster.md) con tu usuario de GitHub y el link a tu fork
— así el asistente sabe dónde encontrar tus entregas.

## Problemas comunes

- **Mi PR se ve vacío o compara contra el repo equivocado** — revisa el
  selector "base repository" del paso 6; es el error más común.
- **`git merge upstream/main` trae conflictos** — normalmente porque
  modificaste un archivo de una semana anterior; resuelve el conflicto a
  mano y continúa (`git add <archivo>` seguido de `git commit`).
- **No veo el check de Actions en mi PR** — puede tardar uno o dos minutos
  en aparecer; si no aparece, revisa la pestaña "Actions" de tu fork
  (¿la habilitaste?) y la tabla de [`docs/autograding.md`](autograding.md).

Si algo no funciona, trae el error a clase o abre un Issue en tu fork.
