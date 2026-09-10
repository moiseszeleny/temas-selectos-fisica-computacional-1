"""Tests públicos de tarea-05.ipynb — visibles para el estudiante.

Cubren las habilidades evaluadas de los dos ejercicios. Como en la tarea
04, las expresiones simbólicas no son serializables a JSON, así que
`tb.ref()` no puede traerlas tal cual (ver el porqué en `conftest.py`):
la comparación se hace **dentro** del notebook y de aquí solo se trae el
booleano que resulta.

Eso tiene además la ventaja de comparar contra los símbolos que el
estudiante declaró de verdad, con sus suposiciones reales — que en esta
tarea deciden el resultado: sin `positive=True`, `solve` del ejercicio 1
devuelve doce raíces en lugar de una.

La comparación es siempre de equivalencia simbólica —
`sp.simplify(resultado - esperado) == 0` — nunca de igualdad de cadenas:
cualquier forma algebraica correcta se da por buena. Importa aquí más que
nunca, porque `dsolve` puede escribir la misma solución de varias formas.

Como la fixture `tb` es de sesión y el kernel se comparte entre tests, todo
lo que se inyecta lleva un guion bajo inicial para no chocar con los
nombres del estudiante.
"""

# --------------------------------------------------------------------------
# Ejercicio 1: el potencial de Lennard-Jones
# --------------------------------------------------------------------------


def test_simbolos_tienen_nombre_y_suposiciones_correctos(tb):
    # Los nombres son los de la fórmula física (r, epsilon, sigma), no los
    # de las variables de Python. Los tres son positivos, y de eso depende
    # que solve devuelva una sola solución.
    tb.inject(
        """
        _nombres = [str(distancia), str(epsilon), str(sigma)]
        _positivos = [
            distancia.is_positive is True,
            epsilon.is_positive is True,
            sigma.is_positive is True,
        ]
        """
    )

    assert tb.ref("_nombres") == ["r", "epsilon", "sigma"]
    assert tb.ref("_positivos") == [True, True, True]


def test_potencial_de_lennard_jones_correcto(tb):
    tb.inject(
        """
        _potencial_esperado = 4*epsilon*(
            (sigma/distancia)**12 - (sigma/distancia)**6
        )
        _potencial_ok = sp.simplify(potencial - _potencial_esperado) == 0
        """
    )

    assert tb.ref("_potencial_ok") is True


def test_fuerza_es_menos_la_derivada_del_potencial(tb):
    # No se compara contra una fórmula escrita a mano: se compara contra la
    # derivada del potencial que el estudiante entregó, que es la definición.
    tb.inject(
        """
        _fuerza_ok = sp.simplify(
            fuerza + sp.diff(potencial, distancia)
        ) == 0
        """
    )

    assert tb.ref("_fuerza_ok") is True


def test_distancia_de_equilibrio_anula_la_fuerza(tb):
    # Dos cosas: que el valor sea el correcto, y que de verdad sea un cero
    # de la fuerza del estudiante.
    tb.inject(
        """
        _equilibrio_ok = sp.simplify(
            distancia_equilibrio - 2**sp.Rational(1, 6) * sigma
        ) == 0
        _anula_la_fuerza = sp.simplify(
            fuerza.subs(distancia, distancia_equilibrio)
        ) == 0
        """
    )

    assert tb.ref("_equilibrio_ok") is True
    assert tb.ref("_anula_la_fuerza") is True


def test_energia_minima_es_menos_epsilon(tb):
    # La profundidad del pozo: V(r_eq) = -epsilon, de donde el parámetro
    # toma su significado físico.
    tb.inject(
        """
        _minimo_ok = sp.simplify(energia_minima + epsilon) == 0
        """
    )

    assert tb.ref("_minimo_ok") is True


