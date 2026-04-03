import pandas as pd

employe=pd.read_csv("employe.csv")

print(employe)

heigh=employe[employe['salary']>50000]
print(heigh)

it= employe[employe['department']=='IT']
print(it)

data=employe[(employe['department']=='IT') &( employe['experience']>3)]
print(data)

sort=employe.sort_values(by="salary", ascending=True)
print(sort)

print(employe['name'])

print(employe[['name' ,'salary'] ])