import pandas as pd
import numpy as np

# file 771MB
# 60M linhas

num_rows = 30_000_000

df = pd.DataFrame({
    "id": range(1, num_rows + 1),
    "name": np.random.choice(["Alice", "Bob", "Charlie", "David"], num_rows),
    "age": np.random.randint(18, 80, num_rows),
    "salary": np.random.uniform(30000, 150000, num_rows).round(2)
})

df.to_csv("large_dataset.csv", index=False)

print("Arquivo CSV gerado com sucesso!")