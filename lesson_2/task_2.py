# 2. Для списка реализовать обмен значений соседних элементов, т.е.
# Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().

list_len = int(input('Введите размер списка: '))

i = 0
list_data = []

while i < list_len:
    list.append(list_data, input(f'Введите {i}-й элемент списка: '))
    i += 1

print(f'Было - {list_data}')

i = 0

while i < list_len:
    if i + 2 > list_len:
        break
    temp = list_data[i]
    list_data[i] = list_data[i + 1]
    list_data[i + 1] = temp
    i += 2

print(f'Стало - {list_data}')
