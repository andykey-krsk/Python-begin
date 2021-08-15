# 5. Продолжить работу над первым заданием.
# Разработать методы, отвечающие за приём оргтехники на склад и передачу в определенное подразделение компании.
# Для хранения данных о наименовании и количестве единиц оргтехники, а также других данных,
# можно использовать любую подходящую структуру, например словарь.

class Storage:
    def __init__(self, name):
        self.name = name
        self.__storage = []

    def add_to_storage(self, unit):
        if unit in self.__storage:
            return
        unit.departament = self.name
        self.__storage.append(unit)

    def storage_to_dep(self, unit, to_dep):
        if (to_dep != "Склад") & (unit in self.__storage):
            self.__storage.remove(unit)
            unit.departament = to_dep
            print(f"{unit.name} с серийным номером: {unit.serial_num} перемещен в подразделение {to_dep}")

    def catlog_of_storage(self):
        print(f"На складе {len(self.__storage)} единиц техники:")
        for i, item in enumerate(self.__storage):
            print(f"{i + 1}. {item.name} серийный номер: {item.serial_num}")


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


unit_1 = Printer("HP", "0001", "Бухгалтерия")
unit_2 = Scaner("Epson", "0002", "Отдел продаж")
unit_3 = Copier("Xerox", "0003", "Склад")

print(unit_1)
unit_1.make_print()
print(unit_2)
unit_2.make_scan()
print(unit_3)
unit_3.make_copy()

storage = Storage("Склад")
storage.add_to_storage(unit_1)
storage.add_to_storage(unit_2)
storage.add_to_storage(unit_3)
storage.catlog_of_storage()

print(unit_1)
print(unit_2)

storage.storage_to_dep(unit_3, "Бухгалтерия")
print(unit_3)
