# utf-8

# Уровень Easy

# Задача-1

fruits = ('яблоко', 'банан', 'киви', 'арбуз')

for index, name in enumerate(fruits):
    print('{}. {}'.format(index + 1, name))

# Задача-2

a = [1, 2, 3, 4, 5]
b = [1, 2, 3]

for name in b:
    a.remove(name)

print(a)

# Задача-3

list = [1, 2, 3, 4, 5, 6, 7, 8]
new_list = []

for i in list:
    if i % 2 == 0:
        new_list.append(i / 4)
    else:
        new_list.append(i * 2)

print(new_list)