import math
import os
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

dirname = os.path.dirname(__file__)

class LinR:

    def __init__(self, x, y, a, e) -> None:
        self.m = len(x)
        self.n = len(x[0]) + 1
        self.X = x
        for i in range(self.m):
            self.X[i].append(1)
        self.X = np.array(self.X)
        self.y = np.array(y)
        self.W = np.array([0] * self.n)
        self.a = a
        self.e = e

    def DCost(self):
        ret = []
        for d in range(self.n):
            res = 0
            for i in range(self.m):
                tmp = 0
                for j in range(self.n):
                    tmp += self.W[j] * self.X[i][j]
                res += (tmp - self.y[i]) * self.X[i][d]
            ret.append(res / self.m)
        return np.array(ret)

    def GradDescent(self):
        dJ = self.DCost()
        self.W = np.subtract(self.W, self.a * dJ)
        flag = np.any((dJ > self.e))

        while flag:
            dJ = self.DCost()
            self.W = np.subtract(self.W, self.a * dJ)
            flag = np.any((dJ > self.e))

        return self.W


class LogR:

    def __init__(self, x, y, a, e) -> None:
        self.m = len(x)
        self.n = len(x[0]) + 1
        self.X = x
        for i in range(self.m):
            self.X[i].append(1)
        self.X = np.array(self.X)
        self.y = np.array(y)
        self.W = np.array([0] * self.n)
        self.a = a
        self.e = e

    def DCost(self):
        ret = []
        for d in range(self.n):
            res = 0
            for i in range(self.m):
                tmp = 0
                for j in range(self.n):
                    tmp -= self.W[j] * self.X[i][j]
                res += ((1/(1 + math.exp(tmp))) - self.y[i]) * self.X[i][d]
            ret.append(res / self.m)
        return np.array(ret)

    def GradDescent(self):
        dJ = self.DCost()
        self.W = np.subtract(self.W, self.a * dJ)
        flag = np.any((dJ > self.e))

        while flag:
            dJ = self.DCost()
            self.W = np.subtract(self.W, self.a * dJ)
            flag = np.any((dJ > self.e))

        return self.W


def costlinr(x, y, w1, w2):
    res = 0
    for i in range(len(x)):
        tmp = 0
        for j in range(len(x[i])):
            tmp += (w1*x[i][j] + w2)
        res += (tmp - y[i])**2
    return res/(2*len(x))


def costlogr(x, y, w1, w2):
    res = 0
    for i in range(len(x)):
        tmp = 0
        for j in range(len(x[i])):
            tmp -= (w1*x[i][j] + w2)
        res += (-y[i]*math.log(1/(1 + math.exp(tmp))) - (1 - y[i])*math.log(1 - (1/(1 + math.exp(tmp)))))
    return res/(len(x))

filename = os.path.join(dirname, 'dataset.csv')
df = pd.read_csv(filename)
X = df.iloc[:, [0]].values.tolist()
y = list(df['Y'])

model1 = LinR(X, y, 0.00075, 0.001)
w = model1.GradDescent()
X_scatter = df['X'].values.tolist()
y_scatter = df['Y'].values.tolist()

X_line = np.array(X_scatter)
y_line = w[0]*X_line + w[1]

plt.plot(X_line, y_line, '-r')
plt.scatter(X_scatter, y_scatter)
plt.show()

w1 = np.linspace(50 ,-50,100 )
w2 = np.linspace(50 ,-50,100 )

X_plot, Y_plot = np.meshgrid(w1, w2)
J = []

for i in range(len(X_plot)):
    temp = []
    for j in range(len(X_plot[i])):
        temp.append(costlinr(X, y, X_plot[i][j], Y_plot[i][j]))
    J.append(temp)
J = np.array(J)
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.plot_surface(X_plot, Y_plot, J)

plt.contour(X_plot, Y_plot, J)
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Contour Plot - Linear Cost Function')
plt.show()

#######

model2 = LogR(X, y, 0.1, 0.0001)
w = model2.GradDescent()

w1 = np.linspace(0.1 ,0 ,100)
w2 = np.linspace(0.1 ,0 ,100)

X_plot, Y_plot = np.meshgrid(w1, w2)
J = []

for i in range(len(X_plot)):
    temp = []
    for j in range(len(X_plot[i])):
        temp.append(costlogr(X, y, X_plot[i][j], Y_plot[i][j]))
    J.append(temp)
J = np.array(J)
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.plot_surface(X_plot, Y_plot, J)

plt.contour(X_plot, Y_plot, J)
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Contour Plot - Cross Entropy Cost Function')
plt.show()