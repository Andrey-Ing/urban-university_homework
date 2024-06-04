from datetime import datetime

print(datetime)


class SuperDate(datetime):
    def __init__(self, year, month=None, day=None, hour=0, minute=0, second=0,
                microsecond=0, tzinfo=None, *, fold=0):
        super().__init__(year=year, month=month, day=day, hour=hour, minute=minute, second=second,
                         microsecond=microsecond, tzinfo=tzinfo, fold=fold)




        hour = 0, minute = 0, second = 0,
        microsecond = 0, tzinfo = None, *, fold = 0):
        self.name = year



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
