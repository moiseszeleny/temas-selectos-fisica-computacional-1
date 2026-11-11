"""Pruebas del paquete ``osciladores``.

Se corren desde ``semana-11/clase/`` con

    python -m pytest tests -v

``python -m`` agrega la carpeta actual a la ruta de búsqueda de Python, y por
eso ``import osciladores`` funciona aquí aunque el paquete no esté instalado.

Cada prueba compara expresiones por **equivalencia simbólica**: resta lo que
devuelve el paquete de lo esperado y comprueba que se simplifica a cero.
"""

import pytest
import sympy as sp

import osciladores
from osciladores.energia import energia_mecanica

t = osciladores.t
x = osciladores.x


def test_ecuacion_sin_friccion_es_la_del_oscilador_libre():
    m, k = sp.symbols("m k", positive=True)

    ecuacion = osciladores.ecuacion_de_movimiento(m, 0, k)

    esperada = m * x(t).diff(t, 2) + k * x(t)
    assert sp.simplify(ecuacion.lhs - esperada) == 0


def test_resolver_sin_friccion_da_un_coseno():
    # m = 1, k = 4: omega = 2. Parte del reposo en x = 1.
    posicion = osciladores.resolver(1, 0, 4, 1, 0)

    assert sp.simplify(posicion - sp.cos(2 * t)) == 0


def test_energia_sin_friccion_se_conserva():
    posicion = osciladores.resolver(1, 0, 4, 1, 0)

    energia = energia_mecanica(1, 4, posicion)

    # Conservada quiere decir que no depende del tiempo.
    assert sp.simplify(sp.diff(energia, t)) == 0


def test_energia_inicial_es_la_del_resorte_estirado():
    # En reposo en x = 1 toda la energía está en el resorte: k x0² / 2 = 2.
    posicion = osciladores.resolver(1, 1, 4, 1, 0)

    energia = energia_mecanica(1, 4, posicion)

    assert sp.simplify(energia.subs(t, 0) - 2) == 0


# --------------------------------------------------------------------------
# TODO en clase 2
# --------------------------------------------------------------------------


def test_resolver_cumple_la_ecuacion_y_las_condiciones_iniciales():
    pytest.skip("TODO en clase 2: borra esta línea y escribe la prueba")


# --------------------------------------------------------------------------
# TODO en clase 3
# --------------------------------------------------------------------------


def test_regimen_de_cada_friccion():
    pytest.skip("TODO en clase 3: borra esta línea y escribe la prueba")


def test_regimen_con_simbolos_avisa():
    pytest.skip("TODO en clase 3: borra esta línea y escribe la prueba")
