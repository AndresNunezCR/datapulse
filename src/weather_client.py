import requests

class WeatherClient:
    """Cliente responsable de comunicarse ocn la API de Open-Meteo"""

    def __init__(self):
        self.base_url = "https://api.open-meteo.com/v1/forecast"

    def get_current_weather(self, latitude, longitude):
        """Obtiene el clima actual para una latitud longitud dadas"""
        params = {
            "latitude" : latitude,
            "longitude" : longitude,
            "current" : "temperature_2m,relative_humidity_2m,wind_speed_10m"
        }

        response = requests.get(self.base_url, params=params)
        response.raise_for_status()

        return response.json()

        
