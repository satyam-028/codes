import pandas as pd

data = {
    "Name": ["satyam","sam","shivam","ayush","saba"],
    "Age": [28,34,22,34,28],
    "Salary": [340000,60000,480000,390000,890000]
}

df = pd.DataFrame(data)
grouped = df.groupby("Age")["Salary"].sum()
print(grouped)