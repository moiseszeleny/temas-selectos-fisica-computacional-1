"""Tests públicos de tarea-04.ipynb — visibles para el estudiante.

Cubren las habilidades evaluadas de los dos ejercicios. Esta es la primera
tarea con SymPy, y eso cambia la mecánica: una expresión simbólica **no**
es serializable a JSON, así que `tb.ref()` no puede traerla tal cual (ver
el porqué en `conftest.py`).

En lugar de sacar la expresión del kernel para compararla aquí, estos tests
hacen la comparación **dentro** del notebook y solo se traen el booleano
que resulta. Tiene dos ventajas sobre reconstruir la expresión con
`sp.sympify`: no depende de cómo se imprima, y compara contra los símbolos
que el estudiante declaró de verdad, con sus suposiciones reales.

La comparación es siempre de equivalencia simbólica —
`sp.simplify(resultado - esperado) == 0` — nunca de igualdad de cadenas:
cualquier forma algebraica correcta se da por buena.

Como la fixture `tb` es de sesión y el kernel se comparte entre tests, todo
lo que se inyecta lleva un guion bajo inicial para no chocar con los
nombres del estudiante.
"""

import pytest


@pytest.fixture(scope="session")
def simbolos_de_prueba(tb):
    """Declara en el kernel los símbolos que usan los tests del ejercicio 2."""
    tb.inject(
        """
        _x = sp.Symbol("x")                    # sin suposiciones: podría ser complejo
        _x_positiva = sp.Symbol("x", positive=True)
        """
    )


# --------------------------------------------------------------------------
# Ejercicio 1: el factor de Lorentz
# --------------------------------------------------------------------------


def test_simbolos_tienen_nombre_y_suposiciones_correctos(tb):
    # El nombre del símbolo es el de la fórmula física (m, v, c), no el de
    # la variable de Python. Las suposiciones son las que el problema
    # garantiza: masa y c positivas, rapidez real.
    tb.inject(
        """
        _nombres = [str(masa), str(rapidez), str(velocidad_luz)]
        _masa_positiva = (masa.is_positive is True)
        _luz_positiva = (velocidad_luz.is_positive is True)
        _rapidez_real = (rapidez.is_real is True)
        """
    )

    assert tb.ref("_nombres") == ["m", "v", "c"]
    assert tb.ref("_masa_positiva") is True
    assert tb.ref("_luz_positiva") is True
    assert tb.ref("_rapidez_real") is True


def test_factor_de_lorentz_correcto(tb):
    tb.inject(
        """
        _lorentz_esperado = 1 / sp.sqrt(1 - rapidez**2 / velocidad_luz**2)
        _lorentz_ok = sp.simplify(factor_lorentz - _lorentz_esperado) == 0
        """
    )

    assert tb.ref("_lorentz_ok") is True


def test_energia_total_correcta(tb):
    tb.inject(
        """
        _energia_esperada = (
            masa * velocidad_luz**2 / sp.sqrt(1 - rapidez**2 / velocidad_luz**2)
        )
        _energia_ok = sp.simplify(energia_total - _energia_esperada) == 0
        """
    )

    assert tb.ref("_energia_ok") is True


def test_energia_en_reposo_es_masa_por_c_cuadrada(tb):
    # Con v = 0 el factor de Lorentz vale 1, y queda la fórmula famosa.
    tb.inject(
        """
        _reposo_ok = sp.simplify(
            energia_en_reposo - masa * velocidad_luz**2
        ) == 0
        """
    )

    assert tb.ref("_reposo_ok") is True


def test_factor_a_media_luz_es_exacto(tb):
    # A v = c/2 el factor vale 2/sqrt(3) = 2*sqrt(3)/3, exacto.
    tb.inject(
        """
        _media_luz_ok = sp.simplify(
            factor_a_media_luz - 2 * sp.sqrt(3) / 3
        ) == 0
        _media_luz_exacto = not factor_a_media_luz.atoms(sp.Float)
        """
    )

    assert tb.ref("_media_luz_ok") is True
    # Un 0.5 en lugar de sp.Rational(1, 2) habría dejado un flotante dentro.
    assert tb.ref("_media_luz_exacto") is True


# --------------------------------------------------------------------------
# Ejercicio 2: equivalencia matemática
# --------------------------------------------------------------------------


def test_son_equivalentes_reconoce_formas_distintas_del_mismo_polinomio(
    tb, simbolos_de_prueba
):
    # El caso que motiva el ejercicio: `==` diría False, y se equivocaría.
    tb.inject(
        """
        _polinomio = son_equivalentes((_x + 1)**2, _x**2 + 2*_x + 1)
        """
    )

    assert tb.ref("_polinomio") is True


def test_son_equivalentes_reconoce_identidad_trigonometrica(tb, simbolos_de_prueba):
    tb.inject(
        """
        _identidad = son_equivalentes(
            sp.sin(_x)**2 + sp.cos(_x)**2, sp.Integer(1)
        )
        """
    )

    assert tb.ref("_identidad") is True


def test_son_equivalentes_distingue_expresiones_distintas(tb, simbolos_de_prueba):
    tb.inject(
        """
        _distintas = son_equivalentes(_x**2, _x**3)
        """
    )

    assert tb.ref("_distintas") is False


def test_son_equivalentes_respeta_las_suposiciones(tb, simbolos_de_prueba):
    # Misma fórmula, dos respuestas: sqrt(x**2) solo es x cuando x >= 0.
    # La decisión es de SymPy, no de la función del estudiante.
    tb.inject(
        """
        _generica = son_equivalentes(sp.sqrt(_x**2), _x)
        _positiva = son_equivalentes(sp.sqrt(_x_positiva**2), _x_positiva)
        """
    )

    assert tb.ref("_generica") is False
    assert tb.ref("_positiva") is True


def test_son_equivalentes_devuelve_bool_de_python(tb, simbolos_de_prueba):
    # log(exp(x)) solo vale x si x es real; con x genérica SymPy no logra
    # decidirlo y `.equals()` devuelve None. La función debe traducir ese
    # "no lo sé" a False, y nunca dejar escapar un None.
    tb.inject(
        """
        _indeciso = son_equivalentes(sp.log(sp.exp(_x)), _x)
        _tipo_indeciso = type(_indeciso).__name__
        _tipo_verdadero = type(
            son_equivalentes((_x + 1)**2, _x**2 + 2*_x + 1)
        ).__name__
        """
    )

    assert tb.ref("_tipo_indeciso") == "bool"
    assert tb.ref("_tipo_verdadero") == "bool"
    assert tb.ref("_indeciso") is False
