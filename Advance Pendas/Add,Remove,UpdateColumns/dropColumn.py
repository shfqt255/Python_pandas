import pandas as pd

data={
        "name": ["Shafqat Ullah","Inam Akram","Muhammad Younas"] ,
         "Salary": [ 30000, 25000, 50000] ,
          "Age": [ 30,50, 24] 

}
df=pd.DataFrame(data)

df.drop(columns=["Salary"], inplace=True)

# inplace = True change the original data do not return copy
# for deleting multiple columns df.drop(columns=["Salary", "Age"], inplace=True)
print(df)

df.drop(index=[0, 2], inplace=True)
print(df)
