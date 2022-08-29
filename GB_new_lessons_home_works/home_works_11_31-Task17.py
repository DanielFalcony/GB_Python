# 17) -Задать список из N элементов, заполненных числами из [-N, N]. Найти произведение элементов на указанных позициях.
# Позиции хранятся в файле file.txt в одной строке одно число

n = int(input("Введите число N: "))
my_list = []
for n in range(-n, n + 2, 2):
    my_list.append(n)
    if n == 0:
        my_list.remove(n)
total_list = [i * n for i in my_list]
print(my_list)
print(total_list)
with open("file.txt", "w", encoding="utf-8") as f:
    for i in total_list:
        f.write('%s\n' % i)
