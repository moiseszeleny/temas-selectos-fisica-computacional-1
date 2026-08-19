"""Tests públicos de tarea-01.ipynb — visibles para el estudiante.

Cubren ambas habilidades evaluadas de la tarea. A diferencia de las tareas
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


def test_posiciones_mrua_vectorizadas_correctas(tb):
    x0, v0, a = 0.0, 5.0, -9.8
    tiempos_esperados = np.linspace(0, 1, 50)
    posiciones_esperadas = x0 + v0 * tiempos_esperados + 0.5 * a * tiempos_esperados**2

    tiempos = np.array(tb.ref("tiempos.tolist()"))
    posiciones = np.array(tb.ref("posiciones.tolist()"))

    assert tiempos.shape == (50,)
    assert np.allclose(tiempos, tiempos_esperados)
    assert np.allclose(posiciones, posiciones_esperadas)
