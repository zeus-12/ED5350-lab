# cosx
num = int(input("Enter the number "))
num_terms = int(input("Enter the number of terms required "))

def cos(x,num_terms):
    cur = 1
    result  = 0
    for i in range (0,num_terms+2,2):
        result+= cur
        cur *=  (-1)*(x ** 2)/((i+1)*(i+2))
    
    return result

print(cos(num,num_terms))