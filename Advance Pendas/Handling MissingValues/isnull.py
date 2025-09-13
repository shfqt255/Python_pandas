import pandas as pd

data={
        "name": ["Shafqat Ullah",None,"Muhammad Younas"] ,
         "Salary": [ 30000, 25000, 50000] ,
          "Age": [ None,50, 24] 

}
df=pd.DataFrame(data)
print(df.isnull()) # return true at index where value is missing

print(df.isnull().sum())
