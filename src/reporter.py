class WeatherReport:
    """Representa un reporte de clima legicle a partir de datos crudos de la API, osea de API a bonito como un toString()"""
    def __init__(self, raw_data, location_name="Ubicacion desconocida"):
        self.location_name = location_name
        self.latitude = raw_data["latitude"]
        self.longitude = raw_data["longitude"]
        self.temperature = raw_data["current"]["temperature_2m"]
        self.humidity = raw_data["current"]["relative_humidity_2m"]
        self.wind_speed = raw_data["current"]["wind_speed_10m"]
        
    def __str__(self):
        return (
            f"📍 Reporte de clima: {self.location_name}\n"
            f"   Latitud: {self.latitude}, Longitud: {self.longitude}\n"
            f"   Temperatura: {self.temperature}°C\n"
            f"   Humedad: {self.humidity}%\n"
            f"   Viento: {self.wind_speed} km/h"
        )