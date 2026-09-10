# Tarea 05: Cálculo simbólico

Entrega antes de la clase de la Semana 6, por **Pull Request dentro de tu
propio fork** — el mismo flujo de las semanas 3 y 4. El paso a paso está en
[`docs/git-guia.md`](../../docs/git-guia.md).

## Qué entregar

`tarea-05.ipynb` con los dos `# TODO` completos, usando los nombres exactos
de variable que pide cada enunciado. No hay que escribir ningún archivo
`.py` ni tocar la carpeta `tests/`.

- **Ejercicio 1 (caso base):** el potencial de Lennard-Jones. Se califica
  que los símbolos lleven las suposiciones que la física garantiza (sin
  ellas, `solve` devuelve doce raíces complejas en lugar de una), que la
  fuerza salga de derivar el potencial y que la distancia de equilibrio
  salga de `solve`, no escrita a mano.
- **Ejercicio 2 (caso límite):** el oscilador forzado y la resonancia. Se
  califica el planteamiento de la ecuación, que la solución cumpla las dos
  condiciones iniciales, y que el límite $\Omega \to \omega$ se tome con
  `sp.limit` — sustituir no sirve ahí, porque el denominador se anula.

## Antes de entregar

- [ ] El notebook corre completo desde un kernel limpio
      (`Kernel → Restart & Run All`) y llega al final sin errores. Un
      notebook que no ejecuta completo no se puede calificar.
- [ ] Verificaste tus soluciones en lugar de creerles: `checkodesol` para
      la ecuación diferencial, y `sp.simplify(a - b) == 0` para cualquier
      resultado que quieras comparar con lo que esperabas.
- [ ] Todas las cantidades son **exactas**: `sp.Rational(1, 6)` en lugar de
      `0.1666`, `sp.pi` en lugar de `math.pi`. Un flotante suelto contamina
      la expresión entera, y hay un test que lo detecta.
- [ ] Contestaste, en la celda de markdown del final, la pregunta del
      ejercicio 2 sobre por qué la amplitud crece sin límite. Esa parte no
      la califica el autograding: la revisa el asistente.
- [ ] Tu rama de entrega está pusheada a **tu fork** (`origin`), y el PR se
      abrió **dentro de tu fork** — revisa el selector *base repository*.

Al abrir el PR, GitHub Actions corre `tests/test_tarea.py` y deja un check
✅ o ❌ en tu Pull Request. Si sale ❌, abre el check para ver qué test
falló: el nombre te dice qué habilidad quedó pendiente.
