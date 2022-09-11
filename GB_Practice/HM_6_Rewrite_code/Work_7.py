# 7) Проверить истинность утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат

def logic_math(x, y, z):
    print(f'¬({x} ⋁ {y} ⋁ {z}) = ¬{x} ⋀ ¬{y} ⋀ ¬{z}) is {(not(x or y or z)) == (not x and not y and not z)}')
    return (not(x or y or z)) == (not x and not y and not z)


if (logic_math(0, 0, 0) and logic_math(1, 0, 0) and logic_math(0, 1, 0) and
        logic_math(0, 0, 1) and logic_math(1, 1, 0) and logic_math(1, 0, 1) and
        logic_math(0, 1, 1) and logic_math(1, 1, 1)):
    print('Выражение Истинно')
else:
    print('Выражение Ложно')