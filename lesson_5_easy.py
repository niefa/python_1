# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

import os
import sys
print('sys.argv = ', sys.argv)


def create_dir(dir_name):
    try:
        os.mkdir(dir_name)
    except FileExistsError:
        print('Невозможно создать')


def delete_dir(dir_name):
    try:
        os.rmdir(dir_name)
    except FileNotFoundError:
        print('Невозможно удалить')


for i in range(1, 10):
    create_dir('dir_' + str(i))

for i in range(1, 10):
    delete_dir('dir_' + str(i))


# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

# Функция для Normal

def show_dir_list():
    list = os.listdir()
    for i in list:
        print(i)


dir_list = next(os.walk('.'))[1]

for i in dir_list:
    print(i)


# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

import shutil

file_name = sys.argv[0]
name, ext = file_name.split('.')
shutil.copy(file_name, '{}_dupl.{}'.format(name, ext))