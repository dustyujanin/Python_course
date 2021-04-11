value = int(input("Введите выручку вашей фирмы: "))
cost = int(input("Введите издержки вашей фирмы: "))
if value > cost :
    profit = value-cost
    rent = int((profit/value)*100)
    print(f"Вы работаете с прибылью  {profit} рублей")
    print(f"Ваша рентабельность {rent} %")
else:
    print("Плохи дела")