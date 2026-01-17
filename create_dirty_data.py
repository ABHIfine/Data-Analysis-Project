import numpy as np
import pandas as pd

name_list = ["abhi", "surya", "ravi", "himanshu","gopal", "deepu", "sunil", "mohan",
              "abhishek", "atul", "lokendra", "yogesh","nikhil","chetan","sunny"]
city_list = ["jaipur","delhi","goa","mumbai"]

n= 1000

data = {
    'Customer-id': range(1, n+1),
    'name': np.random.choice(name_list,size=n),
    'Age': np.where(np.random.rand(n)<0.1, np.nan, np.random.randint(18,90, size=n)),
    'City': np.where(np.random.rand(n) <0.1, None, np.random.choice(city_list, size=n)),
    'Amount': np.random.randint(100,1000, size=n),
    'Rating': np.round(np.random.uniform(1,5, size=n),1)
}

df = pd.DataFrame(data)

df.to_csv("dirty_data.csv", index=False)
print(f"file 'dirty_data.csv' ban gaya hai")
print(df.isnull().sum())


