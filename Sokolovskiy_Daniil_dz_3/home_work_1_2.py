print('Решение задания №1')


def num_translate(number):
    """
    check entering 'number' in dict 'numbers',
    if found, return translate from eng on rus,
    if not found, return 'None'
    """
    numbers = {
        'zero': 'ноль',
        'one': 'один',
        'two': 'два',
        'tree': 'три',
        'four': 'четыре',
        'five': 'пять',
        'six': 'шесть',
        'seven': 'семь',
        'eight': 'восемь',
        'nine': 'девять',
        'ten': 'десять'
    }

    print(numbers.get(number.lower(), None))


num_translate(number=input('Введите число прописью по английски от 0 до 10: '))

print('Решение задания №2')


def num_translate_adv(number):
    """
    check entering 'number' in dict 'numbers',
    else check is 'number' - title
    if found, return translate from eng on rus,
    if not found, return 'None'
    if number was title, return will be title
    """
    numbers = {
        'zero': 'ноль',
        'one': 'один',
        'two': 'два',
        'tree': 'три',
        'four': 'четыре',
        'five': 'пять',
        'six': 'шесть',
        'seven': 'семь',
        'eight': 'восемь',
        'nine': 'девять',
        'ten': 'десять'
    }

    if number.istitle():
        print((numbers.get(number.lower(), None)).title())
    else:
        print(numbers.get(number.lower(), None))


num_translate_adv(number=input('Введите число прописью по английски от 0 до 10: '))
