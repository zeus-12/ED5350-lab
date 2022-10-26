# Query for 2 integers N and M from the user where 0<=N<=100 and 0<=M<=9. These will be the inputs to your function. Using recursion, compute the number of times the integer M occurs in all non-negative integers less than or equal to N. 

N = int(input("Enter N ,0<=N<=100 "))
M = int(input("Enter M ,0<=M<=9 "))

def count_nums(n,m):
    if n == 0:
        if m == 0:
            return 1
        return 0

    elif str(m) in str(n):
        return list(str(n)).count(str(m)) + count_nums(n-1,m)

    else:
        return count_nums(n-1,m)


print(count_nums(N,M))
