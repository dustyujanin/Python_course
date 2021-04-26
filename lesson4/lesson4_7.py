def fact(n):
    t = 1
    for i in range(1,n+1):
        t*=i
        yield t

n=int(input("Factorial chisla: "))

for el in fact(n):
    print(f"{el}")