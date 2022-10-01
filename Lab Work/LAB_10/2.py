from lab1 import LR
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'univariate_linear_regression.csv')

def cost(x, y, w1, w2):
    res = 0
    for i in range(len(x)):
        tmp = 0
        for j in range(len(x[i])):
            tmp += (w1*x[i][j] + w2)
        res += (tmp - y[i])**2
    return res/(2*len(x))

df = pd.read_csv(filename)
X = df.iloc[:, [0]].values.tolist()
y = list(df['y'])
p = LR(X, y, 0.045, 0.00001)
w = p.GradDescent()

X_scatter = df['x'].values.tolist()
y_scatter = df['y'].values.tolist()

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
        temp.append(cost(X, y, X_plot[i][j], Y_plot[i][j]))
    J.append(temp)
J = np.array(J)
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.plot_surface(X_plot, Y_plot, J)

ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Cost Function')
plt.title('Surface Plot')
plt.show()

plt.contour(X_plot, Y_plot, J)
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Contour Plot')
plt.show()
