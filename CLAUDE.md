# CLAUDE.md — Temas selectos de Física Computacional I (Cómputo Simbólico con SymPy)

Curso de la Facultad de Ciencias, UNAM. Semestre 2027-1, 16 semanas.
Stack del curso: **SymPy, Jupyter Notebook, Git/GitHub**.
Este archivo define las convenciones del repositorio. Respétalas en toda sesión,
tanto del profesor como del asistente.

## Estado actual del repositorio

Por ahora el repositorio contiene `CLAUDE.md`, `docs/temario.md`,
`docs/instalacion.md`, `docs/git-guia.md`, `docs/roster.md`,
`requirements.txt`, `plantillas/`, `semana-00/clase/` y `semana-01/`
completa. `docs/politicas.md` es el único elemento de la estructura
objetivo que sigue sin crearse. No asumas que existe sin verificarlo.

El repositorio es **público**: los estudiantes hacen fork para entregar
tareas (ver `docs/git-guia.md`), así que no debe contener datos personales
de estudiantes ni soluciones resueltas de tareas antes de la fecha de
entrega.

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
plantillas/          # plantillas de notebook y de tarea
docs/                # temario, políticas del curso, guía de Git para estudiantes,
                      # roster de forks
```

- Nombres de archivos y carpetas: minúsculas, sin acentos ni espacios, guiones medios.
- Todo se escribe **en español**: el contenido visible para estudiantes y
  también el código — variables, funciones, clases, tests y docstrings.
- Los identificadores van sin acentos ni eñes, para no depender de la
  codificación del teclado de nadie: `desviacion_estandar`,
  `energia_cinetica`, `test_derivada_parcial_correcta`.
- Se conservan en su idioma original los nombres que vienen de Python, de
  SymPy o del ecosistema: `self`, `__init__`, `Symbol`, `subs`, `diff`.
  No se traducen.

## Flujo de trabajo con Git

Esta sección describe cómo se mantiene **este** repositorio (profesor y
asistente). Los estudiantes nunca abren ramas ni PRs contra `main` de este
repo — trabajan dentro de su propio fork y entregan tareas con un PR
**dentro de ese fork**; ver `docs/git-guia.md` para el flujo del estudiante.

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

- **Entrega — dos fases, según si ya se enseñó Git:**
  - **Semanas 1–2:** entrega por **Google Classroom** (fuera de este
    repo) — todavía no se asume que el estudiante sepa Git. El asistente
    corre `pytest tarea/tests/ -v` **localmente** sobre cada notebook
    descargado; no hay push a un fork que dispare Actions automáticamente.
  - **Semana 3 en adelante:** entrega vía PR dentro del fork del
    estudiante (ver `docs/git-guia.md`).
- Cada tarea corta incluye tests de pytest en `tarea/tests/`, corridos por
  un workflow de GitHub Actions (`tarea/.github/workflows/autograding.yml`)
  que se ejecuta automáticamente en el fork de cada estudiante en cada
  push (semana 3 en adelante) — no depende de ningún servicio externo.
- Los tests verifican **equivalencia simbólica**, no igualdad de cadenas:
  usar `sp.simplify(resultado - esperado) == 0` o `.equals()`.
- Nombrar los tests describiendo la habilidad evaluada:
  `test_derivada_parcial_correcta`, no `test_1`.
- Todos los tests de autograding son públicos (visibles al estudiante en
  `tarea/tests/`); no se usan tests ocultos.

## Roles

- **Profesor (Moises):** crea el material en ramas `draft/`, aprueba merges de
  correcciones del asistente, resuelve issues escaladas.
- **Asistente:** revisa PRs de clase (verificar ejecución limpia, claridad,
  erratas), es primer respondedor de issues de estudiantes, corre la revisión
  en lote de tareas y deja retroalimentación línea por línea en el fork y PR
  de cada estudiante (ver `docs/roster.md` para ubicarlos).
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
