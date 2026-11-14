# df.sort_values(by=["age","salary"], ascending=True, inplace=True)

import pandas as pd

data = {
    "Name": ["satyam","sam","shivam"],
    "Age": [28,34,8],
    "Salary": [10000,20000,30000]
}

df = pd.DataFrame(data)
df.sort_values(by=["Age","Salary"], ascending=[True, False], inplace=True)
print("Sorted Age by Descending")
print(df)