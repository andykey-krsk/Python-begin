# 6. Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же,
# но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
# Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом.
# Каждое слово состоит из латинских букв в нижнем регистре. Сделать вывод исходной строки,
# но каждое слово должно начинаться с заглавной буквы. Необходимо использовать написанную ранее функцию int_func().

def int_func_1(str):
    return str.capitalize()


print(int_func_1('text'))


def int_func_2(str):
    words = str.split(' ')
    for i, word in enumerate(words):
        words[i] = int_func_1(word)
    return ' '.join(words)


print(int_func_2('text text'))


# Универсальный вариант
def int_func_3(str):
    words = str.split(' ')
    for i, word in enumerate(words):
        words[i] = word.capitalize()
    return ' '.join(words)


print(int_func_3('text'))

print(int_func_3('text text'))
