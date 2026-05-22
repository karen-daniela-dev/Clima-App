🌦️ Weather App - Python

Aplicación de consola en Python que permite consultar el clima actual de una ciudad utilizando APIs externas (geocoding + clima) y mostrar la información de forma amigable.

🚀 Características
🔍 Búsqueda de ciudades por nombre
🌍 Obtención de coordenadas (latitud y longitud)
☁️ Consulta del clima actual
🧾 Formateo amigable de la información
🧪 Pruebas unitarias con pytest
⚠️ Manejo de errores (ciudad no encontrada, errores de API, timeouts)
🧱 Estructura del proyecto
clima_ciudad/
├── config/
│   └── settings.py         # URLs y parámetros de configuración
├── services/
│   └── weather_service.py  # Lógica para consumir APIs
├── utils/
│   ├── formatter.py        # Formatea la respuesta del clima
│   └── user_input.py       # Manejo de entrada del usuario
├── tests/
│   └── test_weather_service.py  # Pruebas unitarias
├── main.py                 # Punto de entrada
├── requirements.txt        # Dependencias
└── venv/                   # Entorno virtual (ignorar en Git)
⚙️ Instalación
Clona el repositorio:
git clone [<tu-repositorio>](https://github.com/karen-daniela-dev/Clima-App.git)
cd clima_ciudad
Crea y activa un entorno virtual:
python -m venv venv

En Windows:

venv\Scripts\activate

En Linux/Mac:

source venv/bin/activate
Instala las dependencias:
pip install -r requirements.txt
▶️ Uso

Ejecuta la aplicación:

python main.py

Luego ingresa el nombre de una ciudad:

Ingrese una ciudad: Bogotá

Ejemplo de salida:

Ciudad: Bogotá, Colombia
Temperatura: 20°C
Viento: 5 km/h
Precipitación: 0 mm
Día/Noche: Día
🧪 Pruebas

El proyecto incluye pruebas unitarias usando pytest y mocks para simular las APIs.

Ejecutar pruebas:

pytest
🧠 Arquitectura (explicado simple)

Tu app sigue una separación clara de responsabilidades:

main.py → Orquesta todo (flujo principal)
services/ → Lógica de negocio (APIs)
utils/ → Funciones auxiliares (input y formato)
config/ → Configuración externa
tests/ → Validación del comportamiento

👉 Esto es muy parecido a cómo se estructuran proyectos reales.

⚠️ Manejo de errores

La aplicación maneja distintos escenarios:

❌ Ciudad no encontrada → ValueError
❌ Error en API → Exception
❌ Timeout → capturado en pruebas
⚠️ Respuesta incompleta → validación de datos
🔧 Tecnologías usadas
Python 3.13
requests
pytest
unittest.mock
📌 Posibles mejoras
Agregar interfaz gráfica (Tkinter o web con Flask/FastAPI)
Cachear resultados para evitar múltiples llamadas
Soporte para pronóstico (no solo clima actual)
Internacionalización (idiomas)
Logging profesional
👩‍💻 Autor

Proyecto desarrollado como práctica de consumo de APIs, testing y arquitectura en Python.
