# 13) Пользователь задаёт две строки. Определить количество вхождений одной строки в другой.

string1 = 'Привет, как у тебя дела? Это первая строка!'
string2 = 'Привет, дела у меня хорошо! Это вторая строка!'

string1_hub = ""
string2_hub = ""

for i in string1:
    if i.isalpha() or i.isspace():
        string1_hub += i

for i in string2:
    if i.isalpha() or i.isspace():
        string2_hub += i

string1_hub = string1_hub.split(' ')
string2_hub = string2_hub.split(' ')

result = 0

for i in string1_hub:
    if i in string2_hub:
        result += 1

print(result)
