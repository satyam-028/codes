import pandas as pd

data = {
    "Name": ["sam","satyam","shivam","ayush","saba","Raj","joo"],
    "Age": [10,20,30,57,34,44,33],
    "Salary": [3000,4444,3000,7000,8000,5500,78000],
    "Performance Score": [34,53,43,76,87,83,39]
}

df = pd.DataFrame(data)
print(df)


# .loc[]
# df.loc[row_index, "Coolumn_Name"] = new_value
df.loc[1, "Salary"] = 50000
print(df)