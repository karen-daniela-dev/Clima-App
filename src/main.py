"""Punto de entrada de la aplicación de clima."""

from user_input import get_city_name
from weather_service import search_city, get_weather
from formatter import format_weather_output


def main():
    """Función principal de la aplicación."""
    try:
        # Obtener nombre de la ciudad del usuario
        city_name = get_city_name()
        print(f"\n🔍 Buscando información para {city_name}...")
        
        # Buscar la ciudad
        city_data = search_city(city_name)
        print(f"✓ Ciudad encontrada: {city_data['name']}")
        
        # Obtener datos meteorológicos
        print("📡 Obteniendo datos meteorológicos...")
        weather_data = get_weather(city_data["latitude"], city_data["longitude"])
        
        # Mostrar resultado formateado
        output = format_weather_output(city_data, weather_data)
        print(output)
        
    except ValueError as e:
        print(f"❌ Error de validación: {e}")
    except RuntimeError as e:
        print(f"❌ Error: {e}")
    except KeyboardInterrupt:
        print("\n\n👋 Aplicación cancelada.")
    except Exception as e:
        print(f"❌ Error inesperado: {e}")


if __name__ == "__main__":
    main()
