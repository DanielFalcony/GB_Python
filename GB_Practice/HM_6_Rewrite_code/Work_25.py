# 25. Написать программу преобразования десятичного числа в двоичное


def dicimal_to_binary(number):
    result = ''
    while number > 0:
        result = str(number % 2) + result
        number = number // 2

    return f'Число {values} в двоичном коде = {result}'


values = int(input('Введите число:'))
print(dicimal_to_binary(values))
