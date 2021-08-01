# 3. Создать текстовый файл (не программно).
# Построчно записать фамилии сотрудников и величину их окладов (не менее 10 строк).
# Определить, кто из сотрудников имеет оклад менее 20 тысяч, вывести фамилии этих сотрудников.
# Выполнить подсчёт средней величины дохода сотрудников.
# Пример файла:
# Иванов 23543.12
# Петров 13749.32

import os

f_name = "my_file_3.txt"
min_salary = 20000

persons = {}

if os.path.exists(f_name):
    with open(f_name, "r", encoding="utf-8") as file:
        for i, line in enumerate(file):
            content = line.strip("\n").split(' ')
            persons[content[0]] = float(content[1])

    count_persons = len(persons)

    print(f"Всего сотрудников - {count_persons}")

    sum_salary = 0

    for person, salary in persons.items():
        sum_salary += salary
        if salary<min_salary:
            print(f"{person} - {salary} рублей")

    print(f"Средняя зарплата - {round((sum_salary / count_persons), 2)} рублей")
else:
    print(f"Файл {f_name} не найден")
