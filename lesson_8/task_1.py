# 1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
# В рамках класса реализовать два метода. Первый, с декоратором @classmethod,
# должен извлекать число, месяц, год и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod,
# должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
# Проверить работу полученной структуры на реальных данных.

class Date:

    def __init__(self, date_str):
        self.date_str = date_str
        # self.day, self.month, self.year = date_str.split("-")

    @classmethod
    def date_parce(cls, date_str):
        date_arr = date_str.split("-")
        return {"day": int(date_arr[0]), "month": int(date_arr[1]), "year": int(date_arr[2])}

    @staticmethod
    def is_valid_date(date_str):
    # def is_valid_date(day, month, year):
        # date_dict = {'day': day, 'month': month, 'year': year}
        # date_str = f"{day}-{month}-{year}"
        date_dict = Date.date_parce(date_str)
        month_long = [1, 3, 5, 7, 8, 10, 12]
        month_short = [2, 4, 6, 9, 11]
        valid = False
        # проверяем год
        if 0 < date_dict['year'] < 2022:
            valid = True
        else:
            print("неправильный год")

        # проверяем месяц
        if (1 <= date_dict['month'] <= 12) & valid:
            valid = True
        else:
            valid = False
            print("неправильный месяц")

        # проверяем день с учетом месяца
        if (1 <= date_dict['day'] <= 31) & (date_dict['month'] in month_long) & valid:
            valid = True
        else:
            if (1 <= date_dict['day'] <= 30) & (date_dict['month'] in month_short) & valid:
                valid = True

                # проверяем февраль
                if (1 <= date_dict['day'] <= 28) & (date_dict['month'] == 2) & valid:
                    valid = True
                else:
                    valid = False
                    print("неправильный день")

            else:
                valid = False
                print("неправильный день")

        if valid:
            print(f"валидация даты {date_str} прошла успешно")
        else:
            print(f"валидация даты {date_str} не прошла")


date_1 = Date("10-02-2021")
print(date_1.date_parce(date_1.date_str))
print(Date.date_parce("10-02-2021"))

Date.is_valid_date("31-12-2020")
Date.is_valid_date("28-02-2020")
Date.is_valid_date("29-02-2020")
Date.is_valid_date("32-03-2020")
Date.is_valid_date("31-06-2020")
