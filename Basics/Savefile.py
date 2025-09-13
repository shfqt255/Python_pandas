import pandas as pd

data={

    "Name" : ["Shafqat Ullah", "Younas Khan"],
    "age": ["22", "20"],
    "City": ["Islamabad", "Rawalpindi"]

}
df= pd.DataFrame(data) 
print(df)

# df.to_csv("SaveFile.csv") # index false means 0,1 will not print.
df.to_excel("SaveFile.xlsx")