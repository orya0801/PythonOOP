from practice_02.Pizzeria.Pizza.Pizza import Pizza


class PizzaPepperoni(Pizza):
    __name = "Pepperoni"
    __prices = {
        "small": 300,
        "middle": 400,
        "large": 500
    }

    def __init__(self, size="small"):
        super(PizzaPepperoni, self).__init__(size)
        self.__size = size
        self.__price = self.prices[size]

    @classmethod
    def get_name(cls):
        return cls.__name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def prices(self):
        return self.__prices

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        if size in self.__prices:
            self.__size = size
            self.__price = self.__prices[size]
        else:
            raise Exception("Given size doesn't exist for this pizza")

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        self.__price = price

    @classmethod
    def info(cls):
        pizza_info = cls.__name + " - "
        for key in cls.__prices.keys():
            pizza_info += "{0}/".format(key)

        pizza_info = pizza_info[:-1] + "\t"

        for value in cls.__prices.values():
            pizza_info += "{0}/".format(str(value))

        pizza_info = pizza_info[:-1]

        return pizza_info