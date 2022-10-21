import pandas as od
import numpy as np
import matplotlib.pyplot as plt
import random

###### QN1 ######
class KMeans:
    def __init__(self, X, k) -> None:
        self.X = X
        self.d = {}
        self.k = k
        self.c = np.array([self.X[i] for i in range(self.k)])
    
    def fit(self):
        colours_list = ['r', 'g', 'b', 'y', 'm', 'p', 'k']

        self.d = {}
        temp = self.c.copy()
        for point in self.X:
            mn = 0
            mn_dist = float('inf')
            for centroid in self.c:
                if mn_dist > abs((point[0] - centroid[0])**2 + (point[1] - centroid[1])**2):
                    mn = centroid
                    mn_dist = abs((point[0] - centroid[0])**2 + (point[1] - centroid[1])**2)
            self.d[tuple(mn)] = self.d.get(tuple(mn), [])
            self.d[tuple(mn)].append(point)

        for i, n in enumerate(list(self.d.keys())):
            temp[i] = sum(self.d[n])/len(self.d[n])

        while not np.array_equal(temp, self.c):
            x_axis = []
            y_axis = []
            
            for z in range(self.k):
                x_axis.append([self.d[list(self.d.keys())[z]][i][0] for i in range(len(self.d[list(self.d.keys())[z]]))])
                y_axis.append([self.d[list(self.d.keys())[z]][i][1] for i in range(len(self.d[list(self.d.keys())[z]]))])
                plt.scatter(x_axis[z], y_axis[z], c=colours_list[z])
                plt.scatter([list(self.d.keys())[z][0]], [list(self.d.keys())[z][1]], c=colours_list[z], marker='v')
            
            plt.title("Intermediate Grouping of K = "+str(self.k))
            plt.show()
            
            self.d = {}
            self.c = temp.copy()

            for point in self.X:
                mn = 0
                mn_dist = float('inf')
                for centroid in self.c:
                    if mn_dist > abs((point[0] - centroid[0])**2 + (point[1] - centroid[1])**2):
                        mn = centroid
                        mn_dist = abs((point[0] - centroid[0])**2 + (point[1] - centroid[1])**2)
                self.d[tuple(mn)] = self.d.get(tuple(mn), [])
                self.d[tuple(mn)].append(point)

            for i, n in enumerate(list(self.d.keys())):
                temp[i] = sum(self.d[n])/len(self.d[n])

    def costFunc(self):
        J = 0
        for i in self.d.keys():
            for j in self.d[i]:
                J += abs((j[0] - i[0])**2 + (j[1] - i[1])**2)**0.5
        return J/len(self.X)
    
    def points(self):
        return self.d

########## QN 2 #########

X = []

for i in range(10):
    X.append(np.array([random.randint(1, 5), random.randint(1, 5)]))
    X.append(np.array([random.randint(5, 9), random.randint(5, 9)]))
    X.append(np.array([random.randint(9, 13), random.randint(9, 13)]))

j = []
for i in range(1, 6):
    model = KMeans(X, i)
    model.fit()
    j.append(model.costFunc())

plt.plot([i for i in range(1,6)], j)
plt.show()


model = KMeans(X, 3)
model.fit()
d = model.points()
c = list(d.keys())