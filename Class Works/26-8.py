def sum_n(n):
    sum = 0
    for i in range(1,n+1):
        sum+=i
    return sum    
print(sum_n(10))

def factorial(n):
    if n==1:
        return 1
    return n*factorial(n-1)

print(factorial(5))

#  lambda function -
#  - Used for for short functional body
#  - "anonymous function"

avg = lambda *args: sum(args)/len(args)
print(avg(23,234,23,4,234,32,1))

fn = lambda x,y: x+y
print(fn(3,5))

lst = [1,5,2,8,3]

# sorted_list = sorted(lst ,key=lambda a:a-b)
# print(sorted_list)

dct = {"a":1,"h":7,"e":5,"z":6,"d":4}
# for key in dct.items():

print(sorted(dct.items(), key=lambda item: item[1]))


lst1 = [1,2,3,4]
squared_lst1 = list(map(lambda x:x**2, lst1))
print(squared_lst1)

# returns only the cases which satisfied the condition
filtered_lst1 = list(filter(lambda x:x==1,lst1))
print(filtered_lst1)

# reduced_lst1 = list(reduce())