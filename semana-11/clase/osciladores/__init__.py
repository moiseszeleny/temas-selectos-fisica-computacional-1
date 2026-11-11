"""Osciladores armónicos amortiguados, como paquete de Python.

Es el módulo ``oscilador.py`` de la semana 10 partido en dos archivos según de
qué trata cada función:

- ``amortiguado``: la ecuación de movimiento ``m x'' + b x' + k x = 0``, el
  régimen de amortiguamiento y su solución con condiciones iniciales.
- ``energia``: la energía mecánica de la masa a lo largo del movimiento.

Lo que se escribe aquí abajo es lo que se obtiene al hacer
``import osciladores``: así quien usa el paquete no necesita saber en qué
archivo vive cada función.
"""

from osciladores.amortiguado import ecuacion_de_movimiento, regimen, resolver, t, x
