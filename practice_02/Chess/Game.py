from practice_02.Chess.Figures.Figure import Figure, Pawn, Color
from practice_02.Chess.Board import Board


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
    def __init__(self):
        self.player_white = Player(Color.WHITE)
        self.player_black = Player(Color.BLACK)
        self.board = Board()

    def start_game(self):
        self.board.update_board(self.player_white.figures, self.player_black.figures)


game = Game()
game.start_game()
print(game.board)