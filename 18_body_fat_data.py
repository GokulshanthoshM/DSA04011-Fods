import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#storing the data in dictionary
a={
    "age":[23,23,27,27,39,41,47,49,50,52,54,54,56,57,58,58,60,61],
    "%fat":[9.5,26.5,7.8,17.8,31.4,25.9,27.4,27.2,31.2,34.6,42.5,28.8,33.4,30.2,34.1,32.9,41.2,35.7]
    }

#Creating a dataframe using pandas
b=pd.DataFrame(a)
print(b)

#MEAN|MEDIAN|STANDARD DEVIATION
c=b['age'].mean()
d=b['%fat'].mean()
e=b['age'].std()
f=b['%fat'].std()
print(f"Mean of Age is {c}")
print(f"SD of Age is {e}")
print(f"Mean of %fat is {d}")
print(f"SD of %fat is {f}")

#Plotting BOX|SCATTER
b.plot(kind='box',x='age',y='%fat',color='blue')
plt.show()
b.plot(kind='scatter',x='age',y='%fat',color='cyan')
plt.grid()
plt.show()