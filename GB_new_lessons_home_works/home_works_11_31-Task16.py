# 16) -Задать список из n чисел последовательности (1+1n)n и вывести на экран их сумму

def n_summ(n):
    my_list = []
    my_list1 = []
    for n in range(1, n + 1):
        my_list.append(n)
        for i in my_list:
            my_list1.append((1 + 1 / i) ** i)

    return sum(my_list1)


n = 5
print(n_summ(n))
