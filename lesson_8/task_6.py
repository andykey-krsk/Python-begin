# 6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
# Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
# Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей,
# изученных на уроках по ООП.
import copy
from itertools import cycle


class StoregeError(Exception):
    def __init__(self, text):
        self.text = text

    def __str__(self):
        return self.text


class AddStorageError(StoregeError):
    def __init__(self, text):
        self.text = f"Невозможно добавить оборудование на склад:\n {text}\n"


class TransferStorageError(StoregeError):
    def __init__(self, text):
        self.text = f"Невозможно передать оборудование в подразделение:\n {text}\n"


class Storage:
    def __init__(self, name):
        self.name = name
        self.__storage = []

    def add_to_storage(self, unit: "Equipment"):
        try:
            if not isinstance(unit, Equipment):
                raise AddStorageError(f"{unit} не оргтехника")
            if unit in self.__storage:
                return
            unit.departament = self.name
            self.__storage.append(unit)
        except StoregeError as e:
            print(e)

    def storage_to_dep(self, unit: "Equipment", to_dep):
        try:
            if to_dep == "Склад":
                raise TransferStorageError(f"{unit} уже на складе!")
            if not unit in self.__storage:
                raise TransferStorageError(f"{unit} нет на складе!")
            self.__storage.remove(unit)
            unit.departament = to_dep
            print(f"{unit.name} с серийным номером: {unit.serial_num} перемещен в подразделение {to_dep}")

        except TransferStorageError as e:
            print(e)

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


class Human:
    pass


unit_1 = Printer("HP", "9999", "Бухгалтерия")
unit_2 = Scaner("Epson", "8888", "Отдел продаж")
unit_3 = Copier("Xerox", "7777", "Приёмная")

human = Human()

teh_list = [Printer("HP", "0000", "магазин"), Scaner("Epson", "0000", "магазин"), Copier("Xerox", "0000", "магазин")]

storage = Storage("Склад")
count = 1
for temp in cycle(teh_list):
    unit = copy.deepcopy(temp)
    num = str(count).rjust(4, '0')
    unit.serial_num = num
    storage.add_to_storage(unit)
    print(unit)
    count += 1
    if count == 100:
        break

storage.add_to_storage(unit_1)
storage.add_to_storage(unit_2)
storage.add_to_storage(unit_3)
storage.add_to_storage(human)
storage.catlog_of_storage()

print(unit_1)
print(unit_2)

storage.storage_to_dep(unit_3, "Бухгалтерия")
print(unit_3)
