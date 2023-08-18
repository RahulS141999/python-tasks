class A:
    def car(self):
        print("class A's car method")

class B(A):
    def car(self):
        print("class B's car method")

class C(A):
    def car(self):
        print("class C's car method")

class D(B,C):
    pass
        
d = D()
d.car()
