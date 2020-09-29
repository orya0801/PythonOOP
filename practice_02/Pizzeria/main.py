from practice_02.Pizzeria.Restaurant import Restaurant
from practice_02.Pizzeria.Menu import Menu
from practice_02.Pizzeria.Order import Order
from practice_02.Pizzeria.Terminal import Terminal
from practice_02.Pizzeria.Pizza.PizzaBarbecue import PizzaBarbecue
from practice_02.Pizzeria.Pizza.PizzaMargarita import PizzaMargarita
from practice_02.Pizzeria.Pizza.PizzaPepperoni import PizzaPepperoni


def main():
    # Creating pizza
    menu_list = [PizzaBarbecue, PizzaPepperoni, PizzaMargarita]
    menu = Menu(menu_list)

    rest1 = Restaurant(10, 22, menu)
    rest2 = Restaurant(9, 24, menu)

    term1 = Terminal(1, rest1)
    term2 = Terminal(2, rest2)
    rest1.add_terminal(term1)

    rest1.serve_new_guests(2)


if __name__ == '__main__':
    main()
