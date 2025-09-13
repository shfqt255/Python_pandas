"""df.interpolate(
    method='linear',
    axis=0,          # 0 → rows, 1 → columns
    limit=None,      # Max number of NaNs to fill
    inplace=False,   # Modify DataFrame in place
    limit_direction='forward'  # or 'backward', 'both'
)"""

import pandas as pd 

data={
        "name": ["Shafqat Ullah",None,"Muhammad Younas", None, "Amir"] ,
         "Salary": [ 30000, 25000, None, None, 400000] ,
          "Age": [ 30,None, 24, None, 50] 

}
df=pd.DataFrame(data)
"""" 
Copies the last valid value forward.
 df.interpolate(method="Pad", inplace=True)
 """

"""
Backfill / bfill
Opposite of forward fill: takes the next valid value backward.
df.interpolate(method="bfill", limit=3, limit_direction="backward", inplace=True)
df.interpolate(method="bfill", limit=3, limit_direction="forward", inplace=True)

"""

""""
Nearest
Takes the nearest non-NaN value (either forward or backward).

Example:
df.interpolate(method='nearest')
✔ Best for categorical or step-like numeric data (like IDs, labels, grades)."""

df.interpolate(method='nearest', inplace= True, limit=1, limit_direction="backward")
print(df)

