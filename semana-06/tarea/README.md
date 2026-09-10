# Tarea 06: Tres masas acopladas — entregable del Módulo 1

Entrega antes de la clase de la Semana 7, por **Pull Request dentro de tu
propio fork** — el mismo flujo de las semanas 3 a 5. El paso a paso está en
[`docs/git-guia.md`](../../docs/git-guia.md).

Esta entrega **cierra el Módulo 1** y es el entregable del módulo: pesa más que
una tarea semanal y se evalúan tres cosas, no una.

| Qué | Quién lo evalúa |
|---|---|
| Los resultados simbólicos y la gráfica | `tests/test_tarea.py`, automático |
| La discusión física del final | El asistente, leyendo tu notebook |
| El historial de commits | El asistente, mirando tu Pull Request |

## Qué entregar

`tarea-06.ipynb` con los cuatro `# TODO` completos, usando los nombres exactos
de variable que pide cada enunciado, y la celda de discusión contestada. No hay
que escribir ningún archivo `.py` ni tocar la carpeta `tests/`.

- **Ejercicio 1 (planteamiento):** los cuatro símbolos con sus suposiciones y
  las matrices $K$ y $M$ del sistema de tres masas.
- **Ejercicio 2 (modos normales):** las tres frecuencias propias y sus tres
  modos. Los tests no comparan tus modos contra vectores escritos a mano —
  verifican la definición, $K\mathbf{v} = \omega^2 M\mathbf{v}$ — así que
  cualquier múltiplo correcto y cualquier orden se dan por buenos, siempre que
  `modos[i]` corresponda a `frecuencias[i]`.
- **Ejercicio 3 (evolución temporal):** la superposición con
  $\mathbf{x}(0) = (A, 0, 0)$ y reposo inicial, verificada sustituyéndola de
  vuelta en $M\ddot{\mathbf{x}} = -K\mathbf{x}$.
- **Ejercicio 4 (gráfica y reporte):** las tres masas graficadas con `lambdify`
  y Matplotlib, con ejes etiquetados y leyenda, y un reporte cuyas frecuencias
  se insertan con `sp.latex` en lugar de teclearse.

## Sobre el historial de commits

Haz **un commit por ejercicio**, con mensajes en español y en imperativo que
digan qué hiciste: `Plantea las matrices K y M del sistema de tres masas`,
`Obtiene las tres frecuencias propias`, y así. Es lo mismo que venimos haciendo
en el repositorio del curso desde la semana 3.

Un único commit gigante la noche anterior cuesta puntos aunque el notebook esté
perfecto: parte de lo que se evalúa en este entregable es que el trabajo sea
legible por otra persona, y el historial es la mitad de eso.

## Antes de entregar

- [ ] El notebook corre completo desde un kernel limpio
      (`Kernel → Restart & Run All`) y llega al final sin errores. Un notebook
      que no ejecuta completo no se puede calificar.
- [ ] Verificaste tus soluciones en lugar de creerles: el residuo
      $M\ddot{\mathbf{x}} + K\mathbf{x}$ tiene que ser `sp.zeros(3, 1)`, y las
      condiciones iniciales tienen que cumplirse al sustituir $t = 0$.
- [ ] Todas las cantidades son **exactas**: `sp.sqrt(2)` en lugar de `1.4142`,
      `sp.Rational(1, 4)` en lugar de `0.25`. Un flotante suelto contamina la
      expresión entera, y hay un test que lo detecta.
- [ ] La gráfica tiene las tres curvas, los tres ejes etiquetados
      (`set_xlabel`, `set_ylabel`, `set_title`) y su `legend()`. Una gráfica sin
      etiquetas no dice nada, y hay un test que también lo revisa.
- [ ] Contestaste las tres preguntas de la celda de discusión. Esa parte no la
      califica el autograding.
- [ ] Tu rama de entrega está pusheada a **tu fork** (`origin`), y el PR se
      abrió **dentro de tu fork** — revisa el selector *base repository*.

Al abrir el PR, GitHub Actions corre `tests/test_tarea.py` y deja un check ✅ o
❌ en tu Pull Request. Si sale ❌, abre el check para ver qué test falló: el
nombre te dice qué habilidad quedó pendiente.
