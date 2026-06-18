import pandas as pd

# creating a data frame
data = {
    "Name": ["Ganesh", "Ruturaj", "Digvijay"],
    "Age": [21, 22, 20],
    "City": ["Pune", "Mumbai", "Nashik"]
}

df = pd.DataFrame(data)

print("Data Frame is:")
print(df)