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


def linear_search_object(data, condition):
    for i in range(len(data)):
        if condition(data[i]):
            return i
    else:
        return -1
