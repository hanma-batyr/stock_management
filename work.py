# class Calculator:
#     def __init__(self):
#         self.__pi = 3.14

#     def get_pi(self):
#         return self.__pi


# c = Calculator()
# c.pi = 10
# print(c.get_pi())


class Car:
    # метод-конструктор
    def __init__(
        self,
        model: str,
        manufacturer_year: int,
        engine_volume: float,
        color: str,
        price: float,
    ):
        self.__model = model
        self.__manufacturer_year = manufacturer_year
        self.__engine_volume = engine_volume
        self.__color = color
        self.__price = price

    # public - публичный
    # private - приватные
    # protected - защищенный

    def _turn_off(self):
        print("Выключение")

    def turn_on(self):
        self.__start_electro_chain()
        self.__send_energy_to_akb()
        self.__start_val()
        self.__send_fire()

    def __start_electro_chain(self):
        print("Запуск электроцепи")

    def __send_energy_to_akb(self):
        print("Отправка энергии в АКБ")

    def __start_val(self):
        print("Запуск коленчатого вала")

    def __send_fire(self):
        print("Отправка искры")

    def get_model(self):
        return self.__model


    def set_model(self, new_model):
        self.model = new_model

    def get_color(self):
        return self.__color

    @property
    def price(self):
        return self.__price

    # сеттер
    @price.setter
    def price(self, new_price):
        if isinstance(new_price, float) or isinstance(new_price, int):
            if new_price >= 0:
                self.__price = new_price
                return
        raise ValueError("Неправильная новая цена")


toyota = Car("Toyota", 2004, 2.5, "Black", 300000)
toyota.price = 2020
print(toyota.price)