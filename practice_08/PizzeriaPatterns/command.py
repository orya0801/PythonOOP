from __future__ import annotations
from abc import ABC, abstractmethod
from PizzeriaPatterns.Terminal import Terminal


class Command(ABC):
    """
        Интерфейс Команды объявляет метод для выполнения команд
    """

    @abstractmethod
    def execute(self):
        pass


class StartCommand(Command):

    def __init__(self, receiver: Terminal):
        self.receiver = receiver

    def execute(self):
        self.receiver.start_working()


class AddPizzaCommand(Command):

    def __init__(self, receiver: Terminal, pizza_params):
        self.receiver = receiver
        self.pizza_params = pizza_params

    def execute(self):
        pizza = self.receiver.restaurant.menu.get_pizza_by_name(self.pizza_params)
        self.receiver.order.add_pizza_to_order(pizza)


class StopCommand(Command):

    def __init__(self, receiver: Terminal, options, payment=None):
        self.receiver = receiver
        self.options = options
        self.payment = payment

    def execute(self):
        self.receiver.start_payment(self.options)


class Guest:
    """
        В данном случае отправителем будет гость.
        Отправитель связан с одной или несколькими командами.
        Он отправляет запрос команде.
    """

    _on_start = None
    _on_add_pizza = None
    _on_pay = None

    def set_on_start(self, command: Command):
        self._on_start = command

    def set_on_add_pizza(self, command: Command):
        self._on_add_pizza = command

    def set_on_pay(self, command: Command):
        self._on_pay = command

    def start(self):
        if isinstance(self._on_start, Command):
            self._on_start.execute()

    def add_pizza(self):
        if isinstance(self._on_add_pizza, Command):
            self._on_add_pizza.execute()

    def pay(self):
        if isinstance(self._on_pay, Command):
            self._on_pay.execute()