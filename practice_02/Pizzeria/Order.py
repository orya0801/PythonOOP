class Order:
    def __init__(self, terminal, guests):
        self.terminal = terminal
        self.guests = guests
        self.order_list = []
        self.price = 0

    def add_pizza_to_order(self, pizza):
        self.order_list.append(pizza)
        self.price += pizza.price

    def __str__(self):
        order_str = ""

        order_str += "{0}\n".format(self.terminal)
        order_str += "Number of guests: {0}\n".format(self.guests)

        count = 1
        for pizza in self.order_list:
            order_str += "{0}. {1} - {2}\t{3}\n".format(count, pizza.name, pizza.size, pizza.price)
            count += 1

        order_str += "TOTAL: {0}".format(self.price)
            
        return order_str

    def print(self):
        print(self)
