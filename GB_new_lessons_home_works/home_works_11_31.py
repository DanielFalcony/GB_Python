# 11) Сформировать список из  N членов последовательности. Для N = 5: 1, -3, 9, -27, 81 и т.д.

# n = int(input("Введите N: "))
#
#
# def calc(val):
#     if val == 1:
#         return 1
#     else:
#         return (-3) * calc(val - 1)
#
#
# numbers_list = []
#
# for i in range(1, n + 1):
#     numbers_list.append(calc(i))
#
# print(f'Последовательность чисел от 1 до {n}: {numbers_list}')


# 12) Для натурального n создать словарь индекс-значение, состоящий из элементов последовательности 3n + 1.
# Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

# n = 6
# result = {val: (3*val + 1) for val in range(1, n + 1)}
# print(result)

# 13) Пользователь задаёт две строки. Определить количество вхождений одной строки в другой.

# string1 = 'Привет, как у тебя дела? Это первая строка!'
# string2 = 'Привет, дела у меня хорошо! Это вторая строка!'
#
# string1_hub = ""
# string2_hub = ""
#
# for i in string1:
#     if i.isalpha() or i.isspace():
#         string1_hub += i
#
# for i in string2:
#     if i.isalpha() or i.isspace():
#         string2_hub += i
#
# string1_hub = string1_hub.split(' ')
# string2_hub = string2_hub.split(' ')
#
# result = 0
#
# for i in string1_hub:
#     if i in string2_hub:
#         result += 1
#
# print(result)

# 14) Подсчитать сумму цифр в вещественном числе.

# num_one = 1.234
# num_one = str(num_one)
# num_one = num_one.replace(".", "")
# sum_num = 0
# for el in num_one:
#     sum_num += int(el)
#
# print(sum_num)

# 15) Написать программу получающую набор произведений чисел от 1 до N.
# Пример: пусть N = 4, тогда
# [ 1, 2, 6, 24 ]

# n = 4
#
#
# def calc(n):
#     if n == 1:
#         return n
#     else:
#         return n * calc(n - 1)
#
#
# n_list = []
#
# for v in range(1, n + 1):
#     n_list.append(calc(v))
#
# print(f"Произведения чисел от 1 до {n}:  {n_list}")
