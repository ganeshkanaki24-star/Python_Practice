import pandas as pd

data = [["Ganesh", 98], ["Vijay", 88], ['Digvijay', 76]]
df = pd.DataFrame(data, columns=["Name", "Marks"])

df.head()
print(df)

