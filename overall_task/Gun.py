class Gun:
    _max_level = 10

    def __init__(self):
        self._damage = 10
        self._max_ammo = 5
        self._start_speed = 10
        self._upgrade_cost = 5
        self._level = 1
        self._ammo = self._max_ammo

    @property
    def max_level(self):
        return self._max_level

    @property
    def damage(self):
        return self._damage

    @property
    def ammo(self):
        return self._ammo

    @property
    def max_ammo(self):
        return self._max_ammo

    @property
    def start_speed(self):
        return self._start_speed

    @property
    def level(self):
        return self._level

    @property
    def upgrade_cost(self):
        return self._upgrade_cost

    def reload(self):
        if self.ammo < self._max_ammo:
            self.ammo = self._max_ammo

    def fire(self, x, y, new_x, new_y):
        if self.ammo > 0:
            self.ammo -= 1
            linear_eq = [y - new_y, new_x - x, x * new_y - new_x * y]
            return linear_eq
        else:
            print("You don't have enough ammo. Reloading!")
            self.reload()
            return None

    def __calculate_upgrade_cost(self):
        self._upgrade_cost = self._upgrade_cost ** 2
        return self._upgrade_cost

    def upgrade(self, money):
        if money >= self._upgrade_cost:
            money -= self._upgrade_cost
            self._level += 1
            self._start_speed += 1
            self._max_ammo += 1
            self._upgrade_cost = self.__calculate_upgrade_cost()
        else:
            print("You don'y have enough money!")

        return money
