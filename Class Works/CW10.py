#classes inheritance
#'like a' relationship
"""
class Base:
    def __init__(self, name):
        self.name = name
        print('Inside the base class constructor')

    def printbase(self):
        print(self.name)

class Derived(Base):
    def __init__(self, roll, name):
        super().__init__(name)
        self.roll = roll
        print('Inside the derived class constructor')

    def printderived(self):
        print(self.roll)
        print(self.name)

d1 = Derived(50, 'S')
d1.printderived()
"""
#inheritance - key points
#construction of an object - from base to derived
#same thing for constructor - use super().__init__()
#derived class can access data/....
#types of inheritance - multilevel, multiple etc...
#multilevel - Derived1(Base), Derived2(Derived1)
#multiple - class Derived(Base1, Base2)

"""
class Derived1(Base):
    .
    .
    .
    .
class Derived2(Derived1):
    .
    .
"""
class Base1:
class Base2:
    def __init__(self, roll):
        self.roll = roll
        print('Inside base2 constructor')
    def printbase2(self):
        print('Inside base2 print')
        print(self.name)
    def printdata(self):
        print('Inside base2 printdata')
        print(self.name)
class Derived(Base1, Base2):
    def __init__(self, name, roll):
        Base1.__init__(self, name1)
        Base2.__init__(self, name2)
        print('Inside derived1 constructor')
    def printderived1(self):
        print('Inside derived1 print')
        print(self.name, Base2.name)
    def printdata(self):
        print('Inside derived printdata')
        print(self.name, self.name)
d1=Derived('Vishnu', 12345)



