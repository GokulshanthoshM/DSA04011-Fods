import pandas as pd

data={
    123:[1,2,3,4,5,6],
    "user_post":["Post 1","Post 2","Post 3","Post 4","Post 5","Post 6"],
    "post_likes":["Post 1","Post 1","Post 1","Post 1","Post 3","Post 3"]
    }
data[123]=4,5,6,7,8,9
print(data[123])
for key in data:
    print(key)
    print(data[key])
data1=pd.DataFrame(data)
group=data1.groupby('post_likes')['user_post']
print(group.count())