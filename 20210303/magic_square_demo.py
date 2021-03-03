
def magic_square_impl(n, square, pos, used_values, total):
    row = pos // n
    col = pos % n

    for num in range(1, n*n+1):
        if num not in used_values:
            square[row][col] = num
            used_values.add(num)

            if pos == n*n-1:
                # validate magic square
                magic = True
                for i in range(0, n):  # para cada fila
                    sum = 0
                    for j in range(0, n): # suma todas las columnas
                        sum += square[i][j]
                    if sum != total:
                        magic = False
                        break

                if magic is True:
                    for i in range(0, n):  # para cada columna
                        sum = 0
                        for j in range(0, n): # suma todas las filas
                            sum += square[j][i]
                        if sum != total:
                            magic = False
                            break

                if magic is True:
                    sum = 0
                    for i in range(0, n):  # diagonal 1
                        sum += square[i][i]
                    if sum != total:
                        magic = False

                if magic is True:
                    sum = 0
                    for i in range(0, n):  # diagonal 2
                        sum += square[i][n-1-i]
                    if sum != total:
                        magic = False

                if magic is True:
                    print(square)
            else:
                magic_square_impl(n, square, pos + 1, used_values, total)

            used_values.remove(num)

def magic_square(n):
    square = [[0 for i in range(n)] for i in range(n)]
    total = (n * (n*n + 1)) // 2
    magic_square_impl(n, square, 0, set(), total)

n = 3
magic_square(n)
