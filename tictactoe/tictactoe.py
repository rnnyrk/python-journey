"""
Tic Tac Toe Player
"""

import math

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

    for i in range(3): # Loop through the rows
        for j in range(3): # Loop through the columns
            if board[i][j] == X:
                x_count += 1
            elif board[i][j] == O:
                o_count += 1

    print(f"X: {x_count}, O: {o_count}")

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
    for i in range(3): # Loop through the rows
        for j in range(3): # Loop through the columns
            if board[i][j] == EMPTY:
                possible_actions.add((i, j))

    return possible_actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    
    # Check if the action is valid
    possible_actions = actions(board)

    if action not in possible_actions:
        raise Exception("Invalid action")
    
    # Get the current player
    current_player = player(board)

    # Update the new board with the action
    new_board = board[:]
    new_board[action[0]][action[1]] = current_player

    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """

    return False
    # raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    raise NotImplementedError
