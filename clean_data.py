import numpy as np
import pandas as pd

df = pd.read_csv('dirty_data.csv')

df["Age"].fillna(df["Age"].mean(),inplace=True)
df["City"].fillna("jodhpur",inplace=True)

print(df.isnull().sum())
print(df.head(20))



df.to_csv("clean_file.csv", index=False)

print("file 'clean_file.csv' ban gayi hai")
new_df = pd.read_csv('clean_file.csv')

print(new_df.isnull().sum())