orders  = [ "biryani","rice","biryani","biryani","rice","biryani","rice","porotta","rice","roti","roti"]
dct = {}

for item in orders:
    if item not in dct.keys():
        dct[item] = 1
    else:
        dct[item] +=1

# to find max
max_value= max(dct.values())

res = []

for item in dct.keys():
    if dct[item] == max_value:
        res.append(item)

# sorting to get the lexicographically smaller food 
res.sort()
print(res[0])
        

