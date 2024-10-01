# Utiliza una imagen base oficial de Python
FROM python:3.9-slim

# Establecer el directorio de trabajo en el contenedor
WORKDIR /app

# Copiar el script de Python al contenedor
COPY procesar_uf.py .

# Instalar las dependencias
RUN pip install matplotlib pandas

# Copiar el archivo de entrada en el contenedor
COPY input/entrada.csv input/entrada.csv

# Configurar el comando de inicio
CMD ["python", "procesar_uf.py"]
