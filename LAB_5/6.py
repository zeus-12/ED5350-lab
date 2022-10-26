import functools
 
# using map
lst1 = [1,2,3,4]
squared_lst1 = list(map(lambda x:x**2, lst1))
print(squared_lst1)

# returns only the cases which satisfied the condition -- filter
filtered_lst1 = list(filter(lambda x:x!=1,lst1))
print(filtered_lst1)

# reduce
# using reduce to compute sum of list
print(functools.reduce(lambda a, b: a+b, lst1))
