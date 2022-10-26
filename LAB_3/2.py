name= ("vishnu","pranoy","albin")
age=(12,14,16)
salary = (100,200,300)

# without using comprehension
lst=[]
for index in range(len(name)):
    lst.append((name[index],age[index],salary[index]))

tup1 = tuple(lst)
print(tup1)

# comprehension method
lst2 = [(name[i], age[i], salary[i]) for i in range(len(name))]
tup2 = list(lst2)
print(tup2)


#zip fn -- returns an iterator of tuples

lst3 = []
for item in zip(name,age, salary): 
    lst3.append(item)    

print(lst3)


