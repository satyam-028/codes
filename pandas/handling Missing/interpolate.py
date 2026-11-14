import pandas as pd

data = {
    "Name": ["sam","satyam","shivam","ayush","saba","Raj","joo"],
    "Age": [10,None,30,57,34,44,33],
    "Salary": [3000,None,3000,7000,8000,5500,78000],
    "Performance Score": [34,None,43,76,87,83,39]
}

df = pd.DataFrame(data)
print(df)


df.interpolate(method="linear", axis=0, inplace=True)
print(df)