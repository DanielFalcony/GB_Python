"""
Task 24

Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и
минимальным значением дробной части элементов.

Пример:

- [1.1, 1.2, 3.1, 5, 10.01] => 0.19
"""


def fractional(my_list):
    maximum = 0
    minimum = 0
    for v in my_list:
        current = (v % 1)
        if maximum == 0 and minimum == 0:
            maximum = current
            minimum = current
        elif current > maximum:
            maximum = current
        elif current < minimum and current != 0:
            minimum = current

    result = maximum - minimum

    return f'В списке {my_list}, min:{minimum:.2f}, max:{maximum:.2f} их разница = {result:.2f}'


values = [1.1, 1.2, 3.1, 5, 10.01]
print(fractional(values))
