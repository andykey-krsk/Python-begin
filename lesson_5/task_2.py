# 2. Создать текстовый файл (не программно), сохранить в нём несколько строк,
# выполнить подсчёт строк и слов в каждой строке.

import os

f_name = "my_file_2.txt"

if os.path.exists(f_name):
    f = open(f_name, "r", encoding="utf-8")
    content = f.readlines()
    f.close()

    print(f"Строк в файле {f_name} - {len(content)}")

    for i, line in enumerate(content):
        words = len(line.split(' '))
        print(f"Строка {i + 1} - {words} слов")
else:
    print(f"Файл {f_name} не найден")


