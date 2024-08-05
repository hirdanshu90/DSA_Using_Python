class Computer:
    # Define : 
    # Attributes - these are variables
    #  Behaviour - These are Methods or Functions
    # cpu and ram are arguments here. 

    def __init__(self, cpu, ram) -> None:
        print("In init")
        self.cpu = cpu
        self.ram = ram

    def config(self):
        print("Specifications", self.cpu, self.ram, "gb")

    def compare(self, other):
        if self.ram == other.ram:
            return f"They have same ram"
        else:
            return f"Different ram hai bhidu"


com1 = Computer('i5', 8)
com1.config()

com2 = Computer("i8", 32)
com2.compare(com1.ram)



