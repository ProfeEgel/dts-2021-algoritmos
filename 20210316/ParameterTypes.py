def funcA(value):
    value = 10

n = 5
funcA(n)
print(n)

# **********************************

def funcB(lista):
    #lista = [1, 2, 3, 4, 5]
    lista.clear()
    #lista = []

ext_lista = [0, -5, 4, 7]
funcB(ext_lista)
print(ext_lista)

# **********************************

A = [0, 1, 2, 3]

B = A[:]
B[2] = 55
B.append(77)

print(A)
print(B)
