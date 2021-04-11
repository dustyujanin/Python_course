sec_time = int(input("Введите время в секундах: "))
hour = sec_time // 3600
minutes = (sec_time//60)%60
seconds = sec_time%60

if hour < 10:
    hour = str("0" + str(hour))
if minutes < 10:
    minutes = str("0"+str(minutes))
if seconds < 10:
    seconds = str("0"+str(seconds))

print(f"Вы ввели {hour}:{minutes}:{seconds} секунд")

