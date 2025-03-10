1. **Системный уровень**

Тест-кейс 1: Полное движение к цели

Цель: Проверить, что лодка может успешно добраться до заданной точки.

Шаги:
- Создать объекты RowBoat, Rower, Oars и BoatController.
- Установить начальные координаты лодки (0, 0) и угол 0.
- Задать цель (10, 10).
- Вызвать метод move_to_target(10, 10) из BoatController.
- Проверить, что лодка достигла цели с точностью до 0.1.
Ожидаемый результат: Лодка прибывает в точку (10, 10).

Тест-кейс 2: Работа с усталым гребцом

Цель: Проверить, что система корректно обрабатывает усталость гребца.

Шаги:
- Создать объекты RowBoat, Rower (с малой выносливостью), Oars и BoatController.
- Задать цель, которая требует много гребков.
- Вызвать метод move_to_target.
- Проверить, что гребец устал (is_tired == True) и восстанавливается (stamina == 10 после отдыха).
Ожидаемый результат: Гребец отдыхает, когда устает, и продолжает движение.

Тест-кейс 3: Корректировка курса

Цель: Проверить, что лодка корректирует курс, если отклоняется от цели.

Шаги:
- Создать объекты RowBoat, Rower, Oars и BoatController.
- Установить начальные координаты (0, 0) и угол 90 (неправильный курс).
- Задать цель (10, 0).
- Вызвать метод move_to_target.
- Проверить, что лодка поворачивается на правильный угол и достигает цели.
Ожидаемый результат: Лодка корректирует курс и достигает цели.

2. **Интеграционный уровень**

Тест-кейс 1: Взаимодействие лодки и гребца

Цель: Проверить, что гребец правильно управляет лодкой.

Шаги:
- Создать объекты RowBoat, Rower и Oars.
- Вызвать метод row у гребца с целью (10, 0).
- Проверить, что лодка перемещается на расстояние, равное силе гребца.
- Проверить, что выносливость гребца уменьшается.
Ожидаемый результат: Лодка двигается, а выносливость гребца снижается.

Тест-кейс 2: Взаимодействие контроллера и лодки

Цель: Проверить, что контроллер правильно рассчитывает угол поворота.

Шаги:
- Создать объекты RowBoat и BoatController.
- Установить начальные координаты (0, 0) и угол 0.
- Задать цель (10, 10).
- Вызвать метод calculate_target_angle.
- Проверить, что возвращенный угол соответствует ожидаемому значению.
Ожидаемый результат: Угол рассчитывается правильно.

Тест-кейс 3: Взаимодействие весел и гребца

Цель: Проверить, что мощность весел учитывается при расчете расстояния.

Шаги:
- Создать объекты Rower и Oars с разной мощностью.
- Вызвать метод row с одинаковой целью.
- Проверить, что лодка перемещается на разные расстояния в зависимости от мощности весел.
Ожидаемый результат: Расстояние пропорционально мощности весел.

3. **Функциональный уровень**

Тест-кейс 1: Перемещение лодки

Класс: RowBoat

Метод: move_forward

Шаги:
- Создать объект RowBoat с начальными координатами (0, 0) и углом 0.
- Вызвать метод move_forward(10).
- Проверить, что новые координаты равны (10, 0).
Ожидаемый результат: Координаты обновляются корректно.

Тест-кейс 2: Поворот лодки

Класс: RowBoat

Методы: turn_left, turn_right

Шаги:
- Создать объект RowBoat с начальным углом 0.
- Вызвать метод turn_left(90).
- Проверить, что угол стал -90.
- Вызвать метод turn_right(180).
- Проверить, что угол стал 90.
Ожидаемый результат: Угол изменяется корректно.

Тест-кейс 3: Получение мощности весел

Класс: Oars

Метод: get_power

Шаги:
- Создать объект Oars с мощностью 2.
- Вызвать метод get_power.
- Проверить, что возвращаемое значение равно 2.
Ожидаемый результат: Мощность возвращается корректно.

Тест-кейс 4: Усталость гребца

Класс: Rower

Метод: row

Шаги:
- Создать объект Rower с выносливостью 1.
- Вызвать метод row несколько раз.
- Проверить, что гребец устал (is_tired == True).
Ожидаемый результат: Гребец устает после нескольких гребков.