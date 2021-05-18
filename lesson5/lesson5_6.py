f = open("text_6.txt", "r", encoding="utf-8")
my_dict = {}
my_list = f.readlines()
print(my_list)
my_dict = {}
for item in my_list:
    x = item.split(":")[0]
    y = item.split(":")[1].split()
    new_list = []
    sum_n = 0
    for i in y:
        newstr = ''.join((ch if ch in '0123456789' else ' ') for ch in i)
        try:
            sum_n += int(newstr)
        except ValueError:
            pass

    my_dict[x] = sum_n
print(my_dict)
f.close()
