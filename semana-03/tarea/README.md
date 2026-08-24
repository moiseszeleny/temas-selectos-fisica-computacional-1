# Tarea 03: Notebooks bajo control de versiones

Entrega antes de la clase de la Semana 4. Es la primera tarea que se
entrega por **Pull Request dentro de tu propio fork**, no por Google
Classroom: el paso a paso está en
[`docs/git-guia.md`](../../docs/git-guia.md).

## Qué entregar

Son **dos entregas**, y las dos cuentan.

### 1. Tu Pull Request al roster

Tu primer PR del curso: agregar tu fila a `docs/roster.md` con tu usuario
de GitHub y el enlace a tu fork, para que el asistente sepa dónde encontrar
tus entregas. Checklist:

- [ ] Hiciste **fork** del repositorio del curso y lo clonaste.
- [ ] `git remote -v` muestra dos remotos: `origin` (tu fork) y `upstream`
      (el repositorio del curso).
- [ ] Agregaste **tu fila** a la tabla de `docs/roster.md`, sin tocar las
      de los demás.
- [ ] Abriste el PR **dentro de tu propio fork** — revisa el selector
      *base repository*: debe decir `<tu-usuario>/...`, no
      `moiseszeleny/...`. Es el error más común.

### 2. El notebook resuelto

Completa los `# TODO` de `tarea-03.ipynb` con los nombres exactos de
función y las reglas que pide cada enunciado. No necesitas escribir ningún
archivo `.py` ni tocar la carpeta `tests/`.

El ejercicio 2 **reusa** la función del ejercicio 1: no la vuelvas a
escribir, llámala.

## Antes de entregar

Corre tu notebook completo desde un kernel limpio (`Kernel → Restart & Run
All`) y confirma que llega hasta el final sin errores. Un notebook que no
ejecuta completo no se puede calificar.

Al abrir el PR, GitHub Actions corre `tests/test_tarea.py` y deja un check
✅ o ❌ en tu Pull Request. Si sale ❌, abre el check para ver qué test
falló: el nombre te dice qué habilidad quedó pendiente.
