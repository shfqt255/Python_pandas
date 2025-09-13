#  1- number of rows and columns
# 2- columns name
# 3- datatype int64, float64 object etc
# 4- non null counts 
# 5- memory usage of the data frame

import pandas as pd

df=pd.read_json("sample_Data.json")
print(df.info())



data={

    "Name" : ["Shafqat Ullah", "Younas Khan"],
    "age": ["22", "20"],
    "City": ["Islamabad", "Rawalpindi"]

}
df= pd.DataFrame(data) 
print(df.info())