import random
my_list=[random.randint(1,10) for _ in range(10)]
new_list=[]
print(f"Исходный список {my_list}")
l=len(my_list)
for i in range(l):
    n=0
    for el in my_list:
        if el == my_list[i]:
            n+=1
    if n<2:
        new_list.append(my_list[i])

print(f"Новый список {new_list}")
