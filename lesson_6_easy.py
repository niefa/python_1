# Задача - 1
# Опишите несколько классов TownCar, SportCar, WorkCar, PoliceCar
# У каждого класса должны быть следующие аттрибуты:
# speed, color, name, is_police - Булево значение.
# А так же несколько методов: go, stop, turn(direction) - которые должны сообщать,
#  о том что машина поехала, остановилась, повернула(куда)

class TownCar:

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('Городской автомобиль поехал')

    def stop(self):
        print('Городской автомобиль остановился')

    def turn(self, direction):
        print('Городской автомобиль повернул {}'.format(direction))


class SportCar:

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('Спортивный автомобиль поехал')

    def stop(self):
        print('Спортивный автомобиль остановился')

    def turn(self, direction):
        print('Спортивный автомобиль повернул {}'.format(direction))


class WorkCar:

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('Рабочий автомобиль поехал')

    def stop(self):
        print('Рабочий автомобиль остановился')

    def turn(self, direction):
        print('Рабочий автомобиль повернул {}'.format(direction))


class PoliceCar:

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('Полицейский автомобиль поехал')

    def stop(self):
        print('Полицейский автомобиль остановился')

    def turn(self, direction):
        print('Полицейский автомобиль повернул {}'.format(direction))


# Задача - 2
# Посмотрите на задачу-1 подумайте как выделить общие признаки классов
# в родительский и остальные просто наследовать от него.

class Car:

    def __init__(self, speed, color, name, is_police = False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police


class TownCar(Car):

    def go(self):
        print('Городской автомобиль поехал')

    def stop(self):
        print('Городской автомобиль остановился')

    def turn(self, direction):
        print('Городской автомобиль повернул {}'.format(direction))


class SportCar(Car):

    def go(self):
        print('Спортивный автомобиль поехал')

    def stop(self):
        print('Спортивный автомобиль остановился')

    def turn(self, direction):
        print('Спортивный автомобиль повернул {}'.format(direction))


class WorkCar(Car):

    def go(self):
        print('Рабочий автомобиль поехал')

    def stop(self):
        print('Рабочий автомобиль остановился')

    def turn(self, direction):
        print('Рабочий автомобиль повернул {}'.format(direction))


class PoliceCar(Car):

    def go(self):
        print('Полицейский автомобиль поехал')

    def stop(self):
        print('Полицейский автомобиль остановился')

    def turn(self, direction):
        print('Полицейский автомобиль повернул {}'.format(direction))


my_car = TownCar('60', 'серый', 'личный')
work_car = WorkCar('80', 'серый', 'рабочий')
police_car = PoliceCar('120', 'белый', 'полицейский', True)

my_car.go()
work_car.stop()
police_car.turn('налево')