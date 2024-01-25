class City:
    def __init__(self, name: str, latitude: float, longitude: float, population: int):
        self.name = name
        self.latitude = latitude
        self.longitude = longitude
        self.population = population

    def get_coordinates(self):
        return f"Широта - {self.latitude}°, Долгота - {self.longitude}°"


class Country:
    def __init__(self, name: str):
        self.name = name
        self.cities: list[City] = []

    def add_city(self, new_city: City):
        try:
            self.cities.append(new_city)
            print(f"Город {new_city.name} добавлен в страну {self.name}")
        except ValueError:
            print("Переданы неправильные данные")

    def remove_city(self, city_name: str):
            city_to_remove = (city for city in self.cities if city.name == city_name)
            self.cities.remove(city_to_remove)
            print(f"Город {city_name} удален из страны {self.name}")
        else:
            print(f"Города {city_name} нет в списке городов {self.name}")
    def print_cities(self):
        for city in self.cities:
            print(f"{city.name}({city.get_coordinates()}), {city.population}peopls.")


kazakhstan = Country("Kazakhstan")
astana = City("Astana", 90.023201, 87.023232, 1100000)
almaty = City("Almaty", 90.120120102, 89.01320123, 1777000)

kazakhstan.add_city(astana)
kazakhstan.add_city(astana)
kazakhstan.add_city(astana)
kazakhstan.add_city(almaty)
kazakhstan.remove_city("Astana")
kazakhstan.print_cities()