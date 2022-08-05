import random
ar = []

ln = random.randint(10,30)

#creating a list with 20 random values
for i in range (ln):
    ar.append(random.randint(0,100))

ar.sort()
if ln%2 == 0:
    median = ar[ln//2] + ar[ln//2 - 1]
else:
    median = ar[ln//2]

#splitting into multiple subgroups
if ln%2 == 0:
    ar1 = ar[:ln//2]
    ar2 = ar[ln//2: ]   
else:
    ar1 = ar[:ln//2 ]
    ar2 = ar[ln//2: ]


print(median)
print(ar1,ar2)