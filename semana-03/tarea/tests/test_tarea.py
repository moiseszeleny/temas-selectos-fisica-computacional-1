"""Tests públicos de tarea-03.ipynb — visibles para el estudiante.

Cubren las habilidades evaluadas de los dos ejercicios. Esta semana la
tarea trabaja sobre notebooks representados como diccionarios, y eso
simplifica la mecánica respecto a otras semanas: un diccionario de listas,
cadenas y enteros **sí** es serializable a JSON, así que `tb.ref()` puede
traer el resultado tal cual, sin el rodeo de `str(...)` que necesitan los
objetos de SymPy (ver `conftest.py`).

Lo que sí hace falta es *construir* los notebooks de prueba dentro del
kernel del notebook, porque es ahí donde viven las funciones del
estudiante. De eso se encarga la fixture `ayudantes`, que inyecta tres
constructores mínimos. Como la fixture `tb` es de sesión y el kernel se
comparte entre tests, todo lo que se inyecta lleva un guion bajo inicial
para no chocar con los nombres del estudiante.
"""

import pytest


@pytest.fixture(scope="session")
def ayudantes(tb):
    """Inyecta en el kernel constructores para armar notebooks de prueba."""
    tb.inject(
        """
        def _codigo(fuente, salidas=None, contador=None):
            return {
                "cell_type": "code",
                "execution_count": contador,
                "metadata": {},
                "outputs": [] if salidas is None else salidas,
                "source": [fuente],
            }

        def _markdown(fuente):
            return {"cell_type": "markdown", "metadata": {}, "source": [fuente]}

        def _notebook(*celdas):
            return {
                "cells": list(celdas),
                "metadata": {},
                "nbformat": 4,
                "nbformat_minor": 5,
            }

        _salida = [{"output_type": "stream", "name": "stdout", "text": ["42"]}]
        """
    )


def test_limpiar_salidas_vacia_las_salidas_de_las_celdas_de_codigo(tb, ayudantes):
    tb.inject(
        """
        _nb = _notebook(_codigo("print(42)", _salida, 3), _markdown("# Titulo"))
        _limpio = limpiar_salidas(_nb)
        """
    )

    assert tb.ref("_limpio['cells'][0]['outputs']") == []


def test_limpiar_salidas_reinicia_execution_count(tb, ayudantes):
    # La comparación con None se hace dentro del kernel: `tb.ref()` traería
    # el None de vuelta como la cadena "None", no como el objeto.
    tb.inject(
        """
        _nb = _notebook(_codigo("print(42)", _salida, 3))
        _contador_reiniciado = (
            limpiar_salidas(_nb)["cells"][0]["execution_count"] is None
        )
        """
    )

    assert tb.ref("_contador_reiniciado") is True


def test_limpiar_salidas_conserva_el_resto_del_notebook(tb, ayudantes):
    # Quitar salidas no debe tocar nada más: ni el código, ni las celdas de
    # markdown (que no tienen 'outputs' ni 'execution_count' — tampoco hay
    # que agregárselos), ni las llaves de nivel superior del notebook.
    tb.inject(
        """
        _nb = _notebook(_codigo("print(42)", _salida, 3), _markdown("# Titulo"))
        _limpio = limpiar_salidas(_nb)
        """
    )

    assert tb.ref("_limpio['cells'][0]['source']") == ["print(42)"]
    assert tb.ref("_limpio['cells'][1]") == {
        "cell_type": "markdown",
        "metadata": {},
        "source": ["# Titulo"],
    }
    assert tb.ref("_limpio['nbformat']") == 4


def test_limpiar_salidas_no_modifica_el_notebook_original(tb, ayudantes):
    # La función devuelve un notebook nuevo: el que recibe sigue teniendo
    # sus salidas después de llamarla.
    tb.inject(
        """
        _nb = _notebook(_codigo("print(42)", _salida, 3))
        _copia_limpia = limpiar_salidas(_nb)
        _salidas_originales = _nb["cells"][0]["outputs"]
        _contador_original = _nb["cells"][0]["execution_count"]
        """
    )

    # La copia sí quedó limpia...
    assert tb.ref("_copia_limpia['cells'][0]['outputs']") == []
    # ...y el original conserva lo suyo.
    assert tb.ref("_salidas_originales") != []
    assert tb.ref("_contador_original") == 3


def test_celdas_con_cambio_real_ignora_salidas_distintas(tb, ayudantes):
    # Correr el mismo notebook dos veces cambia salidas y contadores, pero
    # no cambia una sola celda: la respuesta correcta es la lista vacía.
    tb.inject(
        """
        _antes = _notebook(_codigo("print(42)", _salida, 1), _markdown("# Titulo"))
        _despues = _notebook(
            _codigo("print(42)", [{"output_type": "stream", "name": "stdout", "text": ["43"]}], 7),
            _markdown("# Titulo"),
        )
        _sin_cambios = celdas_con_cambio_real(_antes, _despues)
        """
    )

    assert tb.ref("_sin_cambios") == []


def test_celdas_con_cambio_real_detecta_edicion_de_codigo(tb, ayudantes):
    tb.inject(
        """
        _antes = _notebook(_markdown("# Titulo"), _codigo("g = 9.81", _salida, 1))
        _despues = _notebook(_markdown("# Titulo"), _codigo("g = 9.80665", _salida, 1))
        _editadas = celdas_con_cambio_real(_antes, _despues)
        """
    )

    assert tb.ref("_editadas") == [1]


def test_celdas_con_cambio_real_acepta_source_como_lista_o_cadena(tb, ayudantes):
    # Las dos formas del formato .ipynb representan el mismo contenido.
    tb.inject(
        """
        _como_lista = _notebook(_codigo("g = 9.81"))
        _como_cadena = _notebook(_codigo("g = 9.81"))
        _como_cadena["cells"][0]["source"] = "g = 9.81"
        _misma_fuente = celdas_con_cambio_real(_como_lista, _como_cadena)

        _partida = _notebook(_codigo("g = 9.81"))
        _partida["cells"][0]["source"] = ["g = ", "9.81"]
        _partida_en_dos = celdas_con_cambio_real(_como_lista, _partida)
        """
    )

    assert tb.ref("_misma_fuente") == []
    assert tb.ref("_partida_en_dos") == []


def test_celdas_con_cambio_real_reporta_celdas_agregadas(tb, ayudantes):
    # Un índice que solo existe en una de las dos versiones cuenta como
    # cambio, tanto si se agregó una celda como si se eliminó.
    tb.inject(
        """
        _corto = _notebook(_markdown("# Titulo"), _codigo("g = 9.81"))
        _largo = _notebook(_markdown("# Titulo"), _codigo("g = 9.81"), _codigo("print(g)"))
        _agregada = celdas_con_cambio_real(_corto, _largo)
        _eliminada = celdas_con_cambio_real(_largo, _corto)
        """
    )

    assert tb.ref("_agregada") == [2]
    assert tb.ref("_eliminada") == [2]
