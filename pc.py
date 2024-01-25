class Computer:
    def __init__(self, video_card: str, RAM: str, motherboard: str, price: float, random_access_memory: str, ssd_drive: str, power_unit: str):
        self.__random_access_memory = random_access_memory
        self.__ssd_drive = ssd_drive
        self.__power_unit = power_unit
        self.__video_card = video_card
        self.__RAM = RAM
        self.__motherboard = motherboard
        self.__price = price
        
    def turn_on(self):
        self.__start_electrik()
        self.__program_execution()
        self.__start_BIOS()
        self.__Screen_output()

    def __start_electrik(self):
        print("процессор получает электрическое питание")

    def __program_execution(self):
        print("начинает выполнение программы")

    def __start_BIOS(self):
        print("Запуск BIOS")

    def __Screen_output(self):
        print("Выводить на экран")

    def get_video_card(self):
        return self.__video_card

    def set_video_card(self, new_video_card):
        self.__video_card = new_video_card

    def get_RAM(self):
        return self.__RAM
    
    def set_RAM(self, new_RAM):
        self.__RAM = new_RAM

    def get_motherboard(self):
        return self.__motherboard
    
    def set_motherboard(self, new_motherboard):
        self.__motherboard = new_motherboard

    def get_random_access_memory(self):
        return self.__random_access_memory

    def set_random_access_memory(self, new_random_access_memory):
        self.__random_access_memory = new_random_access_memory

    def get_ssd_drive(self):
        return self.__ssd_drive

    def set_ssd_drive(self, new_ssd_drive):
        self.__ssd_drive = new_ssd_drive

    def get_power_unit(self):
        return self.__power_unit

    def set_power_unit(self, new_power_unit):
        self.__power_unit = new_power_unit

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price):
        if isinstance(new_price, (float, int)) and new_price >= 0:
            self.__price = new_price
        else:
            raise ValueError("Неправильная новая цена")

PC = Computer("GeForce4090", "Intel core i9", "Intel B760", 5000000, "32GB", "SSD 1TB", "750W")
PC.turn_on()
PC.price = 4000
print(PC.price)