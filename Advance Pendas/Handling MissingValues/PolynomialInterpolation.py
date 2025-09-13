
"""2- Polynomial interpolation

Missing value is filled by fitting a polynomial curve through multiple known points, instead of just a straight line between two points.

The polynomial of degree 2 (quadratic) looks like: y=a0+ a1x + a2x^2

For Heigher Degrees: y=a0+ a1x + a2x^2+a3x^3 + a4x^4 ---------anx^n

"Age": [30, None, 24, None, 40] 
Index (x): 0, 1, 2, 3, 4
Values (y): 30, NaN, 24, NaN, 40
We want to fill missing values at index = 1 and 3.

Step 1: Pick known points
(x0 y0)= (0, 30)
(x2 y2)= (2, 24 )
(x4 y4)= (4, 30)

Now put the value of x and y for each set into farmula to find the value of a 
And then put value into farmula and find the the value. very complex
What does order=2 mean?

order=1 → Linear interpolation (straight line).

order=2 → Quadratic interpolation (curve of degree 2).

order=3 → Cubic interpolation (degree 3 polynomial), and so on.


"""

import pandas as pd

data={
        # "name": ["Shafqat Ullah",None,"Muhammad Younas", None] ,
         "Salary": [ 30000, 25000, 50000, 60000] ,
          "Age": [ 30,None, 24, 25] 

}
df=pd.DataFrame(data)
df.interpolate(method='polynomial', order=2)
#  order means for 2 quadic