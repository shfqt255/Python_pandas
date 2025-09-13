import pandas as pd

data = {
    "name": ["A", "B", "C", "D"],
    "Salary": [100, 200, 150, 50],
    "Age": [30, 30, 30, 25]
}

df = pd.DataFrame(data)
df.sort_values(by=["name","Age", "Salary"], ascending=[True, True, True], inplace=True)
#  It will first sort the name, then the data according to the name.  so age and salary will not change.

print(df)
