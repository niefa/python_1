# utf-8

## Уровень Normal

# Задача-1

while True:
    x = int(input('Введите число от 0 до 10: '))

    if x <= 0:
        print('Число должно быть больше 0')
    elif x >= 10:
        print('Число должно быть меньше 10')
    else:
        print(x ** 2)
        break

# Задача-2

a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))

a = a + b
b = a - b
a = a - b

print(a, b)