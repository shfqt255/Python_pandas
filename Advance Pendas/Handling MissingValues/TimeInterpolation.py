import pandas as pd
import numpy as np

dates = pd.date_range('2025-01-01', periods=5)  
df = pd.DataFrame({"A": [1, np.nan, np.nan, 4, 5]}, index=dates)

print("Before interpolation:\n", df)

print("\nAfter time interpolation:\n", df.interpolate(method='time'))


# how it works search on ChatGPT
