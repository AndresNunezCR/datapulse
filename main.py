from src.weather_client import WeatherClient
from src.reporter import WeatherReport

def main():
    client = WeatherClient()
    
    # Coordenadas de San José, Costa Rica
    datos_crudos = client.get_current_weather(latitude=9.93, longitude=-84.08)
    
    reporte = WeatherReport(datos_crudos, location_name="San José, Costa Rica")
    print(reporte)

if __name__ == "__main__":
    main()