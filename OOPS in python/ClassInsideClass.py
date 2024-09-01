class Student:

    def __init__(self,name,rollno):
        self.name = name
        self.rollno = rollno
        self.lap = self.Laptop(ram, cpu, brand)

    def show (self):
        print(f"Name is - {self.name} and roolno hai - {self.rollno} ")

    class Laptop:
        def __init__(self, ram, cpu, brand):
            self.ram = ram
            self.cpu = cpu
            self.brand = brand
        def print_details(self):
            print(f"Laptop details are -  {self.brand}, {self.cpu}, {self.ram}")


s1 = Student('Navim', 22)
s2 = Student("Hirdanshu", 55)
s2.show()

lap1 =s1.lap(6, "intel", "HP")





