# 15) Написать программу получающую набор произведений чисел от 1 до N.
# Пример: пусть N = 4, тогда
# [ 1, 2, 6, 24 ]


n = 4


def calc(n):
    if n == 1:
        return n
    else:
        return n * calc(n - 1)


n_list = []

for v in range(1, n + 1):
    n_list.append(calc(v))

print(f"Произведения чисел от 1 до {n}:  {n_list}")
