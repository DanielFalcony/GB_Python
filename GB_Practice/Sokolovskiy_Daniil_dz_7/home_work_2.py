# 2. *(вместо 1) Написать скрипт, создающий из config.yaml стартер для проекта со следующей
# структурой:
# |--my_project
#   |--settings
#   | |--__init__.py
#   | |--dev.py
#   | |--prod.py
#   |--mainapp
#   | |--__init__.py
#   | |--models.py
#   | |--views.py
#   | |--templates
#   | |--mainapp
#   | |--base.html
#   | |--index.html
#   |--authapp
#   | |--__init__.py
#   | |--models.py
#   | |--views.py
#   | |--templates
#   | |--authapp
#   | |--base.html
#   | |--index.html
# Примечание: структуру файла config.yaml придумайте сами, его можно создать в любом
# текстовом редакторе «руками» (не программно); предусмотреть возможные исключительные
# ситуации, библиотеки использовать нельзя.

import os

settings = {}

with open('data/config.yaml', 'r', encoding='utf-8') as f:
    lines = dict(map(str.split, f.readlines()))
    # print(lines)

base_dir = lines.pop('base')
for k, v in lines.items():
    os.makedirs(os.path.join(os.curdir, base_dir, k), exist_ok=True)
    # print(f'Создан каталог {k}')
    for i in v.split(','):
        with open(os.path.join(os.curdir, base_dir, k, i), 'w') as f:
            # print(f'Создан файл {i}, в каталоге {k} ')
