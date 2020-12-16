import threading
import time


class Order:
    def __init__(self, terminal):
        self.terminal = terminal
        self.order_list = []
        self.price = 0

    def add_pizza_to_order(self, pizza):
        self.order_list.append(pizza)
        self.price += pizza.price

    def __str__(self):
        order_str = ""

        order_str += "{0}\n".format(self.terminal)

        count = 1
        for pizza in self.order_list:
            order_str += "{0}. {1} - {2}\t{3}\n".format(count, pizza.name, pizza.size, pizza.price)
            count += 1

        order_str += "TOTAL: {0}".format(self.price)

        return order_str

    def print(self):
        print(self)

    # Перегрузка методов сложения и вычитания
    def __add__(self, pizza):
        self.order_list.append(pizza)

    def __sub__(self, pizza):
        self.order_list.remove(pizza)


"""
    Класс OrderHistory предназначен для сохранения всех сделанных заказов в специальный файл history.txt.
    При этом используется блокировка Lock() при записи нового заказа. Подразумевается, что запись будет 
    производится в отдельном потоке, и, чтобы не случилось ситуации, когда два потока обращаются к одному ресурсу 
    одноврменно, используется специальный туннель, который обеспечивает последовательное обращение к файлу истории
    заказов.
"""

from abc import ABC, abstractmethod
import csv


class OrderHistory(ABC):

    def __init__(self):
        self.orders = 0
        self._lock = threading.Lock()
        self.file = None

    def write_order(self, file_name, order):
        self.set_file_name(file_name)
        self.locked_update(order)
        self.finish()

    def set_file_name(self, file_name):
        self.file = file_name

    @abstractmethod
    def locked_update(self, order):
        pass

    def finish(self):
        print("Finish writing order in file.")


class TxtOrderHistory(OrderHistory):

    def locked_update(self, order):
        if order is not None:
            print("\nStart writing order in txt file...\n")
            time.sleep(5)
            with self._lock:
                self.orders += 1
                with open(self.file, 'a') as f:
                    f.write(order + "\n\n")
                    print("\nFinish writing!\n")


class CsvOrderHistory(OrderHistory):

    def locked_update(self, order):
        if order is not None:
            print("\nStart writing order in csv file...\n")
            time.sleep(5)

            with self._lock:
                self.orders += 1

                with open('eggs.csv', 'w', newline='') as csvfile:
                    fieldnames = ['order_id', 'order_price', 'terminal']
                    writer = csv.writer(csvfile, delimiter=' ',
                                        quotechar='|',
                                        quoting=csv.QUOTE_MINIMAL,
                                        fieldnames=fieldnames)
                    writer.writerow({'order_id':self.orders, 'order_price':order.price, 'terminal':order.terminal})