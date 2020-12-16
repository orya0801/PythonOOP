"""
    Класс UserCommandMixin содержит функции, обрабатывающие команды введенные пользователем
"""


class UserCommandMixin:

    def get_command_from_guest(self):
        while True:
            # проверка на целочисленное значение номера команды
            try:
                command = int(input("Enter the command number:"))
                if command in self.commands:
                    return command
            except ValueError:
                return False

    def get_payment_from_guest(self):
        payment = float(input("Enter your payment:"))

        while True:
            if payment < self.order.price:
                print("Please enter payment to cover the price!")
                self.get_payment_from_guest(self.order)
            else:
                print("Your payment: {0}\nYour short change: {1}".format(payment, payment - self.order.price))
                print("Wait for your order!")
                break

    def get_pizza_params_from_user(self):
        while True:
            # Проверка на наличие названия и размеры пиццы при заказе
            try:
                pizza = input("Enter the name and size of the pizza separated by a space: ")
                pizza = pizza.split(' ')
                pizza_name = pizza[0]
                pizza_size = pizza[1]

                return pizza_name, pizza_size

            except IndexError:
                print("Invalid pizza name or size")