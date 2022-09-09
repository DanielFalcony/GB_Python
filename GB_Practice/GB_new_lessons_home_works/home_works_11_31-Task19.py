# 19) Реализовать алгоритм задания случайных чисел. Без использования встроенного генератора псевдослучайных чисел
from random import choice


def generate(start=0, end=999999):
    sheet_list = []
    for v in range(start, end):
        sheet_list.append(v)
    result = choice(sheet_list)
    return result


print(generate())

