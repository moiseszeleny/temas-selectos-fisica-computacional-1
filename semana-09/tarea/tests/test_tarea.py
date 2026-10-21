"""Tests públicos de tarea-09.ipynb — visibles para el estudiante.

Cubren las habilidades evaluadas de los cuatro ejercicios. Como en las tareas
anteriores, las expresiones de SymPy no son serializables a JSON, así que
`tb.ref()` no puede traerlas tal cual (ver `conftest.py`): la comparación se
hace **dentro** del notebook y de aquí solo se trae el booleano que resulta.

Los resultados esperados se escriben a mano, nunca con las variables del
estudiante: si una estuviera mal planteada, el error se copiaría en la
respuesta esperada. La comparación es siempre de equivalencia simbólica —
`sp.simplify(resultado - esperado) == 0` — nunca de igualdad de cadenas.

Todo lo que se inyecta lleva un guion bajo inicial para no chocar con los
nombres del estudiante.
"""

# --------------------------------------------------------------------------
# Ejercicio 1: la energía de Rydberg
# --------------------------------------------------------------------------


def test_energia_rydberg_tiene_dimension_de_energia(tb):
    # La dimensión de la fórmula debe ser la de una energía; si falta un
    # cuadrado de hbar o un factor de e, no lo es.
    tb.inject(
        """
        from sympy.physics.units.systems.si import dimsys_SI
        _energia = dimsys_SI.get_dimensional_dependencies(u.energy)
        _dim_formula = SI._collect_factor_and_dimension(energia_rydberg)[1]
        _dim_ok = dimsys_SI.get_dimensional_dependencies(_dim_formula) == _energia
        _dim_estudiante_ok = (
            dimsys_SI.get_dimensional_dependencies(dimension_energia) == _energia
        )
        """
    )

    assert tb.ref("_dim_ok") is True
    assert tb.ref("_dim_estudiante_ok") is True


def test_rydberg_en_ev_es_trece_punto_seis(tb):
    tb.inject(
        """
        _valor = float(sp.N(rydberg_en_ev.subs(u.eV, 1)))
        _rydberg_ok = abs(_valor - 13.6057) < 1e-3
        """
    )

    assert tb.ref("_rydberg_ok") is True


# --------------------------------------------------------------------------
# Ejercicio 2: conmutadores con [X, P] = i hbar
# --------------------------------------------------------------------------


def test_conmutador_x_p2_correcto(tb):
    # [X, P^2] = [X, P] P + P [X, P] = 2 i hbar P
    tb.inject(
        """
        _esperado = 2 * sp.I * hbar * p_op
        _x_p2_ok = sp.expand(conmutador_x_p2 - _esperado) == 0
        """
    )

    assert tb.ref("_x_p2_ok") is True


def test_conmutador_x2_p_correcto(tb):
    # [X^2, P] = X [X, P] + [X, P] X = 2 i hbar X
    tb.inject(
        """
        _esperado = 2 * sp.I * hbar * x_op
        _x2_p_ok = sp.expand(conmutador_x2_p - _esperado) == 0
        """
    )

    assert tb.ref("_x2_p_ok") is True


# --------------------------------------------------------------------------
# Ejercicio 3: espín 1/2 en una dirección cualquiera
# --------------------------------------------------------------------------


def test_angulos_son_simbolos_reales(tb):
    tb.inject(
        """
        _nombres = [str(theta), str(phi)]
        _reales = [theta.is_real is True, phi.is_real is True]
        """
    )

    assert tb.ref("_nombres") == ["theta", "phi"]
    assert tb.ref("_reales") == [True, True]


def test_matriz_de_espin_en_direccion_n_correcta(tb):
    tb.inject(
        """
        _esperada = (hbar / 2) * sp.Matrix([
            [sp.cos(theta), sp.sin(theta) * sp.exp(-sp.I * phi)],
            [sp.sin(theta) * sp.exp(sp.I * phi), -sp.cos(theta)],
        ])
        _diferencia = (sp.Matrix(espin_n) - _esperada).applyfunc(
            lambda _e: sp.simplify(_e.rewrite(sp.exp))
        )
        _espin_ok = _diferencia == sp.zeros(2, 2)
        """
    )

    assert tb.ref("_espin_ok") is True


def test_valores_propios_del_espin_son_mas_menos_hbar_medios(tb):
    tb.inject(
        """
        _valores_ok = (
            len(valores_propios) == 2
            and {sp.simplify(_k) for _k in valores_propios} == {hbar / 2, -hbar / 2}
        )
        """
    )

    assert tb.ref("_valores_ok") is True


# --------------------------------------------------------------------------
# Ejercicio 4: el oscilador en el estado n = 4
# --------------------------------------------------------------------------


def test_valor_esperado_de_x2_en_n4_correcto(tb):
    # <n|x^2|n> = (hbar / 2 m omega) (2n + 1) = 9 hbar / (2 m omega)
    tb.inject(
        """
        _x2_ok = sp.simplify(x2_n4 - 9 * hbar / (2 * m * omega)) == 0
        """
    )

    assert tb.ref("_x2_ok") is True


def test_energia_del_oscilador_en_n4_correcta(tb):
    tb.inject(
        """
        _energia_ok = sp.simplify(energia_n4 - sp.Rational(9, 2) * hbar * omega) == 0
        """
    )

    assert tb.ref("_energia_ok") is True


def test_virial_potencial_medio_es_la_mitad_de_la_energia(tb):
    tb.inject(
        """
        _virial_ok = sp.simplify(potencial_medio - sp.Rational(9, 4) * hbar * omega) == 0
        """
    )

    assert tb.ref("_virial_ok") is True


# --------------------------------------------------------------------------
# Exactitud
# --------------------------------------------------------------------------


def test_resultados_son_exactos(tb):
    # Un flotante suelto contamina la expresión entera. `rydberg_en_ev` queda
    # fuera a propósito: es un número que se pide evaluar con evalf().
    tb.inject(
        """
        _flotantes = set()
        for _expresion in (
            "conmutador_x_p2",
            "conmutador_x2_p",
            "espin_n",
            "x2_n4",
            "energia_n4",
            "potencial_medio",
        ):
            _flotantes |= sp.sympify(str(eval(_expresion))).atoms(sp.Float)
        _exactos_ok = len(_flotantes) == 0
        """
    )

    assert tb.ref("_exactos_ok") is True
