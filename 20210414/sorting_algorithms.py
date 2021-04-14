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
