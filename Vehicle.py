class Plane:
    def Move(self):
        return "Flying!"

class Car:
    def Move(self):
        return "Driving!"
class Boat:
    def Move(self):
        return "Sailing!"
class Truck:
    def Move(self):
        return "Hauling!"
for Transportations in [Plane(), Car(), Boat(), Truck()]:
    print(Transportations.Move())