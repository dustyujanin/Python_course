input_number = input("Введите число: ")
number_1 = int(input_number)
number_2 = int(input_number+input_number)
number_3 = int(input_number+str(number_2))
sum = number_1 + number_2 + number_3

print(f"Сумма {input_number}+{input_number}{input_number}+{input_number}{input_number}{input_number}= ",sum)