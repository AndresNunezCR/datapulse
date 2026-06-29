from src.weather_client import WeatherClient
from src.reporter import WeatherReport
from src.analyzer import WeatherAnalyzer
from src.history_manager import HistoryManager


def main():
    client = WeatherClient()
    
    # Coordenadas de San José, Costa Rica
    datos_crudos = client.get_current_weather(latitude=9.93, longitude=-84.08)
    
    reporte = WeatherReport(datos_crudos, location_name="San José, Costa Rica")
    print(reporte)
    
    analyzer = WeatherAnalyzer()
    alertas = analyzer.analyze(reporte)
    
    print("\n--- Análisis ---")
    for alerta in alertas:
        print(alerta)
    
    history = HistoryManager()
    history.save_record(reporte)
    print("\n Registro guardado en el histórico.")

if __name__ == "__main__":
    main()