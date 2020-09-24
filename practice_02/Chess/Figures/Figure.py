from enum import Enum


class Color(Enum):
    EMPTY = 0
    WHITE = 1
    BLACK = 2


class Figure:
    _image = (" ", " ")

    def __init__(self, color, x, y):
        self.color = color
        self.x = x,
        self.y = y

    @property
    def image(self):
        if self.color == Color.WHITE:
            return self._image[0]
        return self.image[1]

    def __str__(self):
        if self.color == Color.WHITE:
            return self._image[0]
        return self._image[1]

    def is_move_valid(self, x, y, new_x, new_y, is_beating_enemy_figure):
        raise Exception("Unknown type of figure!")


class Pawn(Figure):
    _image = ('♙', '♟')

    def __init__(self, color, x, y):
        super().__init__(color, x, y)
        _notation = "P"

    @property
    def notation(self):
        return self._notation

    def is_move_valid(self, new_x, new_y, is_beating_enemy_figure=False):
        if not is_beating_enemy_figure:
            if self.x == new_x:
                if self.color == Color.WHITE:
                    if self.y < 3:
                        if new_y == self.y + 1 or new_y == self.y + 2:
                            return True
                    elif self.y >= 3:
                        if new_y == self.y + 1:
                            return True
                elif self.color == Color.BLACK:
                    if self.y > 6:
                        if new_y == self.y - 1 or new_y == self.y - 2:
                            return True
                    elif self.y <= 6:
                        if new_y == self.y - 1:
                            return True
            return False
        else:
            if self.x == new_x - 1 or self.x == new_x + 1:
                if self.color == Color.WHITE and new_y == self.y + 1 or self.color == Color.BLACK and new_y == self.y - 1:
                    return True
            return False



