# utf-8

# Задание-1:
# Дан список, заполненный произвольными целыми числами.
# Получить новый список, элементы которого будут
# квадратами элементов исходного списка
# [1, 2, 4, 0] --> [1, 4, 16, 0]

import random

def random_numbers(count):
    numbers = [random.randint(-100, 100) for _ in range(count)]
    return numbers

numbers = random_numbers(5)
roots = [i ** 0.5 for i in numbers if i >= 0]

print(numbers)
print(roots)

# Задание-2:
# Даны два списка фруктов.
# Получить список фруктов, присутствующих в обоих исходных списках.

fruits_1 = ['яблоко', 'апельсин', 'ананас', 'груша', 'киви', 'грейпфрут']
fruits_2 = ['яблоко', 'груша', 'гранат', 'манго', 'киви', 'грейпфрут']

fruits_final = list(set(fruits_1) & set(fruits_2))

print(fruits_final)

# Задание-3:
# Дан список, заполненный произвольными числами.
# Получить список из элементов исходного, удовлетворяющих следующим условиям:
# + Элемент кратен 3
# + Элемент положительный
# + Элемент не кратен 4

numbers = random_numbers(20)
a = [i for i in numbers if i > 0 and i % 3 == 0 and i % 4 != 0]

print(numbers)
print(a)


