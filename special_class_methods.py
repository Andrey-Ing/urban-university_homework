class House:
    def __init__(self):
        self.numberOfFloors = 0

    def setNewNumberOfFloors(self, floors):
        self.numberOfFloors = floors
        print(f"numberOfFloors = {floors}")


my_house = House()
print(f"Default number of floors in my house = {my_house.numberOfFloors}")
my_house.setNewNumberOfFloors(42)
print(f"Desired number of floors in my house = {my_house.numberOfFloors}")
