import pandas as pd

data = {
    "Name": ["sam","satyam","shivam","ayush","saba","Raj","joo"],
    "Age": [10,20,30,57,34,44,33],
    "Salary": [3000,4444,3000,7000,8000,5500,78000],
    "Performance Score": [34,53,43,76,87,83,39]
}

df = pd.DataFrame(data)

# display the dataframe
print("Sample Datafram")
print(df)

print("Name (single column return series)")
name = df['Name']
print(name)


# selcteing multiple columns
subset = df[["Name","Salary"]]
print("\nSubset with name and salary")
print(subset)