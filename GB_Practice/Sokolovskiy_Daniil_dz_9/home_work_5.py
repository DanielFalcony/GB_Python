# 5. Реализовать класс Stationery (канцелярская принадлежность):
# ● определить в нём атрибут title (название) и метод draw (отрисовка). Метод выводит
# сообщение «Запуск отрисовки»;
# ● создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
# ● в каждом классе реализовать переопределение метода draw. Для каждого класса
# метод должен выводить уникальное сообщение;
# ● создать экземпляры классов и проверить, что выведет описанный метод для каждого
# экземпляра.

print('Решение ДЗ №5')


class Stationery:
    title = 'Parent'

    def draw(self):
        print(f'Запуск отрисовки: {self.title}')


class Pen(Stationery):
    title = 'Pen'

    def draw(self):
        print(f'Пишем с помощью: {self.title}')


class Pencil(Stationery):
    title = 'Pencil'

    def draw(self):
        print(f'Обводим с помощью: {self.title}')


class Handle(Stationery):
    title = 'Handle'

    def draw(self):
        print(f'Выделяем с помощью: {self.title}')


s, p, pe, h = Stationery(), Pen(), Pencil(), Handle()
s.draw(), p.draw(), pe.draw(), h.draw()
