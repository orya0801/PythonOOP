from practice_02.Pizzeria.Restaurant import Restaurant
from practice_02.Pizzeria.Menu import Menu
from practice_02.Pizzeria.Terminal import Terminal
from practice_02.Pizzeria.Pizza import PizzaMargarita, PizzaPepperoni, PizzaBarbecue


def main():
    rest1 = Restaurant(10, 22)
    rest2 = Restaurant(9, 24)

    term1 = Terminal(1, rest1)
    term2 = Terminal(2, rest2)
    rest1.add_terminal(term1)

    rest1.serve_new_guests(2, 12)


if __name__ == '__main__':
    main()
