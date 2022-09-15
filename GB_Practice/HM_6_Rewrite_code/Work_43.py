# 43. Дана последовательность чисел. Получить список
#     уникальных элементов заданной последовательности.
#     Пример: [1, 2, 3, 5, 1, 5, 3, 10] => [2, 10]

from random import randint

def create_list(size, m, n):
    return [randint(m, n) for i in range(size)]

def get_unic_value(list):
    result = []
    for i in list:
        if list.count(i) == 1:
            result.append(i)
    return sorted(result)

size = 10
m = 1
n = 10

origin = create_list(size, m, n)
print(origin)
print(get_unic_value(origin))