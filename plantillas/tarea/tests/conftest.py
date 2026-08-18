"""Infraestructura compartida para calificar tarea-NN.ipynb con pytest.

Los estudiantes no escriben ningún .py: todo vive en el notebook. Este
fixture ejecuta el notebook una sola vez por sesión de pytest con
`testbook` y expone el cliente (`tb`) para que los tests lean, vía
`tb.ref("<nombre_variable>")`, las variables que el estudiante calculó en
sus celdas. Los estudiantes no necesitan leer ni entender este archivo.
"""

import pathlib

import pytest
from testbook import testbook

NOTEBOOK_PATH = pathlib.Path(__file__).parent.parent / "tarea-NN.ipynb"


@pytest.fixture(scope="session")
def tb():
    with testbook(str(NOTEBOOK_PATH), execute=True) as tb:
        yield tb
