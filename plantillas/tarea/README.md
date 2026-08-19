# Plantilla de tarea

Punto de partida para preparar la tarea corta de cualquier semana. Contiene
un notebook con dos ejercicios de ejemplo ya resueltos (solo para que la
plantilla se pueda ejecutar de punta a punta) y la estructura de tests que
califican automáticamente cada entrega.

## Cómo usarla

1. Copia esta carpeta a `semana-NN/tarea/` en el repo del curso.
2. Renombra `tarea-NN.ipynb` con el número real de semana (por ejemplo,
   `tarea-07.ipynb`) — `tests/conftest.py` detecta el notebook por patrón
   (`tarea-*.ipynb`), así que no hace falta tocarlo al renombrar. Luego
   reemplaza dentro del notebook: `<NN>`, `<TEMA>`, `<FECHA DE ENTREGA>` y
   los objetivos de aprendizaje.
3. Sustituye los dos ejercicios de ejemplo (derivada de `x**3` y de `x**n`)
   por el enunciado real de la tarea. Dejalos como `# TODO` para que el
   estudiante los resuelva — **no dejes la solución resuelta** en la rama
   pública antes de la fecha de entrega.
4. Actualiza `tests/test_tarea.py` para que cada test haga `tb.ref(...)`
   sobre los nombres de variable reales que definiste en el notebook, y
   renombra cada test según la habilidad que evalúa
   (`test_<habilidad>_correcta`, no `test_1`). Todos los tests son públicos
   — no se usan tests ocultos en este curso.
5. No hace falta configurar nada más: `.github/workflows/autograding.yml`
   ya corre `tests/test_tarea.py` automáticamente en cada push, dentro del
   fork de cada estudiante (ver `docs/git-guia.md` en la raíz del curso).
   **Excepción — semanas 1 y 2:** todavía no se enseña Git, así que la
   entrega es por Google Classroom, no por PR. Adapta la sección de
   entrega del README (ver `semana-01/tarea/README.md` como ejemplo) y
   ten en cuenta que el asistente correrá los tests localmente sobre cada
   notebook descargado, no vía Actions.

## Cómo funciona el autograding (para el profesor/asistente)

Los estudiantes no escriben ningún `.py`: todo vive en el notebook. Los
tests usan `testbook` para ejecutar el notebook de la tarea (fixture `tb` en
`tests/conftest.py`, compartida entre todos los tests) y leer el resultado
que el estudiante calculó en una celda, comparándolo por equivalencia
simbólica. El porqué del patrón `str(...)` + `sp.sympify(...)` está
documentado en el docstring de `tests/conftest.py` — si cambias las
suposiciones de un símbolo en el notebook, actualízalas también en el test
correspondiente.

Esta mecánica es invisible para el estudiante — no necesita saber pytest ni
testbook antes de la semana 11.

### Verificar localmente

```bash
pip install -r requirements.txt
pytest tests/ -v
```
