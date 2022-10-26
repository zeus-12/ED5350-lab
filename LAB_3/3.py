import random

lst= [random.randint(10,100) for i in range (20)]
print('random list generated',lst)


even_lst=[x for x in lst if x%2==0]
print('list of even numbers= ',even_lst)

odd_lst = [x for x in lst if x%2==1]
print('list of odd numbers= ',odd_lst)

multiple_3_lst = [x for x in lst if x%3==0]
print('list of numbers divisible by 3= ',multiple_3_lst)

