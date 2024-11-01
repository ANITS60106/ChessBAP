import random
from pieces.Piece import Piece


class Goose(Piece):
    def __init__(self, color, position):
        self.name = "Goose"
        super().__init__(color, position)
        self.image = 'images/white_goose.png' if color == 'w' else 'images/black_goose.png'

    def get_possible_moves(self, board, capture_piece_callback):
        moves = []
        directions = [
            (2, 0), (-2, 0), (0, -2), (-1, 1), (-1, -1), (1, -1),
        ]

        for direction in directions:
            new_pos = (self.position[0] + direction[0], self.position[1] + direction[1])
            if 0 <= new_pos[0] < 8 and 0 <= new_pos[1] < 8:
                piece = board[new_pos[0]][new_pos[1]]

                # Normal movement check for Goose
                if not piece or self.is_opponent(piece):
                    moves.append(new_pos)

                # Check for capturing a pawn
                if direction[0] == 2 and self.position[1] < 7:
                    pawn_pos = (self.position[0], self.position[1] + 1)
                    if 0 <= pawn_pos[0] < 8 and 0 <= pawn_pos[1] < 8:
                        pawn = board[pawn_pos[0]][pawn_pos[1]]

                        # Only check for capturing if there is a pawn in front
                        if pawn and pawn.name == 'Pawn':
                            dice_roll = random.randint(1, 6)
                            print(f"Кубик показал: {dice_roll}")

                            if self.name == 'Goose':
                                if dice_roll % 2 == 0 and dice_roll != 6:
                                    # Capture the pawn
                                    moves.append(new_pos)
                                    board[pawn_pos[0]][pawn_pos[1]] = None  # Remove the pawn from the board
                                    capture_piece_callback(pawn)  # Mark that the pawn was captured
                                    print(f"{self.name} съел пешку на {pawn_pos} и переместился на {new_pos}")
                                elif dice_roll == 6:
                                    # Destroy a line if dice shows 6
                                    line_to_destroy = random.randint(0, 7)
                                    print(f"{self.name} выпало 6 - уничтожается линия {line_to_destroy}")
                                    for col in range(8):
                                        target_piece = board[line_to_destroy][col]
                                        if target_piece:
                                            board[line_to_destroy][col] = None
                                            capture_piece_callback(target_piece)
                                            print(
                                                f"{target_piece.name} на позиции ({line_to_destroy}, {col}) уничтожен")
                                else:
                                    print(f"{self.name} не съел пешку на {pawn_pos} (выпало {dice_roll})")

        # Check diagonal moves
        for direction in directions:
            new_pos_diag = (self.position[0] + direction[1], self.position[1] + direction[0])
            if 0 <= new_pos_diag[0] < 8 and 0 <= new_pos_diag[1] < 8:
                piece = board[new_pos_diag[0]][new_pos_diag[1]]
                if not piece or self.is_opponent(piece):
                    moves.append(new_pos_diag)

        return moves
