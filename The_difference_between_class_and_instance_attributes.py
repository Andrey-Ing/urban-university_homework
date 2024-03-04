class Buiding:
    total = 0

    def __init__(self):
        Buiding.total += 1
        self.number = Buiding.total


building_list = []
for i in range(40):
    building_list.append(Buiding())
    print(f'Я объект Buiding № {building_list[i].total}')

print('#####\n', f'Всего нас создано {Buiding.total}')
