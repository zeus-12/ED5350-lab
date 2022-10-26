# Prime Number
def isPrime(num):
    if num == 1:
        return "None"
    i = 2
    while i in range (num):
        if num % i == 0:
            return False
        i += 1
    return True


print(isPrime(79))