from pprint import pprint
print('Решение задания №3')


def thesaurus(*name):
    """
    function take first letter in word,
    make dict "first letter: Word"
    if first letter already in dict,
    add word in dict for key first letter
    """

    names_dict = {}

    for i in name:
        if names_dict.get(i[0]):
            names_dict[i[0]].append(i)
        else:
            names_dict[i[0]] = [i]

    return names_dict


print(thesaurus("Иван", "Мария", "Петр", "Илья"))

print('Решение задания №4')


def thesaurus_adv(*users):
    """
    taking as arguments strings in the format "First Name Last Name"
    and returning a dictionary in which
    the keys are the first letters of the last names,
    and the values are lists
    containing names starting with the corresponding letter.
    in which the last name begins with the corresponding letter
    """

    names_dict = {}

    for i in users:
        name, last_name = i.split(' ')
        if not names_dict.get(last_name[0]):
            names_dict[last_name[0]] = {name[0]: [i]}
        elif not names_dict[last_name[0]].get(name[0]):
            names_dict[last_name[0]][name[0]] = [i]
        else:
            names_dict[last_name[0]][name[0]].append(i)

    return names_dict


pprint(thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева"))
