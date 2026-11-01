# Python 3.11 = mínimo del curso (docs/instalacion.md) y versión del workflow de autograding
FROM mcr.microsoft.com/devcontainers/python:1-3.11-bookworm

# El repositorio apt de Yarn de la imagen base tiene la llave GPG vencida y
# rompe el apt-get update de las features (sshd); el curso no usa Yarn.
RUN rm -f /etc/apt/sources.list.d/yarn.list
