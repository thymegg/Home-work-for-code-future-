import numpy as np
import matplotlib.pyplot as plt

X = np.random.normal(0, 1, 3000)
Y = np.random.normal(3, 4, 3000)

plt.scatter(X, Y, alpha=0.5, s=20, color='blue', marker='o')

plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Scatter Plot of X and Y')

plt.grid(True)

plt.show()
