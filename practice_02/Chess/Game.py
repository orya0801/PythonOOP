from practice_02.Chess.Figures.Pawn import Pawn
from practice_02.Chess.Board import Board
from practice_02.Chess.Color import Color


class Player:
    def __init__(self, color):
        self.color = color
        self.figures = []
        if color == Color.WHITE:
            for i in range(8):
                self.figures.append(Pawn(color, i, 6))
        else:
            for i in range(8):
                self.figures.append(Pawn(color, i, 1))


class Game:
    __current_move = Color.WHITE

    def __init__(self):
        self.player_white = Player(Color.WHITE)
        self.player_black = Player(Color.BLACK)
        self.board = Board()

    def start_game(self):
        self.board.start_board(self.player_white.figures, self.player_black.figures)

    def move(self, x, y, new_x, new_y):
        if self.__current_move == Color.WHITE:
            figures = self.player_white.figures
        else:
            figures = self.player_black.figures

        curr_figure = next((figure for figure in figures if figure.x == x and figure.y == y), None)

        if curr_figure is not None:
            if curr_figure.is_move_valid:
                self.board.update_board(curr_figure, new_x, new_y)
                self.update_player_figures_position(new_x, new_y, x, y)

        self.change_turn()

    def update_player_figures_position(self, new_x, new_y, x, y):
        if self.__current_move == Color.WHITE:
            for i in range(len(self.player_white.figures)):
                if self.player_white.figures[i].x == x and self.player_white.figures[i].y == y:
                    self.player_white.figures[i].x = new_x
                    self.player_white.figures[i].y = new_y
                    break
        else:
            for i in range(len(self.player_black.figures)):
                if self.player_black.figures[i].x == x and self.player_black.figures[i].y == y:
                    self.player_black.figures[i].x = new_x
                    self.player_black.figures[i].y = new_y
                    break

    def change_turn(self):
        if self.__current_move == Color.WHITE:
            self.__current_move = Color.BLACK
        else:
            self.__current_move = Color.WHITE


game = Game()
game.start_game()
print(game.board)
game.move(4, 6, 4, 4)
print(game.board)
game.move(3, 1, 3, 3)
print(game.board)
input()

