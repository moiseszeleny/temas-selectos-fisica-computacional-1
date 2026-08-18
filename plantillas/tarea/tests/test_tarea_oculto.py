"""Tests OCULTOS de tarea-NN.ipynb.

============================================================================
 ADVERTENCIA: este archivo NO se debe commitear al repositorio que reciben
 los estudiantes en GitHub Classroom. Vive aquí, en la plantilla, como
 referencia; al preparar el assignment real se agrega por separado (rama o
 repo privado de calificación), nunca en el repo base que se les entrega.
============================================================================

Cubren casos límite de la misma habilidad que ya evalúan los tests
públicos. Su peso combinado no debe superar el 30% del puntaje de la tarea
(regla de CLAUDE.md).
"""

import sympy as sp


# TODO: renombra este test según la habilidad real evaluada, p. ej.
# test_derivada_parcial_caso_simbolico. Se deja como ejemplo funcional de la
# plantilla; reemplázalo por el/los test(s) ocultos de la tarea real.
def test_derivada_caso_general(tb):
    # Las suposiciones deben coincidir exactamente con las del notebook
    # (x: real; n: positive, integer) para que sp.simplify pueda cancelar.
    x = sp.symbols("x", real=True)
    n = sp.symbols("n", positive=True, integer=True)
    esperado = n * x ** (n - 1)

    # Patrón str(...) + sp.sympify(...): ver por qué en conftest.py.
    resultado = sp.sympify(
        tb.ref("str(resultado_derivada_general)"), locals={"x": x, "n": n}
    )

    assert sp.simplify(resultado - esperado) == 0
