def my_func(x, y):
    z = x ** y
    return z


def my_func2(x, y):
    z = x
    for i in range(y - 1):
        z = z * x
    return z


a = float(input("x: "))
b = int(input("y: "))
p = my_func(a, b)
p1 = my_func2(a, b)
print(p)
print(p1)
