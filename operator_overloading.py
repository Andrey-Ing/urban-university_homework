class Building:
    def __init__(self, number_of_floors=0, building_type=None):
        self.numberOfFloors = number_of_floors
        self.buildingType = building_type

    def __eq__(self, building):
        return (self.numberOfFloors == building.numberOfFloors) &\
               (self.buildingType == building.buildingType)


build_1 = Building()
build_2 = Building(5, 'brick')
build_3 = Building(5, 'tree')
build_4 = Building(5, 'brick')

print(f"Здание build_1 такое же, как и build_1 - {build_1 == build_1}")
print(f"Здание build_1 такое же, как и build_2 - {build_1 == build_2}")
print(f"Здание build_2 такое же, как и build_3 - {build_2 == build_3}")
print(f"Здание build_2 такое же, как и build_4 - {build_2 == build_4}")
