"""
Tic Tac Toe Player
"""

import math
import numpy as np
import copy
import sys


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


def Player(board):
    """
    Returns player who has the next turn on a board.
    """
    if board == initial_state():
        return X

    numpyBoard = np.array(board)
    xstepCount = np.count_nonzero(numpyBoard == X)
    ostepCount = np.count_nonzero(numpyBoard == O)

    if xstepCount > ostepCount:
        return O
    else:
        return X
    raise NotImplementedError


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    result = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                result.add((i, j))

    return result
    raise NotImplementedError


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """

    i = action[0]
    j = action[1]

    if board[i][j] != EMPTY:
        raise Exception('Invalid action')

    opponentPlayer = Player(board)
    newBoard = copy.deepcopy(board)
    newBoard[i][j] = opponentPlayer
    return newBoard
    raise NotImplementedError


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for i in range(3):
        # Check horizontally
        if (board[i][0] == board[i][1] == board[i][2]) and board[i][0] != EMPTY:
            return board[i][0]

        # Check vertically
        if (board[0][i] == board[1][i] == board[2][i]) and board[0][i] != EMPTY:
            return board[0][i]

    # Check diagonally
    if ((board[0][0] == board[1][1] == board[2][2]) or (board[0][2] == board[1][1] == board[2][0])) and board[1][1] != EMPTY:
        return board[1][1]

    return None

    raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) != None:
         return True

    numpyBoard = np.array(board)
    emptyCount = np.count_nonzero(numpyBoard == EMPTY)
    if emptyCount == 0:
        return True

    return False

    raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """

    Gamewinner = winner(board)
    if Gamewinner == X:
        return 1

    if Gamewinner == O:
        return -1

    return 0
    raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None

    currentPlayer = Player(board)
    if currentPlayer == X:
        return Maximum(board)[1]
    else:
        return Minimum(board)[1]
    raise NotImplementedError




def Maximum(board):
    if terminal(board):
        return (utility(board), None)

    value = -sys.maxsize-1
    optimalAction = None
    for action in actions(board):
        possibleResult = Minimum(result(board, action))
        if possibleResult[0] > value:
            value = possibleResult[0]
            optimalAction = action

        # Poor Man's Alpha-Beta Pruning
        if value == 1:
            break

    return (value, optimalAction)


def Minimum(board):
    if terminal(board):
        return (utility(board), None)

    value = sys.maxsize
    optimalAction = None
    for action in actions(board):
        possibleResult = Maximum(result(board, action))
        if possibleResult[0] < value:
            value = possibleResult[0]
            optimalAction = action

        # Poor Man's Alpha-Beta Pruning
        if value == -1:
            break

    return (value, optimalAction)