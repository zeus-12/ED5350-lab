import math
import numpy as np
import matplotlib.pyplot as plt

X = np.linspace(0.1, 0.9, 100)
Y1 = [-np.log(i) for i in X]
Y2 = [-np.log(1-i) for i in X]

plt.plot(X, Y1, label='-log(h(x))')
plt.plot(X, Y2, label='-log(1 - h(x))')
plt.legend()
plt.show()

print("If only one of the log function is plotted, it only extends to either 1 or -1 and not both. So combining both, we can extend to both sides")