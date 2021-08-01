# 1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
# Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы:
# красный, желтый, зеленый. Продолжительность первого состояния (красный) составляет 7 секунд,
# второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение.
# Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
# Проверить работу примера, создав экземпляр и вызвав описанный метод.
# Задачу можно усложнить, реализовав проверку порядка режимов,
# и при его нарушении выводить соответствующее сообщение и завершать скрипт.

from time import sleep
from time import monotonic
from itertools import cycle


class TrafficLight:
    __color = None
    __color_state = {'Красный': 7, 'Желтый': 2, 'Зеленый': 10}
    switch = False
    manual = True

    def running(self):
        if self.switch:
            for color, time in cycle(self.__color_state.items()):
                if self.manual:
                    print("Включено ручное управление")
                    break

                self.__color = color
                self.shine(self.__color, time)
                self.set_timer(time)
                print('')
        else:
            print(f"Светофор выключен")

    def shine(self, color, time):
        print(f"У всетофора горит {color}, будет гореть {time} сек.", end=" ")

    def set_switch(self):
        if self.switch:
            self.switch = False
            print(f"Светофор выключен")
        else:
            self.switch = True
            print(f"Светофор включен")

    def set_manual(self, color):
        self.manual = True
        self.__color = color
        self.shine(self.__color, self.__color_state[color])

    def set_auto(self):
        self.manual = False
        print(f"Светофор работает в автоматическом режиме")
        self.running()

    def set_timer(self, second):
        # sleep(second)
        t = monotonic()
        while second >= 1:
            if monotonic() - t > 1:
                t = monotonic()
                print(second, end=" ")
                second -= 1


traffic_light = TrafficLight()
traffic_light.running()
traffic_light.set_switch()
traffic_light.running()
# traffic_light.set_manual('Зеленый')
traffic_light.set_auto()
