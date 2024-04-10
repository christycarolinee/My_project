#
# Christy
# Pandas Test 
#

import pandas as pd

 # 1. Input 
my_data = pd.read_csv('MENU.csv')
print(my_data)
print(my_data.info())

# 2. Process
# total = my_data['Price'].sum()
# print(total)

# print(my_data['Price'].var())
# print(my_data['Price'].std())

print(my_data['Price'].sort_values())
print(my_data.sort_values('Price'))
print(my_data.sort_values('Price', ascending=False))

# 3. Output
