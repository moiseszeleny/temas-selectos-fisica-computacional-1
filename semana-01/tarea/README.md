# Tarea 01: Jupyter y repaso de Python científico

Entrega antes de la clase de la Semana 2, vía Pull Request en tu
repositorio de GitHub Classroom.

## Qué entregar

Completa los `# TODO` de `tarea-01.ipynb` con tu solución. No necesitas
escribir ningún archivo `.py` ni tocar la carpeta `tests/` — el
autograding corre sobre tu notebook.

## Verificar tu solución localmente

```bash
pip install -r requirements.txt
pytest tests/test_tarea.py -v
```

Los tests en `tests/test_tarea.py` son los mismos (o del mismo tipo) que
GitHub Classroom va a correr para calificar el caso base de cada
ejercicio. Puede haber tests ocultos adicionales, con un peso máximo del
30% del puntaje total, que cubren casos límite de la misma habilidad.

## Cómo funciona el autograding (referencia)

No necesitas entender `pytest` ni `testbook` para esta tarea — eso se ve
formalmente hasta la semana 11. Solo asegúrate de que las variables que
pide cada ejercicio queden definidas con el nombre exacto indicado en el
enunciado.
