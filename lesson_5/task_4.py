# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Напишите программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

import os

f_name = "my_file_4.txt"
f_name_2 = "my_file_4_1.txt"

eng_rus = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}

if os.path.exists(f_name):
    f = open(f_name_2, "w", encoding="utf-8")
    with open(f_name, "r", encoding="utf-8") as file:
        for line in file:
            content = line.strip("\n").split(" ")
            f.write(eng_rus[content[0]] + " - " + content[2] + "\n")

    f.close()
else:
    print(f"Файл {f_name} не найден")
