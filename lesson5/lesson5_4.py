rus_list = ['Один', 'Два', 'Три', 'Четыре']
f = open("text_4.txt", "r", encoding="utf-8")
f2 = open("text4_2.txt", 'w', encoding="utf-8")
my_list = [el for el in f]

for i, item in enumerate(my_list):
    p = item.split("-")
    new_line = rus_list[i] + " -" + p[1]
    f2.writelines(new_line)

f.close()
f2.close()
