"""
Task 27

Строка содержит набор чисел. Показать большее и меньшее число

Символ-разделитель - пробел

"""


def numbers_min_max(number):
    min = 0
    max = 0
    for i in number:
        if i.isdigit():
            i = int(i)
            if min == 0 and max == 0:
                min = i
                max = i
            if i < min:
                min = i
            elif i > max:
                max = i

    return f'В наборе чисел {number}, самое большое число = {max}, самое маленькое = {min}'


str_number = '12 7 85 6 2 3 4 8 1 0 12'
print(numbers_min_max(str_number))
