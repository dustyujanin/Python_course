x = input('Введите слова, разделенные пробелами: ')
x_list = x.split()
i = 1
for word in x_list:
    print(f"{i} : {word[:10]}")
    i += 1
