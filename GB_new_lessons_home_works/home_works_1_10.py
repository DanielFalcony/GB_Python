# 1) По двум заданным числам проверить является ли одно квадратом второго

# def square(a, b):
#     if a * a == b:
#         result = 'a is square b'
#     elif b * b == a:
#         result = 'b is square a'
#     else:
#         result = 'a is not square b and b is not square a'
#
#     return f'{result}, where a={a}, and b={b}'
#
#
# print(square(16, 4))

# 2) Найти максимальное из пяти чисел

# def max_five(*args):
#     result = max(*args)
#
#     return result
#
#
# print(max_five([1, 2, 22, 13, 10]))

# 3) Вывести на экран числа от -N до N

# def numbers(x):
#     a = range(-x, x + 1)
#     val = []
#     for i in a:
#         val.append(i)
#
#     return val
#
#
# print(numbers(5))

# 4) Показать первую цифру дробной части числа

# def num_after_dot(a):
#     result = int((a * 10) % 10)
#
#     return result
#
#
# print(num_after_dot(2.45454))

# 5) Дано число. Проверить кратно ли оно 5 и 10 или 15 но не 30

# def multiplicity(a):
#     if (a % 5 or a % 10 or a % 15) and (a % 30 != 0):
#         result = f'Число {a} кратно 5, 10 или 15 но не кратно 30'
#     else:
#         result = f'Число {a} не кратно 5, 10 или 15 либо кратно 30'
#
#     return result
#
#
# print(multiplicity(150))

# 6) Дано число обозначающее день недели. Вывести его название и указать является ли он выходным.

# def day_of_week(a):
#     days = {
#         1: "Monday",
#         2: "Tuesday",
#         3: "Wednesday",
#         4: "Thursday",
#         5: "Friday",
#         6: "Saturday",
#         7: "Sunday"
#     }
#     if int(a) > 5:
#         result = f'{days.get(a)} - Holiday'
#     else:
#         result = f'{days.get(a)} - Workday'
#
#     return result
#
#
# print(day_of_week(7))

# 7) Проверить истинность утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат

# 8) Сообщить в какой четверти координатной плоскости или на какой оси находится точка с координатами Х и У
#
# def coordinates(x, y):
#     if x > 0:
#         if y > 0:
#             result = f'Точка с кроординатами x:{x}, y:{y} находится в 1 координатной четверти'
#         elif y < 0:
#             result = f'Точка с кроординатами x:{x}, y:{y} находится в 4 координатной четверти'
#         else:
#             result = f'Точка с кроординатами x:{x}, y:{y} находится на оси X'
#     elif x < 0:
#         if y > 0:
#             result = f'Точка с кроординатами x:{x}, y:{y} находится во 2 координатной четверти'
#         elif y < 0:
#             result = f'Точка с кроординатами x:{x}, y:{y} находится в 3 координатной четверти'
#         else:
#             result = f'Точка с кроординатами x:{x}, y:{y} находится на оси X'
#     elif x == 0 and y > 0 or y < 0:
#         result = f'Точка с кроординатами x:{x}, y:{y} находится на оси Y'
#     else:
#         result = f'Точка с кроординатами x:{x}, y:{y} находится на пересечении осей X и Y'
#
#     return result
#
#
# print(coordinates(-5, 5))

# 9) Указав номер четверти прямоугольной системы координат,
# показать допустимые значения координат для точек этой четверти

