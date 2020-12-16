from tkinter import *
from tkinter import messagebox
from Pizzeria.Restaurant import Restaurant
from Pizzeria.Terminal import Terminal
from Pizzeria.Order import Order

LARGE_FONT = ("Verdana", 16)
NORMAL_FONT = ("Verdana", 11)


class PizzeriaApp(Tk):

    def __init__(self, restaurant, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)

        self.restaraunt = restaurant
        self.order = Order(self.restaraunt.terminals[0])
        #   Устанавливаем имя окна
        self.title(restaurant.name)
        #   Устанавливаем размеры окна
        self.geometry("500x700")

        self.frame_menu = MenuFrame(restaurant.menu, self, self)
        self.frame_menu.pack()

        self.frame_order = OrderFrame(self, self)
        self.frame_order.pack()

    def add_pizza_to_order(self, pizza):
        self.order.add_pizza_to_order(pizza)
        self.frame_order.add_pizza_to_list(pizza)
        print(self.order)

    def calculate_order_price(self):
        price = self.order.price
        messagebox.showinfo("Order", "TOTAL PRICE: {0}".format(price))

    def clear_order(self):
        self.order = Order(self.restaraunt.terminals[0])


class MenuFrame(Frame):

    def __init__(self, menu, master, controller):
        Frame.__init__(self, master)
        self.controller = controller
        self.menu = menu
        self.initUI()

    def initUI(self):
        rows_count = 0

        # Menu Title
        self.label_menu = Label(self, text="Menu", font=LARGE_FONT)
        self.label_menu.grid(row=rows_count, column=0, columnspan=4, sticky="nsew")

        rows_count += 1

        # Menu List
        for pizza in self.menu.list:
            self.label_name = Label(self, text=pizza.get_name(), font=NORMAL_FONT)
            self.label_name.grid(row=rows_count, column=0, sticky="nsew", pady=3)

            pizza_obj = pizza()
            for size, price in pizza_obj.prices.items():
                self.label_size = Label(self, text=size, font=NORMAL_FONT)
                self.label_size.grid(row=rows_count, column=1, sticky="nsew", pady=3)

                self.label_size = Label(self, text=price, font=NORMAL_FONT)
                self.label_size.grid(row=rows_count, column=2, sticky="nsew", pady=3)

                self.button_add = Button(self, text="Add", font=NORMAL_FONT)
                self.button_add.bind('<Button-1>', lambda event, a=pizza_obj.name, b=size: self.add_pizza(a, b))
                self.button_add.grid(row=rows_count, column=3, sticky="nsew", pady=3)

                rows_count += 1

    def add_pizza(self, pizza, size):
        pizza = self.menu.get_pizza_by_name(pizza_params=[pizza, size])
        print(pizza)

        self.controller.add_pizza_to_order(pizza)


class OrderFrame(Frame):

    def __init__(self, master, controller):
        Frame.__init__(self, master)
        self.controller = controller
        self.initUI()

    def initUI(self):
        # Order Title
        self.label_menu = Label(self, text="Order", font=LARGE_FONT)
        self.label_menu.pack(ipady=5)

        # Order ListBox
        self.listbox_order = Listbox(self, width=self.master.winfo_screenwidth(), font=NORMAL_FONT)
        self.listbox_order.pack()

        # Calculate Price Button
        self.button_calc = Button(self, text="Calculate price", font=NORMAL_FONT, command=self.calculate_price)
        self.button_calc.pack(pady=5)

        # Delete Pizza from Order:
        self.button_clear = Button(self, text="Clear order", font=NORMAL_FONT, command=self.clear_order)
        self.button_clear.pack(pady=5)

    def add_pizza_to_list(self, pizza):
        pizza_str = "{0}     {1}     {2}".format(pizza.name, pizza.size, pizza.price)
        self.listbox_order.insert(END, pizza_str)

    def calculate_price(self):
        self.controller.calculate_order_price()

    def clear_order(self):
        self.listbox_order.delete(0, END)
        self.controller.clear_order()


rest = Restaurant(10, 22)
term = Terminal(1, rest)

rest.add_terminal(term)

app = PizzeriaApp(rest)
app.mainloop()