import pandas as pd

# read excel file
df = pd.read_excel("student.xlsx", header=1)

# Display the DataFrame
print("Data from Excel file:\n", df)
# Accessing columns
print("\nNames column:\n", df["Name"])
# Accessing rows (first 2 rows)
print("\nFirst 2 rows:\n", df.head(2))
# Display info about DataFrame output
print("\nDataFrame Info:")
df.info()