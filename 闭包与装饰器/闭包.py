def func(n):
    def inner_func(m):
        result = m**n
        return result
    return inner_func

f1 = func(2)
print(f1(3))
print(f1(4))

f2 = func(3)
print(f2(3))
print(f2(4))
