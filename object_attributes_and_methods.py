class House:
    pass


House.numberOfFloors = 10

for floor in range(1, House.numberOfFloors+1):
    print(f'Текущий этаж равен {floor}')
