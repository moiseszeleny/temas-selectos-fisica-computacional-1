# Preparación — Semana 4

Esta semana empieza el Módulo 1 y, con él, SymPy. La herramienta nueva no
requiere instalar nada aparte: ya viene en el `requirements.txt` del curso.
Lo que sí hace falta es que el entorno y el flujo de entrega de la semana 3
estén funcionando, porque a partir de aquí no los volvemos a revisar.

## Checklist

- [ ] SymPy responde en tu entorno **activado**:

  ```bash
  python -c "import sympy; print(sympy.__version__)"
  ```

  Debe imprimir `1.14.0`. Si dice `ModuleNotFoundError`, instala las
  dependencias del curso con `pip install -r requirements.txt` desde la
  raíz del repositorio (ver [`docs/instalacion.md`](../../docs/instalacion.md)).

- [ ] Entregaste la tarea 03 por **Pull Request dentro de tu fork**, y el
      check de GitHub Actions quedó en ✅. Si sigue en ❌, abre el check y
      resuelve el test que falla antes de la clase.

- [ ] Tu fila ya está en [`docs/roster.md`](../../docs/roster.md) del
      repositorio del curso. Es lo que permite que el asistente encuentre
      tus entregas.

- [ ] Sincronizaste tu fork con el repositorio del curso, para tener el
      material de esta semana:

  ```bash
  git switch main
  git pull upstream main
  git push origin main
  ```

- [ ] Puedes explicar, sin ver apuntes, por qué en Python `1/3` no es
      exactamente un tercio. En SymPy esa diferencia importa mucho, y la
      vamos a usar el primer día.

## Si quieres repasar

Nada de esto es obligatorio ni se evalúa:

- El [tutorial oficial de SymPy](https://docs.sympy.org/latest/tutorials/intro-tutorial/index.html)
  (en inglés). Si vas a leer una sola página, que sea
  ["Gotchas"](https://docs.sympy.org/latest/tutorials/intro-tutorial/gotchas.html):
  recoge justo las trampas con las que vamos a tropezar en clase a propósito.
- De la semana 2, la idea de que un objeto matemático **no debe poder
  modificarse**. Los objetos de SymPy son inmutables por la misma razón, y
  eso explica por qué todas sus funciones devuelven una expresión nueva en
  lugar de cambiar la que reciben.
- Del lado de la física, ten a la mano las fórmulas que vamos a usar como
  ejemplos: energía cinética, periodo del péndulo simple, energía del
  oscilador armónico y tiro parabólico. No hay que deducir ninguna — solo
  las vamos a escribir en SymPy.

Como siempre: no lo estudies de más. La clase está diseñada para construir
todo desde cero, y llegar con la duda es mejor que llegar con la respuesta
memorizada.

## Qué traer a la clase

Tu laptop con el entorno activado y el repositorio del curso sincronizado.

La sesión 1 es de símbolos y suposiciones: vas a teclear expresiones y a
verlas por dentro. La sesión 2 es de manipulación y evaluación, y termina
graficando — así que asegúrate de que Matplotlib te funcione dentro del
notebook, como en la semana 1.
