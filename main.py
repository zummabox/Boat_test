import math


class RowBoat:
    def __init__(self, coordinates=(0, 0), speed=0):
        self.coordinates = coordinates #Координаты лодки
        self.speed = speed #Скорость лодки
        self.angle = 0  # Угол направления (0° — прямое движение)
        self.left_oar = True #Наличие левого весла
        self.right_oar = True #Наличие правого весла


    def move_forward(self):
        radians = math.radians(self.angle) #Переводим градус в радианы
        dx = math.cos(radians) * self.speed #Расчет смещения по X
        dy = math.sin(radians) * self.speed #Расчет смещения по Y
        x, y = self.coordinates
        self.coordinates = (x + dx, y + dy) #Обновление координат
        print(f"Лодка движется вперёд. Новые координаты: {self.coordinates}")

    def row_speed(self):
        if self.speed < 5:
            self.speed += 1  # Увеличиваем скорость, пока не достигним максимального значения
        print(f"Скорость лодки: {self.speed}")

    def move_of_oars(self, left_oar: bool, right_oar: bool):
        if left_oar and right_oar:
            self.angle = 0
            print("Оба весла работают → лодка движется прямо")
        elif left_oar:
            self.angle += 90  # Поворот вправо
            print("Работает только левое весло → лодка поворачивает вправо")
        elif right_oar:
            self.angle -= 180  # Поворот влево
            print("Работает только правое весло → лодка поворачивает влево")
        else:
            print("Ошибка: ни одно весло не работает")

        print(f"Текущий угол: {self.angle}°")


boat = RowBoat()

boat.row_speed()
boat.move_forward()

boat.move_of_oars(left_oar=True, right_oar=False)  # Левое весло → вправо
boat.move_forward()

boat.move_of_oars(left_oar=False, right_oar=True)  # Правое весло → влево
boat.move_forward()

boat.move_of_oars(left_oar=True, right_oar=True)  # Оба весла → прямо
boat.move_forward()