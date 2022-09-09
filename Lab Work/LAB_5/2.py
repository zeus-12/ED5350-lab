# factorial
n = int(input("Enter number to find the factorial "))

def fact_loop(n):
    fact_1 = 1
    for item in range (1,n+1):
        fact_1 *= item
    return fact_1

def fact_recursion(n):
    if n ==1 :
        return 1

    return n*fact_recursion(n-1)

print(fact_loop(n),fact_recursion(n))

# fibonacci series
fib_i = int(input("Find the number to find the fib sequence "))


def fib_loop(n):
    f,s=0,1                                         

    for x in range(1,n):
        next=f+s                           
        f=s
        s=next

    return s

def fib_recursion(n):
    if n ==1 or n==2:
        return 1

    return fib_recursion(n-1) + fib_recursion(n-2)


print(fib_loop(fib_i),fib_recursion(fib_i))