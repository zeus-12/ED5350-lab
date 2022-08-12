tup1 = ('Vishnu', 8, 7, 77 ,678)
tup2 = ('Dravid', 7, 17, 77 ,279)
tup = tup1 + tup2
print(ele for ele in tup)

names = ('Dravid', 'Sachin', 'Mithali')
gender = ('Male', 'Male', 'Female')

for n in names:
    print(n)

for n in gender:
    print(n)

lst = []

for index in range(len(names)):
    lst.append((names[index],gender[index]))

print(lst)

tup = tuple(lst)
print(tup)

tups = [(names[i], gender[i]) for i in range(len(names))]
print(tups)


# zip() function - grouping can be achieved by zip() function
# it returns an iterator of tuples

ite = zip(names, gender)  #important
print(*ite)

for ite1 in zip(names,gender):   #important
    print (ite1, *ite1)

# in python ite->next is actually notated as ite.__next__() which is a dunderscore or double underscore

# HW - WAP to print the transpose of a matrix

mat1 = ([1,2,3,4],[5,6,7,8])
print(mat1)
print(*mat1)

# ite = zip(mat1[0],mat1[1])
ite = zip(*mat1)
print(*ite)

lst = list(ite)
print(lst)   #print iterates to ite in line 47