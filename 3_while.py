#
# While test
# Christy
#

sum = 0

while True:
    # 1. Input 
    x1 = input('Type x1: ')
    x2 = input('Type x2: ')
    op = input('Operator: ')

    # 2. Process
    if op == '+':
        sum = int(x1) + int(x2) 
    elif op == '-':
        sum = int(x1) - int(x2) 

    # 3. Output 
    print (f'Result: {sum}')

