# Imagen base de Python
FROM python:3.11-slim

# Crear directorio de trabajo
WORKDIR /app/src

# Copiar requirements
COPY requirements.txt .

# Instalar dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el resto del proyecto
COPY . .


CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]