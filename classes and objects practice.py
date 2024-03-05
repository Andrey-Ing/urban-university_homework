from random import *
class Man:
    def __init__(self, name):
        self.name = name
        self.fullness = 20
        self.food = 10
        self.money = 0

    def __str__(self):
        return 'я - {}, сытость {}, еды осталось {}, денег осталось {}'.format(
            self.name, self.fullness, self.food, self.money)

    def eat(self):
        if self.food > 10:
            print('{} поел'.format(self.name))
            self.fullness += 10
            self.food -= 10
        else:
            print('{} нет еды'.format(self.name))

    def work(self):
        print('{} ходил на работу'.format(self.name))
        self.money += 50
        self.fullness -= 10

    def play_DOTA(self):
        print('{} играл в доту целый день'.format(self.name))
        self.fullness -= 10

    def act(self):
        if self.fullness <= 0:
            print('{} умер...'.format(self.name))
            return
        dice = randint(1, 6)
        if self.fullness < 20:
            self.eat()
        elif self.food < 10:
            self.shopping()
        elif self.money < 50:
            self.work()
        elif dice == 1:
            self.work()
        elif dice == 2:
            self.eat()
        else:
            self.play_DOTA()


vasya = Man(name='Вася')
for day in range(1, 21):
    cprint('============== день {} =============='.format(day), color='yellow')
    vasya.act()
    print(vasya)


