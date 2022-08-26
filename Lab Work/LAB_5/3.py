x = int(input("Enter X "))
power = int(input("Enter Power "))

def exponent(x,power):
    if power == 0:
        return 1
    
    result = 1

    for i in range (abs(power)):
        result *= x

    if power < 0:
        return 1/result
    else:
        return result

print(exponent(x,power))