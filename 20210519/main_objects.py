import json


def bubble_sort(array, comparer):
    n = len(array)
    for j in range(0, n - 1):
        swap_flag = False

        for i in range(0, n - 1 - j):
            if comparer(array[i], array[i + 1]):  # array[i] > array[i + 1]
                array[i], array[i + 1] = array[i + 1], array[i]
                swap_flag = True

        if not swap_flag:
            break


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
    Person("Erika", "Izquierdo", 39),
    Person("Juan", "Pérez", 18),
    Person("Martha", "Montañez", 25)
]

# bubble_sort(data, lambda pA, pB: pA.age > pB.age)
bubble_sort(data, lambda pA, pB: pA.lname > pB.lname)
for p in data:
    print(p)
