import numpy as np
import matplotlib.pyplot as plt

data = np.random.normal(16, 2, 1000)

plt.hist(data, bins=30, color='red', alpha=0.7, edgecolor='black')

plt.xlabel('Время')
plt.ylabel('Частота')
plt.title('Гистограмма результатов забега на 100 метров')

plt.show()