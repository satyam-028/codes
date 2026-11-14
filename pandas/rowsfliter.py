import pandas as pd

data = {
    "Name": ["sam","satyam","shivam","ayush","saba","Raj","joo"],
    "Age": [10,20,30,57,34,44,33],
    "Salary": [3000,4444,3000,7000,8000,5500,78000],
    "Performance Score": [34,53,43,76,87,83,39]
}

df = pd.DataFrame(data)

high_salary = df[df["Salary"] > 5000]
print("Employees with salary > 5000")
print(high_salary)


# filtering rows salary > 50k and age > 30
filtered = df[(df["Age"] > 30) & (df["Salary"] > 5000)]
print("Employee list age > 30 + salary > 5000")
print(filtered)


# using or condition 
filtered_or = df[(df["Age"] > 35) | (df["Performance Score"] > 90)]
print(filtered_or)