import numpy as np
import pandas as pd

data=pd.read_excel('D:\\Fundamentals of data science\\house_data.xlsx')
data1=np.array(data)
bedrooms=data1[:,2].tolist()
sales_price=data1[:,4].tolist()
sum=0
length=0
for bed in range(len(bedrooms)):
    if bedrooms[bed]>=4:
        sum+=sales_price[bed]
        length+=1

print(f'Average of house with 4 bedroom and more is {sum/length}')
        
        
        
