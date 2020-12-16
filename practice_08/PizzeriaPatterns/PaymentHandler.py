from abc import ABC, abstractmethod


class PaymentOptions:

    def __init__(self, cash, card, google_pay):
        self.is_cash = cash
        self.is_card = card
        self.is_google_pay = google_pay


class PaymentHandler(ABC):

    def __init__(self, successor=None):
        self.successor = successor

    @abstractmethod
    def handle(self, payment_option, price):
        pass


class CashPaymentHandler(PaymentHandler):

    def handle(self, payment_options, price):
        if payment_options.is_cash:
            payment = float(input("Enter your payment:"))

            while True:
                if payment < price:
                    print("Please enter payment to cover the price!")
                    self.handle(payment_options, price)
                else:
                    print("Your payment: {0}\nYour short change: {1}".format(payment, payment - price))

                    break

            return True

        elif self.successor is not None:
            self.successor.handle(payment_options, price)

            return False


class CardPaymentHandler(PaymentHandler):

    def handle(self, payment_options, price):
        if payment_options.is_card:
            print("Payment has been made by bank card! Thank you!")

            return True

        elif self.successor is not None:
            self.successor.handle(payment_options, price)

            return False


class GooglePaymentHandler(PaymentHandler):

    def handle(self, payment_options, price):
        if payment_options.is_google_pay:
            print("Payment has been made by Google Pay! Thank you!")

            return True

        elif self.successor is not None:
            self.successor.handle(payment_options, price)

            return False


