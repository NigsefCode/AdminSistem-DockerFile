# Evaluación 2: Docker

- Integrante: Nicolás Sepúlveda Falcón
  
- Curso: Administración de Sistemas



## Introducción
Este proyecto consiste en crear un script en Python que procesa datos financieros de la UF (Unidad de Fomento) y genera un gráfico de líneas mostrando la variación de su valor en el tiempo. El script lee un archivo `entrada.csv` con dos columnas (`dia` y `valor_uf`), genera un gráfico en formato `.jpg` con un timestamp en su nombre, y guarda el gráfico en una carpeta de salida.

Además, el script maneja errores, como la falta de archivos o errores de lectura/escritura, y registra cualquier problema en un archivo `error.log`. También lleva un registro de los datos procesados en un archivo adicional (`entrada.csv.store`).

Cabe destacar que el proyecto se ha configurado para ser ejecutado dentro de un contenedor Docker, asegurando un entorno controlado y reproducible para la ejecución del script.


## Instrucciones de Instalación y Ejecución
### Requisitos Previos
Antes de comenzar con la ejecución del proyecto, asegurarse de tener lo siguiente instalado en su equipo de trabajo:
1. **Python 3.x**
2. **Docker**

En caso de no posee Docker, puede instalarlo de la siguiente manera según el tutorial sacado de [Digital Ocean](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-ubuntu-20-04-es):
Primero, actualizar el Sistema operativo:
```bash
  sudo apt update
  sudo apt upgrade
```
A continuación, instale algunos paquetes que permitan a `apt` usar paquetes a través de HTTPS:
```bash
  sudo apt install apt-transport-https ca-certificates curl software-properties-common
```
Posteriormente, añadir la clave GPG para el repositorio oficial de Docker:
```bash
  curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
```
Agregar al Docker el repositorio APT:
```bash
  sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu focal stable"
```
Actualizar nuevamente:
```bash
  sudo apt update
```
Asegurar de estar a punto de realizar la instalación desde el repositorio de Docker:
```bash
  apt-cache policy docker-ce
```
Por último, instalar Docker y comprobar su funcionamiento:
```bash
  sudo apt install docker-ce
  sudo systemctl status docker
```

### Pasos para Construir y Ejecutar el Proyecto
1. **Crear carpetas**

   Crear una carpeta `input` y `ouput`
   ```bash
      mkdir input
      mkdir output
   ```
   
2. **Crear un archivo de `entrada.csv`**

   Crear un archivo llamado `entrada.csv` dentro de la carpeta `input` con el siguiente formato como ejemplo:
    ```csv
        dia,valor_uf
        2024-01-01,29000
        2024-01-02,29100
        2024-01-03,29200
     ```
   Este archivo contiene los datos de la UF, con dos columnas: `dia` (fecha en formato `yyyy-mm-dd`) y `valor_uf` (valor numérico de la UF). Usted puede cambiar los valores a su gusto, pero debe respetar el formato.
    
3. **Crear el Script de Python `procesar_uf.py`**

   Este script leerá el archivo `entrada.csv`, generará un gráfico de líneas y lo guardará en una carpeta de salida. Además, registrará los datos procesados y manejará errores. Es el Script principal que procesa los datos y genera el gráfico se encuentra en el repositorio que puede copiar.

4. **Crear un archivo de `error.log`**

   Se crea un archivo de registro de errores que son ocurridos durante la ejecución del script. Cabe mencionar que este archivo lo creará el Script `procesar_uf.py` y se almacenará en `output`.

5. **Crear el archivo Dockerfile**

   El archivo Dockerfile está configurado para construir una imagen que incluye:
   - Python 3.x
   - Librerías de `matplotlib` y `pandas`
   - El Script `procesar_uf.py` para procesar el archivo de entrada y generar gráficos.

   En el repositorio se encuentra el archivo Dockerfile que puede copiar y pegar como ejemplo.
   En este ejemplo se utiliza un contenedor Docker para ejecutar un script de Python que procesa datos usando las bibliotecas `matplotlib` y `pandas`. El archivo Dockerfile define la configuración necesaria para crear la imagen del contenedor.

   En la imagen base se utiliza el comando que usa una imagen oficial y liviana de Python 3.9 como base. La versión "slim" es más compacta y optimizada para un entorno mínimo:
   ```bash
     FROM python:3.9-slim
   ```

   Aquí se establece el directorio `/app` dentro del contenedor como el lugar donde se realizarán todas las operaciones:
   ```bash
     WORKDIR /app
   ```

   Este comando copia el script `procesar_uf.py` desde tu máquina local al directorio de trabajo `/app` del contenedor:
   ```bash
     COPY procesar_uf.py .
   ```

   Aquí se instalan las bibliotecas de Python necesarias de `matplotlib` y `pandas`:
   ```bash
     RUN pip install matplotlib pandas
   ```

   En este paso se copia el archivo de datos `entrada.csv` desde el directorio local `input` a la misma ruta en el contenedor.
   ```bash
     COPY input/entrada.csv input/entrada.csv
   ```

   Finalmente, el contenedor está configurado para ejecutar el script `procesar_uf.py`:
   ```bash
     CMD ["python", "procesar_uf.py"]
   ```
   

7. **Contrucción y Ejecución de la Imagen y Contenedor Docker**

   Antes de ejecutar el Script se debe construir la imagen Docker con el siguiente comando:
   ```bash
     docker build -t nombre_imagen .
   ```
   Con esto se creará una imagen Docker. Usted puede colocar el nombre que desea en `nombre_imagen`.

   Posteriormente, para ejecturar el contenedor y procesar los datos, se utiliza el siguiente comando:
   ```bash
     docker run --rm -v $(pwd)/input:/app/input -v $(pwd)/output:/app/output nombre_imagen
   ```
   En este proceso se ejecutará y guardará el gráfico en `output`.

### Manejo de Errores
El Script está preparado para manejar errores como:
- **Archivo no encontrado:**  Si el archivo `entrada.csv`  no está presente en la carpeta input, se generará un archivo error.log en la carpeta `output` con el mensaje correspondiente.
- **Archivo CSV vacío o mal formato:** Si el archivo de entrada está vacío o errores en las columnas de `dia` o `valor_uf` , también se registrará en el archivo `error.log`.

### Notas Adicionales
- Asegurar que las carpetas `input` y `output` tengan los permisos adecuados. En caso de no saber como hacer eso, se puede ejecutar el siguiente comando:
  
   ```bash
     sudo chmod 777 output input
   ```
- Asegurar que los nombres estén bien escritos y todo esté en su carpeta correspondiente:
  - **Dockerfile**
  - **input/**
    - **entrada.csv**
  - **output/**
    - **error_log**
  - **procesar_uf.py**
   


