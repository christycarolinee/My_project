#
# output test
# Christy


# 1. Input 
x1 = input('type x1: ')
x2 = input('type x2: ')
op = input('operator: ')


# 2. Process
if op == '+':
     sum = int(x1) + int(x2) 
elif op == '-':
     sum = int(x1) - int(x2) 


# 3. output 
print (f'result: {sum}')
