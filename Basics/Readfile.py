# import pandas as pd

# df=pd.read_csv("sales_data_sample.csv", encoding="latin1")
  

import pandas as pd
df=pd.read_json("sample_Data.json") 
print(df.head())



# read file from google 
import pandas as pd

file_id = "1q_No4uek1c-wtmPbBhDRSCWZ7dLET6aC"
url = f"https://drive.google.com/uc?id={file_id}"

df = pd.read_json(url)
print(df.head()) # head prints first five rows
