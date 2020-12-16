import asyncio

from Pizzeria.Order import Order
from Pizzeria.UserCommandMixin import UserCommandMixin
from PizzeriaPatterns.PaymentHandler import *


class Terminal(UserCommandMixin):
    commands = {1: "Choose pizza", 2: "Finish order"}

    def __init__(self, term_id, restaurant):
        self.id = term_id
        self.is_working = True
        self.is_busy = False
        self.restaurant = restaurant

        self._ph1 = CashPaymentHandler()
        self._ph2 = CardPaymentHandler()
        self._ph3 = GooglePaymentHandler()

        # Создание цепочки-последовательности объектов обработчиков
        self._ph1.successor = self._ph2
        self._ph2.successor = self._ph3

        self.order = None

    #   Основной метод, реализующий алгоритм работы терминала
    def start_working(self):
        self.is_busy = True
        self.order = Order(self)
        print("Terminal ", self.id)
        self.print_menu()

    def add_pizza_to_order(self,  pizza_params):
        if self.order is not None:
            pizza = self.restaurant.menu.get_pizza_by_name(pizza_params)
            self.order.add_pizza_to_order(pizza)

    def start_payment(self, options):
        print(self.order)
        self._ph1.handle(options, self.order.price)
        asyncio.run(self.restaurant.cooking_async(self.order))

    def commands_to_string(self):
        command_str = ""

        for key, value in self.commands.items():
            command_str += "{0}. {1}\n".format(key, value)

        return command_str

    def print_menu(self):
        print(self.restaurant.menu)
        print(self.commands_to_string())

    def __str__(self):
        return "Terminal {0}".format(self.id)
