"""Energía mecánica del oscilador: cinética del bloque más potencial del resorte."""

import sympy as sp

from osciladores.amortiguado import t


def energia_mecanica(m, k, posicion):
    """Energía E = m v²/2 + k x²/2 de una masa en un resorte.

    Parámetros
    ----------
    m : masa del bloque.
    k : constante del resorte.
    posicion : la posición x(t) como expresión de SymPy en ``t``, por ejemplo
        lo que devuelve ``osciladores.resolver``.

    Devuelve
    --------
    La energía como función de ``t``. Sin fricción es constante; con fricción
    decrece, porque la fricción convierte energía mecánica en calor.
    """
    velocidad = sp.diff(posicion, t)
    return m * velocidad**2 / 2 + k * posicion**2
