"""Tests públicos de tarea-01.ipynb — visibles para el estudiante.

Cubren el caso base de cada habilidad evaluada. A diferencia de las tareas
de semanas posteriores (donde los resultados son objetos de SymPy y hace
falta el patrón `str(...)` + `sp.sympify(...)`), aquí los resultados son
valores de NumPy: `tb.ref(...)` los trae directo, sin pasos intermedios —
ver el porqué de esa diferencia en `conftest.py`.
"""

import numpy as np


def test_media_y_desviacion_correctas(tb):
    mediciones = np.array([2.3, 2.5, 2.1, 2.4, 2.6, 2.2, 2.5, 2.3])

    media = tb.ref("float(media)")
    desviacion_estandar = tb.ref("float(desviacion_estandar)")

    assert np.isclose(media, np.mean(mediciones))
    assert np.isclose(desviacion_estandar, np.std(mediciones))
