class Student:

    def __init__(self,name,rollno):
        self.name = name
        self.rollno = rollno

    def show (self):
        print(f"Name is - {self.name} and roolno hai - {self.rollno} ")


s1 = Student('Navim', 22)
s2 = Student("Hirdanshu", 55)
s2.show()





