import numpy as np

num_experiments = 1000
results = []

for _ in range(num_experiments):
    arr = np.random.randint(1, 11, size=100)
    percentage_greater_than_7 = np.mean(arr > 7) * 100
    results.append(percentage_greater_than_7)

num_equal_to_20_percent = np.mean(np.array(results) == 20)

print(f" {num_equal_to_20_percent * 100}%")