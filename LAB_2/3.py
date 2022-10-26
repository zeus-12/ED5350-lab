# Continue statement - used to skip a particular iteration
def sequence():
    i = -1
    while i < 10:
        i+=1
        if i%2 == 0:
            print(i, end=' ')
        else:
            continue

sequence()