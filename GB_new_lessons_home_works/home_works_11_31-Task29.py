"""
Task 29

Найти НОК двух чисел


"""


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def mcd(n, m):
    return (n / gcd(n, m)) * m


val1 = int(input('Введите значение А: '))
val2 = int(input('Введите значение B: '))

print(int(mcd(val1, val2)))
