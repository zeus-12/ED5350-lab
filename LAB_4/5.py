a = {"a":10,"b":30,"c":85,"d":72}
b = {"a":20,"d":12,"x":82,"w":67}

c = {}

for item in a.keys():
    if item not in c.keys():
        c[item] = a[item]
    else:
        c[item] += a[item]

for item in b.keys():
    if item not in c.keys():
        c[item] = b[item]
    else:
        c[item] += b[item]


print(c)

# all unique values in C by using set.
sett = set()
for item in c.values():
    sett.add(item)

print(sett)