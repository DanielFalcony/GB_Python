import sys

print('Решение задания №6')

with open('data/bakery.csv', 'a', encoding='utf-8') as f:
    f.write(f'{sys.argv[1]}\n')
exit()
