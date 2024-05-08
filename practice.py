#
# christy 
# practice
#

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('diabetes.csv')

#Inspect Structure
df.shape
df.info()

#Inspect Value
df.head()
df.tail()

df2 = df.copy()
df2.loc[2:5, 'Pregnancies'] = None

df2.head(10)

df2.isnull().sum()
df2.shape

df3 = df2.copy()
df3 = df3.dropna()
df3.shape

df2['Glucose_Insulin_Ratio'] = df2['Glucose']/df2['Insulin']
df2.head()

df['Outcome'].value_counts()
df['Outcome'].value_counts(sort=False)
df['Outcome'].value_counts(normalize=True)

