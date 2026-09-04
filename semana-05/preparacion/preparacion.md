# Preparación — Semana 5

Esta semana no hay herramienta nueva que instalar: seguimos en SymPy, que
ya usaste la semana pasada. Lo que cambia es el tipo de operación —
pasamos del álgebra al cálculo— así que la preparación es sobre todo
matemática.

## Checklist

- [ ] Tu entorno sigue funcionando (es el mismo de la semana 4):

  ```bash
  python -c "import sympy; print(sympy.__version__)"
  ```

  Debe imprimir `1.14.0`. Si falla, revisa
  [`docs/instalacion.md`](../../docs/instalacion.md).

- [ ] Entregaste la tarea 04 por **Pull Request dentro de tu fork**, y el
      check de GitHub Actions quedó en ✅.

- [ ] Sincronizaste tu fork con el repositorio del curso para tener el
      material de esta semana:

  ```bash
  git switch main
  git pull upstream main
  git push origin main
  ```

- [ ] Puedes escribir, sin ver apuntes, la receta de la semana 4 para
      decidir si dos expresiones son matemáticamente iguales. La vamos a
      usar todo el tiempo para verificar resultados.

- [ ] Recuerdas que `sp.Rational(1, 2)` y `1/2` no son lo mismo. Sigue
      siendo el error más frecuente, y esta semana se propaga a través de
      derivadas e integrales.

## Si quieres repasar

Nada de esto es obligatorio ni se evalúa:

- Del curso de cálculo: qué es un desarrollo de Taylor y qué significa el
  término de error. En la sesión 1 lo vamos a usar para *deducir* dos
  aproximaciones que ya conoces de física — la de ángulos pequeños del
  péndulo y el límite newtoniano de la energía relativista.
- De ecuaciones diferenciales: por qué una ecuación de segundo orden
  necesita **dos** condiciones iniciales. En la sesión 2 eso deja de ser
  una regla memorizada y se vuelve visible: `dsolve` devuelve `C1` y `C2`,
  y `ics` es lo que las fija.
- Del tutorial oficial de SymPy (en inglés), la página de
  [cálculo](https://docs.sympy.org/latest/tutorials/intro-tutorial/calculus.html)
  y la de [resolvedores](https://docs.sympy.org/latest/tutorials/intro-tutorial/solvers.html).
  Cubren justo lo de estas dos sesiones.
- Ten a la mano las fórmulas que vamos a usar como ejemplos: potencial
  gravitatorio, ley de Hooke, velocidad de escape, tiro parabólico,
  máquina de Atwood y oscilador armónico. No hay que deducir ninguna de
  memoria: varias las vamos a deducir en clase, que es justo el punto.

Como siempre: no lo estudies de más. Llegar con la duda es mejor que
llegar con la respuesta memorizada.

## Qué traer a la clase

Tu laptop con el entorno activado y el repositorio del curso sincronizado.

Las dos sesiones son de puro SymPy, sin gráficas: no necesitas nada que no
hayas usado ya. Lo que sí conviene traer es papel, porque varios resultados
de la semana se verifican mejor comparándolos con lo que uno esperaría a
mano.
