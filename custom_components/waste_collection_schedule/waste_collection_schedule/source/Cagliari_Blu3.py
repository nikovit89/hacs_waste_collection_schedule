from waste_collection_schedule import Collection  # Importa la classe base per la raccolta
from datetime import date, timedelta

TITLE = "Cagliari (Area Blu 3)"
DESCRIPTION = "Waste collection schedule for Cagliari (Area Blu 3)"
URL = "https://www.comune.cagliari.it"

# Definisci il calendario fisso
SCHEDULE = {
    "Monday": "Secco",
    "Tuesday": ["Umido", "Vetro"],
    "Wednesday": "Carta",
    "Thursday": "Umido",
    "Friday": "Plastica",
    "Sunday": "Umido",
}

class Source:
    def __init__(self):
        pass

    def fetch(self):
        today = date.today()
        entries = []
        
        for i in range(30):  # Cicla per i prossimi 30 giorni
            current_day = today + timedelta(days=i)
            weekday = current_day.strftime("%A")
            if weekday in SCHEDULE:
                waste_type = SCHEDULE[weekday]
                if isinstance(waste_type, list):
                    for w in waste_type:
                        entries.append(Collection(current_day, w))
                else:
                    entries.append(Collection(current_day, waste_type))
                    
        return entries