#!/usr/bin/env python3
"""Califica en lote la tarea de una semana, sin depender de los forks.

Uso (desde la raíz del repositorio, con el entorno del curso activado):

    python .github/scripts/revisar-entregas.py 05
    python .github/scripts/revisar-entregas.py 05 --solo-tabla

Para cada estudiante:

1. Busca su PR de entrega: cualquier PR cuya rama venga de su fork y que
   toque un `.ipynb` dentro de `semana-NN/tarea/`, sin importar en qué repo
   se abrió (su fork, el de otra persona o el del curso) ni cómo se llame el
   notebook.
2. Descarga el notebook tal como está en el último commit del PR.
3. Le corre los tests **del curso** (`semana-NN/tarea/tests/` de este repo,
   no los del fork) y lo exporta a HTML con sus salidas.
4. Imprime una tabla con el resultado de todos.

No necesita que el estudiante tenga Actions habilitado ni su fork al día.
Todo se guarda en `revision/semana-NN/` (ignorada por git: las entregas de
los estudiantes no se versionan en este repositorio público). Los forks que
no sean de estudiantes se listan, uno por línea, en `revision/excluir.txt`.

Ejecuta código de los estudiantes: córrelo dentro de un Codespace del repo
del curso (uno solo para todo el grupo), no en tu máquina.
"""

import argparse
import json
import pathlib
import shutil
import subprocess
import sys
import xml.etree.ElementTree as ET

REPO_CURSO = "moiseszeleny/temas-selectos-fisica-computacional-1"
RAIZ = pathlib.Path(__file__).resolve().parents[2]
CAMPOS_PR = (
    "number,state,url,files,headRefOid,headRepository,"
    "headRepositoryOwner,updatedAt,statusCheckRollup"
)


def gh(*argumentos: str) -> str:
    """Corre `gh` y devuelve su salida estándar."""
    return subprocess.run(
        ["gh", *argumentos], check=True, capture_output=True, text=True
    ).stdout


def listar_forks() -> list[str]:
    """Nombres completos (`usuario/repo`) de todos los forks del curso."""
    salida = gh(
        "api", f"repos/{REPO_CURSO}/forks?per_page=100", "--paginate",
        "--jq", ".[].full_name",
    )
    return salida.split()


def listar_prs(repo: str) -> list[dict]:
    """Todos los PRs de un repositorio; lista vacía si no se puede leer."""
    try:
        salida = gh(
            "pr", "list", "-R", repo, "--state", "all",
            "--limit", "200", "--json", CAMPOS_PR,
        )
    except subprocess.CalledProcessError:
        return []
    return json.loads(salida)


def notebooks_de_tarea(pr: dict, semana: str) -> list[str]:
    """Rutas de los notebooks de la tarea que toca el PR."""
    prefijo = f"semana-{semana}/tarea/"
    return [
        archivo["path"] for archivo in pr["files"]
        if archivo["path"].startswith(prefijo)
        and archivo["path"].endswith(".ipynb")
        and "/" not in archivo["path"][len(prefijo):]
    ]


def elegir_entregas(repos: list[str], semana: str) -> dict[str, dict]:
    """Un PR de entrega por estudiante, identificado por el dueño de la rama.

    Si hay varios, gana uno abierto sobre uno cerrado; luego, uno abierto
    dentro de su propio fork (el flujo de `docs/git-guia.md`) sobre uno
    abierto en otro repo; y, entre iguales, el actualizado más recientemente.
    Los PRs del profesor en el repo del curso no cuentan.
    """
    def clave(pr: dict) -> tuple:
        en_su_fork = pr["base"].startswith(pr["headRepositoryOwner"]["login"] + "/")
        return (pr["state"] == "OPEN", en_su_fork, pr["updatedAt"])

    profesor = REPO_CURSO.split("/")[0]
    entregas: dict[str, dict] = {}
    for repo in repos:
        for pr in listar_prs(repo):
            usuario = pr["headRepositoryOwner"]["login"]
            if usuario == profesor or not notebooks_de_tarea(pr, semana):
                continue
            pr["base"] = repo
            actual = entregas.get(usuario)
            if actual is None or clave(pr) > clave(actual):
                entregas[usuario] = pr
    return entregas


def descargar_notebook(pr: dict, ruta: str, destino: pathlib.Path) -> None:
    """Guarda el notebook tal como está en el último commit del PR."""
    repo_cabeza = (
        f"{pr['headRepositoryOwner']['login']}/{pr['headRepository']['name']}"
    )
    contenido = gh(
        "api", "-H", "Accept: application/vnd.github.raw",
        f"repos/{repo_cabeza}/contents/{ruta}?ref={pr['headRefOid']}",
    )
    destino.write_text(contenido, encoding="utf-8")


