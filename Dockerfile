# Imagen de base
FROM python:3.10.4-slim-bullseye
# Setea las variables de entorno
# Desabilita el chequep de actualizaciones de pip
ENV PIP_DISABLE_PIP_VERSION_CHECK=1
# Python no trata de escribir archivos .pyc
ENV PYTHONDONTWRITEBYTECODE=1
# Desabilita las salidas por consola de python en el contenedor
ENV PYTHONUNBUFFERED=1
# Setea el directorio de trabajo en el contenedor
WORKDIR /base
# Instala las dependencias
COPY ./requirements.txt .
RUN pip install -r requirements.txt
# Copia el proyecto entero desde donde está este archivo '.' al directorio de trabajo del contenedor
COPY . .