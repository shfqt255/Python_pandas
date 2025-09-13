import pandas as pd

data={
    "name" : ["Shafqat Ullah", "Muhammad Hamza", "Zaman Khan"],
    "Salary" : [50000, 40000, 30000],
    "Performance": [4, 6, 8]

}

df=pd.DataFrame(data) # It makes Table from the table
print(f"The Sample data is: \n {df}")

column1=df[['name']]
print(column1)
print(df.columns)


print(df[["name", "Salary"]])