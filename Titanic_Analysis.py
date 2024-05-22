#
# christy 
# Titanic panda analysis
#
#

import pandas as pd 
import matplotlib.pyplot as plt 

df = pd.read_csv("titanic.csv")

print(df)

df.head()

df.shape
df.info()

df.describe()

df.fillna(df.median(numeric_only=True).round(1), inplace=True)
df.fillna(df.mean(numeric_only=True).round(1), inplace=True)

print(df)

df.dropna()

gender_counts = df['Sex'].value_counts()
print(gender_counts)

df['Age'].mean()

df[['Pclass', 'Survived']].groupby('Pclass', as_index=False).mean()

df = pd.DataFrame({
    'Pclass': ['1', '2', '3'],
    'Survival' : [0.629630, 0.472826, 0.242363]
})

df.plot(x='Pclass', y='Survival', kind='bar')
plt.xlabel("Pclass")
plt.ylabel("Number of Survival")
plt.title("Number of Survival rate by Pclass")
plt.show()







