from Pizzeria.Menu import Menu
from Pizzeria.Pizza import PizzaBarbecue, PizzaPepperoni, PizzaMargarita


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

    def add_terminal(self, terminal):
        if terminal.restaurant == self:
            self.terminals.append(terminal)
        else:
            raise Exception("Terminal belongs to another restaraunt")

    #   Метод проверки работы ресторана
    def __is_open(self, time):
        if self.close_time >= time >= self.open_time:
            return True
        return False

    #   Метод начала приготовления ресторана
    def __cooking(self, order):
        for pizza in order.order_list:
            pizza.cook()


