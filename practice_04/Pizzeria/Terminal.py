from Pizzeria.Order import Order
from Pizzeria.UserCommandMixin import UserCommandMixin


class Terminal(UserCommandMixin):
    commands = {1: "Choose pizza", 2: "Finish order"}

    def __init__(self, term_id, restaurant):
        self.id = term_id
        self.__is_working = True
        self.__is_busy = False
        self.restaurant = restaurant

    #   Основной метод, реализующий алгоритм работы терминала
    def start_working(self):
        if self.__is_working:
            self.__is_busy = True

            order = Order(self)
            self.print_menu()

            while True:
                command = self.get_command_from_guest()

                if command == 1:
                    pizza_params = self.get_pizza_params_from_user()
                    pizza = self.restaurant.menu.get_pizza_by_name(pizza_params)
                    order.add_pizza_to_order(pizza)

                if command == 2:
                    order.print()
                    self.get_payment_from_guest(order)
                    break

            self.__is_busy = False
            return order
        return None

    def commands_to_string(self):
        command_str = ""

        for key, value in self.commands.items():
            command_str += "{0}. {1}\n".format(key, value)

        return command_str

    def print_menu(self):
        if self.__is_working:
            print(self.restaurant.menu)
            print(self.commands_to_string())
            return True
        return False

    def __str__(self):
        return "Terminal {0}".format(self.id)
