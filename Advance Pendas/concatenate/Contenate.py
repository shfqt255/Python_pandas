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


def_concatenate= pd.concat([df1, df2], axis=0, ignore_index=True)