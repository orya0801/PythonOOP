import asyncio
import time
from random import randint
from Pizzeria.Dish import Dish
from PizzeriaPatterns.DbWorker import DatabaseWorker


class Pizza(Dish):

    def __init__(self, size, name, ingredients, sauce, dough):
        self._name = name
        self.ingredients = ingredients
        self.sauce = sauce
        self.dough = dough

        self._db_worker = DatabaseWorker()

        self._prices = self._db_worker.get_pizza_prices(self._name)

        self._size = size
        self._price = self._db_worker.get_pizza_price(self._name, self._size)

    def __str__(self):
        return "{0}\t{1} - {2}".format(self._name, self._size, self._price)

    """
        Свойства name, prices, ingredients, sauce, dough, price реализуются только для 
        получения значений, так как name, prices, ingredients, sauce, dough являются 
        параметрами по умолчанию, которые содержатся в каждом из наследуемых классов
    """

    @property
    def name(self):
        return self._name

    @property
    def prices(self):
        return self._prices

    @property
    def price(self):
        return self._price

    # Свойство size является основным свойством для работы с экземпляром объекта Pizza
    @property
    def size(self):
        return self._size

    # При установки нового размера пиццы автоматически меняется цена
    @size.setter
    def size(self, size):
        self._size = size
        self._price = self._db_worker.get_pizza_price(self._name, self._size)

    def remove_ingredient(self, ingr):
        self.ingredients.remove(ingr)

    def info(self):
        pizza_info = self._name + " - "
        for key in self._prices.keys():
            pizza_info += "{0}/".format(key)

        pizza_info = pizza_info[:-1] + "\t"

        for value in self._prices.values():
            pizza_info += "{0}/".format(str(value))

        pizza_info = pizza_info[:-1]

        return pizza_info

    """
        private методы __slice_pizza и __slice_ingredients отвечают за 
        этапы приготовления пиццы и вызываются только из метода cook
    """

    async def __slice_pizza(self):
        if self._size == "small":
            sleep_time = (randint(1, 24) / 4)
        elif self._size == "middle":
            sleep_time = (randint(1, 24) / 6)
        else:
            sleep_time = (randint(1, 24) / 8)

        print("{0} - Slicing pizza... - {1} s".format(self._name, sleep_time))
        await asyncio.sleep(sleep_time)

    async def __slice_ingredients(self):
        sleep_time = randint(1, 5)
        print("{0} - Slicing ingredients... - {1} s".format(self._name, sleep_time))
        await asyncio.sleep(sleep_time)

    async def __baking(self):
        sleep_time = randint(1, 8)
        print("{0} - Cooking pizza... - {1} s".format(self._name, sleep_time))
        await asyncio.sleep(sleep_time)

    async def cook(self):
        await self.__slice_ingredients()

        await self.__baking()

        await self.__slice_pizza()

    async def cook_async(self):
        await self.cook()


"""
    Классы PizzaBarbecue, PizzaMargarita, PizzaPepperoni наследуются от
    класса Pizza и содержат в себе статичные атрибуты имени пиццы, ингридиентов,
    соуса и теста. Также в каждом из классов определен classmethod get_name, 
    который используется при поиске пиццы в меню, чтобы определить объект какого
    из классов наследников следует создать при заказе.
"""


class PizzaBarbecue(Pizza):

    __name = "BBQ"
    __origin_ingredients = ["cheese", "chicken", "onions"]
    __sauce = "BBQ"
    __dough = "thin"

    def __init__(self, size="small"):
        super().__init__(size, self.__name, self.__origin_ingredients, self.__sauce, self.__dough)

    @classmethod
    def get_name(cls):
        return cls.__name


class PizzaMargarita(Pizza):

    __name = "Margarita"
    __origin_ingredients = ["cheese", "tomato", "pepper"]
    __sauce = "tomato"
    __dough = "thin"

    def __init__(self, size="small"):
        super().__init__(size, self.__name, self.__origin_ingredients, self.__sauce, self.__dough)

    @classmethod
    def get_name(cls):
        return cls.__name


class PizzaPepperoni(Pizza):

    __name = "Pepperoni"
    __origin_ingredients = ["cheese", "pepperoni", "pepper"]
    __sauce = "tomato"
    __dough = "thick"

    def __init__(self, size="small"):
        super().__init__(size, self.__name, self.__origin_ingredients, self.__sauce, self.__dough)

    @classmethod
    def get_name(cls):
        return cls.__name

