# variant a

my_list = [i ** 3 for i in range(1, 1001, 2)]
dev_seven_sum = 0
check_list = 0

for number in my_list:
    i = number
    while i > 0:
        one_number = i % 10
        i = i // 10
        check_list += one_number
    if check_list % 7 == 0:
        dev_seven_sum += number
    else:
        check_list = 0
        continue

print(f'Решение задачи a. = {dev_seven_sum}')

# variant b (в логике, 17 прибавляется к значению которе делится на 7 без остатка)

my_list = [i ** 3 for i in range(1, 1001, 2)]
my_new_list = []
dev_seven_sum = 0
check_list = 0

for number in my_list:
    i = number
    while i > 0:
        one_number = i % 10
        i = i // 10
        check_list += one_number
    if check_list % 7 == 0:
        check_list = 0
        my_new_list.append(number)
    else:
        check_list = 0
        continue

for number in my_new_list:
    i = (number + 17)
    while i > 0:
        one_number = i % 10
        i = i // 10
        check_list += one_number
    if check_list % 7 == 0:
        check_list = 0
        dev_seven_sum += number
    else:
        check_list = 0
        continue

print(f'Решение задачи b. = {dev_seven_sum}')

# variant c (в логике, 17 прибавляется к значению которе делится на 7 без остатка)

my_list = [i ** 3 for i in range(1, 1001, 2)]
dev_seven_sum = 0
check_list = 0

for number in my_list:
    i = number
    while i > 0:
        one_number = i % 10
        i = i // 10
        check_list += one_number
    if check_list % 7 == 0:
        check_list = 0
        number += 17
        i = number
        while i > 0:
            one_number = i % 10
            i = i // 10
            check_list += one_number
        if check_list % 7 == 0:
            check_list = 0
            dev_seven_sum += number
        else:
            check_list = 0
            continue
    else:
        check_list = 0
        continue

print(f'Решение задачи c. = {dev_seven_sum}')

# variant b (со списком + добавляется 17 к изначальному списку)

my_list = [i ** 3 for i in range(1, 1001, 2)]
my_list_plus = []
numbers_sum = 0
my_list_qube_sum = 0

for i in my_list:
    my_list_plus.append(i + 17)

for i in my_list_plus:
    number = i
    while i > 0:
        one_number = i % 10
        numbers_sum += one_number
        i //= 10
    if numbers_sum % 7 == 0:
        my_list_qube_sum += number
        numbers_sum = 0
    else:
        numbers_sum = 0

print(f'Решение задачи b. = {my_list_qube_sum}')

# variant c (без списка + добавляется 17 к изначальному списку)

my_list = [(i ** 3) + 17 for i in range(1, 1001, 2)]
numbers_sum = 0
my_list_qube_sum = 0

for i in my_list:
    number = i
    while i > 0:
        one_number = i % 10
        numbers_sum += one_number
        i //= 10
    if numbers_sum % 7 == 0:
        my_list_qube_sum += number
        numbers_sum = 0
    else:
        numbers_sum = 0

print(f'Решение задачи c. = {my_list_qube_sum}')
