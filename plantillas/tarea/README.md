# Plantilla de tarea

Punto de partida para preparar la tarea corta de cualquier semana. Contiene
un notebook con dos ejercicios de ejemplo ya resueltos (solo para que la
plantilla se pueda ejecutar de punta a punta) y la estructura de tests que
GitHub Classroom usa para calificar automáticamente.

## Cómo usarla

1. Copia esta carpeta a `semana-NN/tarea/` en el repo del curso.
2. Renombra `tarea-NN.ipynb` a `tarea-NN.ipynb` con el número real de semana,
   y reemplaza dentro del notebook: `<NN>`, `<TEMA>`, `<FECHA DE ENTREGA>` y
   los objetivos de aprendizaje.
3. Sustituye los dos ejercicios de ejemplo (derivada de `x**3` y de `x**n`)
   por el enunciado real de la tarea. Dejalos como `# TODO` para que el
   estudiante los resuelva — **no dejes la solución resuelta** en la rama
   pública (ver "Qué NO hacer" en `CLAUDE.md`).
4. Actualiza `tests/test_tarea.py` (público) y, si aplica,
   `tests/test_tarea_oculto.py` (oculto) para que hagan `tb.ref(...)` sobre
   los nombres de variable reales que definiste en el notebook, y renombra
   cada test según la habilidad que evalúa (`test_<habilidad>_correcta`, no
   `test_1`).
5. **Antes de publicar el assignment**: quita `tests/test_tarea_oculto.py`
   del repositorio base que reciben los estudiantes en GitHub Classroom.
   Ese archivo se agrega aparte, solo en el momento de calificar (por
   ejemplo en una rama o repo privado de calificación) — nunca debe llegar
   al repo que clonan los estudiantes.
6. Crea el assignment en la UI de GitHub Classroom, configurando ahí los
   test cases (comando, puntaje máximo, timeout). Classroom genera su propio
   `.github/workflows/classroom.yml`; verifica que coincida en estructura
   con el de esta plantilla (pesos: 70% público / 30% oculto, respetando el
   máximo de 30% para tests ocultos de `CLAUDE.md`).

## Cómo funciona el autograding (para el profesor/asistente)

Los estudiantes no escriben ningún `.py`: todo vive en el notebook. Los
tests usan `testbook` para ejecutar `tarea-NN.ipynb` (fixture `tb` en
`tests/conftest.py`, compartida entre todos los tests) y leer, con
`tb.ref("<nombre_variable>")`, el resultado que el estudiante calculó en una
celda. Luego se compara por equivalencia simbólica:

```python
resultado = sp.sympify(tb.ref("str(resultado_derivada)"), locals={"x": x})
assert sp.simplify(resultado - esperado) == 0
```

`tb.ref()` solo transfiere valores serializables a JSON, y los objetos de
SymPy no lo son — por eso se pide `str(...)` del resultado y se reconstruye
con `sp.sympify`, pasando en `locals` los mismos símbolos (con las mismas
suposiciones) que declara el notebook. Si cambias las suposiciones de un
símbolo en el notebook, actualízalas también en el test correspondiente.

Esta mecánica es invisible para el estudiante — no necesita saber pytest ni
testbook antes de la semana 11.

### Verificar localmente

```bash
pip install -r requirements.txt
pytest tests/ -v
```
