class Game:
    def __init__(self, autobot, desepticon):
        self.autobot = autobot
        self.desepticon = desepticon
        self.__turn = True  # Если True очередь хода автобота, иначе ход десептикона

    def start(self):
        while True:
            self.__print_actions()
            action = self.__choose_action()

            if action == 1:
                self.__fire()
            elif action == 2:
                self.__transform()
            elif action == 3:
                self.__move()
            else:
                self.__use_special_skill()

            if self.autobot.health <= 0 or self.desepticon.health <= 0:
                print("Game is over!")
                break

            self.__print_info()
            self.__turn = not self.__turn

    def __print_info(self):
        print(self.autobot)
        print(self.desepticon)

    def __print_actions(self):
        print("Choose action:\n1 - Fire\n2 - Transform\n3 -  Move\n4 - Special skill")

    def __choose_action(self):
        action_str = input("Enter the action:")
        return int(action_str)

    def __fire(self):
        gun_str = input("Enter 0 or 1 to choose a weapon:")
        coordinates_str = input("Enter coordinates through space: ")
        coordinates = coordinates_str.split(' ')

        if self.__turn:
            if int(gun_str) == 0:
                gun = self.autobot.gun1
                attack_coord = self.autobot.fire(int(coordinates[0]), int(coordinates[1]), gun)
            else:
                gun = self.autobot.gun2
                attack_coord = self.autobot.fire(int(coordinates[0]), int(coordinates[1]), gun)
        else:
            if int(gun_str) == 0:
                gun = self.desepticon.gun1
                attack_coord = self.desepticon.fire(int(coordinates[0]), int(coordinates[1]), gun)
            else:
                gun = self.desepticon.gun2
                attack_coord = self.desepticon.fire(int(coordinates[0]), int(coordinates[1]), gun)

        self.__give_damage(attack_coord, gun)

    def __give_damage(self, coordinates, gun):
        if self.__turn:
            if self.desepticon.x * coordinates[0] + self.desepticon.y * coordinates[1] + coordinates[2] == 0:
                self.desepticon.update_health(gun.damage, True)
                print("Good shot!")
            else:
                print("Unluck! You miss the shot!")
        else:
            if self.autobot.x * coordinates[0] + self.autobot.y * coordinates[1] + coordinates[2] == 0:
                self.autobot.update_health(gun.damage, True)
                print("Good shot!")
            else:
                print("Unluck! You miss the shot!")

    def __transform(self):
        if self.__turn:
            self.autobot.transform()
        else:
            self.desepticon.transform()

    def __move(self):
        new_x_str = input("Enter new x coordinate: ")
        new_x = int(new_x_str)

        if self.__turn:
            self.autobot.move(new_x)
        else:
            self.desepticon.move(new_x)

    def __use_special_skill(self):
        if self.__turn:
            self.autobot.heal()
        else:
            coordinates_str = input("Enter coordinates through space: ")
            coordinates = coordinates_str.split(' ')
            self.desepticon.teleport(int(coordinates[0]), int(coordinates[1]))