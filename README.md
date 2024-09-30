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
