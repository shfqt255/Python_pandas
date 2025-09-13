import pandas as pd

# Convert dictionaries into DataFrames
df1 = pd.DataFrame({
    "name": ["shfqt","ayaz","shfqt","slman","furqan"],
    "Id": [1,2,3,4,5]
})

df2 = pd.DataFrame({
    "Amount": [120,230,600,44,566],
    "Id": [1,2,4,5,13]
})

# Merge on Id column
print("Inner")
df_merge_inner = pd.merge(df1, df2, on="Id", how="inner")
print(df_merge_inner)

print("Outer")
df_merge_outer = pd.merge(df1, df2, on="Id", how="outer")
print(df_merge_outer)

# Keeps all rows from the LEFT table (df1)

print("left")
df_merge_left = pd.merge(df1, df2, on="Id", how="left")
print(df_merge_left)

# Keeps all rows from the Right table (df2)
print("right")
df_merge_right = pd.merge(df1, df2, on="Id", how="right")
print(df_merge_right)
