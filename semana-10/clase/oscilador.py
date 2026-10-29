"""Oscilador armónico amortiguado.

Una masa ``m`` sujeta a un resorte de constante ``k`` y a una fricción
proporcional a la velocidad, de coeficiente ``b``, obedece

    m x'' + b x' + k x = 0.

Según el signo de ``b**2 - 4*m*k`` el movimiento oscila mientras se apaga
(subamortiguado), regresa al equilibrio lo más rápido posible sin oscilar
(crítico) o regresa lento y sin oscilar (sobreamortiguado). Este módulo
reúne las funciones de la sesión 1 de la semana 10 para que cualquier
notebook las importe con ``import oscilador`` en lugar de copiarlas.
"""

import sympy as sp

# El tiempo y la posición son reales; el tiempo, además, no es negativo.
t = sp.Symbol("t", nonnegative=True)
x = sp.Function("x", real=True)


def ecuacion_de_movimiento(m, b, k):
    """Segunda ley de Newton para la masa: m x'' + b x' + k x = 0."""
    return sp.Eq(m * x(t).diff(t, 2) + b * x(t).diff(t) + k * x(t), 0)


def regimen(m, b, k):
    """Nombre del régimen según el discriminante b² - 4mk (valores numéricos)."""
    discriminante = sp.sympify(b**2 - 4 * m * k)
    if discriminante.is_negative:
        return "subamortiguado"
    if discriminante.is_zero:
        return "crítico"
    return "sobreamortiguado"


def resolver(m, b, k, x0, v0):
    """Posición x(t) que parte de x(0) = x0 con velocidad x'(0) = v0."""
    solucion = sp.dsolve(
        ecuacion_de_movimiento(m, b, k),
        x(t),
        ics={x(0): x0, x(t).diff(t).subs(t, 0): v0},
    )
    return sp.simplify(solucion.rhs)
