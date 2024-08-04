import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

t = np.linspace(0, 2 * np.pi, 100)
plt.figure(figsize=(4,4))
plt.plot(np.sin(2 * t), np.cos(3 * t))
plt.show()

x = np.linspace(0, 4 * np.pi, 100)

plt.figure()
plt.plot(x, np.sin(x), 'r-')
plt.plot(x, np.cos(x), 'b--')
plt.show()

