# Preparación — Semana 1

Antes de la clase necesitas tener el entorno instalado y funcionando. La
guía completa vive en [`docs/instalacion.md`](../../docs/instalacion.md);
aquí solo está el checklist para confirmar que quedó listo.

## Checklist

- [ ] Creaste el entorno (conda o `venv`) e instalaste las dependencias con
      `pip install -r requirements.txt`.
- [ ] El entorno está **activado** en la terminal que vas a usar.
- [ ] `jupyter lab` abre JupyterLab en el navegador sin errores.
- [ ] En un notebook nuevo, la celda

  ```python
  import sympy as sp
  sp.sqrt(8)
  ```

  muestra `2*sqrt(2)` (o su versión renderizada en LaTeX).

Si algo de esto falla, revisa la sección "Problemas comunes" de
`docs/instalacion.md` antes de la clase. Si sigue sin funcionar, tráelo a la
sesión — no necesitas resolverlo solo.

## Si quieres repasar Python básico

La clase asume que ya conoces tipos básicos, `if`/`for`, funciones y listas.
Si sientes que lo tienes oxidado, estos recursos ayudan (no es obligatorio
ni se evalúa, es solo apoyo):

- [Tutorial oficial de Python](https://docs.python.org/es/3/tutorial/) —
  capítulos 3 y 4 (tipos y control de flujo).
- Comprensión de listas (*list comprehensions*): las vamos a usar bastante
  en contraste con los bucles `for` explícitos.

## Qué traer a la clase

Tu laptop con el entorno ya instalado y activado. Vamos a trabajar en vivo
sobre JupyterLab desde la primera celda.
