
import matplotlib.pyplot as plt
import numpy as np
import math

x = np.arange(-5, 5, 0.1)
e = math.e

y = 1 / (1 + e**-x)

plt.plot(x, y)
plt.title("kome/mesi")
plt.show()