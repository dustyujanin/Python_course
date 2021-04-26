ed = ['1:шт', '2:кг', '3:л']
my_list = []
my_dict = []
my_result = dict({})
i = 0

while True:
    i += 1
    print('1.Добавить товар')
    print('2.Посмотреть аналитику')
    print('3.Выход')
    x = int(input("Введите команду: "))
    if x == 3:
        break

    if x == 1:
        name = input('Введите название: ')
        price = int(input('Введите цену: '))
        quan = int(input('Введите кол-во: '))
        while True:
            l = int(input(f'Выберите единицы измерения {ed} : '))
            if l == 1:
                edin = ed[0]
                break
            elif l == 2:
                edin = ed[1]
                break
            elif l == 3:
                edin = ed[2]
                break
            else:
                break
        my_list.append((i, dict({"название": name, "цена": price, "количество": quan, "ед": edin})))

    if x == 2:
        print('Аналитика')
        print("Исходная структура: ",my_list)

        for prod in my_list:
            for key, value in prod[1].items():
                if key in my_result:
                    if value not in my_result.get(key):
                        my_result.get(key).append(value)
                else:
                    my_result.update({key: [value]})

        print("Аналитика: ",my_result)