def calificar(carpeta: pathlib.Path, semana: str) -> str:
    """Corre los tests del curso sobre el notebook; devuelve `pasados/total`."""
    shutil.copytree(
        RAIZ / f"semana-{semana}" / "tarea" / "tests", carpeta / "tests",
        dirs_exist_ok=True, ignore=shutil.ignore_patterns("__pycache__"),
    )
    reporte = carpeta / "pytest.xml"
    try:
        subprocess.run(
            [sys.executable, "-m", "pytest", "tests/test_tarea.py", "-q",
             "-p", "no:cacheprovider", f"--junitxml={reporte.name}"],
            cwd=carpeta, capture_output=True, timeout=600,
        )
    except subprocess.TimeoutExpired:
        return "tiempo agotado"
    if not reporte.exists():
        return "no corrió"
    suite = ET.parse(reporte).getroot().find("testsuite")
    total = int(suite.get("tests"))
    fallidos = int(suite.get("failures")) + int(suite.get("errors"))
    return f"{total - fallidos}/{total}"


def exportar_html(notebook: pathlib.Path, destino: pathlib.Path) -> bool:
    """Ejecuta el notebook y lo guarda como HTML con salidas, aunque falle."""
    resultado = subprocess.run(
        [sys.executable, "-m", "jupyter", "nbconvert", "--to", "html",
         "--execute", "--allow-errors", "--sanitize-html",
         "--ExecutePreprocessor.timeout=300",
         "--output-dir", str(destino.parent), "--output", destino.stem,
         str(notebook)],
        capture_output=True,
    )
    return resultado.returncode == 0


def estado_actions(pr: dict, semana: str) -> str:
    """El check de autograding que dejó Actions en el PR, si existe."""
    nombre = f"Autograding (semana-{semana}/tarea)"
    for check in pr.get("statusCheckRollup") or []:
        if check.get("name") == nombre:
            return {"SUCCESS": "✅", "FAILURE": "❌"}.get(
                check.get("conclusion") or "", "🟡"
            )
    return "sin check"


def main() -> None:
    analizador = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    analizador.add_argument("semana", help="número de semana, p. ej. 05")
    analizador.add_argument(
        "--solo-tabla", action="store_true",
        help="solo localiza las entregas; no descarga ni ejecuta nada",
    )
    argumentos = analizador.parse_args()
    semana = argumentos.semana.zfill(2)

    salida = RAIZ / "revision" / f"semana-{semana}"
    excluir_txt = RAIZ / "revision" / "excluir.txt"
    excluidos = (
        set(excluir_txt.read_text().split()) if excluir_txt.exists() else set()
    )

    forks = [f for f in listar_forks() if f.split("/")[0] not in excluidos]
    entregas = {
        usuario: pr
        for usuario, pr in elegir_entregas([REPO_CURSO, *forks], semana).items()
        if usuario not in excluidos
    }
    usuarios = sorted(
        {f.split("/")[0] for f in forks} | set(entregas), key=str.lower
    )

    print("| Usuario | PR | Notebook | Actions | Tests del curso | HTML |")
    print("|---|---|---|---|---|---|")
    for usuario in usuarios:
        pr = entregas.get(usuario)
        if pr is None:
            print(f"| {usuario} | sin entrega | | | | |")
            continue
        rutas = notebooks_de_tarea(pr, semana)
        # Si el PR trae varios notebooks, se prefiere el del nombre oficial.
        oficial = f"semana-{semana}/tarea/tarea-{semana}.ipynb"
        ruta = oficial if oficial in rutas else rutas[0]
        enlace = f"[#{pr['number']}]({pr['url']}) {pr['state'].lower()}"
        fila = f"| {usuario} | {enlace} | `{pathlib.Path(ruta).name}` " \
               f"| {estado_actions(pr, semana)} |"

        if argumentos.solo_tabla:
            print(f"{fila} | |")
            continue

        carpeta = salida / usuario
        carpeta.mkdir(parents=True, exist_ok=True)
        # Con el nombre oficial, el conftest del curso lo encuentra aunque
        # el estudiante lo haya renombrado.
        notebook = carpeta / f"tarea-{semana}.ipynb"
        try:
            descargar_notebook(pr, ruta, notebook)
        except subprocess.CalledProcessError:
            print(f"{fila} no se pudo descargar | |")
            continue
        tests = calificar(carpeta, semana)
        html = salida / f"{usuario}.html"
        exportado = exportar_html(notebook, html)
        print(f"{fila} {tests} | {html.relative_to(RAIZ) if exportado else 'falló'} |")


if __name__ == "__main__":
    main()
