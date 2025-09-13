import pandas as pd

data={
    "name" : ["Shafqat Ullah", "Muhammad Hamza", "Zaman Khan"],
    "Salary" : [50000, 40000, 30000],
    "Performance": [4, 6, 8],
    "Age": [40,50, 20]

}

df=pd.DataFrame(data) # It makes Table from the table
high_salary=df[df['Salary']< 50000]
print(high_salary)


mul_condition=df[(df['Salary']< 50000) & (df["Performance"]<6) | (df["Age"]>30)]