"""Tests públicos de tarea-NN.ipynb — visibles para el estudiante.

Cubren el caso base de cada habilidad evaluada. Nombra cada test describiendo
la habilidad, no como test_1, test_2, etc. (ver CLAUDE.md).
"""

import sympy as sp


# TODO: renombra este test según la habilidad real evaluada, p. ej.
# test_derivada_parcial_correcta. Se deja como ejemplo funcional de la
# plantilla; reemplázalo por el/los test(s) de la tarea real.
def test_derivada_correcta(tb):
    x = sp.symbols("x", real=True)
    esperado = 3 * x**2

    # tb.ref() solo transfiere valores serializables a JSON: los objetos de
    # SymPy no lo son, así que se pide la representación en texto y se
    # reconstruye acá con las mismas suposiciones que declara el notebook.
    resultado = sp.sympify(tb.ref("str(resultado_derivada)"), locals={"x": x})

    assert sp.simplify(resultado - esperado) == 0
