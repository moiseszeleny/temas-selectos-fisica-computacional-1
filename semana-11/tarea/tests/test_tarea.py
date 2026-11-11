"""Tests públicos de tarea-11.ipynb — visibles para el estudiante.

En esta tarea el estudiante escribe **pruebas**, no resultados. Cada prueba
suya se califica dos veces:

1. Con las funciones correctas del notebook: debe pasar.
2. Con versiones de ``funcion_de_onda`` o ``energia_caja`` que traen un error
   plantado (las de ``MUTANTES``, abajo): debe fallar. Una prueba que pasa con
   código equivocado no está comprobando nada.

Todo se corre **dentro** del kernel del notebook con ``tb.inject``: se
reemplaza la función, se llama a la prueba del estudiante, se anota qué pasó
y se restaura la función original. De aquí solo se trae una cadena con el
resultado (ver ``conftest.py``).

Todo lo que se inyecta lleva un guion bajo inicial para no chocar con los
nombres del estudiante.
"""

import textwrap

import pytest

# --------------------------------------------------------------------------
# Las funciones con errores plantados. Cada una conserva la validación del
# nivel salvo las del ejercicio 4, que es justo lo que prueban.
# --------------------------------------------------------------------------

MUTANTES = {
    # Ejercicio 1: la amplitud está mal y la integral de |psi|^2 no es 1.
    "psi_sin_normalizar": """
        def funcion_de_onda(n, L, x):
            validar_nivel(n)
            return sp.sin(n * sp.pi * x / L)
        """,
    "psi_con_raiz_de_uno_sobre_L": """
        def funcion_de_onda(n, L, x):
            validar_nivel(n)
            return sp.sqrt(1 / L) * sp.sin(n * sp.pi * x / L)
        """,
    # Ejercicio 2: normalizada, pero con medio periodo; los niveles 1 y 2 ya
    # no son ortogonales.
    "psi_con_medio_periodo": """
        def funcion_de_onda(n, L, x):
            validar_nivel(n)
            return sp.sqrt(2 / L) * sp.sin(n * sp.pi * x / (2 * L))
        """,
    # Ejercicio 3: energías que no corresponden a la función de onda...
    "energia_lineal_en_n": """
        def energia_caja(n, m, L):
            validar_nivel(n)
            return n * sp.pi**2 * hbar**2 / (2 * m * L**2)
        """,
    "energia_con_L_sin_cuadrado": """
        def energia_caja(n, m, L):
            validar_nivel(n)
            return n**2 * sp.pi**2 * hbar**2 / (2 * m * L)
        """,
    # ... y un coseno: normalizado, ortogonal y con la energía correcta, pero
    # no se anula en las paredes.
    "psi_coseno": """
        def funcion_de_onda(n, L, x):
            validar_nivel(n)
            return sp.sqrt(2 / L) * sp.cos(n * sp.pi * x / L)
        """,
    # Ejercicio 4: validaciones ausentes o incompletas.
    "sin_validacion": """
        def funcion_de_onda(n, L, x):
            return sp.sqrt(2 / L) * sp.sin(n * sp.pi * x / L)

        def energia_caja(n, m, L):
            return n**2 * sp.pi**2 * hbar**2 / (2 * m * L**2)
        """,
    "acepta_el_cero": """
        def _validar_mal(n):
            n = sp.sympify(n)
            if not (n.is_integer and n.is_nonnegative):
                raise ValueError("nivel no válido")

        def funcion_de_onda(n, L, x):
            _validar_mal(n)
            return sp.sqrt(2 / L) * sp.sin(n * sp.pi * x / L)

        def energia_caja(n, m, L):
            _validar_mal(n)
            return n**2 * sp.pi**2 * hbar**2 / (2 * m * L**2)
        """,
    "acepta_fracciones": """
        def _validar_mal(n):
            if not sp.sympify(n).is_positive:
                raise ValueError("nivel no válido")

        def funcion_de_onda(n, L, x):
            _validar_mal(n)
            return sp.sqrt(2 / L) * sp.sin(n * sp.pi * x / L)

        def energia_caja(n, m, L):
            _validar_mal(n)
            return n**2 * sp.pi**2 * hbar**2 / (2 * m * L**2)
        """,
    "solo_valida_la_funcion_de_onda": """
        def energia_caja(n, m, L):
            return n**2 * sp.pi**2 * hbar**2 / (2 * m * L**2)
        """,
}


