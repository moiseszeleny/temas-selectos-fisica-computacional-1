# Preparación — Semana 8

La semana pasada hicimos cinemática: dónde está cada cosa y cómo se mueve.
Esta semana pasamos a la **dinámica**: `sympy.physics.mechanics` va a generar
las ecuaciones de movimiento por nosotros, con los métodos de Lagrange y de
Kane, y en la sesión 2 las vamos a **integrar numéricamente** para ver al
péndulo doble moverse.

Para eso hay una dependencia nueva: **SciPy**, que trae el integrador
`solve_ivp`. Es lo único que hay que instalar.

## Checklist

- [ ] Entregaste la tarea 07 por **Pull Request dentro de tu fork**, y el check
      de GitHub Actions quedó en ✅.

- [ ] Sincronizaste tu fork con el repositorio del curso, para tener el
      material de esta semana y el `requirements.txt` actualizado:

  ```bash
  git switch main
  git pull upstream main
  git push origin main
  ```

- [ ] Con tu entorno activado, instalaste las dependencias otra vez. `pip`
      solo agrega lo que falta, así que es rápido:

  ```bash
  pip install -r requirements.txt
  ```

  Si usas GitHub Codespaces, crea un codespace nuevo después de sincronizar:
  la configuración instala todo sola.

- [ ] Tu entorno importa SciPy en la versión del curso:

  ```bash
  python -c "import scipy; print(scipy.__version__)"
  ```

  Debe imprimir `1.17.1`. Si falla, revisa
  [`docs/instalacion.md`](../../docs/instalacion.md).

- [ ] Tienes a la mano tu `TODO en clase 2` de la semana 7 —la rapidez al
      cuadrado de la segunda masa del péndulo doble— y tu ejercicio 4 de la
      tarea 07. Los dos reaparecen esta semana como energías cinéticas.

## Si quieres repasar

Nada de esto es obligatorio ni se evalúa:

- De tu curso de mecánica: el Lagrangiano $\mathcal{L} = T - V$ y las
  ecuaciones de Euler-Lagrange. Si puedes escribir las del péndulo simple a
  mano, llegas perfecto; en la sesión 1 empezamos justo por ahí.
- De la semana 6: los modos normales como eigenvectores de $M^{-1}K$. Al final
  de la sesión 1 los sacamos para el péndulo doble.
- Del tutorial oficial de SymPy (en inglés), los ejemplos de
  [`LagrangesMethod`](https://docs.sympy.org/latest/modules/physics/mechanics/lagrange.html)
  y de
  [`KanesMethod`](https://docs.sympy.org/latest/modules/physics/mechanics/kane.html).
  El método de Kane seguramente no lo viste en tus cursos: no te preocupes, en
  la sesión 2 lo presentamos desde cero y solo en la medida en que lo vamos a
  usar.

Como siempre: no lo estudies de más. Llegar con la duda es mejor que llegar con
la respuesta memorizada.

## Qué traer a la clase

Tu laptop con el entorno activado, SciPy instalado y el repositorio del curso
sincronizado.

Trae también papel. Antes de que `mechanics` escriba las ecuaciones de un
péndulo elástico, vale la pena que intentes adivinar qué términos van a
aparecer: la aceleración centrípeta y la de Coriolis de la semana pasada
vuelven a salir, ahora dentro de las ecuaciones de movimiento.
