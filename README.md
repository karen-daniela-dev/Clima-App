🌦️ Aplicación de Clima en Python
📌 Resumen del Proyecto

Esta es una aplicación de consola desarrollada en Python que permite a los usuarios consultar el clima actual de una ciudad ingresando su nombre.

La aplicación utiliza la API de Open-Meteo para:

Buscar la ciudad (geocodificación)
Obtener datos meteorológicos en tiempo real

El sistema está diseñado con una arquitectura modular, separando la lógica en diferentes componentes para facilitar el mantenimiento, pruebas y escalabilidad.

⚙️ Instrucciones de Instalación
Clonar el repositorio:
git clone <URL_DEL_REPOSITORIO>
cd clima
Crear entorno virtual:
python -m venv venv
Activar entorno virtual:
Windows:
venv\Scripts\activate
Linux / Mac:
source venv/bin/activate
Instalar dependencias:
pip install -r requirements.txt
▶️ Guía de Uso

Ejecuta la aplicación con:

python src/main.py

Luego ingresa el nombre de una ciudad cuando se te solicite:

Ingrese una ciudad: Bogotá

La aplicación realizará los siguientes pasos:

Validar la entrada del usuario
Buscar la ciudad en la API
Obtener datos del clima
Mostrar la información formateada
🧾 Ejemplo de Resultados
🔍 Buscando información para Bogotá...
✓ Ciudad encontrada: Bogotá
📡 Obteniendo datos meteorológicos...

🌤️ Clima en Bogotá, Colombia
Temperatura: 18°C
Código de clima: 3
Zona horaria: America/Bogota
🚀 Funcionalidades
✔️ Entrada de usuario validada (user_input.py)
✔️ Búsqueda de ciudad mediante API (search_city)
✔️ Consulta de clima en tiempo real (get_weather)
✔️ Formateo de salida amigable (formatter.py)
✔️ Manejo de errores robusto
✔️ Arquitectura modular
✔️ Pruebas unitarias con pytest
⚠️ Manejo de Errores

La aplicación incluye manejo de errores para:

❌ Ciudad no encontrada → ValueError
❌ Fallos en la API → RuntimeError
❌ Cancelación del usuario (Ctrl + C) → KeyboardInterrupt
❌ Errores inesperados → Exception

Esto permite que la aplicación no falle abruptamente y muestre mensajes claros al usuario.

🌐 Información de la API

Se utiliza la API pública de Open-Meteo:

📍 Geocoding API
Permite buscar ciudades y obtener coordenadas (latitud y longitud)
🌡️ Weather API
Permite obtener datos meteorológicos actuales

Endpoints utilizados:

https://geocoding-api.open-meteo.com/v1/search
https://api.open-meteo.com/v1/forecast

Parámetros configurados en settings.py:

Variables climáticas: temperatura y código del clima
Zona horaria automática
Límite de resultados de búsqueda
🧠 Estructura del Proyecto
clima/
┣ config/
┃ ┗ settings.py
┣ src/
┃ ┣ main.py
┃ ┣ user_input.py
┃ ┣ weather_service.py
┃ ┣ formatter.py
┃ ┗ __init__.py
┣ tests/
┃ ┣ test_formatter.py
┃ ┣ test_weather_service.py
┃ ┗ __init__.py
┣ .env
┣ .gitignore
┗ requirements.txt
🧪 Pruebas

Para ejecutar las pruebas:

pytest

Se incluyen pruebas para:

Formateo de salida
Consumo de la API (usando mocks)
🔮 Mejoras Futuras
Mostrar pronóstico extendido (varios días)
Traducir códigos de clima a descripciones más detalladas
Agregar velocidad del viento y humedad
Implementar interfaz gráfica (Tkinter o web)
Convertir la app en API usando FastAPI
Cachear resultados para mejorar rendimiento
📊 Revisión de Buenas Prácticas (Autoevaluación)

✔️ Nombres claros de funciones (get_weather, search_city)
✔️ Separación de responsabilidades (modularidad)
✔️ Manejo adecuado de errores
✔️ Uso de docstrings
✔️ Código legible y organizado



Proyecto desarrollado como práctica de consumo de APIs, estructura de proyectos en Python y testing.
