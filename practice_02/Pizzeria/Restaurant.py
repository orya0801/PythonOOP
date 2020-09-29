class Restaurant:
    __guests = 0
    __name = "Dodo Pizza"

    def __init__(self, open_time, close_time, menu):
        self.open_time = open_time
        self.close_time = close_time
        self.terminals = []
        self.menu = menu

    @property
    def guests(self):
        return self.__guests

    def serve_new_guests(self, n_guests):
        self.__guests += n_guests

        for term in self.terminals:
            if term.is_working and not term.is_busy:
                order = term.start_working(n_guests)
                break

        self.cooking(order)

    def add_terminal(self, terminal):
        if terminal.restaurant == self:
            self.terminals.append(terminal)
        else:
            raise Exception("Terminal belongs to another restaraunt")

    def is_open(self, time):
        if self.close_time >= time >= self.open_time:
            return True
        return False

    def cooking(self, order):
        for pizza in order.order_list:
            pizza.cook()


