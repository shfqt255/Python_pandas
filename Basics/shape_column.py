import pandas as pd

data={
    "name" : ["Shafqat Ullah", "Muhammad Hamza", "Zaman Khan"],
    "Salary" : [50000, 40000, 30000],
    "Performance": [4, 6, 8]

}

df=pd.DataFrame(data) # It makes Table from the table

print(df.shape)
print(df.columns)