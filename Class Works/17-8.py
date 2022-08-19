empty_set = set()
if not empty_set:
    print("Empty set is null")

seta = {1,2,3,4}
setb = set([1,2,3,4])

setc  = {1,2,"hello",1}

# print(seta,setb,setc)

setb = {6,7,8,9}
seta.update(setb)
print(seta)
# set comprehension
set_comprehension = {i for i in range (10)}
print(set_comprehension)

set1 = {1,2,4}
set2 = {3,5,1}



# mathematical set operation
# print(set1 - set2)
# print(set1 | set2)
# print(set1 & set2)
# print(set1 ^ set2)

set1 |= set2
print(set1)
