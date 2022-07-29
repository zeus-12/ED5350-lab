# WAP to generate 5 random numbers and use them in the arithmetic operators. Also, make use of 'seed' value. 
import random
random.seed(5)
n1 = random.randint(0, 10)

n2 = random.randint(0, 10)
n3 = random.randint(0, 10)
n4 = random.randint(0, 10)

random.seed(5)
n5 = random.randint(0, 10)
#numbers with the same seed always has the same value

print((n1 + n2 )/ n3 + (n4 - n5) )