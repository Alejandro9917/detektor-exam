# Usa una imagen base oficial de Python
FROM python:3.10-slim

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia el archivo requirements.txt al contenedor
COPY requirements.txt .

# Instala las dependencias del archivo requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copia el resto del código fuente al directorio de trabajo del contenedor
COPY . .

# Expone el puerto que usará la aplicación Flask (normalmente el 5000)
EXPOSE 5000

# Establece el entrypoint para ejecutar la aplicación
# Asume que el archivo principal de la aplicación Flask es app.py
CMD [ "python", "-m" , "flask", "run", "--host=0.0.0.0"]