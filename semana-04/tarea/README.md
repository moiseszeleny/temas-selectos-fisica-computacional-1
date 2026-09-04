# Tarea 04: Expresiones simbólicas

Entrega antes de la clase de la Semana 5, por **Pull Request dentro de tu
propio fork** — el mismo flujo que estrenaste en la semana 3. El paso a
paso está en [`docs/git-guia.md`](../../docs/git-guia.md).

## Qué entregar

`tarea-04.ipynb` con los dos `# TODO` completos, usando los nombres exactos
de variable y de función que pide cada enunciado. No hay que escribir
ningún archivo `.py` ni tocar la carpeta `tests/`.

- **Ejercicio 1 (caso base):** el factor de Lorentz y la energía
  relativista. Se califica que los símbolos lleven las suposiciones que la
  física garantiza, que las expresiones sean correctas y que
  `energia_en_reposo` salga de un `subs`, no escrita a mano.
- **Ejercicio 2 (caso límite):** `son_equivalentes(expresion_a, expresion_b)`,
  la comparación matemática que `==` no hace. Se califica también que
  devuelva un `bool` de Python cuando SymPy no logra decidir.

## Antes de entregar

- [ ] El notebook corre completo desde un kernel limpio
      (`Kernel → Restart & Run All`) y llega al final sin errores. Un
      notebook que no ejecuta completo no se puede calificar.
- [ ] Todas las cantidades son **exactas**: `sp.Rational(1, 2)` en lugar de
      `0.5`, `sp.sqrt(...)` en lugar de `** 0.5`, `sp.pi` en lugar de
      `math.pi`. Un flotante suelto contamina la expresión entera, y hay un
      test que lo detecta.
- [ ] Tu rama de entrega está pusheada a **tu fork** (`origin`), y el PR se
      abrió **dentro de tu fork** — revisa el selector *base repository*.

Al abrir el PR, GitHub Actions corre `tests/test_tarea.py` y deja un check
✅ o ❌ en tu Pull Request. Si sale ❌, abre el check para ver qué test
falló: el nombre te dice qué habilidad quedó pendiente.
