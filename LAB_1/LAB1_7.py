string = "Light is faster than sound"
split_str = string.split()

modified_split = []

for index in range (len(split_str)):
    if index in [0,len(split_str)-1]:
        modified_split.append(split_str[index].upper())
    else: 
        modified_split.append(split_str[index].capitalize())

print(" ".join(modified_split))
