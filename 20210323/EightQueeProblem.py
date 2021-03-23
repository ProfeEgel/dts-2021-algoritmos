def print_board(board, n):
    for i in range(n):
        fila = ""
        if i == 0:
            # techo de la fila 0
            for j in range(n):
                if j == 0:
                    fila += "╔═══"
                else:
                    fila += "╦═══"
            fila += "╗"
            print(fila)

            # valores de la fila 0
            fila = ""
            for j in range(n):
                if board[i][j] == 1:
                    fila += "║ Q "
                else:
                    fila += "║   "
            fila += "║"
            print(fila)

        else:
            # techo de la fila i>0
            for j in range(n):
                if j == 0:
                    fila += "╠═══"
                else:
                    fila += "╬═══"
            fila += "╣"
            print(fila)

            # valores de la fila i>0
            fila = ""
            for j in range(n):
                if board[i][j] == 1:
                    fila += "║ Q "
                else:
                    fila += "║   "
            fila += "║"
            print(fila)

    # últimotecho
    fila = ""
    for j in range(n):
        if j == 0:
            fila += "╚═══"
        else:
            fila += "╩═══"
    fila += "╝"
    print(fila)

    # for i in range(len(board)):
    #    print(board[i])


def validate_position(board, n, row, col):
    # validate rows
    sum = 0
    for j in range(n):
        sum += board[row][j]
    if sum > 1:
        return False

    # validate columns
    sum = 0
    for i in range(n):
        sum += board[i][col]
    if sum > 1:
        return False

    # validate main diagonal
    # sum = 0
    # i = row-1
    # j = col-1
    # while (i >= 0) and (j >= 0):
    #     sum += board[i][j]
    #     i, j = i-1, j-1
    #
    # i = row
    # j = col
    # while (i < n) and (j < n):
    #     sum += board[i][j]
    #     i, j = i+1, j+1
    #
    # if sum > 1:
    #     return False

    # validate direct diagonal
    i = row
    j = col
    while (i > 0) and (j > 0):
        i, j = i - 1, j - 1

    sum = 0
    while (i < n) and (j < n):
        sum += board[i][j]
        i, j = i + 1, j + 1

    if sum > 1:
        return False

    # validate inverse diagonal
    i = row
    j = col
    while (i < n - 1) and (j > 0):
        i, j = i + 1, j - 1

    sum = 0
    while (i >= 0) and (j < n):
        sum += board[i][j]
        i, j = i - 1, j + 1

    if sum > 1:
        return False

    return True


def NQueenProblemImpl(n, board, col):
    if col == n:
        print("*********************************")
        print_board(board, n)
    else:
        for row in range(n):
            board[row][col] = 1
            if validate_position(board, n, row, col):
                NQueenProblemImpl(n, board, col + 1)
            board[row][col] = 0


def NQueenProblem(n):
    board = [[0 for i in range(n)] for i in range(n)]
    NQueenProblemImpl(n, board, 0)


n = 8
NQueenProblem(n)
