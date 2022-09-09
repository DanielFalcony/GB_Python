price_list = [25, 31.6, 70, 2, 58.45, 62, 36.8, 72, 315, 2, 98, 24, 11, 15.1, 17, 36.51,
              94, 45, 25.3, 28.9, 6.6, 39.9, 24.5, 98, 57, 584, 11.2]

# Решение пункта "a"

for i, num in enumerate(price_list):
    normal_price = str(f'{float(num)}').split('.')
    while len(normal_price[0]) and len(normal_price[1]) < 2:
        if len(normal_price[0]) < 2:
            normal_price[0] = normal_price[0].zfill(2)
        elif len(normal_price[1]) < 2:
            normal_price[1] = normal_price[1].zfill(2)
        else:
            continue
    print(f'"{normal_price[0]} руб. {normal_price[1]} коп."', end=', ')

# Решение пункта "b"

price_list = [25, 31.6, 70, 2, 58.45, 62, 36.8, 72, 315, 2, 98, 24, 11, 15.1, 17, 36.51,
              94, 45, 25.3, 28.9, 6.6, 39.9, 24.5, 98, 57, 584, 11.2]
print(price_list)
print(f'ID списка до сортировки: {id(price_list)}')

price_list.sort()

print(price_list)
print(f'ID списка после сортировки: {id(price_list)}')

# Решение пункта "c"

price_list = [25, 31.6, 70, 2, 58.45, 62, 36.8, 72, 315, 2, 98, 24, 11, 15.1, 17, 36.51,
              94, 45, 25.3, 28.9, 6.6, 39.9, 24.5, 98, 57, 584, 11.2]
print(price_list)
print(f'ID списка до реверса: {id(price_list)}')

new_price_list = list(reversed(price_list))

print(new_price_list)
print(f'ID списка после реверса: {id(new_price_list)}')

# Решение пункта "d"

price_list = [25, 31.6, 70, 2, 58.45, 62, 36.8, 72, 315, 2, 98, 24, 11, 15.1, 17, 36.51,
              94, 45, 25.3, 28.9, 6.6, 39.9, 24.5, 98, 57, 584, 11.2]

price_list.sort(reverse=True)
print(price_list[:5])
