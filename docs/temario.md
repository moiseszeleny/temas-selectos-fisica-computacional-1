# Temas selectos de Física Computacional I
## Facultad de Ciencias, UNAM — Temario del curso (16 semanas)

### Descripción general

Curso orientado al uso de **SymPy** como sistema de álgebra computacional (CAS), **Jupyter Notebook** como entorno de trabajo interactivo, y **Git/GitHub** como herramientas de control de versiones y colaboración. El objetivo es que el estudiante desarrolle la capacidad de construir, extender y documentar herramientas computacionales propias para la física teórica, culminando en la creación de objetos matemáticos propios (subclases de objetos de SymPy) adaptados a problemas específicos de física.

**Dirigido a:** estudiantes con conocimientos básicos de programación en Python. No se requiere experiencia previa con SymPy, Jupyter o Git.

**Ritmo:** 16 semanas, con **dos sesiones de hora y media por semana** (3 horas semanales). Cada semana tiene su propio notebook por sesión y una tarea corta.

**Objetivo general:** al finalizar el curso, el estudiante será capaz de utilizar SymPy como herramienta de cómputo simbólico para problemas de física teórica, trabajar de forma colaborativa mediante Git/GitHub, y extender la arquitectura de SymPy mediante programación orientada a objetos para representar construcciones matemáticas propias de su área de interés.

---

## Módulo 0 — Entorno de trabajo y fundamentos (Semanas 1–3)

**Semana 1: Jupyter y repaso de Python científico**
- Instalación del entorno (conda/venv, JupyterLab)
- Notebooks: celdas de código vs. markdown, magics (`%timeit`, `%matplotlib inline`), extensiones útiles
- Repaso rápido de NumPy/Matplotlib como contraste con cómputo simbólico
- Buenas prácticas: notebooks reproducibles, orden de ejecución, exportación (nbconvert, `.py`)

**Semana 2: Programación orientada a objetos en Python**
- Clases y objetos: atributos, métodos, `__init__`
- Atributos/métodos de instancia vs. de clase; `@property`, `@classmethod`, `@staticmethod`
- Herencia y `super()`; jerarquías de clases (motivación directa: así está construido SymPy)
- Polimorfismo y *duck typing*
- Métodos especiales (*dunder methods*): `__repr__`, `__str__`, `__eq__`, `__add__`, `__hash__`
- Mutabilidad vs. inmutabilidad de objetos — por qué importa para objetos matemáticos (anticipa que los objetos de SymPy son inmutables)
- Práctica corta: crear una clase `Vector2D` o `Fraccion` propia con operadores sobrecargados (`__add__`, `__mul__`, `__eq__`), como ensayo general de lo que se hará con SymPy en el Módulo 4

**Semana 3: Git y GitHub**
- Modelo mental de Git: repositorio, área de preparación, historial de commits
- Comandos fundamentales: `init`, `clone`, `add`, `commit`, `push`, `pull`, `status`, `log`, `diff`
- Ramas y fusiones; resolución básica de conflictos
- GitHub: repositorios remotos, Pull Requests, Issues, revisión de código
- Notebooks y Git: por qué los diffs de `.ipynb` son problemáticos; configuración de `nbstripout`/`jupytext`

*Entregable:* fork de este repositorio configurado (ver `docs/git-guia.md`)
y primer PR: agregar tu fila a `docs/roster.md` con tu usuario de GitHub y
el link a tu fork.

---

## Módulo 1 — Fundamentos de SymPy (Semanas 4–6)

**Semana 4: Expresiones simbólicas**
- `Symbol`, `symbols`, suposiciones (`assumptions`: real, positive, integer, commutative)
- Construcción y manipulación de expresiones (`Add`, `Mul`, `Pow` a bajo nivel)
- Simplificación: `simplify`, `expand`, `factor`, `collect`, `trigsimp`, `radsimp`
- Sustitución (`subs`), evaluación numérica (`evalf`, `lambdify`)

