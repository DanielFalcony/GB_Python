"""
Task 1

Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.


"""


def simple_multiplier(i):
    n = i
    multi_list = [n]
    while n != 1:
        if n % 2 == 0:
            multi_list.append(n // 2)
            n = n // 2
        elif n % 3 == 0:
            multi_list.append(n // 3)
            n = n // 3
        else:
            multi_list.append(n // n)
            n = n // n

    return print(f'простые множители числа {i} это {multi_list}')


number = int(input('Введите число: '))

print(simple_multiplier(number))
