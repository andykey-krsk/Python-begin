# 2. Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
# Значения данных атрибутов должны передаваться при создании экземпляра класса.
# Атрибуты сделать защищенными. Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
# Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв метра дороги асфальтом,
# толщиной в 1 см * число см толщины полотна. Проверить работу метода.
# Например: 20м * 5000м * 25кг * 5см = 12500 т

class Road:
    __weight_of_square_meter = 25
    __thickness = 5

    def __init__(self, width, length):
        self.__width = width
        self.__length = length

    def get_weight_of_road(self):
        return self.__length * self.__width * self.__weight_of_square_meter * self.__thickness

    def weight_in_ton(self):
        return str(self.__length * self.__width * self.__weight_of_square_meter * self.__thickness/1000) + " тонн"


my_road = Road(20,5000)
print(my_road.get_weight_of_road())
print(my_road.weight_in_ton())
