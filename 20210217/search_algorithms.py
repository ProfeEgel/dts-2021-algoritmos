def linear_search(data, n):  # O(n)
    for i in range(len(data)):
        if data[i] == n:
            return i
    else:
        return -1


def linear_search_conditional(data, condition):
    for i in range(len(data)):
        if condition(data[i]):
            return i
    else:
        return -1


# def linear_searchall_conditional(data, condition):
#     result_data = []
#     for i in range(len(data)):
#         if condition(data[i]):
#             result_data.append(data[i])
#
#     return result_data

def linear_searchall_conditional(data, condition):
    return [e for e in data if condition(e)]

def binary_search(data, n):
    # iter = 0
    low, high = 0, len(data) - 1
    while high >= low:
        # iter = iter + 1
        mid = (low + high) // 2

        if data[mid] == n:
            # print(f'{iter} iteracion(es)')
            return mid
        elif n > data[mid]:
            low = mid + 1
        else:
            high = mid - 1
    else:
        # print(f'{iter} iteracion(es)')
        return -1
