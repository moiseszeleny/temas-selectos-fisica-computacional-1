# Preparación — Semana 2

Esta semana no hay nada que instalar: seguimos con el mismo entorno de la
semana 1. Lo que sí necesitas es llegar con Python básico fresco, porque la
clase construye clases propias desde la primera celda.

## Checklist

- [ ] Tu entorno sigue funcionando: `jupyter lab` abre sin errores con el
      entorno **activado**.
- [ ] El notebook de la semana 1 corre limpio de punta a punta
      (`Kernel → Restart & Run All`). Si algo falla ahí, resuélvelo antes
      de la clase — vamos a dar por sabido ese flujo.
- [ ] Entregaste la tarea 01 en Google Classroom.
- [ ] Puedes explicar, sin ver apuntes, qué hace este código:

  ```python
  def energia_cinetica(v, masa=1.0):
      return 0.5 * masa * v**2
  ```

  En particular: qué es `masa=1.0` y qué pasa si llamas la función sin ese
  segundo argumento.

## Si quieres repasar

La clase asume funciones, diccionarios y desempaquetado de tuplas. Nada de
esto es obligatorio ni se evalúa, es solo apoyo:

- [Tutorial oficial de Python, capítulo 9 — Clases](https://docs.python.org/es/3/tutorial/classes.html).
  Con leer 9.1 a 9.3 antes de la clase es más que suficiente; lo demás lo
  vemos en vivo.
- Diccionarios y el método `.items()`: los usamos para mostrar por qué un
  objeto que puede cambiar es un mal candidato a llave de diccionario.

Si nunca has escrito una clase, **no la estudies de más**: la clase está
diseñada para construir la primera desde cero. Llegar con la duda es mejor
que llegar con la respuesta memorizada.

## Qué traer a la clase

Tu laptop con el entorno activado. Vamos a escribir una clase `Vector2D`
por capas, agregándole capacidades en vivo — vas a estar tecleando casi
toda la sesión.
