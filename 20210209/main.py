from search_algorithms import *

data = [10, 5, 3, 4, 8, 6, 0, 1]

n = 6
index = linear_search(data, n)
if index >= 0:
    print(f'{n} se encontró en la posición {index}')
else:
    print('No se encontró el dato')

index = linear_search_conditional(data, lambda v: 7 < v < 10)
if index >= 0:
    print(f'{data[index]} se encontró en la posición {index}')
else:
    print('No se encontró el dato')


class Person:
    def __init__(self, fname, lname, age):
        self.fname = fname
        self.lname = lname
        self.age = age

    def __str__(self):
        return f'{self.lname}, {self.fname}. {self.age} year(s)'


data = [
    Person("Jaime", "Aviles", 45),
    Person("Pedro", "Mexican", 32),
    Person("Sidartha", "Bañuelos", 28),
    Person("Erika", "Izquierdo", 39)
]

index = linear_search_conditional(data, lambda p: 25 < p.age < 35)
if index >= 0:
    print(f'{data[index]} se encontró en la posición {index}')
else:
    print('No se encontró el dato')
