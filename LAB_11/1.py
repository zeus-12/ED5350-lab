import numpy as np
import matplotlib.pyplot as plt

X = np.linspace(-5, 5, 100)
Y = [1/(1 + np.exp(-i)) for i in X]

plt.plot(X, Y)
plt.show()

print("The sigmoid function is useful for a classification problem because it maps any real number to a value between 0 and 1. hence it can be used to determine the probability of a data point belonging to a certain class.")