def correr_prueba(tb, prueba, mutante=None):
    """Corre la prueba del estudiante en su kernel y devuelve qué pasó.

    Devuelve ``"pasa"`` si la prueba terminó sin error, ``"falla"`` si lanzó
    ``AssertionError`` o el ``Failed`` de ``pytest.raises``, y otro texto si
    lanzó otra excepción (o si la prueba no existe). Las funciones originales
    se restauran siempre, aunque la prueba truene.
    """
    reemplazo = textwrap.dedent(MUTANTES[mutante]) if mutante else ""
    codigo = f"""
import pytest as _pytest

_originales = (funcion_de_onda, energia_caja)
try:
{textwrap.indent(reemplazo, "    ")}
    {prueba}()
    _resultado = "pasa"
except (AssertionError, _pytest.fail.Exception):
    _resultado = "falla"
except Exception as _error:
    _resultado = f"{{type(_error).__name__}}: {{_error}}"
finally:
    funcion_de_onda, energia_caja = _originales
"""
    tb.inject(codigo)
    return tb.ref("_resultado")


def comprobar_que_pasa(tb, prueba):
    resultado = correr_prueba(tb, prueba)
    assert resultado == "pasa", (
        f"{prueba} debe pasar con las funciones correctas del notebook, "
        f"pero dio: {resultado}"
    )


def comprobar_que_detecta(tb, prueba, mutante):
    resultado = correr_prueba(tb, prueba, mutante)
    assert resultado != "pasa", (
        f"{prueba} pasó con la versión '{mutante}', que tiene un error "
        f"plantado (ver MUTANTES en tests/test_tarea.py): tu prueba no lo atrapa"
    )
    assert not resultado.startswith("NameError"), (
        f"No encontré {prueba} en el notebook: {resultado}"
    )


# --------------------------------------------------------------------------
# Ejercicio 1: normalización
# --------------------------------------------------------------------------

PRUEBA_1 = "test_funcion_de_onda_normalizada"


def test_prueba_de_normalizacion_pasa_con_las_funciones_correctas(tb):
    comprobar_que_pasa(tb, PRUEBA_1)


@pytest.mark.parametrize("mutante", ["psi_sin_normalizar", "psi_con_raiz_de_uno_sobre_L"])
def test_prueba_de_normalizacion_detecta_una_amplitud_equivocada(tb, mutante):
    comprobar_que_detecta(tb, PRUEBA_1, mutante)


# --------------------------------------------------------------------------
# Ejercicio 2: ortogonalidad
# --------------------------------------------------------------------------

PRUEBA_2 = "test_estados_ortogonales"


def test_prueba_de_ortogonalidad_pasa_con_las_funciones_correctas(tb):
    comprobar_que_pasa(tb, PRUEBA_2)


def test_prueba_de_ortogonalidad_detecta_estados_no_ortogonales(tb):
    comprobar_que_detecta(tb, PRUEBA_2, "psi_con_medio_periodo")


# --------------------------------------------------------------------------
# Ejercicio 3: Schrödinger y paredes
# --------------------------------------------------------------------------

PRUEBA_3 = "test_cumple_schrodinger_y_se_anula_en_las_paredes"


def test_prueba_de_schrodinger_pasa_con_las_funciones_correctas(tb):
    comprobar_que_pasa(tb, PRUEBA_3)


@pytest.mark.parametrize("mutante", ["energia_lineal_en_n", "energia_con_L_sin_cuadrado"])
def test_prueba_de_schrodinger_detecta_una_energia_equivocada(tb, mutante):
    comprobar_que_detecta(tb, PRUEBA_3, mutante)


def test_prueba_de_schrodinger_detecta_que_no_se_anula_en_las_paredes(tb):
    comprobar_que_detecta(tb, PRUEBA_3, "psi_coseno")


# --------------------------------------------------------------------------
# Ejercicio 4: niveles no válidos
# --------------------------------------------------------------------------

PRUEBA_4 = "test_nivel_no_valido_lanza_error"


def test_prueba_de_nivel_no_valido_pasa_con_las_funciones_correctas(tb):
    comprobar_que_pasa(tb, PRUEBA_4)


@pytest.mark.parametrize(
    "mutante",
    ["sin_validacion", "acepta_el_cero", "acepta_fracciones", "solo_valida_la_funcion_de_onda"],
)
def test_prueba_de_nivel_no_valido_detecta_una_validacion_incompleta(tb, mutante):
    comprobar_que_detecta(tb, PRUEBA_4, mutante)
