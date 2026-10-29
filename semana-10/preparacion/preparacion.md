# Preparación — Semana 10

Esta semana cierra el Módulo 2 y no trae submódulos nuevos de SymPy. Cambia
otra cosa: tu código deja de ser solo tuyo. En la sesión 1 partimos un
notebook largo en un **módulo `.py`** y varios notebooks; en la sesión 2
**revisas el Pull Request de un compañero** y arrancas el **proyecto
intermedio**, que sustituye la tarea de esta semana.

No hay dependencias nuevas.

## Checklist

- [ ] Entregaste la tarea 09 por **Pull Request dentro de tu fork**. Esta vez
      importa doble: en la sesión 2 un compañero va a revisar ese PR, y tú el
      suyo. Si no hay PR, no hay nada que revisar.

- [ ] Sincronizaste tu fork con el repositorio del curso:

  ```bash
  git switch main
  git pull upstream main
  git push origin main
  ```

- [ ] Tu entorno está activado y `python -c "import sympy; print(sympy.__version__)"`
      imprime `1.14.0`. Si no, revisa
      [`docs/instalacion.md`](../../docs/instalacion.md).

- [ ] Puedes entrar a tu cuenta de GitHub desde el navegador de tu laptop. En
      la sesión 2 vas a crear un repositorio nuevo.

## Piensa en tu proyecto

El proyecto intermedio es un sistema físico **que eliges tú**, resuelto con
SymPy de principio a fin. Las instrucciones completas están en
[`../proyecto/README.md`](../proyecto/README.md). Antes de la sesión 2:

- Anota dos o tres sistemas que te interesen. Sirve cualquier cosa de tus
  cursos de física que se pueda atacar con lo de las semanas 4 a 9: un péndulo
  con algo extra, un circuito RLC, una órbita, un sistema de dos niveles...
- Si vas a trabajar en pareja, ponte de acuerdo **antes** de la clase: en la
  sesión 2 una de las dos personas crea el repositorio.

Lo que buscamos es un sistema pequeño que entiendas bien, no uno ambicioso.
Uno que puedas explicar en una hoja.

## Qué traer a la clase

Tu laptop con el entorno activado, el repositorio del curso sincronizado y tu
lista de sistemas candidatos.
