import sys

try:
    print(int(sys.argv[1]) * int(sys.argv[2]) + int(sys.argv[3]))

except IndexError:
    print("Нужно вводить аргументы")
except ValueError:
    print("Надо число")
