"""Tests OCULTOS de tarea-01.ipynb.

============================================================================
 ADVERTENCIA: este archivo NO se debe commitear al repositorio que reciben
 los estudiantes en GitHub Classroom. Vive aquí, en el repo fuente del
 curso, como referencia para el autograding; al preparar el assignment real
 se agrega por separado (rama o repo privado de calificación), nunca en el
 repo base que se les entrega. Ver `README.md`.
============================================================================

Cubren un caso límite: la misma habilidad de operar con NumPy, pero exigiendo
vectorización sobre un arreglo generado (no sobre datos fijos como en el
test público). Su peso combinado no debe superar el 30% del puntaje de la
tarea.
"""

import numpy as np


def test_posiciones_mrua_vectorizadas_correctas(tb):
    x0, v0, a = 0.0, 5.0, -9.8
    tiempos_esperados = np.linspace(0, 1, 50)
    posiciones_esperadas = x0 + v0 * tiempos_esperados + 0.5 * a * tiempos_esperados**2

    tiempos = np.array(tb.ref("tiempos.tolist()"))
    posiciones = np.array(tb.ref("posiciones.tolist()"))

    assert tiempos.shape == (50,)
    assert np.allclose(tiempos, tiempos_esperados)
    assert np.allclose(posiciones, posiciones_esperadas)
