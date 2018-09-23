# Задача - 1
# Вам необходимо создать завод по производству мягких игрушек для детей.
# Вам надо продумать структуру классов,
# чтобы у вас был класс, который создает игрушки на основании:
#  Названия, Цвета, Типа (животное, персонаж мультфильма)
# Опишите процедуры создания игрушки в трех методах:
# -- Закупка сырья, пошив, окраска
# Не усложняйте пусть методы просто выводят текст о том, что делают.
# В итоге ваш класс по производству игрушек должен вернуть объект нового класса Игрушка.

class Toy:

    def __init__(self, name, color, group):
        self.name = name
        self.color = color
        self.group = group


class Fabric:

    def making(self):
        print('...закупаем сырье...')
        print('...шьем...')
        print('...окрашиваем...')
        print('Изготовлена новая игрушка: {}, цвет {}, тип {}'.format(self.name, self.color, self.group))


name = input('Введите название игрушки: ')
color = input('Введите цвет игрушки: ')
group = input('Введите тип игрушки: ')


Fabric.making(Toy(name, color, group))


# Задача - 2
# Доработайте нашу фабрику, создайте по одному классу на каждый тип, теперь надо в классе фабрика
# исходя из типа игрушки отдавать конкретный объект класса, который наследуется от базового - Игрушка

class Toy:

    def __init__(self, name, color, group):
        self.name = name
        self.color = color
        self.group = group


class Animal(Toy):
    def __init__(self, name, color):
        Toy.__init__(self, name, color, 'животное')


class Character(Toy):
    def __init__(self, name, color):
        Toy.__init__(self, name, color, 'персонаж')


class Fabric:
    def making(self):
        print('...закупаем сырье...')
        print('...шьем...')
        print('...окрашиваем...')
        print('Изготовлена новая игрушка: {}, цвет {}, тип {}'.format(self.name, self.color, self.group))


name = input('Введите название игрушки: ')
color = input('Введите цвет игрушки: ')
group_number = input('Выберите тип игрушки: \n'
              '1 - животное \n'
              '2 - персонаж \n')


if group_number == '1':
    Fabric.making(Animal(name, color))
elif group_number == '2':
    Fabric.making(Character(name, color))