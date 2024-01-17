import numpy as np

matrix = np.tile(np.arange(1, 11), (10, 1))


column_sums = np.sum(matrix, axis=0)

print(column_sums)