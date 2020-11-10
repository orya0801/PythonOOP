"""
    Класс UserCommandMixin содержит функции, обрабатывающие команды введенные пользователем
"""


class UserCommandMixin:

    def get_command_from_guest(self):
        while True:
            try:
                command = int(input("Enter the command number:"))
                if command in self.commands:
                    return command
            except ValueError:
                return False

    def get_payment_from_guest(self, order):
        payment = float(input("Enter your payment:"))

        while True:
            if payment < order.price:
                print("Please enter payment to cover the price!")
                self.get_payment_from_guest(order)
            else:
                print("Your payment: {0}\nYour short change: {1}".format(payment, payment - order.price))
                print("Wait for your order!")
                break

    def get_pizza_params_from_user(self):
        while True:
            try:
                pizza = input("Enter the name and size of the pizza separated by a space: ")
                pizza = pizza.split(' ')
                pizza_name = pizza[0]
                pizza_size = pizza[1]

                return pizza_name, pizza_size

            except IndexError:
                print("Invalid pizza name or size")