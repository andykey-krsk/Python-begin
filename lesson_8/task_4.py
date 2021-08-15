# 4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
# А также класс «Оргтехника», который будет базовым для классов-наследников.
# Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определить параметры, общие для приведенных типов.
# В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.

class Storage:
    pass


class Equipment:
    def __init__(self, name, serial_num, departament):
        self.name = name
        self.serial_num = serial_num
        self.departament = departament

    def __str__(self):
        return f"{self.name} {self.serial_num} на ходится в подразделении - {self.departament}"

class Printer(Equipment):
    def make_print(self):
        print("Могу печатать")


class Scaner(Equipment):
    def make_scan(self):
        print("Могу сканировать")


class Copier(Equipment):
    def make_copy(self):
        print("Могу копировать")


printer = Printer("HP", "0001", "Бухгалтерия")
scaner = Scaner("Epson", "0002", "Отдел продаж")
copier = Copier("Xerox", "0002", "Склад")

print(printer)
printer.make_print()
print(scaner)
scaner.make_scan()
print(copier)
copier.make_copy()
