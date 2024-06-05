from datetime import datetime


class SuperDate(datetime):
    def __init__(self, hemispheres, year, month, day, hour=0, minute=0, second=0,
                 microsecond=0, tzinfo=None, *args, fold=0):

        self._times_of_day = {(0, 1, 2, 3, 4, 5): 'Night',
                              (6, 7, 8, 9, 10, 11): 'Morning',
                              (12, 13, 14, 15, 16, 17): 'Day',
                              (18, 19, 20, 21, 22, 23): 'Evening'}
        self._season = None
        self.current_hemispheres = None
        self.set_hemispheres(hemispheres)

    def __new__(cls, hemispheres, year, month, day, hour=0, minute=0, second=0,
                microsecond=0, tzinfo=None, *args, fold=0):
        instance = super().__new__(cls, year=year, month=month, day=day, hour=hour, minute=minute,
                                   second=second, microsecond=microsecond, tzinfo=tzinfo, *args, fold=fold)

        return instance

    def set_hemispheres(self, hemispheres):

        self.current_hemispheres = hemispheres

        northern_season = {(3, 4, 5): 'Spring', (6, 7, 8): 'Summer',
                           (9, 10, 11): 'Autumn', (12, 1, 2): 'Winter'}

        southern_season = {(9, 10, 11): 'Spring', (12, 1, 2): 'Summer',
                           (3, 4, 5): 'Autumn', (6, 7, 8): 'Winter'}

        if hemispheres == 'northern':
            self._season = northern_season
        elif hemispheres == 'southern':
            self._season = southern_season
        else:
            raise ValueError('Должно быть задано либо северное("northern"),'
                             'либо южное("southern") полушарие')

    def get_hemispheres(self):
        return self.current_hemispheres

    def get_season(self):
        for ind_tuple in self._season:
            if self.month in ind_tuple:
                return self._season[ind_tuple]

    def get_time_of_day(self):
        for ind_tuple in self._times_of_day:
            if self.hour in ind_tuple:
                return self._times_of_day[ind_tuple]


sd = SuperDate('northern', 1999, 12, 4, 3, 45)

print(sd.date(), sd.time())

print(sd.get_hemispheres())
print(sd.get_season())
print('*' * 9)
sd.set_hemispheres('southern')
print(sd.get_hemispheres())
print(sd.get_season())
print('*' * 9)
print(sd.get_time_of_day())
