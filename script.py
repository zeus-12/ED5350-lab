## Raw strings & multi-line strings
rawstr = 'i\m learning python now'
print(rawstr)

rawstr1 = r"I\'m learning python now"
print(rawstr1, '\n' , rawstr1)



a = 'hey'
b = "hey"
c = '''hello'''
d = """hey"""

print(a,b,c,d)

multi1 = '''this is a multi
line code'''

multi2 = """this is another
multi line code"""

print(multi1, "\n",multi2)

# string 
str1 = 'hello'
print(str1[0])
print(str1[-1])

#string slicing
print(str1[::-1])

## Pointer
a = 5
b = 5
print(id(a), "\n",id(b))

# check for substring
print('el' in 'Hello')

str = 'Hello '
print(str.swapcase())

#Split Fn

##find out the diff bw a string fn and a partition fn
## write a program, spplit it at diff locations, 1) blank, 2) slash , 3) double slash

string = " /  //  //  / "
print(string.split(' '))
print(string.split('/'))
print(string.split('//'))