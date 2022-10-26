# exponent fn
num = int(input("Enter the number "))
num_terms = int(input("Enter the number of terms required "))

def exp(x,num_terms):
    cur = 1
    result  = 0
    for i in range (num_terms):
        result+= cur
        cur *= (x)/(i+1)
    
    return result

print(exp(num,num_terms))
