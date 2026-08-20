# Preparación — Semana 2

## Checklist

- [ ] Tu entorno sigue funcionando: `jupyter lab` abre sin errores con el
      entorno **activado**.
- [ ] El notebook de la semana 1 corre limpio de punta a punta
      (`Kernel → Restart & Run All`). Si algo falla ahí, resuélvelo antes
      de la clase — vamos a dar por conocido ese flujo.
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
esto es obligatorio ni se evalúa, es solo apoyo — si ya te sientes cómodo
con los tres, sáltate esta sección:

- **Funciones**, con argumentos por defecto y `return`:

  ```python
  def area_rectangulo(base, altura=1.0):
      return base * altura
  ```

- **Diccionarios**: crearlos, acceder por llave y recorrerlos con
  `.items()`. Los vamos a usar para mostrar por qué un objeto que puede
  cambiar es un mal candidato a llave:

  ```python
  constantes = {"g": 9.8, "c": 3e8}
  constantes["g"]                    # 9.8
  for nombre, valor in constantes.items():
      print(nombre, valor)
  ```

- **Desempaquetado de tuplas**: asignar varios nombres a la vez a partir
  de una tupla, en lugar de indexarla uno por uno:

  ```python
  punto = (3.0, 4.0)
  x, y = punto
  ```

- [Tutorial oficial de Python, capítulo 9 — Clases](https://docs.python.org/es/3/tutorial/classes.html).
  Con leer 9.1 a 9.3 antes de la clase es más que suficiente; lo demás lo
  vemos en vivo.

Si nunca has escrito una clase, **no la estudies de más**: la clase está
diseñada para construir la primera desde cero. Llegar con la duda es mejor
que llegar con la respuesta memorizada.

## Qué traer a la clase

Tu laptop con el entorno activado. Vamos a escribir una clase `Vector2D`
por capas, agregándole capacidades en vivo — vas a estar tecleando casi
toda la sesión.
