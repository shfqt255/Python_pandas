import pandas as pd

df=pd.read_csv("sales_data_sample.csv", encoding="latin1")
print(df.head(10)) # Print first 10 rows, 10 not provide by default it will print first 5 rows 
print(df.tail(10)) # Print last 10 rows, 10 not provide by default it will print last 5 rows 