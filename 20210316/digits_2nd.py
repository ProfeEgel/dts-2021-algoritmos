def print_digits_impl(n, digits, result_digits):
    digits.append('0')
    if len(digits) == n:
        # print(''.join(digits))
        result_digits.append(''.join(digits))
    else:
        print_digits_impl(n, digits, result_digits)
    digits.pop()

    digits.append('1')
    if len(digits) == n:
        # print(''.join(digits))
        result_digits.append(''.join(digits))
    else:
        print_digits_impl(n, digits, result_digits)
    digits.pop()


def print_digits(n):
    result_digits = []
    print_digits_impl(n, [], result_digits)
    return result_digits

n = 4
list_digits = print_digits(n)
print(list_digits)
