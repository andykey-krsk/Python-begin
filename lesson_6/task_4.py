# 4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.


class Car:
    speed = 0

    def __init__(self, color, name, is_police):
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self, speed):
        self.speed = speed
        print(f"Поехали!")
        print(f"Автомобиль {self.name}, цвет - {self.color}")
        print(f"Скорость {self.speed} км/ч")

    def stop(self):
        print("Стоп машина")

    def turn(self, direction):
        print(f"Поворот {direction}")

    def show_speed(self):
        print(f"Скорость {self.speed} км/ч")


class PoliceCar(Car):
    pass


class SportCar(Car):
    pass


class TownCar(Car):
    def show_speed(self):
        print(f"Скорость {self.speed} км/ч")
        if self.speed > 60:
            print(f"Превышение скорости на {self.speed - 60} км/ч")


class WorkCar(Car):
    def show_speed(self):
        print(f"Скорость {self.speed} км/ч")
        if self.speed > 40:
            print(f"Превышение скорости на {self.speed - 40} км/ч")


my_police_car = PoliceCar("Синий", "Волга", True)
my_police_car.go(70)
my_police_car.turn("налево")
my_police_car.turn("направо")
my_police_car.speed = 80
my_police_car.show_speed()
my_police_car.stop()

my_sport_car = SportCar("Красный", "Ферари", False)
my_sport_car.go(120)
my_sport_car.turn("налево")
my_sport_car.turn("направо")
my_sport_car.speed = 200
my_sport_car.show_speed()
my_sport_car.stop()

my_town_car = TownCar("Белый", "Хонда", False)
my_town_car.go(50)
my_town_car.turn("налево")
my_town_car.turn("направо")
my_town_car.speed = 80
my_town_car.show_speed()
my_town_car.stop()

my_work_car = WorkCar("Желтый", "Газель", False)
my_work_car.go(30)
my_work_car.turn("налево")
my_work_car.turn("направо")
my_work_car.speed = 60
my_work_car.show_speed()
my_work_car.stop()
