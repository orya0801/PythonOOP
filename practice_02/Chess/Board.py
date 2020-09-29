class Board:
    _empty_cell = '. '

    def __init__(self):
        self._board = [[self._empty_cell] * 8 for y in range(8)]

    @property
    def board(self):
        return self._board

    @board.setter
    def board(self, updated_board):
        self._board = updated_board

    def start_board(self, figures_white, figures_black):
        figures = figures_black + figures_white
        start_board = []

        for y in range(8):
            start_board.append([])
            for x in range(8):
                figure = next((f for f in figures if f.x == x and f.y == y), None)
                if figure is None:
                    start_board[y].append(self._empty_cell)
                else:
                    start_board[y].append(figure.image)

        self.board = start_board

    def update_board(self, figure, new_x, new_y):
        board = self.board
        board[figure.y][figure.x] = self._empty_cell
        board[new_y][new_x] = figure.image
        self.board = board

    def __str__(self):
        res = ''
        for y in range(8):
            res += ''.join(map(str, self.board[y])) + "\n"
        return res

