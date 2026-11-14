# df.sort_values(by="Column Name", True/False, inplace = True)

import pandas as pd

data = {
    "Name": ["satyam","sam","shivam"],
    "Age": [28,34,8],
    "Salary": [10000,20000,30000]
}

df = pd.DataFrame(data)
df.sort_values(by="Age", ascending=False, inplace=True)
# df.sort_values(by="Age", ascending=True, inplace=True)
print("Sorted Age by Descending")
print(df)