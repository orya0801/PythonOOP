from Pizzeria.Menu import Menu
from Pizzeria.Pizza import PizzaBarbecue, PizzaPepperoni, PizzaMargarita
from functools import wraps


def decorator_serve(serve):
    import datetime
    import time

    @wraps(serve)
    def wrapper(self, n_guests, visit_time):
        start = time.time()
        print("Order is created in {}".format(datetime.datetime.now()))
        serve(self, n_guests, visit_time)
        end = time.time()
        print("Order is finished in {}".format(datetime.datetime.now()))
        print("Lead time: {}".format(end - start))

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
                    order = term.start_working()

                if order is not None:
                    break

            self.__cooking(order)
            print("Your order is ready!")
        else:
            print("Closed!")

    @decorator_add_term
    def add_terminal(self, terminal):
        self.terminals.append(terminal)

    #   Метод проверки работы ресторана
    def __is_open(self, time):
        if self.close_time >= time >= self.open_time:
            return True
        return False

    #   Метод начала приготовления ресторана
    def __cooking(self, order):
        for pizza in order.order_list:
            pizza.cook()





