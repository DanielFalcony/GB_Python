import random


print('Решение задания №5')


def get_jokes(a, doubles=False):
    """
    :param a: input numbers of jokes (1-5)
    :param doubles: use words in joke twice or not (Default=False, change on "True" for Eunice)
    :return: return list of jokes
    """
    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

    joke_list = []
    count = 0

    if a > len(nouns):
        a = len(nouns)
    elif 0 <= a <= len(nouns):
        a = a
    else:
        a = 0
        print('Зачем тебе шутки? Ты сам шутник, если указываешь отрицательные значения:D')

    while count != a:
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
