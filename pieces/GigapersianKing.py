from pieces.Piece import Piece


class GigapersianKing(Piece):
    def __init__(self, color, position):
        self.name = 'GigapersianKing'
        super(GigapersianKing, self).__init__(color, position)
        if self.color == 'w':
            self.image = 'images/whitegigachad.jpg'
        else:
            self.image = 'images/blackgigachad.jpg'

        self.value = 9

    def get_possible_moves(self, board):
        straight_line_moves = self.get_possible_straight_line_moves(board)
        diagonal_moves = self.get_possible_diagonal_moves(board)

        knight_moves = self.get_possible_knight_moves(board)

        return straight_line_moves + diagonal_moves + knight_moves

    def get_possible_knight_moves(self, board):
        moves = []
        directions = [
            (2, 1), (1, 2), (-1, 2), (-2, 1),
            (-2, -1), (-1, -2), (1, -2), (2, -1)
        ]

        for direction in directions:
            new_pos = (self.position[0] + direction[0], self.position[1] + direction[1])
            if 0 <= new_pos[0] < 8 and 0 <= new_pos[1] < 8:
                piece = board[new_pos[0]][new_pos[1]]
                if not piece or self.is_opponent(piece):
                    moves.append(new_pos)

        return moves