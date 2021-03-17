import os

def print_board(board):
    for i in range(len(board)):
        print(board[i])


def validate_position(row, col):
    return True


def NQueenProblemImpl(n, board, col):
    if col == n:
        print("*********************************")
        print_board(board)
    else:
        for row in range(n):
            board[row][col] = 1
            if validate_position(row, col):
                NQueenProblemImpl(n, board, col+1)
            board[row][col] = 0


def NQueenProblem(n):
    board = [[0 for i in range(n)] for i in range(n)]
    NQueenProblemImpl(n, board, 0)


n = 4
NQueenProblem(n)
