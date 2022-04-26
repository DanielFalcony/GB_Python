# version №1
duration = input('Введите время в секундах:')
duration = int(duration)

second = duration % 60
print(f'{second} секунд(а)')

minutes = (duration // 60) % 60
print(f'{minutes} минут(а)')

hours = (duration // 3600) % 24
print(f'{hours} час(ов)')

days = duration // (3600 * 24)
print(f'{days} дней')


print(f'{duration} секунд это: {days} дней, {hours} час(ов), {minutes} минут, {second} секунд')

# version №2

duration = input('Введите время в секундах:')
duration = int(duration)

second = duration % 60
minutes = (duration // 60) % 60
hours = (duration // 3600) % 24
days = duration // 86400

if 0 <= duration < 60:
    print(f'{second} секунд(а)')
elif 60 <= duration < 3600:
    print(f'{minutes} минут(а), {second} секунд(а)')
elif 3600 <= duration < 86400:
    print(f'{hours} час(ов), {minutes} минут(а), {second} секунд(а)')
else:
    print(f'{days} дней, {hours} час(ов), {minutes} минут(а), {second} секунд(а)')
