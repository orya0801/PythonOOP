from practice_02.Pizzeria.PizzaPrices import PRICES
import time


class Pizza:

    def __init__(self, size, name, ingredients, sauce, dough):
        self._name = name
        self._ingredients = ingredients
        self._sauce = sauce
        self._dough = dough

        if self._name not in PRICES.keys():
            raise KeyError

        self._prices = PRICES[self._name]

        if size in self._prices:
            self._size = size
            self._price = self._prices[size]
        else:
            raise KeyError

    def __getitem__(self, key):
        if key not in self._prices.keys():
            raise KeyError

        return self._prices[key]

    def __setitem__(self, key, value):
        if key not in self._prices.keys():
            raise KeyError

        self._prices[key] = value

    def __str__(self):
        return "{0}\t{1} - {2}".format(self._name, self._size, self._price)

    @property
    def name(self):
        return self._name

    @property
    def prices(self):
        return self._prices

    @property
    def ingredients(self):
        return self._ingredients

    @property
    def sauce(self):
        return self._sauce

    @property
    def dough(self):
        return self._dough

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        if size not in self._prices.keys():
            raise KeyError

        self._size = size
        self._price = self._prices[size]

    @property
    def price(self):
        return self._price

    def remove_ingredient(self, ingr):
        self._ingredients.remove(ingr)

    def info(self):
        pizza_info = self._name + " - "
        for key in self._prices.keys():
            pizza_info += "{0}/".format(key)

        pizza_info = pizza_info[:-1] + "\t"

        for value in self._prices.values():
            pizza_info += "{0}/".format(str(value))

        pizza_info = pizza_info[:-1]

        return pizza_info

    def __slice_pizza(self):
        print("Slicing pizza...")
        if self._size == "small":
            time.sleep(0.1 * 4)
        elif self._size == "middle":
            time.sleep(0.1 * 6)
        else:
            time.sleep(0.1 * 8)

    def __slice_ingredients(self):
        print("Slicing ingredients...")
        time.sleep(0.5)

    def cook(self):
        self.__slice_ingredients()

        print("Cooking pizza...")
        time.sleep(0.6)

        self.__slice_pizza()


class PizzaBarbecue(Pizza):

    __NAME = "BBQ"
    __origin_ingredients = ["cheese", "chicken", "onions"]
    __sauce = "BBQ"
    __dough = "thin"

    def __init__(self, size="small"):
        super().__init__(size, self.__NAME, self.__origin_ingredients, self.__sauce, self.__dough)

    @classmethod
    def get_name(cls):
        return cls.__NAME


class PizzaMargarita(Pizza):

    __NAME = "Margarita"
    __origin_ingredients = ["cheese", "tomato", "pepper"]
    __sauce = "tomato"
    __dough = "thin"

    def __init__(self, size="small"):
        super().__init__(size, self.__NAME, self.__origin_ingredients, self.__sauce, self.__dough)

    @classmethod
    def get_name(cls):
        return cls.__NAME


class PizzaPepperoni(Pizza):

    __NAME = "Pepperoni"
    __origin_ingredients = ["cheese", "pepperoni", "pepper"]
    __sauce = "tomato"
    __dough = "thick"

    def __init__(self, size="small"):
        super().__init__(size, self.__NAME, self.__origin_ingredients, self.__sauce, self.__dough)

    @classmethod
    def get_name(cls):
        return cls.__NAME

