# CLAUDE.md — Física Computacional (Cómputo Simbólico con SymPy)

Curso de la Facultad de Ciencias, UNAM. Semestre 2027-1, 16 semanas.
Stack del curso: **SymPy, Jupyter Notebook, Git/GitHub**.
Este archivo define las convenciones del repositorio. Respétalas en toda sesión,
tanto del profesor como del asistente.

## Estado actual del repositorio

Por ahora el repositorio solo contiene este `CLAUDE.md` y `docs/temario.md`.
El resto de la estructura descrita abajo (`semana-NN/`, `plantillas/`,
`requirements.txt`, `docs/instalacion.md`, `docs/politicas.md`,
`docs/git-guia.md`, control de versiones con Git) es el diseño objetivo y se
irá creando conforme avance el curso (a partir de la semana 1). No asumas que
esos archivos o carpetas ya existen sin verificarlo.

## Contexto pedagógico

- Estudiantes de física con Python básico; **sin experiencia previa** en SymPy, Jupyter ni Git.
- Objetivo final del curso: que los estudiantes creen objetos matemáticos propios
  como subclases de SymPy (`Function`/`Symbol` en el nivel base; `Expr` con álgebra
  propia en el nivel avanzado).
- El material debe ser ejemplar: los commits, ramas y PRs de este repo son
  también material didáctico. Los estudiantes los leerán.

## Mapa del curso

El temario detallado vive en `docs/temario.md` — esa es la fuente de verdad.
Esta tabla es solo el mapa de progresión: al generar material de la semana N,
**no usar conceptos de módulos posteriores**.

| Semanas | Módulo | Los estudiantes ya dominan |
|---------|--------|---------------------------|
| 1–3   | M0: Jupyter, POO, Git       | Python básico |
| 4–6   | M1: Fundamentos de SymPy    | + POO, Git, notebooks reproducibles |
| 7–10  | M2: SymPy aplicado a física | + símbolos, suposiciones, cálculo y álgebra lineal simbólica |
| 11    | M3: Ingeniería de software  | + `physics.mechanics`, `units`, `quantum`, `diffgeom` |
| 12–15 | M4: Extender SymPy          | + pytest, estructura de paquetes, CI |
| 16    | Presentaciones finales      | — |

Puntos de control:
- **Semana 3:** primer PR de cada estudiante (repo personal + notebook inicial).
- **Semana 10:** proyecto intermedio — punto de control antes del proyecto final.
- **Semanas 12–15:** proyecto final. Nivel base obligatorio (`Function`/`Symbol`);
  nivel avanzado opcional (`Expr` con álgebra propia), evaluado como puntos extra.

Restricciones derivadas del mapa:
- Antes de la semana 2 no asumir clases ni herencia; antes de la semana 3 no
  asumir Git.
- Antes de la semana 4 no usar SymPy en ejemplos, salvo como demostración
  motivacional sin exigir que el estudiante lo escriba.
- Antes de la semana 11 no exigir tests de pytest en el material de clase
  (sí pueden existir en el autograding de tareas, ocultos al estudiante).
- `Expr`, `Basic.__new__`, `args` y los métodos `_eval_*` no aparecen antes de
  la semana 12.

## Estructura del repositorio

```
semana-NN/
├── clase/           # notebook(s) de la sesión
│   └── semana-NN-tema.ipynb
├── preparacion/     # lecturas previas, instrucciones de instalación, etc.
└── tarea/           # tarea corta de la semana
    ├── tarea-NN.ipynb
    └── tests/       # tests de pytest para autograding
plantillas/          # plantillas de notebook y de tarea (GitHub Classroom)
docs/                # temario, políticas del curso, guía de Git para estudiantes
```

- Nombres de archivos y carpetas: minúsculas, sin acentos ni espacios, guiones medios.
- Todo el contenido visible para estudiantes se escribe **en español**.
  El código (nombres de variables, funciones, tests) se escribe en inglés.

## Flujo de trabajo con Git

- `main` es la rama publicada: solo recibe merges vía Pull Request. Nunca hagas
  push directo a `main`.
