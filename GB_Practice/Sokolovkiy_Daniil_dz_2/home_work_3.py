# решение задания № 2 без создания нового списка* v1

my_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

print(f'id моего списка в начале решения v1: {id(my_list)}')

for word in my_list[:]:
    if word.isdigit():
        my_list.insert(my_list.index(word) + 1, '"')
        my_list.insert(my_list.index(word), '"')
        if len(word) < 2:
            my_list[my_list.index(word)] = '0' + word
        else:
            continue
    elif word.find('+') == 0:
        my_list.insert(my_list.index(word) + 1, '"')
        my_list.insert(my_list.index(word), '"')
        my_list[my_list.index(word)] = word.replace('+', '+0')
    else:
        continue

my_list = ' '.join(my_list)

i = 0
edit_check = 0

while i != len(my_list):
    if my_list[i] == '"' and edit_check == 0:
        my_list = my_list[:i + 1] + my_list[i + 2] + my_list[i + 3:]
        edit_check = 1
        i += 1
    elif my_list[i] == '"' and edit_check == 1:
        my_list = my_list[:i - 1] + my_list[i] + my_list[i + 1:]
        edit_check = 0
        i += 1
    else:
        i += 1

print(my_list)
print(f'id моего списка в конце решения v1: {id(my_list)}')

# решение задания № 2 без создания нового списка* v2

my_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

print(f'id моего списка в начале решения v2: {id(my_list)}')

my_list_len = len(my_list)

for i in range(my_list_len):
    number = my_list.pop(0)
    if number.isdigit():
        my_list.append(f'"{int(number):02d}"')
    elif number[0] == '+' and number[1].isdigit():
        my_list.append(f'"+{int(number):02d}"')
    else:
        my_list.append(number)

print(' '.join(my_list))

print(f'id моего списка в конце решения v2: {id(my_list)}')
