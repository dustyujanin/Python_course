f = open("text_5.txt", "w", encoding="utf-8")
my_list = [1, 5, 8, 9, 11]
for i in my_list:
    print(i, file=f, end=' ')
f.close()

f = open("text_5.txt", "r", encoding="utf-8")
new_list = f.readline().split()

print(f"SUM: {sum([int(item) for item in new_list])}")
f.close()
