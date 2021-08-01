# 1. Создать программный файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных будет свидетельствовать пустая строка.
import os

f_name = "my_file.txt"

if os.path.exists(f_name):
    os.remove(f_name)


f = open(f_name, "a")

while True:
    str = input('Введите строку: ')
    if len(str) == 0:
        f.close()
        break
    else:
        str += "\n"
        f.write(str)


f = open(f_name, "r")
content = f.read()
print(f"Содержимое файла {f_name}:")
print(content)
f.close()
