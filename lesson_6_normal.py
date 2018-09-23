# # Задача - 1
# # Ранее мы с вами уже писали игру, используя словари в качестве
# # структур данных для нашего игрока и врага, давайте сделаем новую, но уже с ООП
# # Опишите базовый класс Person, подумайте какие общие данные есть и у врага и у игрока
# # Не забудьте, что у них есть помимо общих аттрибутов и общие методы.
# # Теперь наследуясь от Person создайте 2 класса Player, Enemy.
# # У каждой сущности должы быть аттрибуты health, damage, armor
# # У каждой сущности должно быть 2 метода, один для подсчета урона, с учетом брони противника,
# # второй для атаки противника.
# # Функция подсчета урона должна быть инкапсулирована
# # Вам надо описать игровой цикл так же через класс.
# # Создайте экземпляры классов, проведите бой. Кто будет атаковать первым оставляю на ваше усмотрение.

import random

class Person:

    def __init__(self, name, health, damage, armor):
        self.name = name
        self.health = health
        self.damage = damage
        self.armor = armor


    def _damage(self, damage):
        if self.armor > 0:
            self.armor = self.armor - int(damage)
            if self.armor <= 0:
                self.armor = 0
        else:
            self.health = self.health - int(damage)
            if self.health <= 0:
                self.health = 0

        print('{} пропустил удар, и теперь у него {} здоровья и {} жизней'.format(self.name, self.health, self.armor))


    def attack(self, person):
        person._damage(self.damage)


class Player(Person):
    pass


class Enemy(Person):
    pass


class Fight:
    def __init__(self, person_1, person_2):
        self.person_1 = person_1
        self.person_2 = person_2

    def start(self, person_1, person_2):
        while person_1.health > 0 and person_2.health > 0:
            person_1.attack(person_2)
            if person_2.health == 0:
                print('{} победил!'.format(person_1.name))
                break
            person_2.attack(person_1)
            if person_1.health == 0:
                print('Зло восторжествовало!')


player = Player('Доблестный герой', 100, random.randint(5, 10), random.randint(100, 200))
enemy = Enemy('Богомерзкий злодей', 100, random.randint(5, 10), random.randint(100, 200))

new_fight = Fight(player, enemy)
new_fight.start(player, enemy)