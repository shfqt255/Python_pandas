# What is Interpolation?
# Interpolation is a method of filling missing values (NaN) in your data.
# Instead of dropping NaNs or replacing them with a fixed value (like mean/median), interpolation tries to estimate missing values based on surrounding data.


"""df.interpolate(
    method='linear',
    axis=0,          # 0 → rows, 1 → columns
    limit=None,      # Max number of NaNs to fill
    inplace=False,   # Modify DataFrame in place
    limit_direction='forward'  # or 'backward', 'both'
)"""
import pandas as pd

data={
        "name": ["Shafqat Ullah",None,"Muhammad Younas"] ,
         "Salary": [ 30000, 25000, 50000] ,
          "Age": [ 30,None, 24] 

}
df=pd.DataFrame(data)
# df.interpolate(inplace=True)

# Methods of Interpolate
 
"""
1_ Linear:
Missing value is filled using a straight line between the previous and next known values.
y= y1 + (((x-x1)/(x2-x1))*(y2-y1))
x= index
y= Value

Example:
   "Age": [ 30,None, 24] 
   index =x= 0,1,2
   value=y=30, None, 24

   x=1,  x1=0 , x2=2, 
    y=Nan, y1=30, y2=24

"""
df.interpolate("linear",inplace=True)

print(df)


