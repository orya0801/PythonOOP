from PizzeriaPatterns.PaymentHandler import *
from PizzeriaPatterns.Restaurant import Restaurant
from PizzeriaPatterns.command import *
from PizzeriaPatterns.TemplateMethod import *


def main():
    # Инициализация
    rest1 = Restaurant(10, 22)
    term1 = Terminal(1, rest1)
    g = Guest()

    # Заказ пицц
    g.set_on_start(StartCommand(term1))
    g.start()

    g.set_on_add_pizza(AddPizzaCommand(term1, ["BBQ", "small"]))
    g.add_pizza()

    g.set_on_add_pizza(AddPizzaCommand(term1, ["Margarita", "large"]))
    g.add_pizza()

    # Оплата
    options = PaymentOptions(False, True, False)

    g.set_on_pay(StopCommand(term1, options))
    g.pay()

    # Поток для записи первого заказа
    order_history = TxtOrderHistory()
    order = term1.order

    t1 = threading.Thread(target=order_history.write_order, args=("history.txt", (str(order))))
    t1.start()


if __name__ == "__main__":
    main()
