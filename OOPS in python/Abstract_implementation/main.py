# All are similar kind of objects
from abstract_class import Vehicle
class Bike(Vehicle):
    def __init__(self,n,color):
        super().__init__(n)
        self.color = color
    def start(self):
        print("start with kick")

class Scooty(Vehicle):
    def __init__(self,n):
        self.no_of_tyres = n
    def start(self):
        print("self start")

class Car(Vehicle):
    def __init__(self,n,gears):
        self.no_of_tyres = n
        self.gears = gears
    def start(self):
        print("start with key")

