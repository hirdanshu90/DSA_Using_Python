class A:
    def feature1(self):
        print("Feature 1 working")

    def feature2(self):
        print("Feature 2 working")


class B(A):
    def feature3(self):
        print("Feature 3 working")

    def feature4(self):
        print("Feature 4 working")

class C(B):
    def feature5(self):
        print("Feature 5 working")

class D(B):
    def feature6(self):
        print("Feature 6 working")

a1 = A()

a1.feature1()
a1.feature2()

b1 = B()
b1.feature4()

c1 = C()
c1.feature5()

d1 = D()
d1.feature2()