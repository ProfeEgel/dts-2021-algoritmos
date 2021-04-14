
def bubble_sort(array):
    comparaciones = 0
    intercambios = 0

    n = len(array)
    for j in range(0, n-1):
        swap_flag = False

        for i in range(0, n-1-j):
            comparaciones += 1
            if array[i] > array[i+1]:
                intercambios += 1
                array[i], array[i+1] = array[i+1], array[i]
                swap_flag = True

        if not swap_flag:
            break

        print(f"\n***** PASADA {j}*****")
        print(array)

    print(f"\n comp={comparaciones}, inter={intercambios}")


data = [7, 5, 9, 11, 0, 3, 1, 8]
# data = [0, 1, 3, 5, 7, 8, 9, 11]
# data = [11, 9, 8, 7, 5, 3, 1, 0]
bubble_sort(data)

print("\n***** SORTED *****")
print(data)
