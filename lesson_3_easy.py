# utf-8

# Уровень Easy

# Задание-1
# Создайте функцию, принимающую на вход Имя, возраст и город проживания человека
# Функция должна возвращать строку вида "Василий, 21 год(а), проживает в городе Москва"


def person(name, age, city):
    return '{}, {} год(а), проживает в городе {}'.format(name, age, city)

name = input('Введите имя: ')
age = input('Введите возраст: ')
city = input('Введите город: ')

print(person(name, age, city))

# Задание-2
# Создайте функцию, принимающую на вход 3 числа, и возвращающую наибольшее из них

def max_number(a, b, c):
    num = [a, b, c]
    max_num = (max(num))
    return max_num

a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
c = int(input('Введите третье число: '))

print('Максимальное число: {}'.format(max_number(a, b, c)))

# Задание-3
# Создайте функцию, принимающую неограниченное количество строковых аргументов,
# верните самую длинную строку из полученных аргументов

def string(*arg):
    return max(arg, key = len)

print(string('кртк стрк', 'длинная строка', 'очень длинная строка', 'самая-самая длинная строка','самая длинная строка'))