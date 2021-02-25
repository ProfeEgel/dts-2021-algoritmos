def print_digits_impl(n, digits):
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


print_digits(20)
