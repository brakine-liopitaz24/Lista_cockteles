FROM ubuntu:latest

LABEL maintainer=bqch20@gmail.com

# Instalar actualizaciones y dependencias
RUN apt-get update -y && \
    apt-get install -y python3-pip python3-dev git

# Clonar el proyecto
RUN git clone https://github.com/brakine-liopitaz24/Lista_cockteles.git

# Establecer directorio de trabajo
WORKDIR /Lista_cockteles

# Instalar librerías de requerimientos
RUN pip3 install -r requirements.txt

# Exponer el puerto 7000, el puerto por defecto de Flask
EXPOSE 7000

# Ejecutar el programa
CMD ["python3", "src/app.py"]

