def terminal_test(gameState):
    """ Return True if the game is over for the active player
    and False otherwise.
    """
    if len(gameState.get_leagal_moves()) == 0:
        return True
    else:
        return False

def min_value(gameState):
    """ Return the value for a win (+1) if the game is over,
    otherwise return the minimum value over all legal child
    nodes.
    """
    if terminal_test(gameState) == True:
        return 1
    else:
        score = float("inf")
        for action in gameState.get_legal_moves():
            new_board = gameState.forecast_move(action)
            score = min(score, max_value(new_board))
        return score

def max_value(gameState):
    """ Return the value for a loss (-1) if the game is over,
    otherwise return the maximum value over all legal child
    nodes.
    """
    if terminal_test(gameState) == True:
        return -1
    else:
        score = float("-inf")
        for action in gameState.get_legal_moves():
            new_board = gameState.forecast_move(action)
            score = max(score, min_value(new_board))
        return score
