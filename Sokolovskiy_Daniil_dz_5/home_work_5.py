print('Решение задачи №5')

src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]


def src_count(my_list):  # Можно было реализовать без функции, но для перспективного удобства, так предпочтительней.
    """
    :param my_list: Taken list, with 'int' type of value
    :return: A list with unique values from input list
    """
    result = [i for i in my_list if my_list.count(i) == 1]
    return result


print(src_count(src))
