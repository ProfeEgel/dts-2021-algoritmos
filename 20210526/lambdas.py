def cube(n):
    return n * n * n

def apply_function(data, function):
    return function(data)

print(cube(5))
print(apply_function(8, cube))
print(apply_function(8, lambda n: n * n * n))
print(apply_function(8, lambda n: n**2 + 5))
print(apply_function(8, lambda n: n*(n-1)))
