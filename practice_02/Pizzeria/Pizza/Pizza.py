import time


class Pizza:
    __name = ""
    __prices = {}

    def __init__(self, size):
        self.__size = size
        self.__price = 0

    @classmethod
    def get_name(cls):
        return cls.__name

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        raise Exception("Can't set size for unknown pizza")

    @property
    def price(self):
        return self.__price

    def __str__(self):
        return "{0} - {1}\t{2}".format(self.name, self.size, self.price)

    def cook(self):
        time.sleep(1)
        print("Готовим тесто...")  # Функция замешивания теста
        time.sleep(0.5)
        print("Готовим ингредиенты...")   # Функция подготовки ингредиентов
        time.sleep(0.5)
        print("Готовим пиццу...")   # Функция приготовления пиццы
        time.sleep(2)
        print("Нарезаем...")    # Функция нарезки пиццы
        time.sleep(0.3)
        print("Готово!")
