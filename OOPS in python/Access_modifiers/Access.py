class Student:
    def __init__(self,name,rollno,age):
        self.name = name    # public instance variable
        self._rollno = rollno # protected instance variable
        self.__age = age  # Private instance variable

    def display(self):   # private method
        print(f"Hi myself {self.name} from Student class and rollno is {self._rollno} and age is {self.__age}")

class Branch(Student):
    def show(self):
        print(f"My roll no is {self._rollno}")



b1 = Branch("Hir", 12,55)
b1.show()
b1.display()
