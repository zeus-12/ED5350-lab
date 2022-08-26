# args and kargs should always be the last parameters
def kwvar_arg(**kwargs):
    for k,v in kwargs.items():
        print(k,v)

kwvar_arg(i=10, a=70)

def var_arg(*args):
    for item in args:
        print(item)

var_arg(18,62,2)

def pos_arg(a,b, *args):
    print("positional args are ",a,b)
    for item in args:
        print(item)

pos_arg(1,3,"a","b")

# default argument type
def funcname(i, check = True):
    print(i, check)

funcname(5)
funcname(8,False)

# recursion
def PrintNum(n):
    if n < 1:
        return
    print(n)
    PrintNum(n-1)

PrintNum(5)

# sum of n
def sum_n(n):
    if n==0:
        return 0
    
    return sum_n(n-1)+n

print(sum_n(10))


# lamba
avg = lambda a,b : (a+b)/2
print(avg(1,4))

