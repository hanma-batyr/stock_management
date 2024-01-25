class city:
    def __init__(self, name, latitude, longitude):
        self.name = name
        self.latitude = latitude
        self.longitude = longitude
    def get_coordinates(self):
        return f"Ширина - {self.latitude}, Долгота - {self.longitude}"
class country:
    def __init__ (self, name):
        self.name=name
        self.cities: list[city] = []
    def add_city(self, new_city):
        try 