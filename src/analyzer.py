class WeatherRule:
    """Contraro para reglas de analisis de clima. Cada hija evalua un reporte y devuelve un mensake"""

    def evaluate(self, report):
        raise NotImplementedError("Cada regla debe implementar su promio metodo evaluate()")
    
    def get_value(self, report):
        raise NotImplementedError("Cada regla debe implementar su propio metodo get_value()")
    






class HeatRule(WeatherRule):
    """Evalua segun la temperatura y categoriza en un evento de calor"""
    name = "Temperatura"

    def evaluate(self, report):
        if report.temperature >= 30:
            return f"Calor Intenso: {report.temperature} *C"
        elif report.temperature >= 25:
            return f"Clima calido: {report.temperature} *C"
        return None
    
    def get_value(self, report):
        return f"{report.temperature} *C"
    







class WindRule(WeatherRule):
    """Evalua si la velocidad del viento representa un riesgo."""
    name = "Viento"

    def evaluate(self, report):
        if report.wind_speed >= 40:
            return f" Viento peligroso: {report.wind_speed} km/h"
        elif report.wind_speed >= 20:
            return f" Viento moderado: {report.wind_speed} km/h"
        return None
    
    def get_value(self, report):
        return f"{report.wind_speed} km/h"








class HumidityRule(WeatherRule):
    """Evalua si la humedad relativa es incomoda."""
    name = "Humedad"

    def evaluate(self, report):
        if report.humidity >= 80:
            return f" Humedad muy alta: {report.humidity}%"
        elif report.humidity <= 20:
            return f" Humedad muy baja: {report.humidity}%"
        return None
    
    def get_value(self, report):
        return f"{report.humidity}%"
    



class WeatherAnalyzer:
    """Analiza cada WeatherReport aplicando las reglas (patron strategy)"""

    def __init__(self):
        self.rules = [HeatRule(), WindRule(), HumidityRule()]

    def analyze(self, report):
        results = []
        for rule in self.rules:
            alert = rule.evaluate(report)
            if alert is not None:
                results.append(f" {rule.name}: {alert}")
            else:
                results.append(f" {rule.name}: Normal ({rule.get_value(report)})")
        return results