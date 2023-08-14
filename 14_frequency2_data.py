import pandas as pd

data={
    "cus_id":[1,2,3,4,5,6],
    "cus_name":["Bala","Guhan","Gokul","Shanthosh","nara","naresh"],
    "cus_age":[20,30,20,25,25,25]
    }

data1=pd.DataFrame(data)
group=data1.groupby('cus_age')['cus_id']
print(group.count())