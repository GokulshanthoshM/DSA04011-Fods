import numpy as np
import pandas as pd

file_location='D:/Fundamentals of data science/sales_data_sample1.csv'

dat1= pd.read_csv(file_location,encoding='Latin-1')
print(dat1)

count1=dat1.groupby('ORDERNUMBER')['ORDERDATE']
count2=count1.count()
print("Total number of orders by the customer:")
print(count2)

avg=dat1.groupby('ORDERNUMBER')['QUANTITYORDERED']
avg1=avg.mean()
print("Average of each product: ")
print(avg1)

ear=dat1['ORDERDATE'].min()
lat=dat1['ORDERDATE'].max()

print(f"Ealier date is {ear}")
print(f"Latest date is {lat}")
                  
