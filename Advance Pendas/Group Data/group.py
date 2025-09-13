import pandas as pd

data = {
    "Department": ["HR", "IT", "HR", "IT", "Finance", "HR"],
    "Team": ["A", "A", "B", "B", "A", "B"],
    "Salary": [30000, 50000, 35000, 45000, 60000, 40000],
    "Age": [25, 30, 28, 35, 40, 32]
}

df = pd.DataFrame(data)
print(df)
dept_group = df.groupby("Department")["Salary"].sum() #All rows with the same Department are grouped together.
print(dept_group)

def_mul_aggregation=df.groupby("Department")["Salary"].agg(["sum", "mean", "max"])
print(def_mul_aggregation)

group_multi = df.groupby(["Department", "Team"])["Salary"].sum()
print(group_multi)

