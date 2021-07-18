# 4. Пользователь вводит целое положительное число.
# Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.

n = input("введите целое положительное число: ")

count = 0
max = 0
count_max = 0

while count < len(n):
    if max < int(n[count]):
        max = int(n[count])
        count_max = count + 1

        if max == 9:
            break

    count += 1

print(f"{max} - это самая большая цифра в числе {n}, находится на {count_max} месте")
