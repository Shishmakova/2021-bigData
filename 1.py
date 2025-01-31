import numpy as np
import pandas as pd

rng = np.random.default_rng()
df1 = pd.DataFrame(rng.integers(-1000, 5000, size=(9000, 4)))
df2 = pd.DataFrame(rng.random(size=(9000, 3)))

data = pd.concat([df1, df2], axis=1)

data.columns = [x for x in range(7)]

data.to_csv('morozov', sep='\t')

df = pd.read_csv('morozov_1', sep='\t')

print(df)

for i in range(100):
    df.at[2, np.random.randint(0, 9000)] = None
    df.at[1, np.random.randint(0, 9000)] = -2
    df.at[0, np.random.randint(0, 9000)] = rng.random()
