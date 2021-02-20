call_counter = 0

def fibonacci(n):
    global call_counter
    call_counter += 1

    if n == 0 or n == 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


series = [fibonacci(i) for i in range(12)]  # list comprehension
print(series)
print(f'Se llamó a la función fibonacci {call_counter} veces')