**Semana 5: Cálculo simbólico**
- Derivadas (`diff`), integrales (`integrate`, definidas e indefinidas)
- Límites, series de Taylor (`series`)
- Ecuaciones diferenciales ordinarias (`dsolve`)
- Resolución de ecuaciones y sistemas (`solve`, `solveset`, `linsolve`, `nonlinsolve`)

**Semana 6: Álgebra lineal simbólica y visualización**
- `Matrix`, operaciones matriciales, eigenvalores/eigenvectores simbólicos
- Sistemas de ecuaciones lineales simbólicas
- Graficación simbólica (`sympy.plotting`) vs. numérica (Matplotlib con `lambdify`)
- Introducción a LaTeX embebido (`printing`, `latex()`) para reportes en notebooks

*Entregable:* notebook con solución simbólica completa de un problema clásico (p. ej. oscilador armónico forzado o un sistema de ecuaciones de una situación física), documentado y versionado con commits incrementales.

---

## Módulo 2 — SymPy aplicado a la física (Semanas 7–10)

**Semana 7: `sympy.physics.mechanics` I**
- Marcos de referencia, vectores y diádicas (`ReferenceFrame`, `Vector`)
- Cinemática de partículas y cuerpos rígidos

**Semana 8: `sympy.physics.mechanics` II**
- Formulación Lagrangiana (`LagrangesMethod`)
- Formulación de Kane (`KanesMethod`) como alternativa
- Generación automática de ecuaciones de movimiento

**Semana 9: Otros submódulos de física**
- `sympy.physics.units` — manejo consistente de unidades y dimensiones
- `sympy.physics.quantum` — kets, bras, operadores, conmutadores
- `sympy.physics.vector` y `sympy.diffgeom` — introducción a geometría diferencial simbólica (variedades, formas diferenciales, métricas) como antesala al Módulo 4

**Semana 10: Integración de herramientas + proyecto intermedio**
- Buenas prácticas para notebooks científicos largos (organización en múltiples notebooks/módulos `.py`)
- Uso de Git para trabajo en equipo: revisión de PRs entre estudiantes
- **Proyecto intermedio** (individual o en pareja): modelar un sistema físico de elección propia usando SymPy de principio a fin, con historial de commits significativo y README

---

## Módulo 3 — Prácticas de ingeniería de software científico (Semana 11)

**Semana 11: Estructura de proyectos, pruebas y flujo colaborativo**
- Organización de un paquete de Python (estructura de carpetas, `__init__.py`)
- Pruebas unitarias con `pytest` aplicadas a funciones simbólicas
- Documentación de código (docstrings; generación con Sphinx o mkdocs — mención breve)
- GitHub Actions básico (integración continua: correr pruebas automáticamente) — introductorio
- Manejo de issues, milestones y revisión de código entre pares sobre el proyecto intermedio

*(Módulo comprimido a una semana para preservar dos semanas de mecánica en el Módulo 2.)*

---

## Módulo 4 — Extendiendo SymPy: objetos propios de física teórica (Semanas 12–15)

**Semana 12: Arquitectura interna de SymPy**
- Jerarquía de clases: `Basic` → `Expr` → `Symbol`/`Function`/`AtomicExpr`
- Conexión explícita con la POO de la Semana 2: herencia, métodos especiales e inmutabilidad puestas en práctica a gran escala
- Cómo SymPy representa expresiones como árboles (`args`, `func`, propiedades `.is_...`)
- El sistema de suposiciones (`assumptions0`, métodos `_eval_*`)
- Métodos especiales que SymPy invoca automáticamente (`_eval_simplify`, `_eval_derivative`, `_eval_subs`, etc.)

**Semana 13: Creando subclases — funciones y símbolos personalizados**
- Subclasificar `Function` para crear funciones especiales propias (con reglas de derivación, simplificación o valores especiales definidos)
- Subclasificar `Symbol`/`AtomicExpr` para crear cantidades físicas con propiedades particulares (p. ej. un símbolo que "sabe" sus unidades, o un operador no conmutativo)
- Ejemplos guiados breves de distintas áreas (mecánica, cuántica, geometría) para ilustrar el patrón general, sin profundizar en una sola

