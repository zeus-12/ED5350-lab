nestdict={'vishnu':{'vinod':20,'abcd':36},'efgh':{'ijk':18,'lmno':35}}
for i in nestdict.keys():
  print(i)
for v in nestdict.values():
  print(v,type(v))
  for k in v.keys():
    print(k,v[k])
for v in nestdict.values():
  print(*v)

  nestdict1={**nestdict}
print(nestdict1)

lst1=['a','b','c']
lst2=[1,2,3]
dct3={k:v for k,v in zip(lst1,lst2)}
print(dct3,type(dct3))

dct2={key:value for (key,value) in dct3.items()}

print(dct2,type(dct2))