import pandas as pd
import numpy as np


class LR:

    def __init__(self, x, y, a, e) -> None:
        self.m = len(x)
        self.n = len(x[0]) + 1
        self.X = x
        for i in range(self.m):
            self.X[i].append(1)
        self.X = np.array(self.X)
        self.y = np.array(y)
        self.W = np.array([0]*self.n)
        self.a = a
        self.e = e
    
    def DCost(self):
        ret = []
        for d in range(self.n):
            res = 0
            for i in range(self.m):
                tmp = 0
                for j in range(self.n):
                    tmp += self.W[j]*self.X[i][j]
                res += (tmp - self.y[i])*self.X[i][d]
            ret.append(res/self.m)
        return np.array(ret)

    def GradDescent(self):
        dJ = self.DCost()
        self.W = np.subtract(self.W, self.a*dJ)
        flag = np.any((self.W > self.e))
        
        while flag:
            dJ = self.DCost()
            self.W = np.subtract(self.W, self.a*dJ)
            flag = np.any((self.W > self.e))
        
        return self.W
        