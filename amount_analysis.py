import pandas as pd
import matplotlib.pyplot as plt

data =pd.read_csv("clean_file.csv")
city_avg_amount = data.groupby('City')['Amount'].mean()

bars= plt.bar(city_avg_amount.index, city_avg_amount.values, color="green")
plt.bar_label(bars)
plt.xlabel("city name")
plt.ylabel("average amount")
plt.title("city wise average amount")
plt.savefig("city wise average amount.jpg")
plt.show()
