# n! = n*(n-1)*(n-2)*...*2*1
# 6! = 6*5*4*3*2*1
# 3! = 3*2*1
# 1! = 1
# 0! = 1

# versión iterativa
def factorial_iter(n):
    global call_counter
    call_counter += 1

    fact = 1
    for i in range(1, n + 1):
        fact *= i

    return fact


print('*** versión iterativa ***')
call_counter = 0
for n in range(10):
    print(f'{n}! = {factorial_iter(n)}')

print(f'Se llamó a la función factorial {call_counter} veces')


def factorial_rec(n):
    global call_counter
    call_counter += 1

    if n == 1 or n == 0:
        return 1
    else:
        return n * factorial_rec(n - 1)


print('\n*** versión recursiva ***')
call_counter = 0
for n in range(6):
    print(f'{n}! = {factorial_rec(n)}')

print(f'Se llamó a la función factorial {call_counter} veces')
