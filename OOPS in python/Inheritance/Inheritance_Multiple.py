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

class Male:
    def __init__(self,name):
        print("calling from Male")
        self.name = name
    def flirt(self):
        print("I can flirt")
    def work(self):
        print("I can code")


class Boy(Human,Male):
    def __init__(self,name,language,num_heart):
        Human.__init__(self,num_heart)
        Male.__init__(self,name)
        self.language = language
    def sleep(self):
        print("I can sleep")
    def work(self):
        print("I can test")


boy_1 = Boy("Hir", "Python",3)
print("Ears hai ", boy_1.num_ears)
print("Language aati hai", boy_1.name)
print("Mro hai", Boy.mro())



