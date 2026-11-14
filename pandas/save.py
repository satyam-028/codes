import pandas as pd

data = {
    "Name": ["sam","satyam","shivam"],
    "Age": [10,20,30],
    "City": ["Delhi","Mumbai","Agra"]
}

df = pd.DataFrame(data)
print(df)

# df.to_csv("output.csv", index=False)
df.to_excel("output.xlsx", index=False)
# df.to_json("output.json", index=False)