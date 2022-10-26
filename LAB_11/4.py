import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dirname = os.path.dirname(__file__)

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
                res += ((1/(1 + np.exp(tmp))) - self.y[i]) * self.X[i][d]
            ret.append(res / self.m)
        return np.array(ret)

    def GradDescent(self):
        dJ = self.DCost()
        self.W = np.subtract(self.W, self.a * dJ)
        flag = np.any((abs(dJ) > self.e))

        while flag:
            dJ = self.DCost()
            self.W = np.subtract(self.W, self.a * dJ)
            flag = np.any((abs(dJ) > self.e))

        return self.W

filename = os.path.join(dirname, 'Logistic_regression_ls.csv')
df = pd.read_csv(filename)

df0 = df[df['label'] == 0]
df1 = df[df['label'] == 1]
x0 = list(df0['x1'])
y0 = list(df0['x2'])
x1 = list(df1['x1'])
y1 = list(df1['x2'])

X = df.iloc[:, [0, 1]].values.tolist()
y = list(df['label'])


model = LogR(X, y, 0.1, 0.01)
w = model.GradDescent()


X1 = np.linspace(0, 10, 100)
X2 = np.subtract(-w[0]*X1/w[1], w[2]/w[1])

plt.plot(X1, X2)
plt.scatter(x0, y0)
plt.scatter(x1, y1)
plt.xlabel('X1')
plt.ylabel('X2')
plt.title('Decision Boundary')
plt.show()