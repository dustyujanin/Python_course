def my_func(s):
    global flag
    sum = 0
    flag = False
    for i in s:
        if i.isdigit():
            sum += int(i)
        if i == "q":
            flag = True
            break
    return sum


total = 0

while True:
    my_list = input("Stroka: ").split()
    total += my_func((my_list))
    print(total)
    if flag:
        break
