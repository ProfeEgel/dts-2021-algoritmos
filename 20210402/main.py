def linear_search(data, n):     # O(n)
    for i in range(len(data)):  # n
        if data[i] == n:        # 1
            return i            # 1
    else:                       # 1
        return -1               # 1


data = [10, 5, 3, 4, 8, 6, 0, 1]

n = 6
index = linear_search(data, n)
if index >= 0:
    print(f'{n} se encontró en la posición {index}')
else:
    print('No se encontró el dato')
