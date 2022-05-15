print('Решение задачи №4')

src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]


def src_func(my_list):  # Можно было реализовать без функции, но для перспективного удобства, так предпочтительней.
    """
    :param my_list: Taken list, with 'int' type of value
    :return: A list with values greater than the previous one
    """
    result = [i for n, i in enumerate(my_list) if i > src[n - 1] and n != 0]
    return result


print(src_func(src))
