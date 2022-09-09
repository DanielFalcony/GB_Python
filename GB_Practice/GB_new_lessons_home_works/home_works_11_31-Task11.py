# 11) Сформировать список из  N членов последовательности. Для N = 5: 1, -3, 9, -27, 81 и т.д.

n = int(input("Введите N: "))


def calc(val):
    if val == 1:
        return 1
    else:
        return (-3) * calc(val - 1)


numbers_list = []

for i in range(1, n + 1):
    numbers_list.append(calc(i))

print(f'Последовательность чисел от 1 до {n}: {numbers_list}')
