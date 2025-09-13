import pandas as pd

data={
        "name": ["Shafqat Ullah","Inam Akram","Muhammad Younas"] ,
         "Salary": [ 30000, 25000, 50000] ,
          "Age": [ 30,50, 24] 

}
df=pd.DataFrame(data)
df["Bonus"]= df["Salary"] * 0.1
print(df)
print(df.tail(2))

df.insert(2, "Performance", [2,3,4]) # better approach You have to specify the index
print(df)

df.insert(2, "Performance3", df["Bonus"]* 0.2) # better approach You have to specify the index
print(df)