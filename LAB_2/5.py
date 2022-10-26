#sum of digits
num = input("Enter the number ")
def digitSum(num):
    num = str(num)
    result = 0
    for digit in num:
        result+= int(digit)
    
    return result

print(digitSum(num))