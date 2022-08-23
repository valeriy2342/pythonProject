class Date(object):

    def __init__(self, day=0, month=0, year=0):
        self.day = day
        self.month = month
        self.year = year

    @classmethod
    def text(cls, date):
        day, month, year = map(int, date.split('-'))
        date1 = cls(day, month, year)
        print(cls, date)
        return date1

    @staticmethod
    def check(date):
        day, month, year = map(int, date.split('-'))
        if day <= 31 and day != 0 and month <= 12 and month != 0 and year <= 3999:
            print(date)
            return day, month, year
        else:
            print('Ошибка ввода данных')


d = '03-05-1980'
date2 = Date.text(d)
is_date = Date.check(d)

d = '33-14-2060'
date2 = Date.text(d)
is_date = Date.check(d)