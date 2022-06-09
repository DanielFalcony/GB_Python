# 1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде
# строки формата «день-месяц-год». В рамках класса реализовать два метода. Первый — с
# декоратором @classmethod. Он должен извлекать число, месяц, год и преобразовывать их тип
# к типу «Число». Второй — с декоратором @staticmethod, должен проводить валидацию числа,
# месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на
# реальных данных.


class Data:
    def __init__(self, day_month_year):
        self.day_month_year = str(day_month_year)

    @classmethod
    def extract(cls, day_month_year):
        my_date = []

        for i in day_month_year.split('-'):
            if i != '-':
                my_date.append(i)

        return int(my_date[0]), int(my_date[1]), int(my_date[2])

    @staticmethod
    def valid(day, month, year):
        if 31 < day <= 0:
            return f'Неверная дата дня {day}'
        elif 12 < month <= 0:
            return f'Неверная дата месяца {month}'
        elif 2022 < month <= 0:
            return f'Неверная дата года {year}'
        else:
            return f'Все верно!'

    def __str__(self):
        return f'Текущая дата {Data.extract(self.day_month_year)}'


today = Data('8-6-2022')
print(today)
print(Data.valid(8, 6, 2022))
print(today.extract('08-06-2022'))
