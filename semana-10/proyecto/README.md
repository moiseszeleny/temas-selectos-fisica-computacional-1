# Proyecto intermedio

El punto de control del curso: un sistema físico **que eliges tú**, modelado
con SymPy de principio a fin, en un repositorio propio, con README e historial
de commits que alguien más pueda leer. Vale el **20 %** de la calificación
(ver [`docs/temario.md`](../../docs/temario.md)) y sustituye la tarea de la
semana 10: esta semana no hay `tarea-10.ipynb` ni autograding.

Se hace solo o en pareja.

## Qué se pide

Un sistema físico pequeño que entiendas bien, resuelto con lo que viste en las
semanas 4 a 9: expresiones y suposiciones, cálculo, ecuaciones diferenciales,
álgebra lineal, `physics.mechanics`, `physics.units`, `physics.quantum`. El
proyecto responde **una pregunta concreta**: "¿cómo depende el periodo de la
amplitud?", y no "estudiar el péndulo".

Algunas ideas, solo como punto de partida:

- Un péndulo con resorte, con base móvil o con fricción: ecuaciones con
  `LagrangesMethod`, el límite de pequeñas oscilaciones y modos normales.
- Un circuito RLC: `dsolve`, los regímenes de amortiguamiento y la
  resonancia, con unidades de `physics.units`.
- Una órbita kepleriana: cantidades conservadas, la ecuación de la órbita y
  el periodo con unidades.
- Un sistema de dos niveles o dos espines: el hamiltoniano como matriz, sus
  eigenvalores y la evolución temporal.

## Cómo se organiza

En un **repositorio nuevo** llamado exactamente **`proyecto-intermedio`**, no
en tu fork del curso. El asistente lo busca con ese nombre en la cuenta de cada
estudiante. En pareja, el repo vive en la cuenta de una de las dos personas y
la otra es colaboradora; el README nombra a las dos.

La estructura es la de la sesión 1 de la semana 10:

```
proyecto-intermedio/
├── README.md               # a partir de plantilla-readme.md
├── requirements.txt        # versiones fijas, como el del curso
├── modelo.py               # símbolos, funciones y parámetros (sin display)
├── 01-planteamiento.ipynb  # de 1 a 3 notebooks numerados,
├── 02-solucion.ipynb       # cada uno importa modelo.py
└── 03-graficas.ipynb       # y corre solo desde un kernel limpio
```

El nombre del módulo y de los notebooks puede ser otro; lo que importa es la
forma. Los notebooks se versionan **sin salidas**: `nbstripout --install` en el
clon del proyecto, igual que en el del curso.

Se trabaja en la rama **`desarrollo`**, nunca directo en `main`. En pareja,
cada quien trabaja en su propia rama y abre PRs hacia `desarrollo`, que revisa
la otra persona.

## Fechas: dos entregas

| Entrega | Cuándo | Qué |
|---|---|---|
| **Preliminar** | antes de la clase de la semana 11 | un PR **`desarrollo → main`** abierto en tu repo, **sin fusionar**, con el modelo planteado y al menos un resultado verificado |
| **Final** | antes de la clase de la semana 12 | revisión atendida, PR fusionado a `main` y tag **`entrega-final`** en ese commit |

En la semana 11 un compañero revisa tu PR preliminar con lo que vimos en la
sesión 2 de la semana 10, y tú revisas el suyo. Entre las dos entregas
contestas esa revisión con commits en `desarrollo`. Para la entrega final:

```bash
git switch main
git pull                      # trae el merge que hiciste en GitHub
git tag -a entrega-final -m "Entrega final del proyecto intermedio"
git push origin entrega-final
```

## Cómo se evalúa

| Criterio | Peso | Qué se mira |
|---|---|---|
| Física y SymPy | 30 % | el modelo es correcto; símbolos con suposiciones; cantidades exactas; `display` para mostrar expresiones |
| Verificación | 15 % | el resultado se comprueba: se sustituye de vuelta, un caso límite conocido o una cantidad conservada |
| Organización | 20 % | módulo y notebooks como arriba; cada notebook corre desde un kernel limpio; nada copiado y pegado |
| README | 15 % | otra persona entiende qué es, qué pregunta responde, cómo correrlo y qué se concluye |
| Historial y revisión | 20 % | commits atómicos con mensajes en imperativo; la revisión de la semana 11 contestada hilo por hilo; en pareja, commits **de las dos personas** |

Un proyecto que no corre desde un kernel limpio no se puede calificar.

## Antes de entregar

- [ ] Cada notebook corre completo con **Kernel → Restart Kernel and Run All
      Cells**, por sí solo, sin errores.
- [ ] Ningún valor está escrito dos veces: los parámetros viven en el módulo.
- [ ] Cantidades **exactas**: `sp.Rational(1, 2)` y no `0.5`, salvo en la parte
      numérica de las gráficas.
- [ ] Al menos un resultado **verificado** de forma explícita en el notebook.
- [ ] El README está completo, sin las instrucciones de la plantilla.
- [ ] `git status` limpio y ningún notebook con salidas en el commit
      (`nbstripout --install` hecho en el clon).
- [ ] Para la entrega preliminar: el PR va de `desarrollo` a `main` **en tu
      repo `proyecto-intermedio`** y está abierto. Para la final: fusionado y con
      el tag `entrega-final` en GitHub (pestaña *Tags*).
