def int_func(s):
    new_str = ''
    for i in s:
        new_str = new_str + " " + i.capitalize()
    return new_str


my_str = input("Stroka: ").split()
print(int_func(my_str))
