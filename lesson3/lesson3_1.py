def my_func(a, b):
    c = a / b
    print(f"c= {c}")


try:
    my_func(int(input("a: ")),int(input("b: ")))
except ZeroDivisionError:
    print('Ups')
