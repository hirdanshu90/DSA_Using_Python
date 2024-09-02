class Human:
    def __init__(self, num_heart):
        self.num_eyes = 2
        self.num_ears = 1
        self.num_heart = num_heart
    def eat(self):
        print("I can eat")
    def work(self):
        print("I can work")

class Male(Human):
    def __init__(self,name,heart):
        super().__init__(heart)
        self.name = name
    def flirt(self):
        print("I can flirt")
    def work(self):
        super().work()
        print("I can code")
    def display(self):
        print(f"Hi I am {self.name} and I have {self.num_heart} heart. bas....")
        return 


male_1 = Male("Hir", 1)
male_1.work()
male_1.eat()
print("eyes are ", male_1.num_eyes)
print("Name ", male_1.name)
print("heart are ", male_1.num_heart)
male_1.display()
