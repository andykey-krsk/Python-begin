# 7. Создать вручную и заполнить несколькими строками текстовый файл,
# в котором каждая строка будет содержать данные о фирме: название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1   ООО   10000   5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчёт средней прибыли её не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями,
# а также словарь со средней прибылью. Если фирма получила убытки, также добавить её в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
# Подсказка: использовать менеджер контекста.

import json
import os

f_name = "my_file_7.txt"
f_json = "my_file_7.json"

firms_list = []
firms_profit = {}

profit_sum = 0
profit_count = 0

if os.path.exists(f_name):
    with open(f_name, "r", encoding="utf-8") as r_file:
        profit = 0
        for line in r_file:
            content = line.strip("\n").split(" ")
            profit = int(content[2]) - int(content[3])
            firms_profit[content[0]] = profit

            if profit > 0:
                profit_sum += profit
                profit_count += 1

    firms_list.append(firms_profit)
    firms_list.append({"average_profit": round((profit_sum / profit_count), 2)})

    with open(f_json, "w", encoding="utf-8") as w_file:
        json.dump(firms_list, w_file)
else:
    print(f"Файл {f_name} не найден")
