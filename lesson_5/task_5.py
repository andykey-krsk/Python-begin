# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделённых пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить её на экран.

from random import randint

f_name = "my_file_5.txt"
# nums = []
# for el in range(30):
#     nums.append(str(randint(1, 100)))

nums = [(lambda el: str(randint(1, 100)))(el) for el in range(30)]

f = open(f_name, "w")
f.write(" ".join(nums))
f.close()

f = open(f_name, "r")
content = f.read().split(" ")

nums_sum = 0

for el in content:
    nums_sum += int(el)

print(f"Сумма чисел в файле - {f_name} = {nums_sum}")
