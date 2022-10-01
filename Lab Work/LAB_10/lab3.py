import numpy as np
import pandas as pd
from lab1 import LR
import matplotlib.pyplot as plt
import os
dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'heart.data.csv')

df = pd.read_csv(filename)
y = list(df['heart.disease'])
x = df.iloc[:, [1, 2]]
x = x.values.tolist()

p = LR(x, y, 0.1, 0.1)
w = p.GradDescent()

xx = np.linspace(-10, 10, 100)
yy = np.linspace(-10, 10, 100)

XX, YY = np.meshgrid(xx, yy)
Z = w[0]*XX + w[1]*YY + w[2]

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(XX, YY, Z)

ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')
plt.title('Surface Plot')
plt.show()
