class Transformer:

    def __init__(self, x, y, gun1, gun2):
        self._x = x
        self._y = y
        self.gun1 = gun1
        self.gun2 = gun2
        self._level = 1
        self.__is_car = False
        self._max_health = 20
        self._health = self._max_health

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    @property
    def health(self):
        return self._health

    @property
    def level(self):
        return self._level

    def update_health(self, hp, is_damage):
        if is_damage:
            self._health -= hp
        else:
            self._health += hp

    def transform(self):
        raise Exception("Unknown transformer!")

    def fire(self):
        raise Exception("Unknown transformer!")

    def move(self, new_x):
        self._x = new_x

    def level_up(self):
        self._level += 1
        self._max_health += 10

    def __add__(self, other):
        self._level += other.level
        self._max_health += other.level * 10
        return self

    def __sub__(self, other):
        self._level -= other.level
        self._max_health -= other.level * 10
        return self

    def __str__(self):
        return ":\nLevel: {0}\nHealth: {1}\nCoordinates:[{2} {3}]\n"\
            .format(self._level, self._health, self._x, self._y)
