# sinx
num = int(input("Enter the number "))
num_terms = int(input("Enter the number of terms required "))

def sin(x,num_terms):
    cur = x
    result  = 0
    for i in range (0,num_terms+2,2):
        result+= cur
        cur *=  (-1)*(x ** 2)/((i+2)*(i+3))
    
    return result

print(sin(num,num_terms))
