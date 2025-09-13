import pandas as pd
data ={'Name':['Priyang','Aadhya','Krisha','Vedant','Parshv',
                'Mittal','Archana'],
                'Marks':[98,89,99,87,90,83,99],
                'Gender':['Male','Female','Female','Male','Male',
                         'Female','Female']
               }
df1=pd.DataFrame(data)

#Question 1: Print first three rows of data.
print(f"First three rows of the data: \n {df1.head(3)}")

#Question 2: Print last three rows of data.
print(f"Last three rows of the data: \n {df1.tail(3)}")

#Question 3: Find and print the shape  of data, also print the number of rows and number of columns.
print(f"Shape: {df1.shape}, \t Number of Rows: {df1.shape[0]}, \t Number of Columns: {df1.shape[1]}")

 #Question 4: Print information about the data.
print(f"\n The following are the some information about your data:")
df1.info()

 #Question 5: Check and Print null values in the data.
 # If we use only isnull(), it will return True at each index where the data is missing and False at each index where data is present. 
 # we can also use axis=0,1 to in sum to print the missing values at row wise or column wise.
print(f"\n Null values in the data:\n {df1.isnull().sum()}")


 #Question 6: Get overall statistics about the data. 
"""
count: Tells you how many non-null (not missing) values exist in each column.
unique (only for categorical / object columns)

Number of unique values.
    Name: 7 unique names (no duplicate)
    Gender: 2 unique values (Male, Female)
    Marks: numeric, so NaN here.

Top (only for categorical / object columns)

        The most frequent (mode) value.
        Name: top value is "Priyang" (any one of them since all appear once).
        Gender: "Female" appears most.

freq

    Frequency (count) of the top value.
    Name: Priyang occurs 1 time.
    Gender: "Female" occurs 4 times.
"""
print(f"Last three rows of the data: \n {df1.describe(include='all')}")

 #Question 7: Display Unique elements from a specific column.
print(f"Unique elements in Gender: \n {df1["Gender"].unique()}")

 #Question 8: Display the number of  Unique elements from a specific column.
# nunique works for both a single column and at a dataframe.
print(f"Unique elements in the data: \n {df1.nunique()}")

 #Question 9: Display the count of  Unique elements.
print(f"elements : \n {df1["Gender"].value_counts()}")

 #Question 10: Display the Marks that is between 90 and 100.
print("The Marks between 100 and 90 are: ")
print(df1[(df1["Marks"]>90) & (df1['Marks'] < 100)] )
print(f"Second Method is :\n{df1[df1['Marks'].between(90, 100)]}")

 #Question 12: Display the number of the Marks that is between 90 and 100.
print(f"The Marks between 100 and 90 are: {len(df1[(df1["Marks"]>90) & (df1['Marks'] < 100)])}" )

#Apply Methond: 
#Question 13: Use Apply method, to divide the marks column by 2.
def marks(x):
    return x/2
print(f" Half Marks are : \n {df1['Marks'].apply(marks)}")

#Question 14: Use Apply method, to divide the marks column by 2 and create a new column.
print("Half Marks Column added: ")
df1["Half Marks"]=df1['Marks'].apply(marks)
print(df1)

#Question 15: Use Apply method, to divide the marks column by 2 by using lambda.
print(f"Half Marks by using Lambda: {df1['Marks'].apply(lambda x: x/2)}")

#Question 16: Use Apply method, to find the length of the names.
print(f"The length of the names exists in the column name: \n {(df1['Name'].apply(len))}")

#Question 17: Use Map function, to Map Male with 1 and Female with 0.
print(f"Male : 1 and Female : 0 \n {df1['Gender'].map({'Male': 1 , 'Female': 0})}")
df1["0/1"]=df1['Gender'].map({'Male': 1 , 'Female': 0})
print(df1)

#Question 20: Drop Multiple Columns
print("Two Columns droped ")
df1.drop(["Half Marks", "0/1"], axis=1,  inplace= True)
print(df1)

#Question 20:  Print the marks of Female
print(df1[df1['Gender']=="Female"][["Name", "Marks", "Gender"]])
females = df1.loc[df1['Gender']=="Female", ["Name", "Marks", "Gender"]]
print(females)
