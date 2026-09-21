"""Tests públicos de tarea-07.ipynb — visibles para el estudiante.

Cubren las habilidades evaluadas de los cuatro ejercicios. Como en las tareas
anteriores, ni los vectores de `mechanics` ni las expresiones de SymPy son
serializables a JSON, así que `tb.ref()` no puede traerlos tal cual (ver el
porqué en `conftest.py`): la comparación se hace **dentro** del notebook y de
aquí solo se trae el booleano que resulta.

Los resultados esperados no se construyen con los marcos del estudiante —si
un marco estuviera mal orientado, el error se copiaría en la respuesta
esperada— sino escribiendo a mano los unitarios del aro y de la cuenta en la
base de `N`, que el notebook ya declara. Dos vectores se consideran iguales si
su diferencia, escrita en `N`, se simplifica a cero componente por componente.

La comparación es siempre de equivalencia simbólica —
`sp.simplify(resultado - esperado) == 0` — nunca de igualdad de cadenas.

Como la fixture `tb` es de sesión y el kernel se comparte entre tests, todo lo
que se inyecta lleva un guion bajo inicial para no chocar con los nombres del
estudiante.
"""

# Unitarios del aro (a) y de la cuenta (b) escritos a mano en la base de N, y
# la posición, velocidad y aceleración que se esperan. Se inyecta al principio
# de cada test que los necesita.
ESPERADOS = """
_c, _s = sp.cos(omega*t), sp.sin(omega*t)
_a_x = _c*N.x + _s*N.y
_a_y = -_s*N.x + _c*N.y
_a_z = N.z
_b_x = sp.cos(theta)*_a_x - sp.sin(theta)*_a_z
_b_z = sp.sin(theta)*_a_x + sp.cos(theta)*_a_z

_posicion_esperada = -radio*_b_z
_velocidad_esperada = _posicion_esperada.dt(N)
_aceleracion_esperada = _velocidad_esperada.dt(N)

def _iguales(u, v):
    return (u - v).to_matrix(N).applyfunc(sp.simplify) == sp.zeros(3, 1)
"""


# --------------------------------------------------------------------------
# Ejercicio 1: símbolos y marcos
# --------------------------------------------------------------------------


def test_simbolos_tienen_nombre_y_suposiciones_correctos(tb):
    # Los nombres son los de la física (R, Omega), no los de las variables de
    # Python; y theta tiene que depender del tiempo.
    tb.inject(
        """
        _nombres = [str(radio), str(omega)]
        _suposiciones = [radio.is_positive is True, omega.is_positive is True]
        _theta_ok = theta == me.dynamicsymbols("theta")
        """
    )

    assert tb.ref("_nombres") == ["R", "Omega"]
    assert tb.ref("_suposiciones") == [True, True]
    assert tb.ref("_theta_ok") is True


def test_marco_del_aro_gira_con_omega(tb):
    tb.inject(
        """
        _c, _s = sp.cos(omega*t), sp.sin(omega*t)
        _dcm_aro = sp.Matrix([[_c, _s, 0], [-_s, _c, 0], [0, 0, 1]])
        _aro_ok = sp.simplify(A.dcm(N) - _dcm_aro) == sp.zeros(3, 3)
        """
    )

    assert tb.ref("_aro_ok") is True


def test_marco_de_la_cuenta_gira_alrededor_de_a_y(tb):
    tb.inject(
        """
        _c, _s = sp.cos(theta), sp.sin(theta)
        _dcm_cuenta = sp.Matrix([[_c, 0, -_s], [0, 1, 0], [_s, 0, _c]])
        _cuenta_ok = sp.simplify(B.dcm(A) - _dcm_cuenta) == sp.zeros(3, 3)
        """
    )

    assert tb.ref("_cuenta_ok") is True


# --------------------------------------------------------------------------
# Ejercicio 2: posición, velocidad y aceleración
# --------------------------------------------------------------------------


def test_posicion_de_la_cuenta_correcta(tb):
    tb.inject(ESPERADOS + "\n_posicion_ok = _iguales(posicion, _posicion_esperada)")

    assert tb.ref("_posicion_ok") is True


def test_velocidad_de_la_cuenta_correcta(tb):
    tb.inject(
        ESPERADOS + "\n_velocidad_ok = _iguales(velocidad, _velocidad_esperada)"
    )

    assert tb.ref("_velocidad_ok") is True


def test_aceleracion_de_la_cuenta_correcta(tb):
    tb.inject(
        ESPERADOS
        + "\n_aceleracion_ok = _iguales(aceleracion, _aceleracion_esperada)"
    )

    assert tb.ref("_aceleracion_ok") is True


# --------------------------------------------------------------------------
# Ejercicio 3: velocidad angular y teorema de transporte
# --------------------------------------------------------------------------


def test_velocidad_angular_tiene_giro_del_aro_y_de_la_cuenta(tb):
    tb.inject(
        ESPERADOS
        + """
_omega_esperada = omega*N.z + theta.diff(t)*_a_y
_velocidad_angular_ok = _iguales(velocidad_angular, _omega_esperada)
"""
    )

    assert tb.ref("_velocidad_angular_ok") is True


def test_velocidad_por_transporte_coincide_con_la_directa(tb):
    tb.inject(
        ESPERADOS
        + "\n_transporte_ok = _iguales(velocidad_transporte, _velocidad_esperada)"
    )

    assert tb.ref("_transporte_ok") is True


# --------------------------------------------------------------------------
# Ejercicio 4: rapidez y aceleración a lo largo del aro
# --------------------------------------------------------------------------


def test_rapidez_cuadrada_correcta(tb):
    tb.inject(
        """
        _rapidez_esperada = radio**2 * (
            theta.diff(t)**2 + omega**2 * sp.sin(theta)**2
        )
        _rapidez_ok = sp.simplify(rapidez_cuadrada - _rapidez_esperada) == 0
        """
    )

    assert tb.ref("_rapidez_ok") is True


def test_aceleracion_tangencial_correcta(tb):
    tb.inject(
        ESPERADOS
        + """
_tangencial_esperada = _aceleracion_esperada.dot(_b_x)
_tangencial_ok = sp.simplify(aceleracion_tangencial - _tangencial_esperada) == 0
"""
    )

    assert tb.ref("_tangencial_ok") is True


def test_resultados_son_exactos(tb):
    # Un 0.5 en lugar de sp.Rational(1, 2) habría dejado un flotante, y con él
    # se pierde la exactitud de todo lo que se calcule después.
    tb.inject(
        """
        _flotantes = set()
        for _vector in (posicion, velocidad, aceleracion):
            _flotantes |= _vector.to_matrix(N).atoms(sp.Float)
        _flotantes |= sp.sympify(rapidez_cuadrada).atoms(sp.Float)
        _sin_flotantes = not _flotantes
        """
    )

    assert tb.ref("_sin_flotantes") is True
