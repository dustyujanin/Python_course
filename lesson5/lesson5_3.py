f = open("text_3.txt", "r", encoding="utf-8")
my_list = [el for el in f]
print('Мало получают: ')
sum = 0
for item in my_list:
    p = item.split()
    sum += float(p[1])
    if float(p[1]) < 20000:
        print(p[0])
med = sum / len(my_list)

print(f"Средняя зарплата {med}")
f.close()
