class Computer:
    # Define: 
    # Attributes - these are variables
    # Behaviour - These are Methods or Functions
    # cpu and ram are arguments here. 

    def __init__(self, cpu, ram) -> None:
        print("In init")
        self.cpu = cpu
        self.ram = ram

    def config(self):
        print("Specifications", self.cpu, self.ram, "GB")

    def compare(self, other):
        if self.ram == other.ram:
            return "They have the same RAM"
        else:
            return "They have different RAM"

# Creating two Computer objects
com1 = Computer('i5', 8)
com1.config()

com2 = Computer('i8', 32)

# Correctly comparing the two Computer objects
comparison_result = com2.compare(com1)
print(comparison_result)  # Outputs: They have different RAM