def test_curvatura_en_el_equilibrio_correcta(tb):
    # V''(r_eq) = 36 * 2**(2/3) * epsilon / sigma**2: la constante elástica
    # efectiva de las oscilaciones pequeñas de la molécula.
    tb.inject(
        """
        _curvatura_esperada = (
            36 * 2**sp.Rational(2, 3) * epsilon / sigma**2
        )
        _curvatura_ok = sp.simplify(curvatura - _curvatura_esperada) == 0
        _curvatura_exacta = not curvatura.atoms(sp.Float)
        """
    )

    assert tb.ref("_curvatura_ok") is True
    # Un exponente 1/6 escrito como 0.1666... habría dejado un flotante.
    assert tb.ref("_curvatura_exacta") is True


# --------------------------------------------------------------------------
# Ejercicio 2: el oscilador forzado y la resonancia
# --------------------------------------------------------------------------


def test_ecuacion_forzada_bien_planteada(tb):
    # Se comprueba que la ecuación diga lo que dice el enunciado, sin exigir
    # de qué lado del igual quedó cada término: se compara la diferencia
    # entre los dos lados.
    tb.inject(
        """
        _residuo_esperado = (
            masa * posicion(tiempo).diff(tiempo, 2)
            + masa * frecuencia_propia**2 * posicion(tiempo)
            - fuerza_maxima * sp.cos(frecuencia_forzamiento * tiempo)
        )
        _residuo_estudiante = ecuacion_forzada.lhs - ecuacion_forzada.rhs
        _ecuacion_ok = sp.simplify(
            _residuo_estudiante - _residuo_esperado
        ) == 0 or sp.simplify(
            _residuo_estudiante + _residuo_esperado
        ) == 0
        """
    )

    assert tb.ref("_ecuacion_ok") is True


def test_movimiento_resuelve_la_ecuacion(tb):
    # La verificación de la sesión 2: sustituir la solución de vuelta en la
    # ecuación y comprobar que el residuo se anula.
    tb.inject(
        """
        _verificacion = sp.checkodesol(ecuacion_forzada, solucion_forzada)
        _resuelve = _verificacion[0] is True
        """
    )

    assert tb.ref("_resuelve") is True


def test_movimiento_cumple_las_condiciones_iniciales(tb):
    # Parte del origen y en reposo: sin esto, la solución tendría constantes
    # libres y no describiría este experimento.
    tb.inject(
        """
        _en_reposo_inicial = sp.simplify(
            movimiento.diff(tiempo).subs(tiempo, 0)
        ) == 0
        _desde_el_origen = sp.simplify(movimiento.subs(tiempo, 0)) == 0
        """
    )

    assert tb.ref("_desde_el_origen") is True
    assert tb.ref("_en_reposo_inicial") is True


def test_movimiento_es_la_diferencia_de_dos_cosenos(tb):
    # La forma cerrada conocida. Cualquier reescritura equivalente pasa.
    tb.inject(
        """
        _movimiento_esperado = (
            fuerza_maxima
            / (masa * (frecuencia_propia**2 - frecuencia_forzamiento**2))
            * (
                sp.cos(frecuencia_forzamiento * tiempo)
                - sp.cos(frecuencia_propia * tiempo)
            )
        )
        _movimiento_ok = sp.simplify(movimiento - _movimiento_esperado) == 0
        """
    )

    assert tb.ref("_movimiento_ok") is True


def test_movimiento_en_resonancia_crece_con_el_tiempo(tb):
    # El límite Omega -> omega da F_0*t*sin(omega*t)/(2*m*omega): la
    # amplitud ya no es constante, crece linealmente con el tiempo.
    tb.inject(
        """
        _resonancia_esperada = (
            fuerza_maxima * tiempo * sp.sin(frecuencia_propia * tiempo)
            / (2 * masa * frecuencia_propia)
        )
        _resonancia_ok = sp.simplify(
            movimiento_en_resonancia - _resonancia_esperada
        ) == 0
        # Y ya no depende de la frecuencia de forzamiento: el límite se tomó.
        _sin_frecuencia_forzamiento = (
            frecuencia_forzamiento not in movimiento_en_resonancia.free_symbols
        )
        """
    )

    assert tb.ref("_resonancia_ok") is True
    assert tb.ref("_sin_frecuencia_forzamiento") is True
