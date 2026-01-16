import numpy as np 
import pandas as pd
import time

name_list = ["abhi", "ravi", "abhishek", "deepu","deepak","gopal","lokendra","yogesh","himanshu","lucky"]
city_list =["jaipur","delhi","mumbai","goa","ajmer","sikar"]
Category_list = ["it","business","sports","teacher","full stack developer"]

start =time.time()
n = 1000000

data = {
    'Customer-id': range(1, n+1),
    'name': np.random.choice(name_list, size=n),
    'Age': np.random.randint(18,90, size=n),
    'City': np.random.choice(city_list, size=n),
    'Category' : np.random.choice(Category_list, size=n),
    'Amount': np.random.randint(100,1000, size=n),
    'Rating': np.round(np.random.uniform(1,5, size=n),1)
}

df = pd.DataFrame(data)
end= time.time()
df.to_csv("fast.csv", index=False)

print("----------RESULT--------------")
print(f"file 'fast.csv' ban gayi hai with {n} rows")
print (f"how much time taken {end-start:.5} second main")
print("-------------END---------------")
