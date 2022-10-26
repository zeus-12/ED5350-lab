import numpy as np
import matplotlib.pyplot as plt


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
    w = start + p*direction
    print("Critical Point at", w)
    return w


s = np.array([2, 1])
d = np.array([2, 5])
res = unidirectional(s, d, 0, 100)
if res.all():
    m = J(res[0], res[1])
    print("Minimum Value of Function along given Direction :", m)

    x = np.arange(0, 100, 0.01)
    y = np.arange(0, 100, 0.01)
    a = np.arange(0, 10, 0.01)
    x1 = s[0] + a*d[0]
    y1 = s[1] + a*d[1]

    X, Y = np.meshgrid(x, y)
    Z = J(X, Y)
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(X, Y, Z)
    ax.set_xlabel('W1')
    ax.set_ylabel('W2')
    ax.set_zlabel('J')
    plt.show()

    plt.contour(X, Y, Z)
    plt.plot(x1, y1)
    plt.scatter(res[0], res[1])
    plt.xlabel('W1')
    plt.ylabel('W2')
    plt.show()

# No, the search direction is not a gradient descent one because the negative of gradient at the given point does not match the given direction