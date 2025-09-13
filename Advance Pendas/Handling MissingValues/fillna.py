

import pandas as pd

data={
        "name": ["Shafqat Ullah",None,"Muhammad Younas"] ,
         "Salary": [ 30000, 25000, 50000] ,
          "Age": [ None,50, 24] 

}
df=pd.DataFrame(data)
# df.fillna(0, inplace=True)
print(df)

df["Age"].fillna(df["Age"].mean(), inplace=True)

print(df)
# a = {
# "key": "value",
# "harry": "code",
# "marks": "100",
# "list": [1, 2, 9]
# }
# print(a["key"]) # Output: "value"
# print(a["list"][0:2]) # Output: [1, 2, 9]