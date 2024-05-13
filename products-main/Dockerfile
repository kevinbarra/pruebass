FROM python:3.10-alpine

# Instalar dependencias necesarias para compilar psycopg2
RUN apk add --no-cache gcc musl-dev postgresql-dev

# Establecer directorio de trabajo
WORKDIR /app

# Copiar requirements.txt y luego instalar las dependencias
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Copiar el resto de la aplicación
COPY . .

EXPOSE 5000

# Ejecutar la aplicación
CMD ["python", "app.py"]