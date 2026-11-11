# Tarea 11: Pruebas que atrapan errores

Entrega antes de la clase de la Semana 12, por **Pull Request dentro de tu
propio fork**, con el mismo flujo de las semanas 3 a 9. El paso a paso está en
[`docs/git-guia.md`](../../docs/git-guia.md).

Esta semana también vence la entrega final del proyecto intermedio: la tarea es
corta a propósito.

## Qué entregar

`tarea-11.ipynb` con las cuatro funciones de prueba completas, con los nombres
exactos que pide cada enunciado, y la celda de discusión contestada. No toques
la celda de `funcion_de_onda` y `energia_caja`, ni la carpeta `tests/`.

- **Ejercicio 1:** `test_funcion_de_onda_normalizada`, para $n = 1, 2, 3$.
- **Ejercicio 2:** `test_estados_ortogonales`, todos los pares distintos
  entre 1 y 3.
- **Ejercicio 3:** `test_cumple_schrodinger_y_se_anula_en_las_paredes`, para
  $n = 1, 2, 3$.
- **Ejercicio 4:** `test_nivel_no_valido_lanza_error`, con `pytest.raises`
  para $n = 0$, $-1$ y $\tfrac12$ en las dos funciones.

## Cómo se califica

Al revés que en las tareas anteriores: el autograding no revisa resultados,
revisa **tus pruebas**. Cada una se corre dos veces:

1. Con las funciones correctas del notebook: debe **pasar**.
2. Con versiones que traen un error plantado: debe **fallar**. Los errores
   plantados están en `MUTANTES`, al principio de
   [`tests/test_tarea.py`](tests/test_tarea.py), a la vista.

Si un test del autograding falla, su mensaje dice qué error plantado se le
escapó a tu prueba. Las pruebas comparan por equivalencia simbólica,
`sp.simplify(resultado - esperado) == 0`, como en clase.

## Antes de entregar

- [ ] El notebook corre completo desde un kernel limpio
      (`Kernel → Restart & Run All`) y llega al final sin errores. Un notebook
      que no ejecuta completo no se puede calificar.
- [ ] Debajo de cada prueba se imprime que pasó con las funciones correctas.
- [ ] Probaste al menos una prueba a mano contra una función con un error:
      redefínela en una celda de borrador, corre tu prueba, comprueba que
      truena y **borra esa celda** antes del commit.
- [ ] Contestaste las tres preguntas de la celda de discusión. Esa parte no la
      califica el autograding: la revisa el asistente.
- [ ] Tu rama de entrega está pusheada a **tu fork** (`origin`), y el PR se
      abrió **dentro de tu fork**: revisa el selector *base repository*.

Al abrir el PR, GitHub Actions corre `tests/test_tarea.py` y deja un check ✅ o
❌. Desde la sesión 2 de esta semana sabes qué hay detrás: el workflow
`.github/workflows/autograding.yml` del curso, la misma receta que escribiste
para tu proyecto.
