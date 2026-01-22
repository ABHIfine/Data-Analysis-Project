import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv("clean_file.csv")
city_counts = data['City'].value_counts()
bars = plt.bar(city_counts.index, city_counts.values, color = "#CFBF2B")
plt.bar_label(bars)
plt.xlabel("CITY NAME")
plt.ylabel("Total Numbers")
plt.title("Total Customer Per City")
plt.savefig("Total Customer Per City.jpg")
plt.show()



