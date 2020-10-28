from Pizzeria.Restaurant import Restaurant
from Pizzeria.Terminal import Terminal


def main():
    rest1 = Restaurant(10, 22)
    rest2 = Restaurant(9, 24)

    term1 = Terminal(1, rest1)
    term2 = Terminal(2, rest2)
    rest1.add_terminal(term1)

    rest1.serve_new_guests(2, 12)


if __name__ == '__main__':
    main()
