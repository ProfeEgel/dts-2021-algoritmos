
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-10, 10, 0.1)
y = x**3 + 2*x + 5

plt.plot(x, y)
plt.show()
