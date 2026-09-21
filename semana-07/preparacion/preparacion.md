# Preparación — Semana 7

Empieza el **Módulo 2**: SymPy aplicado a la física. Esta semana entramos a
`sympy.physics.mechanics`, el submódulo de mecánica clásica. Viene incluido en
SymPy, así que no hay nada nuevo que instalar — pero sí conviene comprobarlo.

## Checklist

- [ ] Tu entorno importa el submódulo y en la versión del curso:

  ```bash
  python -c "import sympy, sympy.physics.mechanics; print(sympy.__version__)"
  ```

  Debe imprimir `1.14.0`. Si falla, revisa
  [`docs/instalacion.md`](../../docs/instalacion.md).

- [ ] Entregaste la tarea 06 —el entregable del Módulo 1— por **Pull Request
      dentro de tu fork**, y el check de GitHub Actions quedó en ✅.

- [ ] Sincronizaste tu fork con el repositorio del curso para tener el material
      de esta semana:

  ```bash
  git switch main
  git pull upstream main
  git push origin main
  ```

- [ ] Recuerdas qué significa que una matriz sea **ortogonal** y qué es un
      eigenvector (semana 6). Las matrices de rotación de la sesión 1 son
      ortogonales, y los ejes principales de inercia son eigenvectores.

## Si quieres repasar

Nada de esto es obligatorio ni se evalúa:

- De tus cursos de mecánica: el producto cruz y la regla de la mano derecha.
  En la sesión 1 SymPy hace las cuentas, pero conviene poder predecir hacia
  dónde apunta un torque antes de verlo salir.
- Las coordenadas polares, y la pregunta de por qué la aceleración en polares
  tiene **cuatro** términos y no dos. Si nunca te convenció la deducción del
  libro, mejor: en la sesión 2 la vamos a obtener en tres líneas.
- Del tutorial oficial de SymPy (en inglés), la introducción a
  [vectores y marcos de referencia](https://docs.sympy.org/latest/modules/physics/vector/vectors.html)
  y la de
  [cinemática](https://docs.sympy.org/latest/modules/physics/vector/kinematics.html).

Como siempre: no lo estudies de más. Llegar con la duda es mejor que llegar con
la respuesta memorizada.

## Qué traer a la clase

Tu laptop con el entorno activado y el repositorio del curso sincronizado.

Trae también papel. Esta semana es la más geométrica del curso: los marcos
rotados, las direcciones de las velocidades y la aceleración de Coriolis se
entienden mucho mejor dibujando ejes con flechitas que mirando
$\hat{b}_x$ en la pantalla.
