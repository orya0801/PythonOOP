from overall_task.Transformer import Transformer
import time


class Autobot(Transformer):

    def __init__(self, x, y, gun1, gun2):
        super(Autobot, self).__init__(x, y, gun1, gun2)
        self.__is_car = False

    def transform(self):
        time.sleep(1)
        self.__is_car = not self.__is_car

    def fire(self, x, y, gun):
        if not self.__is_car:
            if gun == self.gun1:
                return self.gun1.fire(self._x, self._y, x, y)
            else:
                return self.gun2.fire(self._x, self._y, x, y)
        else:
            print("Desepticon can fire only when he isn't a car!")

    def heal(self):
        if self.__is_car:
            if self._max_health > self._health + 20:
                self._health += 20
            else:
                self._health = self._max_health
        else:
            print("Autobot can heal only when he is a car!")

    def __str__(self):
        autobot_str = "Autobot" + super().__str__()
        return autobot_str
