import pandas as pd

# Read CSV
df = pd.read_csv("E:/Python/python Pendas/sales_data_sample.csv", encoding="latin1")

# Add new column
df["Total_Price"] = df["QUANTITYORDERED"] * df["PRICEEACH"]

# Show first few rows
# print(df[["ORDERNUMBER", "QUANTITYORDERED", "PRICEEACH", "Total_Price"]].head())
print(df.head())
