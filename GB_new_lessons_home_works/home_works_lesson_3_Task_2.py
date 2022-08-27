"""
Task 2

Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент,
второй и предпоследний и т.д.

Пример:

- [2, 3, 4, 5, 6] => [12, 15, 16];
- [2, 3, 5, 6] => [12, 15]
"""
import math


def calc_summ(my_list):
    count = 0
    back_count = -1
    result = []
    while count < math.ceil(len(my_list) / 2):
        result.append(my_list[count] * my_list[back_count])
        count += 1
        back_count -= 1

    return result


values = [2, 3, 5, 6, 8, 2, 7, 2, 5]
print(calc_summ(values))
