# Preparación — Semana 3

Esta semana la herramienta nueva es **Git**, y buena parte de lo que suele
consumir la clase es instalación y cuentas. Todo eso tiene que llegar
resuelto: la guía completa vive en
[`docs/instalacion.md`](../../docs/instalacion.md).

## Checklist

- [ ] `git --version` responde con un número de versión en tu terminal. Si
      dice `command not found`, sigue la sección "Git" de
      `docs/instalacion.md` y **abre una terminal nueva** después de
      instalar.
- [ ] Configuraste tu identidad, porque es la que queda escrita en cada
      commit que hagas:

  ```bash
  git config --global user.name "Tu Nombre"
  git config --global user.email "tu_correo@ejemplo.com"
  ```

- [ ] Tienes cuenta de GitHub, con sesión abierta en el navegador que vas a
      usar en clase.
- [ ] Resolviste **cómo te vas a autenticar** al hacer `git push`: un
      *personal access token* por HTTPS, o una llave SSH. Este es el punto
      que más tiempo se lleva y el que no queremos resolver en vivo — ver
      la sección "Cuenta de GitHub" de `docs/instalacion.md`.
- [ ] Entregaste la tarea 02 en Google Classroom. Es la última que se
      entrega así: a partir de esta semana las tareas se entregan por Pull
      Request.
- [ ] Sabes moverte mínimamente en la terminal: `cd` para entrar a una
      carpeta, `ls` (o `dir` en Windows) para ver qué hay, `mkdir` para
      crear una carpeta. En la sesión 1 vas a estar tecleando ahí casi todo
      el tiempo.

## Si quieres repasar

Nada de esto es obligatorio ni se evalúa:

- [Pro Git, capítulos 1 y 2](https://git-scm.com/book/es/v2) (en español, y
  gratis). Con la introducción y "Fundamentos de Git" es más que
  suficiente.
- Si nunca has usado una terminal, practica antes moverte por tus carpetas
  con `cd` y `ls`: entrar a una, subir un nivel con `cd ..`, crear una con
  `mkdir prueba`. Son tres comandos, y quitártelos de encima antes de la
  clase te deja concentrarte en Git.

Igual que con las clases: no lo estudies de más. Git se entiende
tecleándolo, no leyéndolo, y la sesión está diseñada para construir el
flujo completo desde cero.

## Qué traer a la clase

Tu laptop, la terminal abierta **al lado** del notebook, y tu sesión de
GitHub iniciada en el navegador.

La sesión 1 es casi toda terminal: vas a crear un repositorio de práctica
desde cero, romperlo a propósito con un conflicto y repararlo. La sesión 2
es donde haces tu fork del curso y abres tu primer Pull Request, que es el
entregable de la semana — sales de la clase con él hecho.
