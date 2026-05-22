"""Módulo para manejar entrada del usuario."""


def get_city_name() -> str:
    """Obtiene el nombre de la ciudad del usuario."""
    city = input("Ingresa el nombre de una ciudad: ").strip()
    
    if not city:
        raise ValueError("El nombre de la ciudad no puede estar vacío.")
    
    return city
