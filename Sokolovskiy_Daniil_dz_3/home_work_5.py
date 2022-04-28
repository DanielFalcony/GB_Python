import random


print('Решение задания №5')


def get_jokes(number_joke, doubles=False):
    """
    :param number_joke:
    :param doubles: use words in joke twice or not (Default=False, change on "True" for use doubles)
    :return: return list of jokes
    """
    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

    joke_list = []
    count = 0

    if number_joke > len(nouns):
        number_joke = len(nouns)
    elif 0 <= number_joke <= len(nouns):
        number_joke = number_joke
    else:
        number_joke = 0
        print('Первым аргументом функции, нужно ввести положительное значение от 1 до 5')

    while count != number_joke:
        i = len(nouns) - 1
        if not doubles:
            joke_list.append(f'{nouns.pop(int(random.randint(0, i)))}, '
                             f'{adverbs.pop(int(random.randint(0, i)))}, '
                             f'{adjectives.pop(int(random.randint(0, i)))}')
            count += 1
        else:
            joke_list.append(f'{nouns[random.randint(0, i)]}, '
                             f'{adverbs[random.randint(0, i)]}, '
                             f'{adjectives[random.randint(0, i)]}')

            count += 1

    print(joke_list)


get_jokes(10, doubles=True)
