#list of lists
a=[1,2,3,4,5]
b=[11,12,13,14,15]
c=[a,b]
print('list of lists',c)

#individual elements accessing
print('some list elements: ',c[0][0],c[1][0],c[0][4])

#list unpacked
x=[1,2,3,4]
y=[10,11,*x,13]
print('unpacked list', y, type(y))

s='Sharath'
l=[*s]
print('unpacking of a string to a list',l)

#list comprehension
lst=[num for num in range(10)]
print('list created using list comprehension= ',lst)

#the above is equivalent to the following
lst=[]
for num in range(10):
    lst.append(num)
print('list created without list comprehension= ',lst)

import random
lst1=[random.randint(10,100) for num in range(10)]
print('list created= ',lst1)

lst2=[[x,x**2,x**3]for x in range(10)]
print('list of lists with squares and cubes= ',lst2)

#use if condition in comprehension
lst3=[x for x in range(20) if x%2==0]
print('list of even numbers less than 10= ',lst3)

lst4=[x for x in range(20) if x%2==0 if x>10 and x<15]
print('list of even numbers greater than 10 but less than 15= ',lst4)


#ifelse
al_list=[]
for alph in 'alphabet':
    if alph in 'aeiou':
        al_list.append(alph)
    else:
        al_list.append('!')

print(al_list)

al_list=[]
al_list=['!' if alph not in 'aeiou' else alph for alph in 'alphabet']

arr=[[1,2,3,4],[5,6,7,8]]
print(arr[0])
for ele in arr:
    for num in ele:
        print(num)

lst=[num for ele in arr for num in ele]
print(lst)