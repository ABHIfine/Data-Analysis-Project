import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("DATA.csv")
df['Group'] = pd.cut(df['Age'], bins=[0, 25, 50, 100], labels=['Young', 'Adult', 'Senior'])

data = df.groupby('Group')['Amount'].mean()
bars = plt.bar(data.index, data.values, color='orange')
plt.bar_label(bars)  

plt.xlabel("Age Group")
plt.ylabel("Average Amount")
plt.title("Age Group Analysis")
plt.savefig("Age Group Analysis.jpg")
plt.show()