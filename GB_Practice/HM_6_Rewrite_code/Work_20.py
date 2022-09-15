# 20. Определить, присутствует ли в заданном списке строк некоторое число

from random import randint
import itertools

def search(args, val):
    if str(val) in args:
        return f'Значение {str(val)} присутсвует в списке {args}'
    else:
        return f'Значение {str(val)} отсутсвует в списке {args}'


list_new = ['abw', '213', 'bbe', 'ler3at']
v = input(f'Введите значение для поиска для поиска по списку:\n'
          f'{list_new}\n'
          f'-->: ')

print(search(list_new, v))


# Нахождение числа во вложенном списке

# def get_list(raw, col, frst, last):
#     return [[randint(frst, last) for j in range(col)] for i in range(raw)]
#
#
# def find_number(n, mylist):
#     return n in list(itertools.chain(*mylist))
#
#
# raw = 6
# col = 2
# frst = 4
# last = 100
# mylist = get_list(raw, col, frst, last)
#
# print(mylist)
# n = int(input(('Введите число: ')))
# print(find_number(n, mylist))