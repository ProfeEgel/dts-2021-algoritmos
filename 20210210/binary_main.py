from search_algorithms import *

data = [-11, -5, -3, 0, 1, 4, 7, 8, 9, 10, 14, 16]

n = 9
index = binary_search(data, n)
if index >= 0:
    print(f'{n} se encontró en la posición {index}')
else:
    print('No se encontró el dato')
