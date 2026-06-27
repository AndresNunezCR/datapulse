from src.weather_client import WeatherClient

def main():
    client = WeatherClient()
    
    # Coordenadas de San José, Costa Rica
    clima = client.get_current_weather(latitude=9.93, longitude=-84.08)
    
    print(clima)

if __name__ == "__main__":
    main()