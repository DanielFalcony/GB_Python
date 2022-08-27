"""
Task 5


Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

Пример:

- для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
"""


def fibonacci(n):
    result = []
    fib1 = 1
    fib2 = 0
    for i in range(1, n + 1):
        fib1, fib2 = fib2, fib1 + fib2
        result.append(fib2)
    fib1 = 1
    fib2 = -1
    for i in range(2, n):
        fib1, fib2 = fib2, fib1 - fib2
        result.insert(0, fib2)

    return f'Для числа n={n}, Список Фибоначи = {result}'


n = 8

print(fibonacci(n))


