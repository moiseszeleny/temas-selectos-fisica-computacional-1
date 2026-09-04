"""Infraestructura compartida para calificar la tarea con pytest.

Los estudiantes no escriben ningún .py: todo vive en el notebook. El
fixture `tb` ejecuta el notebook una sola vez por sesión de pytest con
`testbook` y expone el cliente para que los tests lean, vía
`tb.ref("<expresión>")`, las variables que el estudiante calculó en sus
celdas.

`tb.ref()` solo transfiere a Python valores serializables a JSON, y los
objetos de SymPy no lo son: por eso los tests piden `str(<variable>)` y
reconstruyen el resultado con `sp.sympify(..., locals={...})`, pasando los
mismos símbolos (con las mismas suposiciones) que declara el notebook — ver
el patrón completo en `test_tarea.py`. Los estudiantes no necesitan leer ni
entender este archivo.
"""

import pathlib

import pytest
from testbook import testbook

TAREA_DIR = pathlib.Path(__file__).parent.parent


def _encontrar_notebook() -> pathlib.Path:
    """Ubica el notebook de la tarea sin asumir un nombre de archivo fijo.

    Se busca por patrón (`tarea-*.ipynb`), no por el nombre literal de la
    plantilla, porque el notebook se renombra al adaptarla a la semana real
    (p. ej. `tarea-07.ipynb`) — así no hace falta tocar este archivo al
    hacerlo.
    """
    notebooks = sorted(TAREA_DIR.glob("tarea-*.ipynb"))
    if not notebooks:
        raise FileNotFoundError(
            f"No se encontró ningún notebook 'tarea-*.ipynb' en {TAREA_DIR}"
        )
    if len(notebooks) > 1:
        raise RuntimeError(
            f"Se esperaba un solo notebook de tarea en {TAREA_DIR}, se "
            f"encontraron {len(notebooks)}: {notebooks}"
        )
    return notebooks[0]


NOTEBOOK_PATH = _encontrar_notebook()


@pytest.fixture(scope="session")
def tb():
    with testbook(str(NOTEBOOK_PATH), execute=True) as tb:
        yield tb
