class Instructor():
    height = 5
    def __init__(self,name, age):
        self.name = name
        self.age = age
        self.sport = None
    def name_age(self, cash):
        return f"name and age are: {self.name} and {self.age} and cash hai {cash}"
    def school(self, school):
        return f"school hai {school}"


instructor_1 = Instructor("Jenny", 44)
print(instructor_1.name_age(10000))
print(instructor_1.school("Infosys"))
