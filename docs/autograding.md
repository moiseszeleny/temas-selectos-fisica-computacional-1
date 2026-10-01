# Autograding: qué debe aparecer y a quién

Cómo se califican automáticamente las tareas (semana 3 en adelante) y qué
ve cada quien. Las tareas de las semanas 1 y 2 se entregan por Google
Classroom y el asistente corre los tests de forma local; no pasan por aquí.

## Cómo funciona

1. Entregas con un Pull Request **dentro de tu propio fork** (ver
   [`git-guia.md`](git-guia.md)).
2. El workflow `.github/workflows/autograding.yml` (uno solo, en la raíz del
   repositorio) se dispara con el PR, y también con cada push a una rama que
   no sea `main`.
3. Las ramas `draft/` (material del profesor, con la tarea sin resolver a
   propósito) se omiten: ni el push ni su PR califican.
4. Detecta qué `semana-NN/tarea/tarea-NN.ipynb` cambió y califica **solo esa
   tarea**. Si no cambió ningún `tarea-NN.ipynb`, no hay nada que calificar.
5. Instala `semana-NN/tarea/requirements.txt`, ejecuta tu notebook completo
   desde un kernel limpio y corre `pytest tests/test_tarea.py -v`.
6. Cada test revisa una habilidad por **equivalencia simbólica**, no por
   igualdad de texto: cualquier forma algebraica correcta cuenta.

Los tests son públicos: están en `semana-NN/tarea/tests/test_tarea.py`.

## Qué ves tú (estudiante)

**Una sola vez:** habilita Actions en tu fork: pestaña **Actions** → botón
verde para confirmar y habilitar los workflows (GitHub lo muestra en inglés:
«I understand my workflows, go ahead and enable them»). Sin esto no corre
nada.

**En tu PR**, al final de la conversación, en el recuadro de *checks*:

| Símbolo | Significa |
|---|---|
| 🟡 Autograding (`semana-NN/tarea`) — en curso | Está corriendo; tarda de 1 a 3 minutos |
| ✅ Autograding (`semana-NN/tarea`) — pasó | Todos los tests pasaron |
| ❌ Autograding (`semana-NN/tarea`) — falló | Al menos un test falló, o el notebook no ejecutó completo |

Además aparece un job corto, **Detectar tarea**, que siempre debe salir ✅.

Da clic en **Details** del job `Autograding (...)` → paso **Tests**. Eso es
lo que debes ver cuando todo va bien:

```text
collected 11 items

tests/test_tarea.py::test_simbolos_tienen_nombre_y_suposiciones_correctos PASSED [  9%]
tests/test_tarea.py::test_potencial_de_lennard_jones_correcto PASSED     [ 18%]
...
============================== 11 passed in 12.40s ==============================
```

Cuando algo falta, el test sale `FAILED` (el nombre dice qué habilidad quedó
pendiente) y debajo aparece el error de la celda del notebook. Esta es una
salida real, de una tarea sin resolver (los `...` del `# TODO` siguen ahí):

```text
tests/test_tarea.py::test_simbolos_tienen_nombre_y_suposiciones_correctos FAILED [  9%]
tests/test_tarea.py::test_potencial_de_lennard_jones_correcto FAILED     [ 18%]
...
E           AttributeError: 'ellipsis' object has no attribute 'is_positive'
...
============================== 11 failed in 1.78s ==============================
```

El error de la celda (aquí `'ellipsis'`, porque el ejercicio sigue sin
resolver) te dice dónde mirar en tu notebook.

**Si sale ❌:**

1. Lee el nombre del test que falló y el mensaje debajo (`assert` o el error de
   la celda del notebook).
2. Si el error viene de una celda (`TestbookRuntimeError`), tu notebook no
   ejecuta completo: en Jupyter, *Kernel → Restart & Run All* y corrige.
3. Verifica que usaste los **nombres de variable exactos** que pide el
   enunciado, y cantidades exactas (`sp.Rational`, `sp.pi`), no flotantes.
4. Haz commit y push a la misma rama: el check se vuelve a correr solo.

**Qué no califica el autograding:** las celdas de discusión (markdown). Un ✅ no
es la calificación final: el asistente revisa además esa parte y deja
comentarios línea por línea en tu PR. En la tarea de la semana 6 se evalúan
también la discusión y tu historial de commits.

## Qué ve el profesor / asistente

- **En cada PR del fork** (ubícalo con [`roster.md`](roster.md)): los mismos
  checks que ve el estudiante. Un ✅ significa que la parte automática está
  bien; falta revisar la discusión y dejar la retroalimentación en el PR.
- **En el fork, pestaña Actions:** una ejecución por push o PR, con el
  nombre del job `Autograding (semana-NN/tarea)` y el log completo de pytest.
- **Desde la terminal** (sin entrar a cada fork):

  ```bash
  gh pr list  -R <usuario>/temas-selectos-fisica-computacional-1 --state all
  gh pr checks <número> -R <usuario>/temas-selectos-fisica-computacional-1
  gh run list -R <usuario>/temas-selectos-fisica-computacional-1 --limit 5
  gh run view <id-de-run> -R <usuario>/... --log-failed
  ```

- **Sin check (fork sin Actions habilitado, o semanas 1–2):** descarga el
  notebook y corre localmente, con el entorno del curso:

  ```bash
  pytest semana-NN/tarea/tests/ -v
  ```

  Mismo resultado que en Actions, porque son los mismos tests.
- **Re-ejecutar** un check desde el fork requiere permisos de escritura en él;
  si no los tienes, pide al estudiante un nuevo push o corre localmente.

## Si no aparece ningún check

| Qué ves | Causa probable | Qué hacer |
|---|---|---|
| El PR no tiene sección de checks | Actions no está habilitado en el fork | Pestaña **Actions** del fork → habilitarlo; luego un push nuevo |
| El PR dice `base repository: moiseszeleny/...` | El PR se abrió contra el repositorio del curso, no contra el fork | Cerrarlo y abrir uno nuevo con base en `<tu-usuario>/...` (ver `git-guia.md`, paso 6) |
| Solo aparece **Detectar tarea** ✅, sin `Autograding (...)` | En el PR no cambió ningún `tarea-NN.ipynb` | Confirmar que la tarea resuelta está en la rama del PR |
| ❌ en el paso **Instalar dependencias** | Falla `pip install -r requirements.txt` | Revisar el log; avisar al profesor (no es culpa del estudiante) |
| ❌ en **Tests**, `TestbookRuntimeError` | El notebook no ejecuta completo | Restart & Run All y corregir la celda que falla |
| ❌ en **Tests**, falla un solo test | Esa habilidad no es correcta | Releer el enunciado y los nombres de variable |
