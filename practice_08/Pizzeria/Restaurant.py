import asyncio

from Pizzeria.Menu import Menu
from Pizzeria.Pizza import PizzaBarbecue, PizzaPepperoni, PizzaMargarita
from functools import wraps
from threading import Thread


def decorator_serve(serve):
    import datetime
    import time

    @wraps(serve)
    def wrapper(self, n_guests, visit_time):
        start = time.time()
        print("Order is created in {}".format(datetime.datetime.now()))
        order = serve(self, n_guests, visit_time)
        end = time.time()
        print("Order is finished in {}".format(datetime.datetime.now()))
        print("Lead time: {}".format(end - start))

        return order
    return wrapper


def decorator_add_term(add_term):
    def term_is_not_belong_to_rest():
        print("Terminal belongs to another restaraunt")

    @wraps(add_term)
    def wrapper(self, terminal):
        if terminal.restaurant == self:
            return add_term(self, terminal)
        else:
            return term_is_not_belong_to_rest()

    return wrapper


class Restaurant:
    # Счетчик гостей всех ресторанов сети
    __guests = 0
    # Имя ресторана
    __name = "Dodo Pizza"

    def __init__(self, open_time, close_time):
        self.open_time = open_time
        self.close_time = close_time
        self.terminals = []
        # Отношение композиции
        self.menu = Menu([PizzaPepperoni, PizzaMargarita, PizzaBarbecue])

    @property
    def guests(self):
        return self.__guests

    @property
    def name(self):
        return self.__name

    #   Метод, реализующий обслуживание новых гостей
    @decorator_serve
    def serve_new_guests(self, n_guests, time):
        if self.__is_open(time):
            self.__guests += n_guests

            while True:
                for term in self.terminals:
                    if term.is_working and not term.is_busy:
                        order = term.start_working()
                        break

                if order is not None:
                    break

            #   Асинхронное приготовление пиццы
            asyncio.run(self.cooking_async(order))
            print("Your order is ready!")

            return order
        else:
            print("Closed!")
            return None

    @decorator_add_term
    def add_terminal(self, terminal):
        self.terminals.append(terminal)

    #   Метод проверки работы ресторана
    def __is_open(self, time):
        if self.close_time >= time >= self.open_time:
            return True
        return False

    #   Асинхронный метод приготовления пиццы
    async def cooking_async(self, order):
        cooking_tasks = self.__get_cooking_tasks(order)

        await asyncio.wait(cooking_tasks)

    #   Метод начала приготовления ресторана
    def __get_cooking_tasks(self, order):
        cooking_tasks = []

        for pizza in order.order_list:
            cooking_tasks.append(pizza.cook_async())

        return cooking_tasks



