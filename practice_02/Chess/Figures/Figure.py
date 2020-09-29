from practice_02.Chess.Color import Color


class Figure:
    _image = None
    _notation = None

    def __init__(self, color, x, y):
        self.color = color
        self._x = x
        self._y = y

    @property
    def image(self):
        return self._image[0 if self.color == Color.BLACK else 1]

    @property
    def notation(self):
        return self._notation

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, x):
        self._x = x

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, y):
        self._y = y

    def __str__(self):
        return self.image

    def is_move_valid(self, x, y, new_x, new_y, is_beating_enemy_figure):
        raise Exception("Unknown type of figure!")






