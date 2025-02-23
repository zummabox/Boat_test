import math
import time


class RowBoat:
    """
    The RowBoat class represents a rowing boat.
    It has coordinates and a direction angle.

    Attributes:
        coordinates: Current coordinates of the boat (x, y).
        angle: Direction angle of the boat in degrees.
    """
    def __init__(self, coordinates=(0, 0), angle=0):
        self.coordinates = coordinates
        self.angle = angle

    def move_forward(self, distance):
        """
        Moves the boat forward by the specified distance.

        Parameters:
            distance: Distance to move the boat.

        Output:
            Updates the boat's coordinates and prints the new coordinates.
        """
        radians = math.radians(self.angle)
        dx = math.cos(radians) * distance
        dy = math.sin(radians) * distance
        x, y = self.coordinates
        self.coordinates = (x + dx, y + dy)
        print(f"Лодка движется вперёд. Новые координаты: {self.coordinates}")

    def turn_left(self, degrees):
        """
        Turns the boat left by the specified angle.

        Parameters:
            degrees: Angle to turn left in degrees.
        """
        self.angle -= degrees

    def turn_right(self, degrees):
        """
        Turns the boat right by the specified angle.

        Parameters:
            degrees (float): Angle to turn right in degrees.
        """
        self.angle += degrees

class Oars:
    """
    The Oars class represents oars with a certain power.

    Attributes:
        power: Power of the oars.
    """
    def __init__(self, power=1):
        self.power = power

    def get_power(self):
        """
        Returns the current power of the oars.

        Returns:
            Power of the oars.
        """
        return self.power


class Rower:
    """
    The Rower class represents a rower with strength and stamina.

    Attributes:
        strength: Strength of the rower.
        stamina: Stamina of the rower.
        tired: Flag indicating if the rower is tired.
    """
    def __init__(self, strength=1, stamina=10):
        self.strength = strength
        self.stamina = stamina
        self.tired = False

    def is_tired(self):
        """
        Checks if the rower is tired.

        Returns:
            bool: True if the rower is tired, otherwise False.
        """
        return self.tired

    def row(self, oars, boat, target_x, target_y):
        """
        Performs a rowing action. Moves the boat towards the target point.

        Parameters:
            oars: Oars object.
            boat: Boat object.
            target_x: X-coordinate of the target.
            target_y: Y-coordinate of the target.

        Output:
            Updates the rower's state and moves the boat.
        """
        if self.tired:
            print("Гребец устал!")
            return 0

        self.stamina -= 1
        if self.stamina == 0:
            self.tired = True
            print("Гребец устал!")

        power = oars.get_power() * self.strength

        current_x, current_y = boat.coordinates
        distance_to_target = math.sqrt((target_x - current_x) ** 2 + (target_y - current_y) ** 2)

        if distance_to_target < power:
            power = distance_to_target

        boat.move_forward(power)

    def rest(self):
        """
        Restores the rower's stamina.

        Output:
            Prints the stamina recovery process.
        """
        while self.stamina < 10:
            self.stamina += 1
            print(f"Гребец восстанавливает силы... {self.stamina}/10")
            time.sleep(0.5)

        self.tired = False
        print("Гребец отдохнул и готов к новым гребкам!")


class BoatController:
    """
    The BoatController class manages the boat, rower, and oars.

    Attributes:
        boat: Boat object.
        rower: Rower object.
        oars: Oars object.
    """
    def __init__(self, boat, rower, oars):
        self.boat = boat
        self.rower = rower
        self.oars = oars

    def calculate_target_angle(self, target_x, target_y):
        """
        Calculates the angle needed to reach the target point.

        Parameters:
            target_x: X-coordinate of the target.
            target_y: Y-coordinate of the target.

        Returns:
            float: Target angle in degrees.
        """
        current_x, current_y = self.boat.coordinates
        dx = target_x - current_x
        dy = target_y - current_y
        return math.degrees(math.atan2(dy, dx))

    def turn_towards_target(self, target_angle):
        """
        Turns the boat towards the target point.

        Parameters:
            target_angle: Target angle in degrees.
        """
        current_angle = self.boat.angle
        angle_diff = target_angle - current_angle

        if abs(angle_diff) < 5:
            self.boat.angle = target_angle
            return

        if angle_diff > 0:
            self.boat.turn_right(10)
        else:
            self.boat.turn_left(10)

        print(f"Лодка поворачивается. Текущий угол: {self.boat.angle}, Целевой угол: {target_angle}")

    def move_to_target(self, target_x, target_y):
        """
        Moves the boat to the target point.

        Parameters:
            target_x: X-coordinate of the target.
            target_y: Y-coordinate of the target.

        Output:
            Prints the process of moving the boat to the target.
        """
        while True:
            target_angle = self.calculate_target_angle(target_x, target_y)
            self.turn_towards_target(target_angle)

            current_x, current_y = self.boat.coordinates
            distance = math.sqrt((current_x - target_x) ** 2 + (current_y - target_y) ** 2)

            if distance < 0.1:
                print("Цель достигнута!")
                break

            current_angle = self.boat.angle
            angle_diff = abs(target_angle - current_angle)
            if angle_diff > 180:
                angle_diff = 360 - angle_diff

            if angle_diff > 5:
                continue

            if not self.rower.is_tired():
                self.rower.row(self.oars, self.boat, target_x, target_y)
                new_x, new_y = self.boat.coordinates
                new_distance = math.sqrt((target_x - new_x) ** 2 + (target_y - new_y) ** 2)

                if new_distance > distance:
                    overshoot_distance = new_distance - distance
                    self.boat.move_forward(overshoot_distance)
                    print("Лодка корректирует положение.")
                    break
            else:
                self.rower.rest()

    def move_forward(self, distance):
        """
        Moves the boat forward by the specified distance.

        Parameters:
            distance: Distance to move the boat.

        Output:
            Updates the boat's coordinates and prints the new coordinates.
        """

        radians = math.radians(self.boat.angle)
        dx = math.cos(radians) * distance
        dy = math.sin(radians) * distance
        x, y = self.boat.coordinates
        new_coordinates = (x + dx, y + dy)

        if new_coordinates == self.boat.coordinates:
            print("Предупреждение: Лодка не двигается! Проверьте угол поворота!")

        self.boat.coordinates = new_coordinates
        print(f"Лодка движется вперёд. Новые координаты: {self.boat.coordinates}")


if __name__ == "__main__":
    # Создаем объекты
    boat = RowBoat(coordinates=(0, 0), angle=0)
    rower = Rower(strength=3, stamina=5)
    oars = Oars(power=2)
    controller = BoatController(boat, rower, oars)

    # Тест 1: Движение к цели
    print("Тест 1: Движение к цели (5, 5)")
    controller.move_to_target(5, 5)

    # Тест 2: Прямолинейное движение
    print("\nТест 2: Прямолинейное движение на 10 итераций")
    controller.move_forward(10)
