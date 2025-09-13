# It will drop the columns or rows if it contains null

import pandas as pd

data={
        "name": ["Shafqat Ullah",None,"Muhammad Younas"] ,
         "Salary": [ 30000, 25000, 50000] ,
          "Age": [ None,50, 24] 

}
df=pd.DataFrame(data)

df.dropna(axis=1, inplace=True)# by default axis=0
print(df)