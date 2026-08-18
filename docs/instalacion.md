# Instalación del entorno

Guía para preparar el entorno de trabajo del curso antes de la semana 1.
Instala una de las dos opciones (conda o `venv`) — no hace falta hacer ambas.

## Prerrequisitos

- Python ≥ 3.11.
- Una cuenta de GitHub (se usará a partir de la semana 3).

## Opción A: conda

```bash
conda create -n fisica-computacional python=3.11
conda activate fisica-computacional
pip install jupyterlab sympy matplotlib
```

## Opción B: `venv` + `pip`

```bash
python3 -m venv .venv
source .venv/bin/activate   # en Windows: .venv\Scripts\activate
pip install --upgrade pip
pip install jupyterlab sympy matplotlib
```

> Estos son los paquetes mínimos para arrancar. Cuando se prepare la semana 1
> se formalizarán en un `requirements.txt` con versiones fijas, como indica
> `CLAUDE.md`.

## Verificación

Con el entorno activado:

```bash
jupyter lab
```

Debe abrirse JupyterLab en el navegador. Crea un notebook nuevo y corre en
una celda:

```python
import sympy as sp
sp.sqrt(8)
```

Si el resultado se muestra como `2*sqrt(2)` (o su versión renderizada en
LaTeX), el entorno está listo.

## Problemas comunes

- **`jupyter: command not found`** — revisa que el entorno (conda o `venv`)
  esté activado en la misma terminal donde corres el comando.
- **`ModuleNotFoundError: No module named 'sympy'`** — el kernel de Jupyter
  no corresponde al entorno donde instalaste los paquetes; verifica con
  `jupyter kernelspec list` o reinstala el kernel con
  `python -m ipykernel install --user`.
- **Conflictos entre conda y `venv` en la misma máquina** — usa solo una de
  las dos opciones; mezclar ambas suele causar problemas de rutas.

Si algo no funciona, trae el error a la primera clase o abre un Issue en tu
repositorio del curso.
