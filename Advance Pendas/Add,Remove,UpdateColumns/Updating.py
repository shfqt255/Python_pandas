import pandas as pd

data={
        "name": ["Shafqat Ullah","Inam Akram","Muhammad Younas"] ,
         "Salary": [ 30000, 25000, 50000] ,
          "Age": [ 30,50, 24] 

}
df=pd.DataFrame(data)

# Update single value
df.loc[2, "Salary"] = 60000
print(df)

print(df["Salary"][2])

# Update multiple value Age

df["Age"]=[34,67,56]
print(df)