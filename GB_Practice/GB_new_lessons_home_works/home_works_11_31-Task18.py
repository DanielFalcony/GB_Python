# # 18) Реализовать алгоритм перемешивания списка.
from random import randint


def randomize(new_list, val):
    for i in range(val - 1, 0, -1):
        j = randint(0, i + 1)
        new_list[i], new_list[j] = new_list[j], new_list[i]
    return new_list


my_list = [1, 2, 3, 4, 5, 6, 7, 8]
n = len(my_list)
print(randomize(my_list, n))
