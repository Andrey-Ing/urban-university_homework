from threading import Thread
from time import sleep


class Knight(Thread):
    def __init__(self, name, skill, enemies=50):
        super().__init__()
        self.name = name
        self.skill = skill
        self.enemies = enemies

    def run(self):
        day = 0
        if self.enemies > 0:
            print(f'{self.name}, на нас напали {self.enemies} врагов!')
        while self.enemies > 0:
            sleep(1)
            day += 1
            self.enemies -= self.skill
            if self.enemies < 0:
                self.enemies = 0
            print(f'{self.name}, сражается {day}-й день, осталось врагов {self.enemies}')

        print(f'Врагов не осталось! {self.name} одержал победу за {day} дня(дней)')


knight1 = Knight("Sir Lancelot", 13, 120)
knight2 = Knight("Sir Galahad", 24, 160)
knight1.start()
knight2.start()
knight1.join()
knight2.join()
