# pd.merge(df1,df2, on="Column_Name", how="type of join")

import pandas as pd

# customer dataframe
df_customers = pd.DataFrame({
    "CustomerID": [1,2,3],
    "Name": ["Satyam","Sam","Shivam"]
})

# order dataframe
df_order = pd.DataFrame({
    "CustomerID": [1,2,4],
    "OrderAmount": [250,450,350]
})

# merge
df_merged = pd.merge(df_customers, df_order, on="CustomerID", how="inner")
# df_merged = pd.merge(df_customers, df_order, on="CustomerID", how="outer")
# df_merged = pd.merge(df_customers, df_order, on="CustomerID", how="left")
# df_merged = pd.merge(df_customers, df_order, on="CustomerID", how="right")
# df_merged = pd.merge(df_customers, df_order, on="CustomerID", how="cross")
print("inner join")
print(df_merged)