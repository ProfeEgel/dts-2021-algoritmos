
def func(n):
    print(hasattr(func,"x"))
    func.x += 1
    return n * n

func(8)
print(func.x)
