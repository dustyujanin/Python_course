while True:
    month = int(input('Введите число от 1 до 12: '))
    if month <= 0 or month > 12:
        print('Кажется, такого месяца не существует')
    else:
        break
# Решение задачи через list

list_season = [[12, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11]]
i = 0
for x in list_season:
    if month in list_season[i]:
        break
    i += 1
if i == 0:
    print('Вы ввели зимний месяц')
elif i == 1:
    print('Весна на дворе')
elif i == 2:
    print('Ура! лето!')
else:
    print('Осень настала!')

# Решение задачи через dict
dict_season = {'Зима': (1, 2, 12),
               'Весна': (3, 4, 5),
               'Лето': (6, 7, 8),
               'Осень': (9, 10, 11)}
for k in dict_season.keys():
    if month in dict_season[k]:
        print(f"На дворе {k}")
        break
