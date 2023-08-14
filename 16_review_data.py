import pandas as pd

data={
    "user_id":[1,2,3,4,5,6],
    "user_review":["good","worst","Outstanding","ok","poor","excellent"],
    "frequency":["good","Excellent","good","worst","good","worst"]
    }

data1=pd.DataFrame(data)
group=data1.groupby('frequency')['user_review']
print(group.count())
