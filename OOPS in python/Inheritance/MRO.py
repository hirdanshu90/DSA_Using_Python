class A:
    def __init__(self):
        print("A's __init__")

class B(A):
    def __init__(self):
        super().__init__()
        print("B's __init__")

class C(A):
    def __init__(self):
        super().__init__()
        print("C's __init__")

class D(B,C):
    def __init__(self):
        super().__init__()
        print("D's __init__")      

class E(D,C):
    def __init__(self):
        super().__init__()
        print("E's __init__")

e = E()
print(E.mro())