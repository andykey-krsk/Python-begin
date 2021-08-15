# 7. Реализовать проект «Операции с комплексными числами».
# Создайте класс «Комплексное число», реализуйте перегрузку методов сложения и умножения комплексных чисел.
# Проверьте работу проекта, создав экземпляры класса (комплексные числа) и выполнив сложение и умножение созданных экземпляров.
# Проверьте корректность полученного результата.

class ComplexNumber:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, other):
        sum_r = self.real + other.real
        sum_i = self.imaginary + other.imaginary
        znak = ""
        if sum_i >= 0:
            znak = "+"
        return str(sum_r) + znak + str(sum_i) + "i"

    def __mul__(self, other):
        mult_r = (self.real * other.real) - (self.imaginary * other.imaginary)
        mult_i = (self.real * other.imaginary) + (other.real * self.imaginary)
        znak = ""
        if mult_i >= 0:
            znak = "+"
        return str(mult_r) + znak + str(mult_i) + "i"

    def __str__(self):
        znak = ""
        if self.imaginary >= 0:
            znak = "+"
        return str(self.real) + znak + str(self.imaginary) + "i"


c_num_1 = ComplexNumber(10, 20)
c_num_2 = ComplexNumber(1, -1)
c_num_3 = ComplexNumber(3, 6)

print(c_num_1)
print(c_num_2)
print(c_num_3)

print(f"Сумма {c_num_1} + {c_num_3} = {c_num_1 + c_num_3}")
print(f"Сумма {c_num_1} + {c_num_2} = {c_num_1 + c_num_2}")
print(f"Сумма {c_num_2} + {c_num_3} = {c_num_2 + c_num_3}")

print(f"Произведение {c_num_1} * {c_num_3} = {c_num_1 * c_num_3}")
print(f"Произведение {c_num_1} * {c_num_2} = {c_num_1 * c_num_2}")
print(f"Произведение {c_num_2} * {c_num_3} = {c_num_2 * c_num_3}")
