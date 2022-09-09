# 22) Найти сумму чисел списка стоящих на нечетной позиции

def calc_summ(my_list):
    count = 0
    result = 0
    for i in my_list:
        count += 1
        if count % 2 != 0:
            result += i

    return f'Сумма чисел на нечетных позициях списка {my_list} = {result}'


values = [0, 5, 2, 13, 11, 8, 7, 2]
print(calc_summ(values))
