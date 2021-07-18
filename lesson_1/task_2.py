# 2. Пользователь вводит время в секундах.
# Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.

time_sec = int(input("введите время в секундах: "))
sec = time_sec % 60
min = time_sec // 60
hour = min // 60
min = min % 60

sec = str(sec)

if len(sec) < 2:
    sec = "0" + sec

min = str(min)

if len(min) < 2:
    min = "0" + min

hour = str(hour)

if len(hour) < 2:
    hour = "0" + hour

print(f"{time_sec} секунд равно {hour}:{min}:{sec}")
