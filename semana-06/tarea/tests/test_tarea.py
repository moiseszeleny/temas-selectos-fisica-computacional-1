"""Tests públicos de tarea-06.ipynb — visibles para el estudiante.

Cubren las habilidades evaluadas de los cuatro ejercicios. Como en las tareas
04 y 05, las expresiones simbólicas no son serializables a JSON, así que
`tb.ref()` no puede traerlas tal cual (ver el porqué en `conftest.py`): la
comparación se hace **dentro** del notebook y de aquí solo se trae el booleano
que resulta.

Eso tiene además la ventaja de comparar contra los símbolos y las matrices que
el estudiante declaró de verdad. Los modos normales, por ejemplo, no se
comparan contra vectores escritos a mano —un eigenvector está definido salvo un
factor, y `eigenvects` puede devolverlos en cualquier orden— sino contra su
propia definición: `K v = omega**2 M v`.

La comparación es siempre de equivalencia simbólica —
`sp.simplify(resultado - esperado) == 0` — nunca de igualdad de cadenas.

La parte de discusión del notebook no se califica aquí: la revisa el asistente,
junto con el historial de commits, porque esta tarea es el entregable del
Módulo 1.

Como la fixture `tb` es de sesión y el kernel se comparte entre tests, todo lo
que se inyecta lleva un guion bajo inicial para no chocar con los nombres del
estudiante.
"""

# --------------------------------------------------------------------------
# Ejercicio 1: el planteamiento matricial
# --------------------------------------------------------------------------


def test_simbolos_tienen_nombre_y_suposiciones_correctos(tb):
    # Los nombres son los de la física (t, m, k, A), no los de las variables
    # de Python. Las tres cantidades positivas deben declararse como tales.
    tb.inject(
        """
        _nombres = [
            str(tiempo), str(masa), str(constante), str(amplitud)
        ]
        _suposiciones = [
            tiempo.is_real is True,
            masa.is_positive is True,
            constante.is_positive is True,
            amplitud.is_positive is True,
        ]
        """
    )

    assert tb.ref("_nombres") == ["t", "m", "k", "A"]
    assert tb.ref("_suposiciones") == [True, True, True, True]


def test_matriz_de_rigidez_correcta(tb):
    tb.inject(
        """
        _rigidez_esperada = constante * sp.Matrix([
            [2, -1, 0],
            [-1, 2, -1],
            [0, -1, 2],
        ])
        _rigidez_ok = sp.simplify(rigidez - _rigidez_esperada) == sp.zeros(3, 3)
        _rigidez_simetrica = rigidez.is_symmetric()
        """
    )

    assert tb.ref("_rigidez_ok") is True
    # La simetría no es un adorno: viene de que la fuerza deriva de un
    # potencial, y si falla es que hay un signo mal puesto.
    assert tb.ref("_rigidez_simetrica") is True


def test_matriz_de_masas_correcta(tb):
    tb.inject(
        """
        _masas_ok = sp.simplify(masas - masa*sp.eye(3)) == sp.zeros(3, 3)
        """
    )

    assert tb.ref("_masas_ok") is True


# --------------------------------------------------------------------------
# Ejercicio 2: frecuencias y modos normales
# --------------------------------------------------------------------------


def test_las_tres_frecuencias_propias_son_correctas(tb):
    # Se comparan como conjunto: el orden en que las devuelva eigenvects no
    # es parte de la respuesta.
    tb.inject(
        """
        _esperadas = [
            sp.sqrt(constante*(2 - sp.sqrt(2))/masa),
            sp.sqrt(2*constante/masa),
            sp.sqrt(constante*(2 + sp.sqrt(2))/masa),
        ]
        _son_tres = len(frecuencias) == 3
        _emparejadas = all(
            any(sp.simplify(_dada - _esperada) == 0 for _dada in frecuencias)
            for _esperada in _esperadas
        )
        """
    )

    assert tb.ref("_son_tres") is True
    assert tb.ref("_emparejadas") is True


def test_cada_modo_es_eigenvector_de_su_frecuencia(tb):
    # La definición misma: K v = omega**2 M v. No se compara contra vectores
    # escritos a mano porque un eigenvector está definido salvo un factor.
    tb.inject(
        """
        _son_tres_modos = len(modos) == 3
        _modos_ok = all(
            sp.simplify(
                rigidez*_vector - _omega**2 * masas * _vector
            ) == sp.zeros(3, 1)
            for _omega, _vector in zip(frecuencias, modos)
        )
        _ninguno_es_cero = all(_vector != sp.zeros(3, 1) for _vector in modos)
        """
    )

    assert tb.ref("_son_tres_modos") is True
    assert tb.ref("_modos_ok") is True
    # El vector cero cumple la ecuación pero no es un modo normal.
    assert tb.ref("_ninguno_es_cero") is True


# --------------------------------------------------------------------------
# Ejercicio 3: la evolución temporal
# --------------------------------------------------------------------------


def test_movimiento_cumple_las_condiciones_iniciales(tb):
    tb.inject(
        """
        _inicial_ok = sp.simplify(
            movimiento.subs(tiempo, 0) - sp.Matrix([amplitud, 0, 0])
        ) == sp.zeros(3, 1)
        _parte_del_reposo = sp.simplify(
            sp.diff(movimiento, tiempo).subs(tiempo, 0)
        ) == sp.zeros(3, 1)
        """
    )

    assert tb.ref("_inicial_ok") is True
    assert tb.ref("_parte_del_reposo") is True


def test_movimiento_satisface_el_sistema(tb):
    # Sustituir de vuelta en M x'' = -K x: el residuo debe ser la matriz cero.
    tb.inject(
        """
        _residuo = sp.simplify(
            masas * sp.diff(movimiento, tiempo, 2) + rigidez * movimiento
        )
        _residuo_ok = _residuo == sp.zeros(3, 1)
        """
    )

    assert tb.ref("_residuo_ok") is True


def test_movimiento_es_exacto(tb):
    # Un 1.4142 en lugar de sp.sqrt(2) habría dejado un flotante, y con él se
    # pierde la posibilidad de simplificar el residuo a cero exacto.
    tb.inject(
        """
        _sin_flotantes = not movimiento.atoms(sp.Float)
        """
    )

    assert tb.ref("_sin_flotantes") is True


# --------------------------------------------------------------------------
# Ejercicio 4: la gráfica y el reporte
# --------------------------------------------------------------------------


def test_grafica_tiene_las_tres_masas_y_ejes_etiquetados(tb):
    # La calidad de la gráfica la juzga el asistente; aquí solo se comprueba
    # que existe, que trae las tres curvas y que los ejes dicen qué es qué.
    tb.inject(
        """
        _hay_tres_curvas = len(ax.lines) >= 3
        _etiquetas = [
            ax.get_xlabel(), ax.get_ylabel(), ax.get_title()
        ]
        _hay_leyenda = ax.get_legend() is not None
        """
    )

    assert tb.ref("_hay_tres_curvas") is True
    assert all(etiqueta.strip() for etiqueta in tb.ref("_etiquetas"))
    assert tb.ref("_hay_leyenda") is True


def test_reporte_incluye_las_tres_frecuencias_en_latex(tb):
    # El punto del ejercicio es que las frecuencias no se tecleen a mano: el
    # LaTeX de cada una tiene que aparecer literal dentro del reporte.
    tb.inject(
        """
        _es_cadena = isinstance(reporte, str)
        _todas_aparecen = all(
            sp.latex(_omega) in reporte for _omega in frecuencias
        )
        """
    )

    assert tb.ref("_es_cadena") is True
    assert tb.ref("_todas_aparecen") is True
