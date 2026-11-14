import pandas as pd

data = {
    "Name": ["sam","satyam","shivam","ayush","saba","Raj","joo"],
    "Age": [10,20,30,57,34,44,33],
    "Salary": [3000,4444,3000,7000,8000,5500,78000],
    "Performance Score": [34,53,43,76,87,83,39]
}

df = pd.DataFrame(data)
print(df)


# square brackets df["Column_Name"] = some_data
df["Bouns"] = df["Salary"] * 0.1
print(df)


# using insert()
# df.insert(loc, "Column_Name", some_data)
df.insert(0, "Emoloyee ID", [10,20,30,40,50,60,70])
print(df)