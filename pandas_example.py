import pandas as pd
'''
data = {
    "dept": ["HR", "HR", "IT","IT"],
    "salary" : [10000, 15000, 20000, 25000]
}
df = pd.DataFrame(data)
result = df.groupby("dept")["salary"].mean()
print(result)
'''
# find greter than 70 marks using pandas and lambda
student = {
    "name": ['Ganesh','Digvijay','Ruturaj','Patil','vijay'],
    "marks": [77, 60, 80, 55, 90]
}
df = pd.DataFrame(student)
show = df[df['marks'].apply(lambda x : x < 70)]
print(show)
