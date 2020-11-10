from Pizzeria.Restaurant import Restaurant
from Pizzeria.Terminal import Terminal
from Pizzeria.Order import OrderHistory
import threading
from Pizzeria.Pizza import PizzaMargarita, Pizza


def main():
    order_history = OrderHistory()

    rest1 = Restaurant(10, 22)

    term1 = Terminal(1, rest1)
    term2 = Terminal(2, rest1)
    rest1.add_terminal(term1)
    rest1.add_terminal(term2)

    order = rest1.serve_new_guests(2, 12)

    t = threading.Thread(target=order_history.locked_update, args=(str(order),))
    t.start()

    order = rest1.serve_new_guests(2, 12)

    t = threading.Thread(target=order_history.locked_update, args=(str(order),))
    t.start()


if __name__ == '__main__':
    main()
