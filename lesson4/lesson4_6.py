import itertools

try:
    x = int(input("Enter start digit: "))
    y = int(input("Enter number of digits: "))
except ValueError:
    print("Not digit!!!")

for i in itertools.islice(itertools.count(x), y):
    print(i)

my_list = input("Enter your list: ").split()
print(my_list)
len = int(input("Enter the number of cycles: "))
for item in itertools.cycle(my_list):
    len -= 1
    print(item)
    if len < 1:
        break
