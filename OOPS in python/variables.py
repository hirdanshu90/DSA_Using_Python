class Car:
    wheels = 4
    def __init__(self,brand, com):
        self.brand = brand
        self.com = com

    def print(self):
        print(f"{self.brand} is {self.com}")

    

c1 = Car("BMW", "FORD" )
c2 = Car("Maruti", "Suzuki")

c1.print()
c2.print()