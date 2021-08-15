# 2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
# Проверьте его работу на данных, вводимых пользователем.
# При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту ситуацию
# и не завершиться с ошибкой.

class DivByZero(Exception):
    def __init__(self, numerator, divider):
        self.divider = numerator
        self.denominator = divider

    @staticmethod
    def div_by_zero(numerator, divider):
        try:
            return (numerator / divider)
        except:
            return (f"Нельзя делить на ноль")


numerator = float(input("Введите знаменатель: "))
divider = float(input("Введите делитель: "))

print(DivByZero.div_by_zero(numerator, divider))