**Semana 14: Álgebras y estructuras más complejas**
- Subclasificar `Expr` para objetos con reglas de multiplicación/suma propias (p. ej. operadores no conmutativos, cantidades tensoriales con reglas de contracción)
- Uso de `Basic.__new__` y manejo de `args` para construir objetos compuestos válidos dentro del framework de SymPy
- Integración con impresión (`_sympystr`, `_latex`) para que los objetos propios se vean bien en notebooks

**Semana 15: Desarrollo del proyecto final**
- Trabajo guiado en clase sobre el proyecto final
- Revisión de diseño en pares (¿la clase propuesta es coherente con el framework de SymPy? ¿aprovecha `assumptions`, `_eval_*`, impresión?)

*Entregable:* diseño e implementación de al menos una clase propia (subclase de `Function`, `Symbol` o `Expr`) que represente un objeto matemático de física teórica elegido libremente por el estudiante, con pruebas y documentación.

---

## Semana 16 — Presentación de proyectos finales

- Cada estudiante/equipo presenta su repositorio final: el objeto/clase creada (nivel base, y avanzado si aplica), su justificación física y matemática, pruebas, y un notebook de demostración
- Evaluación por pares además de la evaluación docente
- Cierre del curso: discusión sobre el ecosistema más amplio (otros CAS, dónde sigue SymPy, contribuir a proyectos open source)

---

## Niveles del proyecto final

| Nivel | Alcance | Carácter |
|---|---|---|
| **Base** | Subclase de `Function` o `Symbol` con al menos un comportamiento propio (derivación, simplificación, impresión), con pruebas y documentación | Obligatorio |
| **Avanzado** | Subclase de `Expr` con álgebra propia (reglas de suma/multiplicación, manejo de `args`, `__new__`) | Opcional, evaluado como puntos extra |

---

## Evaluación sugerida

| Componente | Peso |
|---|---|
| Tareas semanales (notebooks, Módulos 0–2) | 25% |
| Proyecto intermedio (Semana 10) | 20% |
| Participación en revisión de código (PRs, code reviews) | 10% |
| Proyecto final — nivel base (obligatorio) | 25% |
| Uso apropiado de Git a lo largo del curso (calidad del historial de commits) | 10% |
| Proyecto final — nivel avanzado (opcional) | hasta +10% extra |

*Nota:* el nivel avanzado del proyecto final se evalúa como puntos adicionales sobre el 100% base, no como requisito.

---

## Bibliografía y recursos sugeridos

- Documentación oficial de SymPy: https://docs.sympy.org
- Meurer, A. et al. *"SymPy: symbolic computing in Python"*, PeerJ Computer Science, 2017 (artículo de referencia sobre la arquitectura de SymPy)
- Documentación de `sympy.physics.mechanics` y tutoriales asociados
- Pro Git Book (Chacon & Straub) — disponible gratis en https://git-scm.com/book
- Jupyter documentation: https://docs.jupyter.org
- Coderefinery (Git for science): https://coderefinery.org/lessons/

---

### Notas para el instructor

- Dado que el nivel de entrada asume bases de Python pero no de SymPy/Jupyter/Git, las primeras tres semanas (incluida la de POO) son clave y no deben comprimirse.
- El hilo conductor del Módulo 4 se dejó deliberadamente flexible: se recomienda tener 2–3 ejemplos cortos preparados de distintas áreas (uno de mecánica clásica, uno de cuántica, uno de geometría/tensores) para que cada estudiante pueda elegir la dirección de su proyecto final según su propio interés.
- El proyecto intermedio (Semana 10) funciona como punto de control para detectar a tiempo problemas de manejo de Git o de SymPy antes del proyecto final.
