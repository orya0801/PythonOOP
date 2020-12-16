from abc import ABC, abstractmethod
import csv
import threading
import time


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