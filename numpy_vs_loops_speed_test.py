import numpy as np 
import pandas as pd

name_list = ["abhi", "ravi", "abhishek", "deepu","deepak","gopal","lokendra","yogesh","himanshu","lucky"]
city_list =["jaipur","delhi","mumbai","goa","ajmer","sikar"]
Category_list = ["it","business","sports","teacher","full stack developer"]

n = 1000

data = {
    'Customer-id': range(1, n+1),
    'name': np.random.choice(name_list, size=n),
    'Age': np.random.randint(18,90, size=n),
    'City': np.random.choice(city_list, size=n),
    'Category' : np.random.choice(Category_list, size=n),
    'Amount': np.random.randint(100,1000, size=n),
    'Rating': (np.random.uniform(1,5, size=n),1)
}