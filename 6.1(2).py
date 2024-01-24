import numpy as np
import matplotlib.pyplot as plt

def complex_function(x):
    return np.sin(x) * np.cos(2 * x) + (x ** 2) / (1 + np.exp(-x)) - 3 * np.cos(3 * x)

X = np.linspace(-5, 5, 500)

Y = complex_function(X)

plt.plot(X, Y, linestyle='dashed', color='green', alpha=0.5)

plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('График сложной алгебраической функции')

plt.suptitle('Вот такая моя функция', fontsize=16, fontweight='bold')

plt.grid(True)

plt.show()