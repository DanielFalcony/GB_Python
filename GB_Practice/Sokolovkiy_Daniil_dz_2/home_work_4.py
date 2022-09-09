new_list = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА',
            'токарь высшего разряда нИКОЛАй', 'директор аэлита']

for word in new_list:
    word = word.title()
    words = word.split(' ')
    print(f'Привет, {words[-1]}!')

# version №2

for word in new_list:
    hello_name = word.split()[-1].capitalize()
    print(f'Привет, {hello_name}!')
