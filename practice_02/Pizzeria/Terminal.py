from Pizzeria.Order import Order


class Terminal:
    __commands = {1: "Choose pizza", 2: "Finish order"}

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
            self.__print_menu()

            while True:
                command = self.__get_command_from_guest()

                if command == 1:
                    pizza_params = self.__get_pizza_params_from_user()
                    pizza = self.restaurant.menu.get_pizza_by_name(pizza_params)
                    order.add_pizza_to_order(pizza)

                if command == 2:
                    order.print()
                    self.__get_payment_from_guest(order)
                    break

            self.__is_busy = False
            return order
        return None

    def __print_menu(self):
        if self.__is_working:
            print(self.restaurant.menu)
            print(self.__commands_to_string())
            return True
        return False

    def __commands_to_string(self):
        command_str = ""

        for key, value in self.__commands.items():
            command_str += "{0}. {1}\n".format(key, value)

        return command_str

    def __get_command_from_guest(self):
        while True:
            try:
                command = int(input("Enter the command number:"))
                if command in self.__commands:
                    return command
            except ValueError:
                return False

    def __get_payment_from_guest(self, order):
        payment = float(input("Enter your payment:"))

        while True:
            if payment < order.price:
                print("Please enter payment to cover the price!")
                self.__get_payment_from_guest(order)
            else:
                print("Your payment: {0}\nYour short change: {1}".format(payment, payment - order.price))
                print("Wait for your order!")
                break

    def __get_pizza_params_from_user(self):
        while True:
            try:
                pizza = input("Enter the name and size of the pizza separated by a space: ")
                pizza = pizza.split(' ')
                pizza_name = pizza[0]
                pizza_size = pizza[1]

                return pizza_name, pizza_size

            except IndexError:
                print("Invalid pizza name or size")

    def __str__(self):
        return "Terminal {0}".format(self.id)
