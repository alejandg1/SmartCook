# SmartCook - Tu aplicativo web de recetario con IA

## Descripción del Proyecto
SmartCook es una aplicación web que facilita la planificación de comidas en casa, utilizando inteligencia artificial para analizar el contenido del refrigerador a partir de una fotografía. A partir de los ingredientes identificados, sugiere recetas que se pueden preparar aprovechando lo que ya tienes disponible, ayudando así a reducir el desperdicio de alimentos y simplificar el proceso de cocinar en casa.

## Objetivos
- Simplificar la planificación de comidas con recetas personalizadas según los ingredientes disponibles.
- Maximizar el uso eficiente de los alimentos y reducir el desperdicio.
- Facilitar una experiencia culinaria creativa y conveniente.
- Adaptarse a las necesidades y preferencias de cada usuario.

## Público Objetivo
Personas interesadas en la cocina que deseen optimizar su tiempo y recursos usando los ingredientes que ya tienen en casa.

## Funcionalidades Principales
- Captura de imagen del interior de la nevera para análisis.
- Reconocimiento automático de ingredientes con IA.
- Sugerencia dinámica de recetas personalizadas.
- Gestión de recetas e historial de platos preparados.
- Sistema de usuarios con registro y personalización de recetas favoritas.
- Interfaz intuitiva y responsiva.

## Tecnologías Utilizadas
- **Backend:** Django (Python)
- **Frontend:** HTML, CSS, JavaScript
- **Bases de datos:** PostgreSQL
- **Despliegue:** Railway.app
- **APIs de IA:** Reconocimiento de imágenes para clasificación de ingredientes.

## Requisitos y Dependencias

### Python
- Python 3.12.3
- Django 5.0.6
- openai, pillow, crispy-bootstrap5, psycopg2-binary, pydantic, requests, entre otras (ver `requirements.txt`).

### JavaScript/NodeJS
- Node v20.11.0
- npm 10.5.0

## Instalación Básica

1. Clona el repositorio del proyecto:
```

git clone https://github.com/alejandg1/SmartCook.git
cd SmartCook

```
2. (Opcional) Crea y activa un entorno virtual de Python:
```


# En Linux/MacOS

python -m venv venv
source venv/bin/activate

# En Windows

python -m venv venv
.\venv\Scripts\activate

```
3. Instala las dependencias de Python:
```

pip install -r requirements.txt

```
4. Configura las variables de entorno en el archivo `.env`:
```

APIKEY=sk-proj-XXXXX (tu clave de API)

```
5. Ejecuta el proyecto:
```

python manage.py runserver

```
6. Ingresa a la interfaz desde tu navegador en `http://localhost:8000`.

## Uso Básico

- Registra una cuenta o inicia sesión.
- Sube una foto del interior de tu nevera o toma una foto directamente desde la app.
- Espera el análisis automático y consulta las sugerencias de recetas según tus ingredientes.
- Guarda tus recetas favoritas e historial de cocina.