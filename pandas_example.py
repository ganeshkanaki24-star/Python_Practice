import pandas as pd

data = {
    "dept": ["HR", "HR", "IT","IT"],
    "salary" : [10000, 15000, 20000, 25000]
}
df = pd.DataFrame(data)
result = df.groupby("dept")["salary"].mean()
print(result)