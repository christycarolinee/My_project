#
# James 
# Pandas Practice
#

import pandas as pd 
  
df = pd.read_csv("smoker 1.csv")

print(df)

# Inspect structure 
df.shape
df.info

# Inspect value
df.head()
df.tail()

