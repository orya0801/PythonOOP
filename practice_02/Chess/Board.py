class Board:
    _empty_cell = '.'

    def __init__(self):
        self.board = [["."] * 8 for y in range(8)]

    def update_board(self, figures_white, figures_black):
        figures = figures_black + figures_white

        for y in range(8):
            for x in range(8):
                figure = next((f for f in figures if f.x == x and f.y == y), None)
                print(figure)
                if figure is None:
                    self.board[y][x] = self._empty_cell
                else:
                    self.board[y].insert(x, figure.image)

    def __str__(self):
        res = ''
        for y in range(8):
            res += ''.join(map(str, self.board[y])) + "\n"
        return res

