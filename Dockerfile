# Usa la imagen oficial de Python
FROM python:3.11-slim

# Establece el directorio de trabajo en el contenedor
WORKDIR /app

# Copia los archivos de requirements para instalar las dependencias
COPY requirements.txt requirements.txt

# Instala las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copia el resto del código de la aplicación al contenedor
COPY . .

# Expone el puerto en el que Flask correrá
EXPOSE 5000

# Establece la variable de entorno para que Flask corra en modo producción
ENV FLASK_ENV=production

# Configura el punto de entrada para ejecutar la aplicación
CMD ["flask", "run", "--host=0.0.0.0"]
