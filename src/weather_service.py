"""Módulo para obtener datos meteorológicos de Open-Meteo."""

import requests
from config.settings import (
    OPEN_METEO_BASE_URL,
    OPEN_METEO_WEATHER_URL,
    SEARCH_LIMIT,
    WEATHER_VARIABLES,
    TIMEZONE,
)


def search_city(city_name: str) -> dict:
    """
    Busca una ciudad usando la API de geocodificación de Open-Meteo.
    
    Args:
        city_name: Nombre de la ciudad a buscar
        
    Returns:
        Diccionario con datos de la ciudad (latitud, longitud, nombre)
    """
    params = {
        "name": city_name,
        "count": SEARCH_LIMIT,
        "language": "es",
    }
    
    try:
        response = requests.get(OPEN_METEO_BASE_URL, params=params)
        response.raise_for_status()
        data = response.json()
        
        if not data.get("results"):
            raise ValueError(f"No se encontró la ciudad '{city_name}'.")
        
        result = data["results"][0]
        return {
            "name": result.get("name"),
            "country": result.get("country"),
            "latitude": result.get("latitude"),
            "longitude": result.get("longitude"),
        }
    except requests.exceptions.RequestException as e:
        raise RuntimeError(f"Error al conectar con la API: {e}")


def get_weather(latitude: float, longitude: float) -> dict:
    """
    Obtiene datos meteorológicos para una ubicación.
    
    Args:
        latitude: Latitud de la ubicación
        longitude: Longitud de la ubicación
        
    Returns:
        Diccionario con datos meteorológicos
    """
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "current": WEATHER_VARIABLES,
        "timezone": TIMEZONE,
    }
    
    try:
        response = requests.get(OPEN_METEO_WEATHER_URL, params=params)
        response.raise_for_status()
        data = response.json()
        
        current = data.get("current", {})
        return {
            "temperature": current.get("temperature_2m"),
            "weather_code": current.get("weather_code"),
            "timezone": data.get("timezone"),
        }
    except requests.exceptions.RequestException as e:
        raise RuntimeError(f"Error al obtener datos meteorológicos: {e}")
