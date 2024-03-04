"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    
    # Loop the board to check the number of X and O
    x_count = 0
    o_count = 0

    for row in range(3):
        for col in range(3):
            if board[row][col] == X:
                x_count += 1
            elif board[row][col] == O:
                o_count += 1

    # If the number of X is greater than O, then it is O's turn
    # Otherwise it is X's turn, also when the board is empty, cause X start
    if (x_count > o_count):
        return O
    else:
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """

    # Create a set to store the possible actions
    possible_actions = set()

    # Loop through the board to check for empty cells
    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col] == EMPTY:
                possible_actions.add((row, col))

    return possible_actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    
    # Check if the action is valid
    possible_actions = actions(board)

    if action not in possible_actions:
        raise Exception("Invalid action")
    
    row, col = action
    copy_board = copy.deepcopy(board)
    copy_board[row][col] = player(board)

    return copy_board


def check_row(board, player):
    """
    Check if the player has 3 in a row
    """
    for row in range(len(board)):
        if board[row][0] == player and board[row][1] == player and board[row][2] == player:
            return True

    return False


def check_col(board, player):
    """
    Check if the player has 3 in a column
    """
    for col in range(len(board[0])):
        if board[0][col] == player and board[1][col] == player and board[2][col] == player:
            return True

    return False


def check_diag(board, player):
    """
    Check if the player has 3 in a diagonal
    """
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True

    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
        return True

    return False


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """

    if check_row(board, X) or check_col(board, X) or check_diag(board, X):
        return X
    elif check_row(board, O) or check_col(board, O) or check_diag(board, O):
        return O

    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """

    # Check if there is a winner
    if winner(board):
        return True

    # If there is no specific winner, check if the board is full
    if len(actions(board)) != 0:
        return False

    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """

    # Check if there is a winner
    winner_player = winner(board)
    print(f"Utility winning player: {winner_player}")

    if winner_player == X:
        return 1
    elif winner_player == O:
        return -1
    
    return 0


def max_value(board):
    value = -math.inf

    # Check if recursion gives a terminal board
    if (terminal(board)):
        return utility(board)
    
    possible_actions = actions(board)
    for action in possible_actions:
        new_board = result(board, action)

        # Maxamizing player action that produces the lowest value of min_value
        value = max(value, min_value(new_board))

    return value


def min_value(board):
    value = math.inf

    # Check if recursion gives a terminal board
    if (terminal(board)):
        return utility(board)
    
    possible_actions = actions(board)
    for action in possible_actions:
        new_board = result(board, action)

        # Minimizing player action that produces the highest value of max_value
        value = min(value, max_value(new_board))

    return value


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """

    current_player = player(board)
    possible_actions = actions(board)
    plays = []

    if terminal(board):
        return None

    elif current_player == X:
        for action in possible_actions:
            value = min_value(result(board, action))
            plays.append([value, action])
    
    elif current_player == O:
        for action in possible_actions:
            value = max_value(result(board, action))
            plays.append([value, action])

    # Return the action with the lowest value
    print(f"Plays: {plays}")
    return sorted(plays, key=lambda x: x[0])[0][1]

