# 19. Реализовать алгоритм задания случайных чисел.
# Без использования встроенного генератора псевдослучайных чисел

import datetime

min_n = 10
max_n = 100

def get_rand():
    return datetime.datetime.now().microsecond%10

n = get_rand()

print(n)

