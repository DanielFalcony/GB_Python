# 26. Дано число. Составить список чисел Фибоначчи,
# в том числе для отрицательных индексов

def fibonacci(n):
    result = []
    fib1 = 1
    fib2 = 0
    for i in range(1, n + 1):
        if fib2 == 0:
            result.append(fib2)
        fib1, fib2 = fib2, fib1 + fib2
        result.append(fib2)
    fib1 = 1
    fib2 = -1
    for i in range(2, n):
        if fib2 == -1:
            result.insert(0, fib2)
        fib1, fib2 = fib2, fib1 - fib2
        result.insert(0, fib2)

    return f'Для числа n={n}, Список Фибоначи = {result}'


n = int(input('Введите число: '))

print(fibonacci(n))