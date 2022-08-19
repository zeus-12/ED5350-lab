st = "heythere"
dct ={}

for item in st:
    if item not in dct.keys():
        dct[item] = 1
    else:
        dct[item] +=1

# first unique letter
for item in dct.keys():
    if dct[item] == 1:
        print(item)
        break

# remove duplicates w.o using set
new_str = ""
for item in st:
    if item not in new_str:
        new_str+= item

print(new_str)

# remove duplicates using set
sett = set(list(st))
print(sett)