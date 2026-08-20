"""Tests públicos de tarea-02.ipynb — visibles para el estudiante.

Cubren las habilidades evaluadas de los dos ejercicios. La tarea de esta
semana no produce números, sino **objetos** de una clase que define el
estudiante, y una instancia de `Fraccion` no es serializable a JSON: igual
que con los objetos de SymPy, `tb.ref()` no puede traerla tal cual (ver el
porqué en `conftest.py`). La solución es la misma de siempre — pedirle al
notebook una *proyección* serializable del objeto: `.numerador`,
`.denominador`, `repr(...)` o el resultado booleano de una comparación.

Dos de los tests necesitan comprobar que algo **falla** (el `ValueError`
del denominador cero y el `AttributeError` de una propiedad de solo
lectura). Eso no se puede expresar como una sola expresión, así que usan
`tb.inject()` para correr un `try`/`except` dentro del kernel del notebook.
Como la fixture `tb` es de sesión y el kernel se comparte entre tests, las
variables que se inyectan llevan un guion bajo inicial para no chocar con
las del estudiante.
"""


def test_fraccion_expone_numerador_y_denominador(tb):
    assert tb.ref("Fraccion(3, 4).numerador") == 3
    assert tb.ref("Fraccion(3, 4).denominador") == 4


def test_repr_reconstruye_la_fraccion(tb):
    assert tb.ref("repr(Fraccion(3, 4))") == "Fraccion(3, 4)"


def test_fracciones_equivalentes_son_iguales(tb):
    # 1/2 y 2/4 son la misma fracción: __eq__ compara por valor, no por
    # los enteros que se pasaron al constructor.
    assert tb.ref("Fraccion(1, 2) == Fraccion(2, 4)") is True
    assert tb.ref("Fraccion(1, 2) == Fraccion(1, 3)") is False


def test_denominador_cero_lanza_value_error(tb):
    tb.inject(
        """
        try:
            Fraccion(1, 0)
            _error_denominador = "no lanzó nada"
        except ValueError:
            _error_denominador = "ValueError"
        except Exception as _e:
            _error_denominador = type(_e).__name__
        """
    )

    assert tb.ref("_error_denominador") == "ValueError"


def test_fraccion_es_inmutable(tb):
    # Las propiedades son de solo lectura: sin setter, asignar debe fallar.
    tb.inject(
        """
        _f = Fraccion(3, 4)
        try:
            _f.numerador = 99
            _error_inmutable = "no lanzó nada"
        except AttributeError:
            _error_inmutable = "AttributeError"
        except Exception as _e:
            _error_inmutable = type(_e).__name__
        _valor_tras_intento = _f.numerador
        """
    )

    assert tb.ref("_error_inmutable") == "AttributeError"
    # Y la fracción sigue valiendo lo mismo después del intento fallido.
    assert tb.ref("_valor_tras_intento") == 3


def test_suma_normalizada(tb):
    # 1/2 + 1/3 = 5/6, ya reducida.
    assert tb.ref("(Fraccion(1, 2) + Fraccion(1, 3)).numerador") == 5
    assert tb.ref("(Fraccion(1, 2) + Fraccion(1, 3)).denominador") == 6

    # 1/2 + (-1/2) = 0, que normalizado es 0/1.
    assert tb.ref("(Fraccion(1, 2) + Fraccion(-1, 2)).numerador") == 0
    assert tb.ref("(Fraccion(1, 2) + Fraccion(-1, 2)).denominador") == 1


def test_producto_normalizado_y_con_signo_en_el_numerador(tb):
    # 2/3 * 3/4 = 6/12, que reducida es 1/2.
    assert tb.ref("(Fraccion(2, 3) * Fraccion(3, 4)).numerador") == 1
    assert tb.ref("(Fraccion(2, 3) * Fraccion(3, 4)).denominador") == 2

    # 1/2 * 1/(-3) = -1/6: el signo va en el numerador, nunca abajo.
    assert tb.ref("(Fraccion(1, 2) * Fraccion(1, -3)).numerador") == -1
    assert tb.ref("(Fraccion(1, 2) * Fraccion(1, -3)).denominador") == 6
