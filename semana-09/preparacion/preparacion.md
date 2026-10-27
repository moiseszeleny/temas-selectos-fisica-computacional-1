# Preparación — Semana 9

Hasta ahora las expresiones eran símbolos sin dimensión y la física era
clásica. Esta semana SymPy ayuda con dos cosas que todo físico necesita:
**unidades** (`sympy.physics.units`), para no sumar metros con segundos, y el
**álgebra de operadores** de la mecánica cuántica (`sympy.physics.quantum`),
donde el orden de los factores sí altera el producto. Cierra la semana el
oscilador armónico, resuelto sin una sola integral.

No hay dependencias nuevas: todo viene incluido en SymPy.

## Checklist

- [ ] Entregaste la tarea 08 por **Pull Request dentro de tu fork**, y el check
      de GitHub Actions quedó en ✅.

- [ ] Sincronizaste tu fork con el repositorio del curso:

  ```bash
  git switch main
  git pull upstream main
  git push origin main
  ```

- [ ] Tu entorno está activado y `python -c "import sympy; print(sympy.__version__)"`
      imprime `1.14.0`. Si no, revisa
      [`docs/instalacion.md`](../../docs/instalacion.md).

## Si quieres repasar

Nada de esto es obligatorio ni se evalúa:

- De tu curso de mecánica cuántica: el conmutador $[x, p] = i\hbar$ y los
  operadores de escalera $a$, $a^\dagger$ del oscilador armónico.
- Del álgebra lineal: las matrices de Pauli y sus eigenvalores.
- De la semana 6: `eigenvals()` y `eigenvects()`; los usamos para el espín.
- Del tutorial oficial de SymPy (en inglés), la página de
  [`physics.units`](https://docs.sympy.org/latest/modules/physics/units/index.html).

Como siempre: no lo estudies de más. Llegar con la duda es mejor que llegar con
la respuesta memorizada.

## Qué traer a la clase

Tu laptop con el entorno activado y el repositorio del curso sincronizado.
Trae papel: antes de que `Commutator` reduzca $[X, P^2]$, intenta hacerlo a
mano con la regla de Leibniz.
