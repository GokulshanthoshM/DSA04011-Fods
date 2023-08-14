import pandas as pd
import numpy as np
data1=pd.read_csv("D:\Fundamentals of data science\supermarket_sales - Sheet1.csv")
print(data1)
data2=np.array(data1)[:,9]
print(data2)
avg1=sum(data2)/len(data2)
print(f"average of sales is {avg1}")
