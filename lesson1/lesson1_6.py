km_1 = int(input('Введите кол-во км в первый день: '))
km_max = int(input("Введите максимальное кол-во км : "))
day=1
km=km_1
while km<=km_max:
    km*=1.1
    day+=1

print(f"На {day}й день спорстмен достиг результата не менее {km_max} км")