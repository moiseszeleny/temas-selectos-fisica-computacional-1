# Instalación del entorno

Guía para preparar el entorno de trabajo del curso: Python/Jupyter antes de
la semana 1, y Git/GitHub antes de la semana 3. Para Python, instala una de
las dos opciones (conda o `venv`) — no hace falta hacer ambas.

## Prerrequisitos

- Python ≥ 3.11.
- Una cuenta de GitHub (se usará a partir de la semana 3).
- El archivo [`requirements.txt`](../requirements.txt) del repositorio del
  curso, guardado en la misma carpeta donde vas a correr los comandos de
  abajo. Todavía no usamos Git (eso empieza en la semana 3): en la página
  del archivo en GitHub, usa el botón **Raw** y guarda esa página como
  `requirements.txt`.

## Opción A: conda

```bash
conda create -n fisica-computacional python=3.11
conda activate fisica-computacional
pip install -r requirements.txt
```

## Opción B: `venv` + `pip`

```bash
python3 -m venv .venv
source .venv/bin/activate   # en Windows: .venv\Scripts\activate
pip install --upgrade pip
pip install -r requirements.txt
```

> El `requirements.txt` de la raíz del repo fija las versiones exactas de
> `jupyterlab`, `sympy`, `matplotlib` y el resto de las dependencias del
> curso, para que todos trabajemos con las mismas versiones.

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

## Git

Necesario a partir de la semana 3, pero conviene instalarlo desde ahora.

- **Windows:** descarga el instalador desde
  [git-scm.com/downloads](https://git-scm.com/downloads) y sigue el asistente
  (las opciones por defecto funcionan bien).
- **macOS:** `brew install git` (con [Homebrew](https://brew.sh)), o instala
  las "Command Line Tools" con `xcode-select --install`.
- **Linux (Debian/Ubuntu):** `sudo apt install git`.

Verifica la instalación:

```bash
git --version
```

Configura tu identidad (se usa para firmar tus commits):

```bash
git config --global user.name "Tu Nombre"
git config --global user.email "tu_correo@ejemplo.com"
```

## Cuenta de GitHub

1. Crea una cuenta gratuita en [github.com/signup](https://github.com/signup)
   si todavía no tienes una.
2. Activa la autenticación en dos pasos (recomendado).
3. Configura cómo te vas a autenticar al hacer `git push` desde tu máquina:
   HTTPS con un
   [personal access token](https://github.com/settings/tokens), o SSH
   siguiendo la
   [guía oficial de GitHub](https://docs.github.com/es/authentication/connecting-to-github-with-ssh).

## Editor de código: Visual Studio Code

Editor con más herramientas de desarrollo:

1. Descárgalo desde [code.visualstudio.com](https://code.visualstudio.com/).
2. Instala la extensión **Python** (Microsoft) y la extensión **Jupyter**
   (Microsoft) desde el panel de extensiones, para poder abrir y ejecutar
   notebooks `.ipynb` directamente en VS Code.

## Problemas comunes

- **`jupyter: command not found`** — revisa que el entorno (conda o `venv`)
  esté activado en la misma terminal donde corres el comando.
- **`ModuleNotFoundError: No module named 'sympy'`** — el kernel de Jupyter
  no corresponde al entorno donde instalaste los paquetes; verifica con
  `jupyter kernelspec list` o reinstala el kernel con
  `python -m ipykernel install --user`.
- **Conflictos entre conda y `venv` en la misma máquina** — usa solo una de
  las dos opciones; mezclar ambas suele causar problemas de rutas.
- **`git: command not found`** — abre una terminal nueva después de instalar
  Git (a veces hace falta reiniciarla para que reconozca el comando).

Si algo no funciona, trae el error a la primera clase o abre un Issue en tu
repositorio del curso.
