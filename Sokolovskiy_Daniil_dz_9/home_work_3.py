# 3. Реализовать базовый класс Worker (работник):
# ● определить атрибуты: name, surname, position (должность), income (доход);
# ● последний атрибут должен быть защищённым и ссылаться на словарь, содержащий
# элементы «оклад» и «премия», например, {"wage": wage, "bonus": bonus};
# ● создать класс Position (должность) на базе класса Worker;
# ● в классе Position реализовать методы получения полного имени сотрудника
# (get_full_name) и дохода с учётом премии (get_total_income);
# ● проверить работу примера на реальных данных: создать экземпляры класса Position,
# передать данные, проверить значения атрибутов, вызвать методы экземпляров.

print('Решение ДЗ №3')


class Worker:
    def __init__(self, name, surname, position, wage, bonus, months):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}
        self.months = months


class Position(Worker):
    def get_full_name(self):
        print(f'Сотрудник {self.name} {self.surname} работает в должности {self.position}')

    def get_total_income(self):
        print(f'Общая прибыль сотрудника за {self.months} месяц(ев) составила:\
 {sum(self._income.values()) * self.months} долларов {self._income}')


worker = Position('Петр', 'Петров', 'Programmer', 1200, 3000, 2)

worker.get_full_name()
worker.get_total_income()
print(worker.name)
print(worker.position)
