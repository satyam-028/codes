import pandas as pd

data = {
    "Name": ["sam","satyam","shivam"],
    "Age": [10,20,30],
    "City": ["Delhi","Mumbai","Agra"]
}

df = pd.DataFrame(data)
print("Displaying the info of data set")
print(df.info())
