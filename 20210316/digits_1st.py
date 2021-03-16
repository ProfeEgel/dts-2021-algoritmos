def print_digits_impl(n, digits):
    # digits = digits[:]
    digits.append('0')
    if len(digits) == n:
        print(''.join(digits))
    else:
        print_digits_impl(n, digits)
    digits.pop()

    digits.append('1')
    if len(digits) == n:
        print(''.join(digits))
    else:
        print_digits_impl(n, digits)
    digits.pop()


def print_digits(n):
    print_digits_impl(n, [])


import time

time_array = []

for i in range(4, 5):
    start_time = time.time()
    print_digits(i)
    end_time = time.time()
    time_array.append(end_time - start_time)
else:
    print(time_array)
