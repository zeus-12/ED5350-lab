mat1=[[1,2,3],[4,5,6]]
mat2=[[5,6,7],[1,2,3]]
it = zip(mat1,mat2)
print(*it)
for it in zip(mat1,mat2):
    print(it)
    for it1 in zip(*it):
        print(sum(it1))

# comprehension
lst=[[sum(it1) for it1 in zip(*it)] for it in zip(mat1,mat2)]
print(lst)

lst=[[it1[0]-it1[1] for it1 in zip(*it)] for it in zip(mat1,mat2)]
print(lst)

#dictionaries
#dc2={} #empty dictionary
dict1={20 : 100, 10 : 50, 50 : 250}
for k in dict1:
    print(k)
for v in dict1.items():
    print(v)

for k in dict1.keys():
    print(k)

for k in dict1.values():
    print(k)
#define a dictionary and print all its values using the corresponding keys
dict={'a': 1,'b' : 2, 'c' : 3,'d' : 4, 'e' : 5}
for k in dict.keys():
    print(k,dict[k])