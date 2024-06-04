from datetime import datetime

print(datetime)


class SuperDate(datetime):

    def __init__(self, hemispheres, year, month=None, day=None, hour=0, minute=0, second=0,
                microsecond=0, tzinfo=None, *args, fold=0):
        super().__init__(year=year, month=month, day=day, hour=hour, minute=minute, second=second,
                         microsecond=microsecond, tzinfo=tzinfo, *args, fold=fold)

        self.season = None
        if hemispheres == 'northern':
            self.season = {3:'Summer', 8:'Autumn', 'Winter', 'Spring'}


            В
            северном
            полушарии
            весна
            начинается
            1
            марта, лето — 1
            июня, осень — 1
            сентября, а
            зима — 1
            декабря.В
            южном
            полушарии
            весна
            начинается
            1
            сентября, лето — 1
            декабря, осень — 1
            марта, зима — 1
            июня.
            3: «Лето», 8: «Осень», «Зима», «Весна».
        = {3:'Summer', 8:'Autumn', 'Winter', 'Spring'}

        southern
        northern

    def get_season(self):
        self._month





        1.
        get_season - должен
        возвращать
        сезон
        года(Summer, Autumn, Winter, Spring)
        2.
        get_time_of_day - должен
        возвращать
        время
        суток
        (Morning: 6-12; Day: 12-18, Evening: 18-0, Night: 0-6)(последнее
        число
        не
        включено
        в
        промежуток)


        Пример
        работы
        класса:

        a = SuperDate(2024, 2, 22, 12)
        print(a.get_season())
        print(a.get_time_of_day())

        Вывод
        на
        консоль:
        Winter
        Day



def __init__(self, id, name, Add, Emails):
    class Emp():
        def __init__(self, id, name, Add):
            self.id = id
            self.name = name
            self.Add = Add

    # Class freelancer inherits EMP
    class Freelance(Emp):
        def __init__(self, id, name, Add, Emails):
            super().__init__(id, name, Add)
            self.Emails = Emails

    Emp_1 = Freelance(103, "Suraj kr gupta", "Noida", "KKK@gmails")
    print('The ID is:', Emp_1.id)
    print('The Name is:', Emp_1.name)
    print('The Address is:', Emp_1.Add)
    print('The Emails is:', Emp_1.Emails)


a = SuperDate(2024, 2, 22, 12)
print(a.get_season())
print(a.get_time_of_day())


class Freelance(Emp):
    def __init__(self, id, name, Add, Emails):
        super().__init__(id, name, Add)
        self.Emails = Emails
