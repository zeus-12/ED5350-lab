import pandas as pd
import numpy as np
import os


class NeuralNetwork:
    def __init__(self, hl, X, y) -> None:
        self.hidden = hl
        self.X = X.T
        self.size = len(self.X)
        self.m = len(self.X[0])
        self.y = y
        self.W = {}

        for i in range(self.hidden + 1):
            if i == 0:
                self.W[i] = np.random.rand(self.size + 1, self.size)
            elif i == self.hidden:
                self.W[i] = np.random.rand(1, self.size + 1)
            else:
                self.W[i] = np.random.rand(self.size + 1, self.size + 1)

        self.b = {}
        self.A = {}
        self.Z = {}

        for i in range(self.hidden + 1):
            if i == self.hidden:
                self.b[i] = np.random.rand(1, 1)
            else:
                self.b[i] = np.random.rand(self.size + 1, 1)
        for i in range(self.hidden + 1):
            if i == 0:
                self.Z[i] = np.dot(self.W[i], self.X) + self.b[i]
                self.A[i] = 1/(1 + np.exp(-1*self.Z[i]))
            else:
                self.Z[i] = np.dot(self.W[i], self.A[i-1]) + self.b[i]
                self.A[i] = 1/(1 + np.exp(-1*self.Z[i]))
        
        self.c = False
        self.dj = {}
        self.db = {}
        self.flag = {}

        for i in range(self.hidden + 1):
            if i == 0:
                self.dj[i] = np.dot((self.A[self.hidden] - self.y), self.X.T)/self.m
            else:
                self.dj[i] = np.dot((self.A[self.hidden] - self.y), self.A[i-1].T)/self.m
            self.db[i] = np.sum(self.A[self.hidden] - self.y, axis=1, keepdims=True)/self.m
            self.flag[i] = np.any(abs(self.dj[i]) > 0.001)
            self.c = self.c or self.flag[i]
        
        if self.c:
            for i in range(self.hidden + 1):
                if self.flag[i]:
                    self.W[i] -= 0.1*self.dj[i]
                    self.b[i] -= 0.1*self.db[i]
        
    def fit(self):
        while self.c:
            self.c = False
            for i in range(self.hidden + 1):
                if i == 0:
                    self.Z[i] = np.dot(self.W[i], self.X) + self.b[i]
                    self.A[i] = 1/(1 + np.exp(-1*self.Z[i]))
                else:
                    self.Z[i] = np.dot(self.W[i], self.A[i-1]) + self.b[i]
                    self.A[i] = 1/(1 + np.exp(-1*self.Z[i]))
                    
            for i in range(self.hidden + 1):
                if i == 0:
                    self.dj[i] = np.dot((self.A[self.hidden] - self.y), self.X.T)/self.m
                else:
                    self.dj[i] = np.dot((self.A[self.hidden] - self.y), self.A[i-1].T)/self.m
                self.db[i] = np.sum(self.A[self.hidden] - self.y, axis=1, keepdims=True)/self.m
                self.flag[i] = np.any(abs(self.dj[i]) > 0.3)
                self.c = self.c or self.flag[i]
            
            
            for i in range(self.hidden + 1):
                self.W[i] -= 0.00001*self.dj[i]
                self.b[i] -= 0.00001*self.db[i]
            print(self.dj)
    
    def predict(self, x):
        xi = x.T
        xj = 1/(1 + np.exp(-1*(np.dot(self.W[0], xi) + self.b[0])))
        res = 1/(1 + np.exp(-1*(np.dot(self.W[self.size-1], xj) + self.b[self.size-1])))
        for i in range(len(res[0])):
            if res[0][i] < 0.5:
                res[0][i] = 0
            else:
                res[0][i] = 1
        return res

dirname = os.path.dirname(__file__)    
filename = os.path.join(dirname, 'logistic_regression_dataset.csv')
df = pd.read_csv(filename)

df_train = df[:int(0.7*len(df))]
df_test = df[int(0.7*len(df)):]

X_train = np.array(df_train.iloc[:, [0, 1]].values.tolist())
y_train = np.array([df_train['label']])

X_test = np.array(df_test.iloc[:, [0, 1]].values.tolist())
y_test = np.array([df_test['label']])

model = NeuralNetwork(1, X_train, y_train)
model.fit() 
res = model.predict(X_test)
print(res)