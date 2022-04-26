for percent in range(1, 101):
    number_remain = percent % 10
    number_integer = percent // 10

    if number_integer == 0 and number_remain == 1:
        print(f'{percent} процент')
    elif number_integer >= 2 and number_remain == 1:
        print(f'{percent} процент')
    elif number_integer >= 1 and number_remain == 0:
        print(f'{percent} процентов')
    elif number_integer == 0 and 2 <= number_remain <= 4:
        print(f'{percent} процента')
    elif number_integer >= 2 and 2 <= number_remain <= 4:
        print(f'{percent} процента')
    elif number_integer == 0 and 5 <= number_remain <= 9:
        print(f'{percent} процентов')
    elif number_integer >= 2 and 5 <= number_remain <= 9:
        print(f'{percent} процентов')
    elif number_integer == 1 and 1 <= number_remain <= 9:
        print(f'{percent} процентов')
    else:
        print('что-то пошло не так...')
