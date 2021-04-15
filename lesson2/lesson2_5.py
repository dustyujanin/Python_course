my_list = [7, 5, 3, 3, 2]

while True:
    i = 0
    n = input('Введите натуральное число: ')
    if n.isdigit():
        n=int(n)
        if n == 0:
            break
        for k in my_list:

            if n<=k:
                i += 1
            else:
                index=i
                break
        my_list.insert(i, n)
        print('ВЫ получили новый список: ',my_list)
        print('Для выхода введите 0')
        print('=' * 100)
    else:
        print('Это не похоже на число')


