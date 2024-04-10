#
# Christy 
# BMI CALCULATOR 
#


while True:
    # 1. Input 
    weight = float (input('Type Enter your weight in kilograms: '))
    height = float (input('Type Enter your height in meters: '))
    

    # 2. Process
    bmi = weight / ( height ** 2)

      
    # 3. Output 
    print("Your BMI is: ", bmi)

    option = input ('Continue ? (yes/no) :')
    if option == 'yes' :
                continue
    else: 
            break


    
  



