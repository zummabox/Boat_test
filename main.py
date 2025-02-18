import math
import time


class RowBoat:
    def __init__(self, coordinates=(0, 0), speed=0):
        self.coordinates = coordinates
        self.speed = speed
        self.angle = 0

    def move_forward(self):
        radians = math.radians(self.angle)
        dx = math.cos(radians) * self.speed
        dy = math.sin(radians) * self.speed
        x, y = self.coordinates
        self.coordinates = (x + dx, y + dy)
        print(f"Лодка движется вперёд. Новые координаты: {self.coordinates}")

    def increase_speed(self, row_power):
        self.speed += row_power * 0.5
        print(f"Скорость лодки увеличена до {self.speed}")


    def move_of_oars(self, left_oar: bool, right_oar: bool):
        if left_oar and right_oar:
            self.angle = 0
            print("Оба весла работают → лодка движется прямо")
        elif left_oar:
            self.angle += 15  # Поворот вправо
            print("Работает только левое весло → лодка поворачивает вправо")
        elif right_oar:
            self.angle -= 15  # Поворот влево
            print("Работает только правое весло → лодка поворачивает влево")
        else:
            print("Ошибка: ни одно весло не работает")

        print(f"Текущий угол: {self.angle}°")

class Oars:
    def __init__(self, power=1, frequency=1):
        self.row_power = power
        self.row_frequency = frequency

    def set_row_power(self, power: int):
        self.row_power = power
        print(f"Сила гребка установлена на {self.row_power}")

    def set_row_frequency(self, frequency: int):
        self.row_frequency = frequency
        print(f"Частота гребка установлена на {self.row_frequency}")


class Rower:
    def __init__(self, strength=3, stamina=10):
        self.strength = strength
        self.stamina = stamina
        self.tired = False

    def operate_oars(self, oars: Oars, boat: RowBoat):
        if self.tired:
            print("Гребец слишком устал и не может грести.")
            return

        oars.set_row_power(self.strength)
        boat.increase_speed(oars.row_power)

        self.reduce_stamina()

    def reduce_stamina(self):
        self.stamina -= 1
        print(f"Выносливость гребца: {self.stamina}")

        if self.stamina == 0:
            self.tired = True
            print("Гребец устал и больше не может грести!")

    def rest(self):
        while self.stamina < 10:
            self.stamina += 1
            print(f"Гребец восстанавливает силы... {self.stamina}/10")
            time.sleep(1)

        self.tired = False
        print("Гребец отдохнул и готов к новым гребкам!")


# === Тестирование ===

boat = RowBoat()
oars = Oars()
rower = Rower(strength=3, stamina=5)

for _ in range(6):  # Попробуем 6 раз грести
    rower.operate_oars(oars, boat)
    boat.move_forward()

if rower.stamina == 0:  # Если гребец устал, даём ему отдохнуть
    rower.rest()

rower.operate_oars(oars, boat)  # После отдыха продолжаем грести
boat.move_forward()