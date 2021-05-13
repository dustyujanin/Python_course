import json

f = open("text_7.txt", "r", encoding="utf-8")
my_list = f.readlines()
print(my_list, ' ', len(my_list))
i = 0
total = 0
my_dict = {}
my_dict2 = {}
for item in my_list:
    f_name = item.split(' ')[0]
    revenue = int(item.split(' ')[2])
    cost = int(item.split(' ')[3])
    profit = revenue - cost
    my_dict[f_name] = profit
    if profit > 0:
        i += 1
        total += profit
    print(f_name, profit)
med_profit = total / i
my_dict2['average_profit'] = med_profit

final_list = [my_dict, my_dict2]
print(final_list)

with open("my_json.json", "w", encoding="utf-8") as my_json:
    json.dump(final_list, my_json)
