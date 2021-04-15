mylist = []
while True:
    mylist_len = int(input('Введите кол-во элементов списка: '))
    if mylist_len <= 0:
        print('Маловато будет')
    else:
        break
i = 0
t = 1
while i < mylist_len:

    c = input(f'Введи {i} значение: ')
    mylist.append(c)
    i += 1
    if i % 2 == 0:
        mylist[i - 2], mylist[i - 1] = mylist[i - 1], mylist[i - 2]

print('Исходный список ', mylist)
