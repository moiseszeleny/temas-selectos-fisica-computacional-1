"""Tests públicos de tarea-NN.ipynb — visibles para el estudiante.

Cubren el caso base de cada habilidad evaluada. Nombra cada test describiendo
la habilidad que evalúa, no como test_1, test_2, etc.
"""

import sympy as sp


# TODO: renombra este test según la habilidad real evaluada, p. ej.
# test_derivada_parcial_correcta. Se deja como ejemplo funcional de la
# plantilla; reemplázalo por el/los test(s) de la tarea real.
def test_derivada_correcta(tb):
    # x debe tener las mismas suposiciones que en el notebook (real=True):
    # sp.simplify solo cancela si ambos lados usan el mismo símbolo.
    x = sp.symbols("x", real=True)
    esperado = 3 * x**2

    # Patrón str(...) + sp.sympify(...): ver por qué en conftest.py.
    resultado = sp.sympify(tb.ref("str(resultado_derivada)"), locals={"x": x})

    assert sp.simplify(resultado - esperado) == 0
