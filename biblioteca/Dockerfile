# Utilizar una imagen base de Python
FROM python:3.12-slim

# Configurar variables de entorno
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Instalar dependencias del sistema necesarias para mysqlclient
RUN apt-get update && apt-get install -y \
    gcc \
    default-libmysqlclient-dev \
    && apt-get clean

# Crear y establecer el directorio de trabajo en el contenedor
WORKDIR /app

# Copiar los archivos de requisitos al contenedor
COPY requirements.txt /app/requirements.txt

# Instalar las dependencias de Python
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el resto de la aplicación
COPY . /app

# Comando por defecto (puedes ajustarlo según tu proyecto)
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
