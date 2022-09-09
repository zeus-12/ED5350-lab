# classwork sept 1
class Department:
    def __init__(self, dname='EnggDesign'):
        self._deptname = dname

    def print_dept(self):
        print(self._deptname)

class Faculty:
    def __init__(self, dept, fname = 'Vishnu', fid):
        self._fname = fname
        self._fid = fid
        self._dobj = Department(dept)

    def print_faculty(self):
        print(self._fname, self._fid,self._dobj)
        

f1 = Faculty('Engg.Design', 'Ramanathan', '12')
f1.print_faculty()



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
    def __sub__(self,other):
        C = Complex()
        C._real = self._real - other._real
        C._imag = self._imag - other._imag
        return C



C1 = Complex(4,5)
C1.PrintComplex()
C2 = Complex(10,12)
C2.PrintComplex()
C3 = C1.AddComplex(C2)
C3.PrintComplex()
C4 = C1 + C2 #the dunderscored __add__ will now be used for the '+' operator
C4.PrintComplex()
C5 = C1.SubComplex(C2)
C5.PrintComplex()
C6 = C1 - C2
C6.PrintComplex()
#homework - build a class for matrix
#hw - find a list of operators that can be overloaded

import math
class CMV:
    count = 0
    def __init__(self, n = '', s = 0, c = ''):
        self._name = n
        self._size = s
        self._color = c
        CMV.count +=1

    def display(self):
        print(CMV.count)

c1 = CMV('S', 1, 'B')
print(CMV.count)
c2 = CMV('S', 1, 'B')
print(CMV.count)
CMV.display(c1)
CMV.display(c2)

#dynamic creation of attributes


#class containership and class inheritance -> two important aspects of class
#class containership


