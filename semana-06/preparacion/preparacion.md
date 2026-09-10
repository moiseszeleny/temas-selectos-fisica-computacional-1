# Preparación — Semana 6

Esta semana sí estrenamos herramientas: además de SymPy vamos a usar **NumPy y
Matplotlib** para graficar. Ya venían en el `requirements.txt` del curso desde
la semana 1, así que no hay que instalar nada nuevo — pero sí conviene
comprobar que están.

Es también la semana que **cierra el Módulo 1**, y la tarea es el entregable
del módulo. Léela en cuanto salga, no el día antes.

## Checklist

- [ ] Tu entorno tiene las tres bibliotecas y en las versiones del curso:

  ```bash
  python -c "import sympy, numpy, matplotlib; print(sympy.__version__, numpy.__version__, matplotlib.__version__)"
  ```

  Debe imprimir `1.14.0 2.3.5 3.11.1`. Si falla, revisa
  [`docs/instalacion.md`](../../docs/instalacion.md).

- [ ] Una gráfica se ve dentro del notebook, no en una ventana aparte. Abre
      Jupyter, y en una celda:

  ```python
  import matplotlib.pyplot as plt

  fig, ax = plt.subplots()
  ax.plot([0, 1, 2], [0, 1, 4])
  plt.show()
  ```

  Si no aparece nada, agrega `%matplotlib inline` en una celda anterior y
  vuelve a intentar.

- [ ] Entregaste la tarea 05 por **Pull Request dentro de tu fork**, y el check
      de GitHub Actions quedó en ✅.

- [ ] Sincronizaste tu fork con el repositorio del curso para tener el material
      de esta semana:

  ```bash
  git switch main
  git pull upstream main
  git push origin main
  ```

- [ ] Recuerdas qué hace `lambdify` (semana 4). Esta semana es el puente entre
      lo simbólico y la gráfica, y lo vamos a usar todo el tiempo.

## Si quieres repasar

Nada de esto es obligatorio ni se evalúa:

- Del curso de álgebra lineal: qué es un eigenvector. La frase que conviene
  llevar a la sesión 1 es la geométrica — *una dirección que la matriz no
  cambia, solo estira o encoge*— y no la receta de calcular determinantes a
  mano, que de eso ya se encarga SymPy.
- De mecánica: por qué dos osciladores acoplados tienen **dos** frecuencias
  propias en lugar de una. Si nunca lo has visto, no importa: en la sesión 1 lo
  vamos a deducir, y el resultado es de los que se entienden mejor al verlos
  salir de la cuenta.
- Del tutorial oficial de SymPy (en inglés), la página de
  [matrices](https://docs.sympy.org/latest/tutorials/intro-tutorial/matrices.html)
  y la de
  [graficación](https://docs.sympy.org/latest/modules/plotting.html).
- Si nunca has usado Matplotlib más allá de `plt.plot`, la
  [guía rápida](https://matplotlib.org/stable/users/explain/quick_start.html)
  explica el patrón `fig, ax = plt.subplots()` que usamos en la sesión 2.

Como siempre: no lo estudies de más. Llegar con la duda es mejor que llegar con
la respuesta memorizada.

## Qué traer a la clase

Tu laptop con el entorno activado y el repositorio del curso sincronizado.

La sesión 1 es de puro álgebra simbólica; la sesión 2 es la primera del curso
en la que vas a producir gráficas, así que asegúrate antes de que Matplotlib
dibuje dentro del notebook — depurar eso en clase cuesta tiempo de todos.

Conviene también traer papel: los modos normales de la sesión 1 se entienden
mucho mejor dibujando las dos masas con flechitas que mirando el vector
$(-1, 1)$ en la pantalla.
