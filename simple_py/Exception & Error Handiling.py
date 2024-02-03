     
#*************************************************
#Exception & Error Handiling
#*************************************************    
def divide(a, b):
    
    try:
        division = a / b
    except ZeroDivisionError:
        print("Please enter valid input")
    else:
        print("Result =", division)
    #finally:
       # print("Program executed")
a=int(input("Enter the value of a :"))
b=int(input("Enter the value of b:"))
divide(a, b)

#*88888888888888888888888888888888888888
def divide(a, b):
    division =a/b
    print(divide)
    



a=int(input("Enter the value of a :"))
b=int(input("Enter the value of b:"))
divide(a, b)













#*************************************************   
def divide(a, b):
    try:
        division = a / b
    except ZeroDivisionError:
        print("Please enter valid input")
    else:
        print("Result =", division)
    finally:

        print("Program executed")
while True:
    try:
        a=int(input("Enter the value of a :"))
        b=int(input("Enter the value of b:"))
    except ValueError :
        print("Please enter valid input")
        break
    continue
        

divide(a, b)