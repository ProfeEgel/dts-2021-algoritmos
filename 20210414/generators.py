def generator1():
    yield 1
    yield 2
    yield 3


def generator2():
    j = 0
    while j < 10:
        yield j
        j = j + 1


def my_range(n):
    j = 0
    while j < n:
        yield j
        j = j + 1


def fibonacci(n):
    i = 0
    fib = 1
    fib_1 = 0

    while i < n:
        if i == 0 or i == 1:
            yield i

        fib_new = fib + fib_1
        yield fib_new
        fib_1 = fib
        fib = fib_new
        i = i + 1


for i in fibonacci(10):
    print(i)
