"""
Tic Tac Toe Player
"""

import math

X = "X"
O = "O"
EMPTY = None

options = []


def initial_state():
    """
    Returns starting state of the board.
    """
    return [["X", EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    #raise NotImplementedError
    return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """

    print("Actions Test!")

    for i in range(3):
        for j in range(3):
            if (board[i][j] == EMPTY):
                #board = ttt.result(board, (i, j))
                print("EMPTY SLOT")
                options.append(tuple((i, j)))


    print("POSSIBLE ACTIONS: " + str(options))

    #raise NotImplementedError


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """

    print("Row: " + str(action[0]))
    print("Column: " + str(action[1]))

    i = action[0]
    j = action[1]

    board[i][j] = player(board)

    return board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    #raise NotImplementedError
    return False

def score(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """

    raise NotImplementedError
