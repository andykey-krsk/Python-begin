# 6. Сформировать (не программно) текстовый файл.
# В нём каждая строка должна описывать учебный предмет и наличие лекционных,
# практических и лабораторных занятий по предмету. Сюда должно входить и количество занятий.
# Необязательно, чтобы для каждого предмета были все типы занятий.
# Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести его на экран.
# Примеры строк файла:  Информатика:   100(л)   50(пр)   20(лаб).
#                       Физика:   30(л)   —   10(лаб)
#                       Физкультура:   —   30(пр)   —
# Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}

import os

f_name = "my_file_6.txt"

my_list = {}

if os.path.exists(f_name):
    with open(f_name, "r", encoding="utf-8") as file:
        for line in file:
            content = line.strip("\n").split(" ")
            sum_hours = 0
            for el in content:
                digit = ''
                for symvol in el:
                    if symvol.isdigit():
                        digit += symvol

                if digit.isdigit():
                    sum_hours += int(digit)

            my_list[content[0].strip(":")] = sum_hours

    print(my_list)
else:
    print(f"Файл {f_name} не найден")
