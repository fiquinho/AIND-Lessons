from minimax_helpers import *


def minimax_decision(gameState):
    """ Return the move along a branch of the game tree that
    has the best possible value.  A move is a pair of coordinates
    in (column, row) order corresponding to a legal move for
    the searching player.

    You can ignore the special case of calling this function
    from a terminal state.
    """

    best_score = float("-inf")
    best_move = None

    for action in gameState.get_legal_moves():
        new_board = gameState.forecast_move(action)
        score = min_value(new_board)
        if score > best_score:
            best_score = score
            best_move = action

    return best_move

