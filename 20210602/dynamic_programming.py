def factorial(n):
    global call_counter
    call_counter += 1

    if not hasattr(factorial, "mem"):
        factorial.mem = [1, 1]  # stop-values

    if len(factorial.mem) > n:
        return factorial.mem[n]
    else:
        if len(factorial.mem) > n-1:
            f = n * factorial.mem[n-1]
        else:
            f = n * factorial(n - 1)
        factorial.mem.insert(n, f)

        return f


print('\n*** versión recursiva ***')
call_counter = 0
for n in range(20):
    print(f'{n}! = {factorial(n)}')

# 191 llamadas recursivas para n = 20 (sin programación dinámica)
print(f'Se llamó a la función factorial {call_counter} veces')
