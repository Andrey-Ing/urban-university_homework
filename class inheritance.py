class Car:
    price = 1000000

    def horse_powers(self, power):
        return f'Мощность двигателя {__class__} = {power} л.с'


class Nissan(Car):
    price = 5000000

    def horse_powers(self, power):
        return f'Мощность двигателя Nissan = {power} л.с.'


class Kia(Car):
    price = 4000000

    def horse_powers(self, power):
        return f'Мощность двигателя Kia = {power} л.с.'


car = Car()
nissan_car = Nissan()
kia_car = Kia()

print(f'==== car ====\nprice = {car.price}\n{car.horse_powers(100)}')
print(f'==== nissan_car ====\nprice = {nissan_car.price}\n{nissan_car.horse_powers(336)}')
print(f'==== kia_car ====\nprice = {kia_car.price}\n{kia_car.horse_powers(210)}')
