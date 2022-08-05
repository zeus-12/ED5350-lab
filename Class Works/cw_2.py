a = input('Enter the number a')
b = input('Enter the number b')
c = input('Enter the number c')

#using relational and logical

if a<b and a<c:
    print ('a is the smallest')
elif b<c:
    print ('b is the smallest')  
else:
    print('c is the smallest')

if(a<b):
    if(a<c):
        print ('a is the smallest')
    else:
        print ('c is the smallest')
else:
    print ('b is the smallest')

if a<b<c or a<c<b:
    print('a is the smallest')
elif b<c:
    print('b is the smallest')
else:
    print('c is the smallest')

#using conditional expression find largest of a and b
max = a if a>b else b
max1 = max if max>c else c
print(max)

# qn
a = 10
b =5

print(a!= b!= a)

for i in range(0,10,1):
    print(i)
    i = 20

for i in range(0,10,1):
    i = 20
    print(i)

#why value of i does not get renewed

#i = 0
#for i<10:       #it is not a iterable
#    i = i +1
#    print(i)


