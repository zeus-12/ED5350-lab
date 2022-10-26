class Complex:
    def __init__(self, re=0, im = 0):
        self._real = re
        self._imag = im

    def PrintComplex(self):
        print(self._real,'+ i', self._imag)

    def AddComplex(self, other): #whenever calling two , self gets C1 and C2 gets C2
        C = Complex()
        C._real = self._real + other._real
        C._imag = self._imag + other._imag
        return C

# operator overloading
    def __add__(self, other): #whenever calling two , self gets C1 and C2 gets C2
        C = Complex()
        C._real = self._real + other._real
        C._imag = self._imag + other._imag
        return C

    def SubComplex(self, other):
        C = Complex()
        C._real = self._real - other._real
        C._imag = self._imag - other._imag
        return C

# operator overloading
    def __sub__(self,other):
        C = Complex()
        C._real = self._real - other._real
        C._imag = self._imag - other._imag
        return C


    def MultiComplex(self, other):
        C = Complex()
        C._real = self._real * other._real
        C._imag = self._imag * other._imag
        return C


# operator overloading
    def __mul__(self,other):
        C = Complex()
        C._real = self._real * other._real
        C._imag = self._imag * other._imag
        return C


    def DiviComplex(self, other):
        C = Complex()
        C._real = self._real / other._real
        C._imag = self._imag / other._imag
        return C

# operator overloading
    def __truediv__(self,other):
        C = Complex()
        C._real = self._real / other._real
        C._imag = self._imag / other._imag
        return C

            
    def FloorDivComplex(self,other):
        C = Complex()
        C._real = self._real // other._real
        C._imag = self._imag // other._imag
        return C

# operator overloading
    def __floordiv__(self,other):
        C = Complex()
        C._real = self._real // other._real
        C._imag = self._imag // other._imag
        return C


C1 = Complex(4,15)
C1.PrintComplex()

C2 = Complex(10,12)

C3 = C1.AddComplex(C2)
C3.PrintComplex()

C4 = C1 + C2 #the dunderscored __add__ will now be used for the '+' operator
C4.PrintComplex()

C5 = C1.SubComplex(C2)
C5.PrintComplex()

C6 = C1 - C2
C6.PrintComplex()

C7 = C1.MultiComplex(C2)
C7.PrintComplex()

C8 = C1 * C2
C8.PrintComplex()

C9 = C1.DiviComplex(C2)
C9.PrintComplex()

C10 = C1 // C2
C10.PrintComplex()

C11 = C1 / C2
C11.PrintComplex()

C13 = C1.FloorDivComplex(C2)
C13.PrintComplex()

C12 = C1 // C2
C12.PrintComplex()