- Preparación de clase: rama `draft/semana-NN`. El PR lo revisa y aprueba el
  asistente antes del merge.
- Correcciones menores post-clase (typos, erratas): rama `fix/semana-NN-descripcion`.
- Al final de cada clase, etiquetar la versión resuelta del notebook:
  `clase-NN-resuelta`.
- Commits atómicos con mensajes en español, modo imperativo, máximo ~72
  caracteres en el título. Ejemplo: `Agrega ejercicio de conmutadores a la clase 7`.
- Al final del semestre se congela la edición con un tag `vAAAA-S`
  (p. ej. `v2027-1`); `main` sigue evolucionando para la siguiente edición.

## Notebooks

- **Siempre** verifica antes de abrir un PR que el notebook ejecuta completo y
  en orden desde un kernel limpio (`jupyter nbconvert --execute` o equivalente).
- Los notebooks se versionan **sin salidas**: `nbstripout` está configurado como
  filtro de git. No desactivarlo ni hacer commit de salidas.
- Estructura de un notebook de clase:
  1. Celda de título: tema, número de semana, objetivos de aprendizaje (3 máx.).
  2. Celda de imports (solo lo necesario; `sympy` se importa como `import sympy as sp`,
     nunca `from sympy import *` — excepto si la lección trata precisamente de eso).
  3. Secciones con encabezados Markdown (`##`), alternando explicación breve y código.
  4. Celdas de "en vivo": ejercicios incompletos marcados con `# TODO en clase`,
     que se resuelven durante la sesión.
  5. Celda final: resumen de lo aprendido y vínculo a la tarea de la semana.
- Preferir varias celdas cortas a una celda larga. Cada celda debe poder
  explicarse en clase en menos de dos minutos.

## Código y estilo SymPy

- Python ≥ 3.11, SymPy fijado a la versión declarada en `requirements.txt`.
- Usar `sp.symbols` con supuestos explícitos cuando importen
  (`real=True`, `positive=True`); comentar por qué.
- Mostrar resultados con `sp.init_printing()` / MathJax, no con `print`.
- En las semanas de subclassing: toda subclase de SymPy incluye docstring en
  español con la motivación física del objeto.

## Tareas y autograding

- Cada tarea corta incluye tests de pytest en `tarea/tests/` que GitHub
  Classroom ejecuta automáticamente.
- Los tests verifican **equivalencia simbólica**, no igualdad de cadenas:
  usar `sp.simplify(resultado - esperado) == 0` o `.equals()`.
- Nombrar los tests describiendo la habilidad evaluada:
  `test_derivada_parcial_correcta`, no `test_1`.
- Los tests públicos (visibles al estudiante) cubren el caso base; puede haber
  tests ocultos para casos límite, pero nunca más del 30% del puntaje.

## Roles

- **Profesor (Moises):** crea el material en ramas `draft/`, aprueba merges de
  correcciones del asistente, resuelve issues escaladas.
- **Asistente:** revisa PRs de clase (verificar ejecución limpia, claridad,
  erratas), es primer respondedor de issues de estudiantes, corre la revisión
  en lote de tareas y deja retroalimentación línea por línea en los repos de
  Classroom.
- Claude Code puede preparar borradores, ejecutar verificaciones y abrir PRs,
  pero **el merge a `main` siempre lo hace una persona**.

## Qué NO hacer

- No reescribir material de semanas ya impartidas (solo ramas `fix/` para erratas).
- No agregar dependencias sin actualizar `requirements.txt` y justificarlo en el PR.
- No incluir soluciones de tareas en ramas públicas antes de la fecha de entrega.
- No usar celdas mágicas de shell (`!pip install ...`) dentro de los notebooks;
  la instalación vive en `docs/instalacion.md`.

## Comandos útiles

```bash
# Verificar que un notebook ejecuta en limpio
jupyter nbconvert --to notebook --execute --inplace semana-NN/clase/*.ipynb

# Correr los tests de una tarea
pytest semana-NN/tarea/tests/ -v

# Configurar nbstripout (una sola vez por clon)
nbstripout --install
```
