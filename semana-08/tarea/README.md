# Tarea 08: La cuenta en el aro, ahora con dinámica

Entrega antes de la clase de la Semana 9, por **Pull Request dentro de tu
propio fork** — el mismo flujo de las semanas 3 a 7. El paso a paso está en
[`docs/git-guia.md`](../../docs/git-guia.md).

## Qué entregar

`tarea-08.ipynb` con los cuatro `# TODO` completos, usando los nombres exactos
de variable que pide cada enunciado, y la celda de discusión contestada. No hay
que escribir ningún archivo `.py` ni tocar la carpeta `tests/`, ni cambiar la
celda de imports: `t`, `N` y `centro` ya vienen declarados y los tests los usan.

- **Ejercicio 1 (el sistema):** los símbolos con sus suposiciones, los marcos
  del aro y de la cuenta, el punto y la partícula con su energía potencial. Se
  califica la energía potencial por separado, así que un signo equivocado en
  la gravedad se detecta aquí y no en la ecuación de movimiento.
- **Ejercicio 2 (Lagrange):** el Lagrangiano y la ecuación de movimiento con
  `LagrangesMethod`.
- **Ejercicio 3 (Kane):** la velocidad generalizada, la velocidad angular
  escrita con ella y la ecuación de movimiento con `KanesMethod`. Hay un test
  que compara tus dos métodos entre sí.
- **Ejercicio 4 (equilibrios):** la aceleración angular despejada, el
  equilibrio fuera del fondo y la velocidad de giro crítica.

Los tests no comparan cadenas ni te exigen una forma particular de las
ecuaciones: despejan la aceleración de tu ecuación y la comparan con la
esperada, simplificando la diferencia. Una ecuación multiplicada por una
constante o con el signo cambiado se da por buena.

## Antes de entregar

- [ ] El notebook corre completo desde un kernel limpio
      (`Kernel → Restart & Run All`) y llega al final sin errores. Un notebook
      que no ejecuta completo no se puede calificar.
- [ ] Hiciste el ejercicio 3 **después** del 2, en ese orden en el notebook:
      el `set_ang_vel` de Kane cambia las velocidades que ve Lagrange.
- [ ] Verificaste tus soluciones en lugar de creerles: los `rhs()` de Kane y
      de Lagrange, con $\dot\theta \to u$, difieren en cero.
- [ ] Los escalares y las ecuaciones están etiquetados con `sp.Eq`, como en
      clase.
- [ ] Todas las cantidades son **exactas**: `sp.Rational(1, 2)` en lugar de
      `0.5`. Un flotante suelto contamina la expresión entera, y hay un test que
      lo detecta.
- [ ] Contestaste las tres preguntas de la celda de discusión. Esa parte no la
      califica el autograding: la revisa el asistente.
- [ ] Tu rama de entrega está pusheada a **tu fork** (`origin`), y el PR se
      abrió **dentro de tu fork** — revisa el selector *base repository*.

Al abrir el PR, GitHub Actions corre `tests/test_tarea.py` y deja un check ✅ o
❌ en tu Pull Request. Si sale ❌, abre el check para ver qué test falló: el
nombre te dice qué habilidad quedó pendiente.
