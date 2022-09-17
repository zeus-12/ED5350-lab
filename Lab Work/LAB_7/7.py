import matplotlib.pyplot as plt
import numpy as np
import math

x = np.linspace(-3.14, 3.14, 100)
y = [math.sin(i) for i in x]
plt.plot(x, y, '-r')
plt.xlabel('x')
plt.ylabel('Sin(x)')
plt.title('Sin Graph')
plt.show()

y = [math.cos(i) for i in x]
plt.plot(x, y, '-r')
plt.xlabel('x')
plt.ylabel('Cos(x)')
plt.title('Cos Graph')
plt.show()

y = [math.tan(i) for i in x]
plt.plot(x, y, '-r')
plt.xlabel('x')
plt.ylabel('Tan(x)')
plt.title('Tan Graph')
plt.show()
