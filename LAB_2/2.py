#a part
num1 = 12
num2 = 100
num3 = 41


print(max(num1,num2,num3))
ar = [num1,num2,num3]
ar.sort()
print(ar[-1])

# b part
# 2 conditional operators
if (num1 > num2):
    if(num1>num3):
        print(num1)
    else:
        print(num3)
else:
    if(num2>num3):
        print(num2)
    else:
        print(num3)

# 1 conditonal operator
maxi = num1 if (num1 > num2 and num1>num3) else (num3 if (num3 > num2 and num3>num1) else num2)
print(maxi)

