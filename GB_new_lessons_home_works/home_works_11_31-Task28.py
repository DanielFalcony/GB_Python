"""
Task 27

Найти корни квадратного уравнения Ax² + Bx + C = 0
a) Математикой
b) Используя дополнительные библиотеки*


"""

import math

print('Введите коэффициенты для уравнения')
print('Ax^2 + Bx + c = 0:')
a = float(input('A = '))
b = float(input('B = '))
c = float(input('C = '))

discr = b**2 - 4 * a * c
print(f'Дискриминант D = {discr:.2f}')

if discr > 0:
    x1 = (-b + math.sqrt(discr)) / (2 * a)
    x2 = (-b - math.sqrt(discr)) / (2 * a)
    print(f'x1 = {x1:.2f} \nx2 = {x2:.2f}')
elif discr == 0:
    x = -b / (2 * a)
    print(f'x = {x:.2f}')
else:
    print('Корней нет')
