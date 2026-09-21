# Tarea 07: Una cuenta en un aro que gira

Entrega antes de la clase de la Semana 8, por **Pull Request dentro de tu
propio fork** — el mismo flujo de las semanas 3 a 6. El paso a paso está en
[`docs/git-guia.md`](../../docs/git-guia.md).

## Qué entregar

`tarea-07.ipynb` con los cuatro `# TODO` completos, usando los nombres exactos
de variable que pide cada enunciado, y la celda de discusión contestada. No hay
que escribir ningún archivo `.py` ni tocar la carpeta `tests/`, ni cambiar la
celda de imports: `t`, `N` y `centro` ya vienen declarados y los tests los usan.

- **Ejercicio 1 (marcos):** los símbolos con sus suposiciones y los marcos del
  aro y de la cuenta, orientados con `orient_axis`. Se califica cada matriz de
  cosenos directores, así que un eje o un ángulo equivocado se detecta aquí y
  no tres ejercicios después.
- **Ejercicio 2 (cinemática del punto):** posición, velocidad y aceleración de
  la cuenta en `N`, obtenidas con `Point` — no derivando componentes a mano.
- **Ejercicio 3 (velocidad angular):** la velocidad angular de la cuenta y la
  comprobación de que $\boldsymbol{\omega} \times \mathbf{r}$ reproduce la
  velocidad del ejercicio 2.
- **Ejercicio 4 (interpretación):** la rapidez al cuadrado y la aceleración a lo
  largo del aro, simplificadas. La primera vuelve la semana que viene como
  parte de la energía cinética.

Los tests no comparan cadenas ni te exigen expresar los vectores en una base
particular: comparan la diferencia con el resultado esperado, escrita en `N` y
simplificada. Cualquier forma equivalente se da por buena.

## Antes de entregar

- [ ] El notebook corre completo desde un kernel limpio
      (`Kernel → Restart & Run All`) y llega al final sin errores. Un notebook
      que no ejecuta completo no se puede calificar.
- [ ] Verificaste tus soluciones en lugar de creerles: la diferencia entre
      `velocidad_transporte` y `velocidad`, expresada en `N` y simplificada,
      tiene que ser el vector cero.
- [ ] Los vectores están etiquetados con `Math` y `me.vlatex`, y los escalares
      con `sp.Eq`, como en clase.
- [ ] Todas las cantidades son **exactas**: `sp.Rational(1, 2)` en lugar de
      `0.5`. Un flotante suelto contamina la expresión entera, y hay un test que
      lo detecta.
- [ ] Contestaste las tres preguntas de la celda de discusión. Esa parte no la
      califica el autograding: la revisa el asistente.
- [ ] Tu rama de entrega está pusheada a **tu fork** (`origin`), y el PR se
      abrió **dentro de tu fork** — revisa el selector *base repository*.

Al abrir el PR, GitHub Actions corre `tests/test_tarea.py` y deja un check ✅ o
❌ en tu Pull Request. Si sale ❌, abre el check para ver qué test falló: el
nombre te dice qué habilidad quedó pendiente.
