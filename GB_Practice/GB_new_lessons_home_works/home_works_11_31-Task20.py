# 20) Определить, присутствует ли в заданном списке строк, некоторое число

def search(args, val):
    for i in args:
        if val in i:
            return True
    return False


list_new = ['abw', '213', 'bbe', 'ler3at']
v = '2'

print(search(list_new, v))
