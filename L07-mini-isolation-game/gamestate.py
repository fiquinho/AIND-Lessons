from copy import deepcopy

BOARD_X_DIM = 3
BOARD_Y_DIM = 2


class GameState:

    def __init__(self):

        self._board = [[0] * BOARD_Y_DIM for _ in range(BOARD_X_DIM)]
        self._board[-1][-1] = 1

        self.step_number = 0
        self.players_positions = [None, None]
        self.player_turn = 0

    def forecast_move(self, move):
        """ Return a new board object with the specified move
        applied to the current game state.

        Parameters
        ----------
        move: tuple
            The target position for the active player's next move
        """
        new_board = deepcopy(self)

        if move in new_board.get_legal_moves():

            player_new_x_position = move[0]
            player_new_y_position = move[1]

            new_board._board[player_new_x_position][player_new_y_position] = 1

            new_board.players_positions[new_board.player_turn] = move
            new_board.player_turn = 1 if new_board.player_turn == 0 else 0
            new_board.step_number += 1

            return new_board
        else:
            print("Invalid move...")
            return new_board

    def get_legal_moves(self):
        """ Return a list of all legal moves available to the
        active player.  Each player should get a list of all
        empty spaces on the board on their first move, and
        otherwise they should get a list of all open spaces
        in a straight line along any row, column or diagonal
        from their current position. (Players CANNOT move
        through obstacles or blocked squares.) Moves should
        be a pair of integers in (column, row) order specifying
        the zero-indexed coordinates on the board.
        """

        possible_moves = []

        if self.step_number == 0 or self.step_number == 1:
            for x in range(BOARD_X_DIM):
                for y in range(BOARD_Y_DIM):
                    if self._board[x][y] == 0:
                        possible_moves.append((x, y))
            return possible_moves

        move_directions = [(-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)]

        for move in move_directions:
            actual_player_position = self.players_positions[self.player_turn]
            keep_moving = True
            new_x_position = actual_player_position[0] + move[0]
            new_y_position = actual_player_position[1] + move[1]
            while keep_moving:
                if new_x_position < 0 or new_x_position >= BOARD_X_DIM:
                    keep_moving = False
                elif new_y_position < 0 or new_y_position >=  BOARD_Y_DIM:
                    keep_moving = False
                elif self._board[new_x_position][new_y_position] == 1:
                    keep_moving = False
                else:
                    possible_moves.append((new_x_position, new_y_position))
                    new_x_position += move[0]
                    new_y_position += move[1]

        return possible_moves