"""Módulo para formatear la salida de manera amigable."""


def format_weather_output(city: dict, weather: dict) -> str:
    """
    Formatea los datos meteorológicos en un formato amigable.
    
    Args:
        city: Diccionario con datos de la ciudad
        weather: Diccionario con datos meteorológicos
        
    Returns:
        String formateado para mostrar al usuario
    """
    city_name = city.get("name")
    country = city.get("country", "")
    temperature = weather.get("temperature")
    
    output = f"""
╔═══════════════════════════════════════╗
║      INFORMACIÓN DEL CLIMA            ║
╚═══════════════════════════════════════╝

📍 Ubicación: {city_name}, {country}
🌡️  Temperatura: {temperature}°C
⏰ Zona horaria: {weather.get("timezone")}

═══════════════════════════════════════
"""
    return output
