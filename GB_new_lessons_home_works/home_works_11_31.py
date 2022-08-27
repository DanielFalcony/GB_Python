# 11) Сформировать список из  N членов последовательности. Для N = 5: 1, -3, 9, -27, 81 и т.д.

# n = int(input("Введите N: "))
#
#
# def calc(val):
#     if val == 1:
#         return 1
#     else:
#         return (-3) * calc(val - 1)
#
#
# numbers_list = []
#
# for i in range(1, n + 1):
#     numbers_list.append(calc(i))
#
# print(f'Последовательность чисел от 1 до {n}: {numbers_list}')


# 12) Для натурального n создать словарь индекс-значение, состоящий из элементов последовательности 3n + 1.
# Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

# n = 6
# result = {val: (3*val + 1) for val in range(1, n + 1)}
# print(result)

# 13) Пользователь задаёт две строки. Определить количество вхождений одной строки в другой.

# string1 = 'Привет, как у тебя дела? Это первая строка!'
# string2 = 'Привет, дела у меня хорошо! Это вторая строка!'
#
# string1_hub = ""
# string2_hub = ""
#
# for i in string1:
#     if i.isalpha() or i.isspace():
#         string1_hub += i
#
# for i in string2:
#     if i.isalpha() or i.isspace():
#         string2_hub += i
#
# string1_hub = string1_hub.split(' ')
# string2_hub = string2_hub.split(' ')
#
# result = 0
#
# for i in string1_hub:
#     if i in string2_hub:
#         result += 1
#
# print(result)

# 14) Подсчитать сумму цифр в вещественном числе.

# num_one = 1.234
# num_one = str(num_one)
# num_one = num_one.replace(".", "")
# sum_num = 0
# for el in num_one:
#     sum_num += int(el)
#
# print(sum_num)

# 15) Написать программу получающую набор произведений чисел от 1 до N.
# Пример: пусть N = 4, тогда
# [ 1, 2, 6, 24 ]
# import random
#
# n = 4
#
#
# def calc(n):
#     if n == 1:
#         return n
#     else:
#         return n * calc(n - 1)
#
#
# n_list = []
#
# for v in range(1, n + 1):
#     n_list.append(calc(v))
#
# print(f"Произведения чисел от 1 до {n}:  {n_list}")

# 16) -Задать список из n чисел последовательности (1+1n)n и вывести на экран их сумму



# 17) -Задать список из N элементов, заполненных числами из [-N, N]. Найти произведение элементов на указанных позициях.
# Позиции хранятся в файле file.txt в одной строке одно число

# # 18) Реализовать алгоритм перемешивания списка.
# from random import randint
#
#
# def randomize(new_list, n):
#     for i in range(n - 1, 0, -1):
#         j = randint(0, i + 1)
#         new_list[i], new_list[j] = new_list[j], new_list[i]
#     return new_list
#
#
# new_list = [1, 2, 3, 4, 5, 6, 7, 8]
# n = len(new_list)
# print(randomize(new_list, n))

# 19) Реализовать алгоритм задания случайных чисел. Без использования встроенного генератора псевдослучайных чисел
from random import choice


def generate(start=0, end=999999):
    sheet_list = []
    for v in range(start, end):
        sheet_list.append(v)
    result = choice(sheet_list)
    return result


print(generate())

# 20) Определить, присутствует ли в заданном списке строк, некоторое число
