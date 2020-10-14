from overall_task.Transformer import Transformer
import time


class Desepticon(Transformer):

    def __init__(self, x, y, gun1, gun2):
        super().__init__(x, y, gun1, gun2)
        self.__is_car = False

    def transform(self):
        time.sleep(2)
        self.__is_car = not self.__is_car

    def fire(self, x, y, gun):
        if self.__is_car is False:
            if gun == self.gun1:
                return self.gun1.fire(self._x, self._y, x, y)
            else:
                return self.gun2.fire(self._x, self._y, x, y)
        else:
            print("Desepticon can fire only when he isn't a car!")

    def teleport(self, x, y):
        if self.__is_car:
            self._x = x
            self._y = y
        else:
            print("Desepticon can use teleport only when he is a car!")

    def __str__(self):
        desepticon_str = "Desepticon" + super().__str__()
        return desepticon_str
