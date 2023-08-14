import numpy as np
import pandas as pd
import xlrd
import openpyxl 
file_location='D:\\Fundamentals of data science\\student_data.xlsx'
df=pd.read_excel(file_location)
print(df)
data1=np.array(df)

#math avg

maths=np.array(df)[:,2]
len1=len(maths)
avg1=sum(maths)/len1
print(f"Average of maths is {avg1}")
#english avg

english=np.array(df)[:,3]
len2=len(english)
avg2=sum(english)/len2
print(f"Average of english is {avg2}")

#science avg

science=np.array(df)[:,4]
len3=len(science)
avg3=sum(science)/len3
print(f"Average of science is {avg3}")

#history av5

history=np.array(df)[:,2]
len4=len(history)
avg4=sum(history)/len4
print(f"Average of maths is {avg4}")

#Highest average

def high_avg(avg1,avg2,avg3,avg4):
    high=[avg1,avg2,avg3,avg4]
    return np.max(high)

print(f"highest average is {high_avg(avg1,avg2,avg3,avg4)}")
    
