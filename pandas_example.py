'''
import pandas as pd

data = {
    "dept": ["HR", "HR", "IT","IT"],
    "salary" : [10000, 15000, 20000, 25000]
}
df = pd.DataFrame(data)
result = df.groupby("dept")["salary"].mean()
print(result)
'''
'''
# find greter than 70 marks using pandas and lambda
student = {
    "name": ['Ganesh','Digvijay','Ruturaj','Patil','vijay'],
    "marks": [77, 60, 80, 55, 90]
}
df = pd.DataFrame(student)
show = df[df['marks'].apply(lambda x : x < 70)]
print(show)
'''

import csv
data = [
    ['name', 'age', 'city'],
    ['Alice', 30, 'New York'],
    ['Bob', 25, 'Los Angeles'],
    ['Charlie', 35, 'Chicago']
]

# Create the file
with open('data.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)

print("CSV file created successfully.")

with open('data.csv', mode='r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)