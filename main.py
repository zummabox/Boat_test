import math
import time
from asyncio import current_task


class RowBoat:
    def __init__(self, coordinates=(0, 0), angle=0):
        self.coordinates = coordinates
        self.angle = angle

    def move_forward(self, distance):
        radians = math.radians(self.angle)
        dx = math.cos(radians) * distance
        dy = math.sin(radians) * distance
        x, y = self.coordinates
        self.coordinates = (x + dx, y + dy)
        print(f"Лодка движется вперёд. Новые координаты: {self.coordinates}")


    def turn_left(self, degrees):
        self.angle -= degrees

    def turn_right(self, degrees):
        self.angle += degrees

class Oars:
    def __init__(self, power=1):
        self.power = power

    def get_power(self):
        return self.power


class Rower:
    def __init__(self, strength=3, stamina=10):
        self.strength = strength
        self.stamina = stamina
        self.tired = False

    def is_tired(self):
        return self.tired

    def row(self, oars):
        if self.tired:
            print("Гребец устал!")
            return 0

        self.stamina -= 1
        if self.stamina == 0:
            self.tired = True
            print("Гребец устал!")

        return oars.get_power() * self.strength

    def rest(self):
        while self.stamina < 10:
            self.stamina += 1
            print(f"Гребец восстанавливает силы... {self.stamina}/10")
            time.sleep(1)

        self.tired = False
        print("Гребец отдохнул и готов к новым гребкам!")


class BoatController:
    def __init__(self, boat, rower, oars):
        self.boat = boat
        self.rower = rower
        self.oars = oars

    def calculate_target_angle(self, target_x, target_y):
        current_x, current_y = self.boat.coordinates
        dx = target_x - current_x
        dy = target_y - current_y
        return math.degrees(math.atan2(dy, dx))

    def turn_towards_target(self, target_angle):
        current_angle = self.boat.angle
        angle_diff = target_angle - current_angle

        if angle_diff > 180:
            angle_diff -= 360
        elif angle_diff < -180:
            angle_diff += 360

        if angle_diff > 0:
            self.boat.turn_left(5)
        elif angle_diff < 0:
            self.boat.turn_right(5)

    def move_to_target(self, target_x, target_y):
        while True:
            target_angle = self.calculate_target_angle(target_x, target_y)

            self.turn_towards_target(target_angle)

            current_x, current_y = self.boat.coordinates
            distance = math.sqrt((current_x - target_x) ** 2 + (current_y - target_y) ** 2)
            if distance < 0.1:
                print("Цель достигнута!")
                break

            if not self.rower.is_tired():
                power = self.rower.row(oars)
                self.boat.move_forward(power)
            else:
                self.rower.rest()

    def move_forward(self, ticks):
        for _ in range(ticks):
            if not self.rower.is_tired():
                power = self.rower.row(self.oars)
                self.boat.move_forward(power)
            else:
                self.rower.rest()



# Создаем объекты
boat = RowBoat(coordinates=(0, 0), angle=0)
rower = Rower(strength=3, stamina=5)
oars = Oars(power=2)
controller = BoatController(boat, rower, oars)

# Двигаем лодку вперед на 10 итераций
controller.move_forward(10)