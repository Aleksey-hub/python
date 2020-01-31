# Реализовать класс «Дата», функция-конструктор которого должна принимать
# дату в виде строки формата «день-месяц-год». В рамках класса реализовать два метода.
# Первый, с декоратором @classmethod, должен извлекать число, месяц,
# год и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod,
# должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
# Проверить работу полученной структуры на реальных данных.

class Date:
    def __init__(self, date):
        self.date = date

    @classmethod
    def date_to_int(cls, date):
        if cls.validation(date) == True:
            day, month, year = date.split('-')
            day = int(day)
            month = int(month)
            year = int(year)
            return day, month, year
        else:
            return 0, 0, 0

    @staticmethod
    def validation(date):
        day, month, year = date.split('-')
        try:
            day = int(day)
            month = int(month)
            year = int(year)
            if day > 31 or day < 1:
                print('Введена некоректная дата')
                return False
            elif month > 12 or month < 1:
                print('Введена некоректная дата')
                return False
            else:
                print('Введена коректная дата')
                return True
        except ValueError:
            print('Введена некоректная дата')
            return False


Date.validation('31-13-1989')
day, month, year = Date.date_to_int('31-12-1989')
print(f'{day}.{month}.{year}')