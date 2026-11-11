# Preparación — Semana 11

Esta semana es el Módulo 3 completo: cómo se organiza y se prueba el código de
un proyecto científico. En la sesión 1 el módulo del oscilador se vuelve un
**paquete** con **pruebas de pytest**; en la sesión 2 esas pruebas corren
solas en GitHub (**integración continua**), organizas lo pendiente con
**issues** y revisas el **PR preliminar** del proyecto intermedio de un
compañero.

No hay dependencias nuevas: `pytest` ya venía en `requirements.txt` desde el
principio del curso, porque es lo que corre el autograding de tus tareas.

## Checklist

- [ ] Abriste tu **PR preliminar** `desarrollo → main` en tu repositorio
      `proyecto-intermedio`, **sin fusionar**, con el modelo planteado y al
      menos un resultado verificado (ver
      [`../../semana-10/proyecto/README.md`](../../semana-10/proyecto/README.md)).
      En la sesión 2 un compañero lo revisa: si no hay PR, no hay nada que
      revisar.

- [ ] Sincronizaste tu fork con el repositorio del curso:

  ```bash
  git switch main
  git pull upstream main
  git push origin main
  ```

- [ ] Tu entorno está activado y responde así:

  ```bash
  python -c "import sympy; print(sympy.__version__)"   # 1.14.0
  python -m pytest --version                            # pytest 9.1.1
  ```

  Si no, revisa [`docs/instalacion.md`](../../docs/instalacion.md).

- [ ] Tienes clonado `proyecto-intermedio` en tu laptop y puedes entrar a tu
      cuenta de GitHub desde el navegador.

## Lectura breve

Antes de la sesión 1, abre
[`.github/workflows/autograding.yml`](../../.github/workflows/autograding.yml),
en la raíz del repo del curso. Es lo que pone el ✅ o ❌ en tus PRs de tarea
desde la semana 3. No hace falta entenderlo todo; busca las líneas que dicen
`pip install` y `pytest` y piensa qué hacen. En la sesión 2 lo leemos juntos.

## Qué traer a la clase

Tu laptop con el entorno activado, el fork sincronizado, tu repositorio
`proyecto-intermedio` clonado y el link de tu PR preliminar.
