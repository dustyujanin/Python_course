# f = open("mytext.txt", 'w')
# my_list = ['fdsfds', 'vv ss', 'ggf  f f']
# for line in my_list:
#     f.writelines(line + '\n')
# f.close()

f = open("mytext.txt", 'r')

mlist = [len(x.rstrip().split()) for x in f if x.rstrip()]
f.close()
for n, l in enumerate(mlist):
    print(f"In {n} line {l} word")
print(f"Total lines: {n + 1}")
