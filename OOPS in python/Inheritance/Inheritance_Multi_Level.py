class Human:
    def __init__(self,num_heart):
        print("calling from Human")
        self.num_eyes = 2
        self.num_ears = 1
        self.num_heart = num_heart
    def eat(self):
        print("I can eat")
    def work(self):
        print("I can work")

class Male(Human):
    def __init__(self,num_heart,name):
        print("calling from Male")
        super().__init__(num_heart)
        self.name = name
    def sleep(self):
        print("I can sleep")
    def work(self):
        print("I can code")

class Boy(Male):
    def __init__(self,name,language,num_heart):
        super().__init__(name, num_heart)
        self.language = language
    def sleep(self):
        print("I can sleep")
    def work(self):
        super().work()
        print("I can test")

class Programmer(Boy):
    def work(self):
        print("I can code in Python")

boy_1 = Boy("Hir","Java",5)
boy_1.work()
print("eyes are ", boy_1.num_eyes)

# programmer_1 = Programmer()
# programmer_1.work()
# print("HEllo")