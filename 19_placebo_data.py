import pandas as pd

a={
    'drugs':[10,20,30,40,50,44,33,22,11,45],
    'placebo':[12,65,76,44,56,87,63,15,79,77]
  }

b=pd.DataFrame(a)
print(b)

len1=len(b['drugs'])
sample_mean=b['drugs'].mean()
sd=b['drugs'].std()
standard_error=sd/len1
cof=sample_mean+(standard_error*1.96)
cof1=sample_mean-(standard_error*1.96)
print(f"Confidence Intervals is drugs is {cof} | {cof1}")

len2=len(b['placebo'])
sample_mean1=b['placebo'].mean()
sd1=b['placebo'].std()
standard_error1=sd1/len2
cof2=sample_mean1+(standard_error1*1.96)
cof3=sample_mean-(standard_error1*1.96)
print(f"Confidence Intervals of placebo is {cof2} | {cof3}")