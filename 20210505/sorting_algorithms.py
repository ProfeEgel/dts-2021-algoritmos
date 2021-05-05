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


def insertion_sort_2(array):
    n = len(array)
    for i in range(n - 1):  # pasadas
        jmin = i
        for j in range(i, n):  # búsqueda del mínimo
            if array[j] < array[jmin]:
                jmin = j

        aux = array[jmin]
        while jmin > i:
            array[jmin] = array[jmin - 1]
            jmin -= 1
        array[i] = aux


def insertion_sort_2_generator(array):
    n = len(array)
    for i in range(n - 1):  # pasadas
        jmin = i
        for j in range(i, n):  # búsqueda del mínimo
            if array[j] < array[jmin]:
                jmin = j

        aux = array[jmin]
        while jmin > i:
            array[jmin] = array[jmin - 1]
            # yield array
            jmin -= 1
        array[i] = aux
        yield array

    yield array


def insertion_sort(array):
    n = len(array)
    for i in range(1, n):  # pasadas
        value = array[i]
        j = i
        while j > 0 and array[j - 1] > value:
            array[j] = array[j - 1]
            j = j - 1

        array[j] = value


def insertion_sort_generator(array):
    n = len(array)
    for i in range(1, n):  # pasadas
        value = array[i]
        j = i
        while j > 0 and array[j - 1] > value:
            array[j] = array[j - 1]
            yield array
            j = j - 1

        array[j] = value
        yield array

    yield array


def quicksort_impl(array, lo, hi):
    if lo < hi:
        pivote = hi
        hi = hi - 1

        i = lo
        j = hi
        while i < j:
            while array[i] < array[pivote] and i < pivote:
                i += 1
            while array[j] > array[pivote] and j > 0:
                j -= 1
            if i < j:
                array[i], array[j] = array[j], array[i]

        if array[pivote] < array[i]:
            array[pivote], array[i] = array[i], array[pivote]

        quicksort_impl(array, lo, j)
        quicksort_impl(array, i + 1, pivote)


def quicksort(array):
    return quicksort_impl(array, 0, len(array) - 1)


def quicksort_impl_generator(array, lo, hi):
    if lo < hi:
        pivote = hi
        hi = hi - 1

        i = lo
        j = hi
        while i < j:
            while array[i] < array[pivote] and i < pivote-1:
                i += 1
            while array[j] >= array[pivote] and j > 0:
                j -= 1
            if i < j:
                array[i], array[j] = array[j], array[i]
                yield array

        if array[pivote] < array[i]:
            array[pivote], array[i] = array[i], array[pivote]
            yield array

        yield from quicksort_impl_generator(array, lo, j)
        yield from quicksort_impl_generator(array, i + 1, pivote)

    yield array


def quicksort_generator(array):
    yield from quicksort_impl_generator(array, 0, len(array) - 1)
