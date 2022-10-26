import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-3.14, 3.14, 0.1)
y = np.arange(-3.14, 3.14, 0.2)

[X, Y] = np.meshgrid(x, y)
Z = np.cos(X) + np.sin(Y)

plt.contour(X, Y, Z)
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Contour Plot')

plt.show()