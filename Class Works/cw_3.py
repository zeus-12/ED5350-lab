lst=[1,2,4,5]
print(lst[1:3])
lst1=[2,4,5]
lst2=[lst,lst1]
print(type(lst2,),lst2)

lst=['vishnu','vinod','macbook','pro']
for item in lst:
  print(item,len(item))

"""list- mutable, concatenated,search, sort,deletion (using index or range of indices), conversion/other functions(str to ist, len, max, min , sum,)
shalow copy, deep copy
"""

lst=[1,3,5,7,6]
print(lst)
lst[0]=0
lst[2:4]=[4,8]
print(lst)

print('a' in ['a','b','e'])

lst=[1,2,3,6,3]
lst_s=sorted(lst)
print(lst)
print(lst_s)
del(lst_s[2])
print(lst_s)
del(lst_s[:])
print(lst_s)

print(max(list('Raman')))
print(ord('a'))
print(min(list('Raman')))
print(sorted(list('Raman')))
print(len(list('Raman')))

lst=[]
if not lst:
  print(True)

"""define a list of marks and print max, min, avg"""

lst=[4,5,7,10,9]
print("max- ",max(lst))
print("min- ",min(lst))
print("Avg- ",sum(lst)/len(lst))

"""append- at end
pop- remove last
remove- element
insert- after as certain position
sort- asc and desc
count
index

"""

lst=[4,6,7,3,2,3]
lst.append(5)
print(lst)
lst.pop()
print(lst)
lst.pop(3)
print(lst)
lst.sort()
print(lst)
lst.remove(7)
print(lst)
lst.insert(2,5)
print(lst)
print(lst.count(5))
print(lst.index(4))
lst.sort(reverse=True)
print(lst.reverse())