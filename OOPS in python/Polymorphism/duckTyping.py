class Pycharm:
    def execute(self):
        print("Compiling")
        print("Running")

class Vscode:
    def execute(self):
        print("Spell check")
        print("some Check")
        print("Compiling")
        print("Running")

class Laptop:
    def code(self,ide):
        ide.execute()


ide = Vscode()
lap1 = Laptop()
lap1.code(ide)
