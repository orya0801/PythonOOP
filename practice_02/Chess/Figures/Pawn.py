from practice_02.Chess.Figures.Figure import Figure
from practice_02.Chess.Color import Color


class Pawn(Figure):
    _image = ('♙', '♟')
    _notation = "P"

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
        else:
            if self.x == new_x - 1 or self.x == new_x + 1:
                if self.color == Color.WHITE and new_y == self.y + 1 or self.color == Color.BLACK and new_y == self.y - 1:
                    return True

        return False
