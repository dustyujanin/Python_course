f = open('mytext.txt', 'w')
while True:
    my_str = input("Enter your data:")
    f.write(my_str + "\n")
    print("Done")
    if my_str == "":
        break
f.close()
