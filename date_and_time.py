from datetime import datetime


class SuperDate(datetime):
    def __new__(cls, hemispheres, year, month, day, hour=0, minute=0, second=0,
                microsecond=0, tzinfo=None, *args, fold=0):
        instance = super().__new__(cls, year=year, month=month, day=day, hour=hour, minute=minute,
                                   second=second, microsecond=microsecond, tzinfo=tzinfo, *args, fold=fold)

        cls.season = cls._hemispheres_inite(cls, hemispheres)
        return instance

    def _hemispheres_inite(self, hemispheres):

        northern_season = {(3, 4, 5): 'Spring', (6, 7, 8): 'Summer',
                           (9, 10, 11): 'Autumn', (12, 1, 2): 'Winter'}

        southern_season = {(9, 10, 11): 'Spring', (12, 1, 2): 'Summer',
                           (3, 4, 5): 'Autumn', (6, 7, 8): 'Winter'}

        if hemispheres == 'northern':
            return northern_season
        elif hemispheres == 'southern':
            return southern_season
        else:
            raise ValueError('Должно быть задано либо северное("northern"),'
                             'либо южное("southern") полушарие')

    def set_hemispheres(self, hemispheres):
        self.season = self._hemispheres_inite(hemispheres)

    def get_season(self):
        for ind_tuple in self.season:
            if self.month in ind_tuple:
                return self.season[ind_tuple]


rr = SuperDate('northern', 1999, 12, 4)
print(rr.get_season())
rr.set_hemispheres('southern')
print(rr.get_season())
