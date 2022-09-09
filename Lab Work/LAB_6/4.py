class Base1:
    def __init__(self, real, imaginary):
        self.r = real
        self.i = imaginary

    def __add__(self, o):
        r1 = self.r + o.r
        r2 = self.i + o.i
        if r2 >= 0:
            return str(r1) + ' + i' + str(r2)
        else:
            return str(r1) + ' - i' + str(-1 * r2)

    def __sub__(self, o):
        r1 = self.r - o.i
        r2 = self.r - o.i
        if r2 >= 0:
            return str(r1) + ' + i' + str(r2)
        else:
            return str(r1) + ' - i' + str(-1*r2)

    def add(self, o):
        r1 = self.r + o.r
        r2 = self.i + o.i
        if r2 >= 0:
            return str(r1) + ' + i' + str(r2)
        else:
            return str(r1) + ' - i' + str(-1 * r2)

    def sub(self, o):
        r1 = self.r - o.r
        r2 = self.i - o.i
        if r2 >= 0:
            return str(r1) + ' + i' + str(r2)
        else:
            return str(r1) + ' - i' + str(-1*r2)


class Base2:
    def __init__(self, real, imaginary):
        self.r = real
        self.i = imaginary

    def __mul__(self, o):
        r1 = self.r*o.r - self.i*o.i
        r2 = self.r*o.i + self.i*o.r
        if r2 >= 0:
            return str(r1) + ' + i' + str(r2)
        else:
            return str(r1) + ' - i' + str(-1 * r2)

    def __floordiv__(self, o):
        r1 = (self.r*o.r + self.i*o.i)//(o.i*o.i + o.r*o.r)
        r2 = (self.i * o.r - self.r * o.i)//(o.i*o.i + o.r*o.r)
        if r2 >= 0:
            return str(r1) + ' + i' + str(r2)
        else:
            return str(r1) + ' - i' + str(-1 * r2)

    def __truediv__(self, o):
        r1 = (self.r * o.r + self.i * o.i) / (o.i * o.i + o.r * o.r)
        r2 = (self.i * o.r - self.r * o.i) / (o.i * o.i + o.r * o.r)
        if r2 >= 0:
            return str(r1) + ' + i' + str(r2)
        else:
            return str(r1) + ' - i' + str(-1 * r2)

    def mul(self, o):
        r1 = self.r*o.r - self.i*o.i
        r2 = self.r*o.i + self.i*o.r
        if r2 >= 0:
            return str(r1) + ' + i' + str(r2)
        else:
            return str(r1) + ' - i' + str(-1 * r2)

    def floordiv(self, o):
        r1 = (self.r*o.r + self.i*o.i)//(o.i*o.i + o.r*o.r)
        r2 = (self.i * o.r - self.r * o.i)//(o.i*o.i + o.r*o.r)
        if r2 >= 0:
            return str(r1) + ' + i' + str(r2)
        else:
            return str(r1) + ' - i' + str(-1 * r2)

    def truediv(self, o):
        r1 = (self.r * o.r + self.i * o.i) / (o.i * o.i + o.r * o.r)
        r2 = (self.i * o.r - self.r * o.i) / (o.i * o.i + o.r * o.r)
        if r2 >= 0:
            return str(r1) + ' + i' + str(r2)
        else:
            return str(r1) + ' - i' + str(-1 * r2)


class Base12(Base1, Base2):
    def __init__(self, real, imaginary):
        super().__init__(real, imaginary)


a = Base12(1, 2)
b = Base12(3, 4)
print("\nAddition\nOverloading :", a+b, "\nWithout Overloading :", a.add(b))
print("\nSubtraction\nOverloading :", a-b, "\nWithout Overloading :", a.sub(b))
print("\nMultiplication\nOverloading :", a*b, "\nWithout Overloading :", a.mul(b))
print("\nFloor Division\nOverloading :", a//b, "\nWithout Overloading :", a.floordiv(b))
print("\nDivision\nOverloading :", a/b, "\nWithout Overloading :", a.truediv(b))