def bubble_sort(array):
    n = len(array)
    for j in range(0, n - 1):
        swap_flag = False

        for i in range(0, n - 1 - j):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                swap_flag = True

        if not swap_flag:
            break


def bubble_sort_generator(array):
    n = len(array)
    for j in range(0, n - 1):
        swap_flag = False

        for i in range(0, n - 1 - j):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                swap_flag = True
                yield array

        if not swap_flag:
            break

    yield array


def bubble_sort_debug(array):
    comparaciones = 0
    intercambios = 0

    n = len(array)
    for j in range(0, n - 1):
        swap_flag = False

        for i in range(0, n - 1 - j):
            comparaciones += 1
            if array[i] > array[i + 1]:
                intercambios += 1
                array[i], array[i + 1] = array[i + 1], array[i]
                swap_flag = True

        if not swap_flag:
            break

        print(f"\n***** PASADA {j}*****")
        print(array)

    print(f"\n comp={comparaciones}, inter={intercambios}")


def selection_sort(array):
    n = len(array)
    for i in range(n - 1):  # pasadas
        jmin = i
        for j in range(i, n):  # búsqueda del mínimo
            if array[j] < array[jmin]:
                jmin = j

        array[i], array[jmin] = array[jmin], array[i]


def selection_sort_generator(array):
    n = len(array)
    for i in range(n - 1):  # pasadas
        jmin = i
        for j in range(i, n):  # búsqueda del mínimo
            if array[j] < array[jmin]:
                jmin = j

        array[i], array[jmin] = array[jmin], array[i]
        yield array

    yield array


def insertion_sort(array):
    n = len(array)
    for i in range(n - 1):  # pasadas
        jmin = i
        for j in range(i, n):  # búsqueda del mínimo
            if array[j] < array[jmin]:
                jmin = j

        aux = array[jmin]
        while jmin > i:
            array[jmin] = array[jmin-1]
            jmin -= 1
        array[i] = aux


def insertion_sort_generator(array):
    n = len(array)
    for i in range(n - 1):  # pasadas
        jmin = i
        for j in range(i, n):  # búsqueda del mínimo
            if array[j] < array[jmin]:
                jmin = j

        aux = array[jmin]
        while jmin > i:
            array[jmin] = array[jmin-1]
            # yield array
            jmin -= 1
        array[i] = aux
        yield array

    yield array
