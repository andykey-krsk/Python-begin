# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.

def my_func(num_1, num_2, num_3):
    max_1 = num_1
    if max_1 > num_2:
        max_2 = num_2
    else:
        max_1 = num_2
        max_2 = num_1

    if max_2 < num_3:
        max_2 = num_3

    return max_1 + max_2


args = input('введите три числа, разделенные пробелами: ').split(' ')

print(my_func(float(args[0]), float(args[1]), float(args[2])))

