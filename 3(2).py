import pandas as pd
import numpy as np

data = {
    'Column_A': np.random.rand(10),
    'Column_B': np.random.randint(1, 100, 10),
    'Column_C': np.random.choice(['A', 'B', 'C'], 10)
}

df = pd.DataFrame(data)

print("Первые три строки:\n", df.head(3))

print("\nПоследние три строки:\n", df.tail(3))

df.to_csv('my_dataframe.csv', index=False)
print("\nDataFrame сохранен в my_dataframe.csv")