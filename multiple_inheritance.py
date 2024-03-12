class Vehicle:
    vehicle_type = 'none'


class Car:
    price = 1000000

    def horse_powers(self):
        return f'Мощность двигателя неизвестна'


class Nissan(Vehicle, Car):
    price = 13000000
    vehicle_type = 'Car'

    def horse_powers(self):
        return f'Мощность двигателя Nissan 758 л.с.'


my_car = Nissan()
print(f'Тип транспортного средства {my_car.vehicle_type}, цена {my_car.price}')
