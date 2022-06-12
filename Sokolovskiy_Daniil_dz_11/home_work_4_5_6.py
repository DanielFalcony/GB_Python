# 4. Начать работу над проектом «Склад оргтехники». Создать класс, описывающий склад. А также
# класс «Оргтехника», который будет базовым для классов-наследников. Эти классы —
# конкретные типы оргтехники (принтер, сканер, ксерокс). В базовом классе определить
# параметры, общие для приведённых типов. В классах-наследниках реализовать параметры,
# уникальные для каждого типа оргтехники.
# 5. Продолжить работу над предыдущим заданием. Разработать методы, которые отвечают за
# приём оргтехники на склад и передачу в определённое подразделение компании. Для
# хранения данных о наименовании и количестве единиц оргтехники, а также других данных,
# можно использовать любую подходящую структуру (например, словарь).
# 6. Продолжить работу над предыдущим заданием. Реализовать механизм валидации вводимых
# пользователем данных. Например, для указания количества принтеров, отправленных на
# склад, нельзя использовать строковый тип данных.


print('Решение задачи №4, №5, №6')


class Warehouse:
    def __init__(self, type_off, count, depart):
        self.type_off = type_off
        self.count = count
        self.depart = depart
        self.my_warehouse = []
        self.my_list = {}

    # def __str__(self):
    #     return f'{self.type_off} Кол-во {self.count} Департамент {self.depart}'

    # @classmethod
    def logistic(self):
        # global choice
        choice = 0
        while True:
            try:
                choice = input(f'Выберите номер устройства или введи "q" что бы закончить:'
                               f'\n1 : {p}'
                               f'\n2 : {s}'
                               f'\n3 : {x}'
                               f'\nВведите значение:')
                if choice != 'q':
                    count = input(f'Введите кол-во товара шт.: ')
                    department = input('Введите в какой департамент отправляем: ')
                if choice == '1':
                    uniqe = {'Устройство': p.__str__(), 'Кол-во': count, 'Департамент': department}
                    self.my_list.update(uniqe)
                    self.my_warehouse.append(self.my_list)
                    print(f'На складе для передачи:\n {self.my_warehouse}')
                elif choice == '2':
                    uniqe = {'Устройство': s.__str__(), 'Кол-во': count, 'Департамент': department}
                    self.my_list.update(uniqe)
                    self.my_warehouse.append(self.my_list)
                    print(f'На складе для передачи:\n {self.my_warehouse}')
                elif choice == '3':
                    uniqe = {'Устройство': x.__str__(), 'Кол-во': count, 'Департамент': department}
                    self.my_list.update(uniqe)
                    self.my_warehouse.append(self.my_list)
                    print(f'На складе для передачи:\n {self.my_warehouse}')
                elif choice.lower() == 'q':
                    print('Пополнение склада закончено')
                    break
                else:
                    raise OwnError('Введено неверное значение!')
            except OwnError as err:
                print(err)
        return f'На складе хранится: {self.my_warehouse}'
        return Warehouse.logistic(self)


class OwnError(ValueError):
    def __init__(self, val):
        self.val = val


class OffEquip:
    def __init__(self, color, can_print, scan, copy):
        self.color = color
        self.can_print = can_print
        self.scan = scan
        self.copy = copy

    def __str__(self):
        return f'Оргтехника - Цвет: {self.color}, Печатает: {self.can_print}, ' \
               f'Сканирует: {self.scan}, Копирует: {self.copy}'


class Printer(OffEquip):
    def __str__(self):
        return f'Принтер - Цвет: {self.color}, Печатает: {self.can_print}, ' \
               f'Сканирует: {self.scan}, Копирует: {self.copy}'


class Scaner(OffEquip):
    def __str__(self):
        return f'Сканер - Цвет: {self.color}, Печатает: {self.can_print}, ' \
               f'Сканирует: {self.scan}, Копирует: {self.copy}'


class Xerox(OffEquip):
    def __str__(self):
        return f'Ксерокс - Цвет: {self.color}, Печатает: {self.can_print}, ' \
               f'Сканирует: {self.scan}, Копирует: {self.copy}'


o = OffEquip('Белый', 'Да', 'Да', 'Да')
p = Printer('Белый', 'Да', 'Нет', 'Нет')
s = Scaner('Белый', 'Нет', 'Да', 'Нет')
x = Xerox('Белый', 'Да', 'Да', 'Да')
print(o)
print(p)
print(s)
print(x)
ware = Warehouse(o, 10, 'market')
print(Warehouse.logistic(ware))
