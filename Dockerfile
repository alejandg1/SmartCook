FROM python:3.11-slim

ENV DEBIAN_FRONTEND=noninteractive

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir --upgrade pip \
 && pip install --no-cache-dir -r requirements.txt

COPY . .

RUN python manage.py collectstatic --noinput

EXPOSE 8000

# Script para ejecutar migraciones y luego iniciar gunicorn
CMD ["sh", "-c", "python manage.py migrate && gunicorn application.wsgi:application --bind 0.0.0.0:8000"]
