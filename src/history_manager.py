import csv
import os
from datetime import datetime

class HistoryManager:
    """Guarda y lee el reporte historico del clima, luego convierte a CSV"""

    def __init__(self, filepath="data/weather_history.csv"):
        self.filepath = filepath
        self._ensure_file_exists()

    def _ensure_file_exists(self): #supuestamente el "_" al principio de fn significa que sera usada internamente por la clase, como un private
        if not os.path.exists(self.filepath): # solo si el archivo NO existe, lo crea con encabezados
            with open(self.filepath, mode="w", newline="", encoding="utf-8") as file: #el with cierra el archivo 
                writer = csv.writer(file)
                writer.writerow(["timestamp", "location", "temperature", "humidity", "wind_speed"])

    def save_record(self, report):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        with open(self.filepath, mode="a", newline="", encoding="utf-8") as file: #mode a es append y mode w es write 
            writer = csv.writer(file)
            writer.writerow([
                timestamp,
                report.location_name,
                report.temperature,
                report.humidity,
                report.wind_speed
            ])
