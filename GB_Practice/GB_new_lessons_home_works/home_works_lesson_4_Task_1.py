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
        elif n % 5 == 0:
            multi_list.append(n // 5)
            n = n // 5
        elif n % 7 == 0:
            multi_list.append(n // 7)
            n = n // 7
        elif n % 9 == 0:
            multi_list.append(n // 9)
            n = n // 9
        else:
            n = n // n

    return print(f'простые множители числа {i} это {multi_list}')


number = int(input('Введите число: '))

print(simple_multiplier(number))
