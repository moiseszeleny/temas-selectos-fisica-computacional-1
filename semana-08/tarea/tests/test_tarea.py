"""Tests públicos de tarea-08.ipynb — visibles para el estudiante.

Cubren las habilidades evaluadas de los cuatro ejercicios. Como en las tareas
anteriores, ni los objetos de `mechanics` ni las expresiones de SymPy son
serializables a JSON, así que `tb.ref()` no puede traerlos tal cual (ver el
porqué en `conftest.py`): la comparación se hace **dentro** del notebook y de
aquí solo se trae el booleano que resulta.

Los resultados esperados se escriben a mano —el Lagrangiano, la aceleración
angular, los equilibrios—, nunca con los marcos ni los métodos del
estudiante: si uno estuviera mal planteado, el error se copiaría en la
respuesta esperada.

Las ecuaciones de movimiento se comparan **despejando** la aceleración
($\\ddot\\theta$ en Lagrange, $\\dot u$ en Kane) y restándole la esperada. Así
se da por buena cualquier forma equivalente de la ecuación, aunque venga
multiplicada por una constante o con el signo cambiado —Kane y Lagrange, de
hecho, la dan con signos opuestos—.

La comparación es siempre de equivalencia simbólica —
`sp.simplify(resultado - esperado) == 0` — nunca de igualdad de cadenas.

Como la fixture `tb` es de sesión y el kernel se comparte entre tests, todo lo
que se inyecta lleva un guion bajo inicial para no chocar con los nombres del
estudiante.
"""

# La aceleración angular que se espera, escrita a mano. Se inyecta al
# principio de cada test que la necesita.
ESPERADOS = """
_aceleracion_esperada = sp.sin(theta) * (
    omega**2 * sp.cos(theta) - gravedad / radio
)
"""


# --------------------------------------------------------------------------
# Ejercicio 1: el sistema
# --------------------------------------------------------------------------


def test_simbolos_tienen_nombre_y_suposiciones_correctos(tb):
    # Los nombres son los de la física (R, Omega, m, g), no los de las
    # variables de Python; y theta tiene que depender del tiempo.
    tb.inject(
        """
        _simbolos = (radio, omega, masa, gravedad)
        _nombres = [str(_s) for _s in _simbolos]
        _suposiciones = [_s.is_positive is True for _s in _simbolos]
        _theta_ok = theta == me.dynamicsymbols("theta")
        """
    )

    assert tb.ref("_nombres") == ["R", "Omega", "m", "g"]
    assert tb.ref("_suposiciones") == [True, True, True, True]
    assert tb.ref("_theta_ok") is True


def test_particula_tiene_masa_y_energia_potencial_correctas(tb):
    # La vertical es n_z: la cuenta está a una altura -R cos(theta) del centro.
    tb.inject(
        """
        _masa_ok = sp.simplify(particula.mass - masa) == 0
        _potencial_esperada = -masa * gravedad * radio * sp.cos(theta)
        _potencial_ok = (
            sp.simplify(particula.potential_energy - _potencial_esperada) == 0
        )
        """
    )

    assert tb.ref("_masa_ok") is True
    assert tb.ref("_potencial_ok") is True


# --------------------------------------------------------------------------
# Ejercicio 2: Lagrange
# --------------------------------------------------------------------------


def test_lagrangiano_correcto(tb):
    # T = m v^2 / 2, con la rapidez al cuadrado de la tarea 07; V = -m g R cos.
    tb.inject(
        """
        _lagrangiano_esperado = (
            masa * radio**2 / 2
            * (theta.diff(t)**2 + omega**2 * sp.sin(theta)**2)
            + masa * gravedad * radio * sp.cos(theta)
        )
        _lagrangiano_ok = (
            sp.simplify(lagrangiano - _lagrangiano_esperado) == 0
        )
        """
    )

    assert tb.ref("_lagrangiano_ok") is True


def test_ecuacion_de_lagrange_equivale_a_la_esperada(tb):
    tb.inject(
        ESPERADOS
        + """
_despejes = sp.solve(ecuacion_lagrange, theta.diff(t, 2))
_lagrange_ok = (
    len(_despejes) == 1
    and sp.simplify(_despejes[0] - _aceleracion_esperada) == 0
)
"""
    )

    assert tb.ref("_lagrange_ok") is True


