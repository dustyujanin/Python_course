import random

new_list = []
my_list = [random.randint(5, 50) for _ in range(10)]
l = len(my_list)
i = 0
print(f"Исходный список {my_list}")

for _ in my_list:
    if my_list[i + 1] > my_list[i]:
        new_list.append(my_list[i + 1])
    if i >= l - 2:
        break
    i += 1
print(f"Сгенерированный список {new_list}")
