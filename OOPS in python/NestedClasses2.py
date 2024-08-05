class Student:
    def __init__(self, name, rollno):
        self.name = name
        self.rollno = rollno
        self.lap = None  # Initialize with None

    def show(self):
        print(f"Name is - {self.name} and roll no is - {self.rollno}")
        if self.lap:
            self.lap.show()  # Show laptop details if available

    def set_laptop(self, ram, cpu, brand):
        self.lap = self.Laptop(ram, cpu, brand)  # Set laptop details

    class Laptop:
        def __init__(self, ram, cpu, brand):
            self.ram = ram
            self.cpu = cpu
            self.brand = brand

        def show(self):
            print(f"Laptop details are - {self.brand}, {self.cpu}, {self.ram} GB RAM")

# Create Student objects
s1 = Student('Navim', 22)
s2 = Student("Hirdanshu", 55)

# Set laptop details separately
s1.set_laptop(16, "Intel", "Dell")
s2.set_laptop(8, "AMD", "HP")

# Display student and laptop information
s1.show()
s2.show()