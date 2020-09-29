class Menu:
    def __init__(self, menu):
        self.list = menu

    def get_pizza_by_name(self, pizza_params):
        pizza = next((pizza for pizza in self.list if pizza.get_name() == pizza_params[0]), None)

        if pizza is None:
            raise Exception("Pizza not found!")

        new_pizza = pizza(pizza_params[1])

        return new_pizza

    def __str__(self):
        menu_str = "Menu:\n"

        for pizza in self.list:
            menu_str += "\t{0}\n".format(pizza.info())

        return menu_str
