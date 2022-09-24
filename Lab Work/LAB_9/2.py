import numpy as np
import matplotlib.pyplot as plt


def delJ(x, y):
    return 2*(x - 10), 2*(y - 10)


def J(x, y):
    return (x - 10)**2 + (y - 10)**2


def unidirectional(start, direction, a, b):
    d = (a + b)/1000000.0
    p1 = a
    p2 = p1 + d
    p3 = p2 + d

    while True:
        w1 = start + p1*direction
        w2 = start + p2*direction
        w3 = start + p3*direction

        if J(w1[0], w1[1]) >= J(w2[0], w2[1]) and J(w3[0], w3[1]) >= J(w2[0], w2[1]):
            bracket = [p1, p3]
            break
        else:
            if p3 > b:
                print("No Minima in given Range")
                return
            else:
                p1 = p2
                p2 = p3
                p3 += d

    p = (bracket[0] + bracket[1])/2
    w = start + p * direction
    x = np.arange(0, 50, 0.01)
    y = np.arange(0, 50, 0.01)

    X, Y = np.meshgrid(x, y)
    Z = J(X, Y)

    plt.contour(X, Y, Z)
    plt.scatter(w[0], w[1])
    plt.xlabel('W1')
    plt.ylabel('W2')
    plt.show()
    return p


print("Fixing Value of Alpha")
d = 0.0001
e = 10**(-10)
a, b = 2, 1

while True:
    c1, c2 = delJ(a, b)

    if abs(c1) > e and abs(c2) > e:
        a, b = a - d*c1, b - d*c2
    else:
        print("Critical Point at :", a, b)
        break

print("\nFinding Value of Alpha using Line Method")
a, b = 2, 1
while True:
    start = np.array([a, b])
    c1, c2 = delJ(a, b)
    direction = np.array([-c1, -c2])
    d = unidirectional(start, direction, 0, 100)

    if abs(c1) > e and abs(c2) > e:
        a, b = a - d*c1, b - d*c2
    else:
        print("Critical Point at :", a, b)
        break