# --------------------------------------------------------------------------
# Ejercicio 3: Kane
# --------------------------------------------------------------------------


def test_velocidad_angular_de_la_cuenta_usa_u(tb):
    # Tras set_ang_vel, el giro de la cuenta respecto al aro se escribe con u
    # a lo largo de a_y, que en la base de N es (-sen, cos, 0) de Omega t.
    tb.inject(
        """
        _u_ok = u == me.dynamicsymbols("u")
        _a_y = -sp.sin(omega*t)*N.x + sp.cos(omega*t)*N.y
        _omega_esperada = omega*N.z + u*_a_y
        _diferencia = (B.ang_vel_in(N) - _omega_esperada).to_matrix(N)
        _angular_ok = _diferencia.applyfunc(sp.simplify) == sp.zeros(3, 1)
        """
    )

    assert tb.ref("_u_ok") is True
    assert tb.ref("_angular_ok") is True


def test_ecuacion_de_kane_equivale_a_la_esperada(tb):
    tb.inject(
        ESPERADOS
        + """
_despejes = sp.solve(ecuacion_kane, u.diff(t))
_kane_ok = (
    len(_despejes) == 1
    and sp.simplify(_despejes[0] - _aceleracion_esperada) == 0
)
"""
    )

    assert tb.ref("_kane_ok") is True


def test_kane_y_lagrange_coinciden(tb):
    # Los dos métodos del estudiante, uno contra el otro, en primer orden.
    tb.inject(
        """
        _lagrange_en_u = metodo_lagrange.rhs().subs(theta.diff(t), u)
        _coinciden = sp.simplify(metodo_kane.rhs() - _lagrange_en_u) == sp.zeros(2, 1)
        """
    )

    assert tb.ref("_coinciden") is True


# --------------------------------------------------------------------------
# Ejercicio 4: equilibrios
# --------------------------------------------------------------------------


def test_aceleracion_theta_correcta(tb):
    tb.inject(
        ESPERADOS
        + """
_aceleracion_ok = sp.simplify(aceleracion_theta - _aceleracion_esperada) == 0
"""
    )

    assert tb.ref("_aceleracion_ok") is True


def test_equilibrio_lateral_correcto(tb):
    # Se acepta cualquier forma equivalente de arccos(g / (R Omega^2)), pero
    # tiene que ser la solución entre 0 y pi/2: se comprueba con valores en
    # los que el equilibrio existe (Omega por encima de la crítica).
    tb.inject(
        """
        _esperado = sp.acos(gravedad / (radio * omega**2))
        _valores = {radio: 1, gravedad: sp.Rational(981, 100), omega: 5}
        _numerico = sp.N(sp.sympify(equilibrio_lateral).subs(_valores))
        _equilibrio_ok = bool(
            sp.Abs(_numerico - sp.N(_esperado.subs(_valores))) < 1e-12
            and sp.simplify(sp.cos(equilibrio_lateral) - sp.cos(_esperado)) == 0
        )
        """
    )

    assert tb.ref("_equilibrio_ok") is True


def test_omega_critica_correcta(tb):
    tb.inject(
        """
        _critica_ok = (
            sp.simplify(omega_critica - sp.sqrt(gravedad / radio)) == 0
        )
        """
    )

    assert tb.ref("_critica_ok") is True


def test_resultados_son_exactos(tb):
    # Un 0.5 en lugar de sp.Rational(1, 2) habría dejado un flotante, y con él
    # se pierde la exactitud de todo lo que se calcule después.
    tb.inject(
        """
        _flotantes = set()
        for _expresion in (lagrangiano, ecuacion_lagrange, ecuacion_kane,
                           aceleracion_theta, equilibrio_lateral, omega_critica):
            _flotantes |= sp.sympify(_expresion).atoms(sp.Float)
        _sin_flotantes = not _flotantes
        """
    )

    assert tb.ref("_sin_flotantes") is True
