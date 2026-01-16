import numpy as np 
import pandas as pd
import time

name_list = ["abhi", "ravi", "abhishek", "deepu","deepak","gopal","lokendra","yogesh","himanshu","lucky"]
city_list =["jaipur","delhi","mumbai","goa","ajmer","sikar"]
Category_list = ["it","business","sports","teacher","full stack developer"]

numpy_start =time.time()
n = 1000000

# ==========================================
# 🚀 METHOD 1: NumPy (Fast Way)
# ==========================================

data = {
    'Customer-id': range(1, n+1),
    'name': np.random.choice(name_list, size=n),
    'Age': np.random.randint(18,90, size=n),
    'City': np.random.choice(city_list, size=n),
    'Category' : np.random.choice(Category_list, size=n),
    'Amount': np.random.randint(100,1000, size=n),
    'Rating': np.round(np.random.uniform(1,5, size=n),1)
}

df_numpy = pd.DataFrame(data)
numpy_end= time.time()
time_taken = numpy_end-numpy_start
print(f"NUMPY HOW MUCH TIME TAKEN {time_taken:.5f} in a seconds")

# ==========================================
# 🐢 METHOD 2: For Loop (Slow Way)
# ==========================================

start = time.time()

simple ={
    'CUSTOMER-ID' :range(1, n+1),
    'NAME': [np.random.choice(name_list)
             for _ in range(n)],
    'AGE': [np.random.randint(18,90)
            for _ in range(n)],
    'CITY':[np.random.choice(city_list)
            for _ in range(n)],
    'CATEGORY': [np.random.choice(Category_list)
                 for _ in range(n)],
    'AMOUNT': [np.random.randint(100,1000)
               for _ in range(n)],
    'RATING':[np.round(np.random.uniform(1,5),1)
                       for _ in range(n)]
            
}

df_loop = pd.DataFrame(simple)
end= time.time()
simple_time_taken = end-start
print(f"FOR LOOP HOW MUCH TIME TAKEN {simple_time_taken:.5f}")

# ==========================================
# 🏆 RESULT
# ==========================================

print("-------------final result--------------")
print(f"how much time taken in {time_taken:.5f} numpy")
print (f"how much time taken {simple_time_taken:.5f} for loop")

difference = simple_time_taken/time_taken
print(f"conclsion : NUMPY is {difference:.2f} times FASTER!")
df_numpy.to_csv("fast.csv", index=False)