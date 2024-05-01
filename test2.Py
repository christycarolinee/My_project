#
# Christy
# Pandas Practice
#

import pandas as pd 
import matplotlib.pyplot as plt
  
df = pd.read_csv("smoker 1.csv")

print(df)

# Inspect structure 
df.shape
df.info

# Visualize 
df['smoker'].hist()
plt.show()

df['smoker'].value_counts()
df['treatment'].value_counts()
df['outcome'].value_counts()

#Mean
df['smoker'].mean()
df['treatment'].mean()
df['outcome'].mean()

#Sum 
df.sum()
df.sum(axis=1)

df.describe()

#Selection
df['smoker']
df[0:3]

df.loc[0:3,'smoker']
df.iloc[1,0]