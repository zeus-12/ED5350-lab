import os
import numpy as np
import pandas as pd
import random
import matplotlib.pyplot as plt

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'data.csv')

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

x1 = []
d = {}

for i in range(10):
    x1.append([random.randint(1, 5), random.randint(1, 5), 0])
    x1.append([random.randint(9, 13), random.randint(9, 13), 1])
    
df = pd.DataFrame(x1, columns=['x', 'y', 'target'])
df.to_csv(filename, index=False)

df = pd.read_csv(filename)
df_train = df[:int(0.7*len(df))]
df_test = df[int(0.7*len(df)):]
X = df_train.iloc[:, [0, 1]].values.tolist()
y = list(df_train['target'])

model = LogR(X, y, 0.5, 0.0001)
w = model.GradDescent()

df0 = df_train[df_train['target'] == 0]
df1 = df_train[df_train['target'] == 1]

x0 = list(df0['x'])
y0 = list(df0['y'])
x1 = list(df1['x'])
y1 = list(df1['y'])

X1 = np.linspace(0, 10, 100)
X2 = np.subtract(-w[0]*X1/w[1], w[2]/w[1])

plt.plot(X1, X2)
plt.scatter(x0, y0)
plt.scatter(x1, y1)
plt.xlabel('X1')
plt.ylabel('X2')
plt.title('Decision-Boundary')
plt.show()


X = df_test.iloc[:, [0, 1]].values.tolist()
y = list(df_test['target'])
y_predicted = []

for i in range(len(X)):
    tmp = np.dot(w, [X[i][0], X[i][1], 1])
    if tmp < 0:
        y_predicted.append(0)
    else:
        y_predicted.append(1)

conf_matrix = {}
for i in range(len(y)):
    if y[i] == y_predicted[i]:
        if y[i] == 1:
            conf_matrix['TP'] = conf_matrix.get('TP', 0) + 1
        else:
            conf_matrix['TN'] = conf_matrix.get('TN', 0) + 1
    else:
        if y[i] == 1:
            conf_matrix['FN'] = conf_matrix.get('FN', 0) + 1
        else:
            conf_matrix['FP'] = conf_matrix.get('FP', 0) + 1

P = conf_matrix.get('TP', 0)/(conf_matrix.get('TP', 0) + conf_matrix.get('FP', 0))
R = conf_matrix.get('TP', 0)/(conf_matrix.get('TP', 0) + conf_matrix.get('FN', 0))
F = 2*P*R/(P+R)
A = (conf_matrix.get('TP', 0) + conf_matrix.get('TN', 0))/(conf_matrix.get('TP', 0) + conf_matrix.get('FN', 0) + conf_matrix.get('TN', 0) + conf_matrix.get('FP', 0))


print("Precision :", P)
print("Recall :", R)
print("F1 Score :", F)
print("Accuracy :", A)
