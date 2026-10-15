# Tarea 09: Constantes atómicas, conmutadores y espín

Entrega antes de la clase de la Semana 10, por **Pull Request dentro de tu
propio fork** — el mismo flujo de las semanas 3 a 8. El paso a paso está en
[`docs/git-guia.md`](../../docs/git-guia.md).

## Qué entregar

`tarea-09.ipynb` con los cuatro `# TODO` completos, usando los nombres exactos
de variable que pide cada enunciado, y la celda de discusión contestada. No hay
que escribir ningún archivo `.py` ni tocar la carpeta `tests/`, ni cambiar la
celda de imports: `hbar`, `m` y `omega` ya vienen declarados y los tests los
usan.

- **Ejercicio 1 (unidades):** la energía de Rydberg escrita con las constantes
  de `sympy.physics.units`, su dimensión y su valor en eV.
- **Ejercicio 2 (conmutadores):** $[X, P^2]$ y $[X^2, P]$ a partir de
  $[X, P] = i\hbar$.
- **Ejercicio 3 (espín):** la matriz del espín 1/2 en una dirección
  arbitraria y sus eigenvalores.
- **Ejercicio 4 (oscilador):** $\langle x^2\rangle$, la energía y el teorema
  del virial para $n = 4$.

Los tests no comparan cadenas: restan tu resultado de la respuesta esperada y
simplifican. Una forma equivalente de escribirlo se da por buena.

## Antes de entregar

- [ ] El notebook corre completo desde un kernel limpio
      (`Kernel → Restart & Run All`) y llega al final sin errores. Un notebook
      que no ejecuta completo no se puede calificar.
- [ ] Los resultados están mostrados con `display` o `sp.Eq`, como en clase.
- [ ] Todas las cantidades son **exactas**: `sp.Rational(1, 2)` en lugar de
      `0.5`. Solo `rydberg_en_ev` es un decimal, a propósito.
- [ ] Contestaste las tres preguntas de la celda de discusión. Esa parte no la
      califica el autograding: la revisa el asistente.
- [ ] Tu rama de entrega está pusheada a **tu fork** (`origin`), y el PR se
      abrió **dentro de tu fork** — revisa el selector *base repository*.

Al abrir el PR, GitHub Actions corre `tests/test_tarea.py` y deja un check ✅ o
❌ en tu Pull Request. Si sale ❌, abre el check para ver qué test falló: el
nombre te dice qué habilidad quedó pendiente.
